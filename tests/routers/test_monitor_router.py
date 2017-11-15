import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.monitor import MonitorRouter, ZenossHub, ZenossCollector
import monitor_resp


pytest_plugins = "pytest-responses"
url = 'https://zenoss/zport/dmd'
headers = dict(
    ContentType='application/json'
)
resp_body_template = dict(
    result=dict(
        success=True,
        data=[],
    )
)


def request_callback(request):
    rdata = json.loads(request.body)
    resp_headers = dict(ContentType='application/json')

    def getTree(rdata):
        return monitor_resp.tree

    def getInfo(rdata):
        if rdata['id'] == "newcollector":
            return monitor_resp.newcollector
        return monitor_resp.testcollector

    def getCollector(rdata):
        return monitor_resp.params

    def addCollector(rdata):
        return monitor_resp.add

    method = locals()[rdata['method']]
    resp_body = method(rdata['data'][0])

    return (200, resp_headers, json.dumps(resp_body))


def responses_callback(responses):
    responses.add_callback(
        responses.POST,
        '{0}/monitor_router'.format(url),
        callback=request_callback,
        content_type='application/json',
    )


class TestMonitorRouter(object):

    def test_monitor_router_init(self):
        mr = MonitorRouter(url, headers, False)
        assert mr.id is None

    def test_monitor_router_tree(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        resp = mr.tree()
        assert len(resp) == 2
        assert len(resp[0]['children']) == 1
        assert resp[0]['name'] == "localhost"
        assert resp[1]['name'] == "testhub"

    def test_monitor_router_list_hubs(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        resp = mr.list_hubs()
        assert len(resp) == 2
        assert resp[0]['name'] == "localhost"
        assert resp[1]['name'] == "testhub"
        assert resp[0]['uid'] == "Monitors/Hub/localhost"
        assert resp[1]['uid'] == "Monitors/Hub/testhub"

    def test_monitor_router_list_collectors(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        resp = mr.list_collectors()
        assert len(resp) == 2
        assert resp[0]['name'] == "localhost"
        assert resp[0]['devcount'] == 0
        assert resp[0]['hub'] == "localhost"
        assert resp[0]['uid'] == "Monitors/Performance/localhost"
        assert resp[1]['name'] == "testcollector"
        assert resp[1]['devcount'] == 179
        assert resp[1]['hub'] == "testhub"
        assert resp[1]['uid'] == "Monitors/Performance/testcollector"

    def test_monitor_router_get_hubs(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        resp = mr.get_hubs()
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossHub)
        assert isinstance(resp[1], ZenossHub)

    def test_monitor_router_get_hub(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        resp = mr.get_hub('testhub')
        assert isinstance(resp, ZenossHub)
        assert resp.name == "testhub"
        assert resp.devcount == 0
        assert len(resp.collectors) == 1

    def test_monitor_router_get_bad_hub(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        resp = mr.get_hub('badhub')
        assert resp is None

    def test_monitor_router_zenosshub_get_collectors(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        zh = mr.get_hub('testhub')
        resp = zh.get_collectors()
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossCollector)
        assert resp[0].name == "testcollector"

    def test_monitor_router_zenosshub_get_collector(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        zh = mr.get_hub('testhub')
        resp = zh.get_collector('testcollector')
        assert isinstance(resp, ZenossCollector)
        assert resp.name == "testcollector"
        assert resp.devcount == 179
        assert resp.text == "testcollector"
        assert resp.path == "/zport/dmd/Monitors/Performance/testcollector"
        assert resp.id == ".zport.dmd.Monitors.Performance.testcollector"
        assert resp.configCycleInterval == 360
        assert resp.pingCycleInterval == 60
        assert resp.discoveryNetworks == ""
        assert resp.description == ""
        assert resp.modelerCycleInterval == 720
        assert resp.processCycleInterval == 180
        assert resp.meta_type == "PerformanceConf"
        assert resp.wmiqueryTimeout == 100
        assert resp.statusCycleInterval == 60
        assert resp.eventlogCycleInterval == 60
        assert resp.wmibatchSize == 10
        assert resp.pingTimeOut == 1.5
        assert resp.winCycleInterval == 60
        assert resp.pingTries == 2
        assert resp.inspector_type == "PerformanceConf"
        assert resp.zenProcessParallelJobs == 10

    def test_monitor_router_zenosshub_get_bad_collector(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        zh = mr.get_hub('testhub')
        resp = zh.get_collector('badcollector')
        assert resp is None

    def test_monitor_router_zenosshub_add_collector(self, responses):
        responses_callback(responses)

        mr = MonitorRouter(url, headers, False)
        zh = mr.get_hub('testhub')
        resp = zh.add_collector('newcollector', source='testcollector', pool='TEST')
        assert isinstance(resp, ZenossCollector)
        assert resp.name == "newcollector"
        assert resp.devcount == 0
        assert resp.text == "newcollector"
        assert resp.path == "/zport/dmd/Monitors/Performance/newcollector"
        assert resp.id == ".zport.dmd.Monitors.Performance.newcollector"
        assert resp.configCycleInterval == 360
        assert resp.pingCycleInterval == 60
        assert resp.discoveryNetworks == ""
        assert resp.description == ""
        assert resp.modelerCycleInterval == 720
        assert resp.processCycleInterval == 180
        assert resp.meta_type == "PerformanceConf"
        assert resp.wmiqueryTimeout == 100
        assert resp.statusCycleInterval == 60
        assert resp.eventlogCycleInterval == 60
        assert resp.wmibatchSize == 10
        assert resp.pingTimeOut == 1.5
        assert resp.winCycleInterval == 60
        assert resp.pingTries == 2
        assert resp.inspector_type == "PerformanceConf"
        assert resp.zenProcessParallelJobs == 10
