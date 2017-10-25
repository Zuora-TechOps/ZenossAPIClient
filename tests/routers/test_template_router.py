import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.template import TemplateRouter, ZenossTemplate, ZenossDataSource, ZenossDataPoint, ZenossThreshold, ZenossGraph
import template_resp

pytest_plugins = "pytest-responses"
url = 'https://zenoss/zport/dmd'
headers = dict(
    ContentType='application/json'
)


def request_callback(request):
    rdata = json.loads(request.body)
    resp_headers = dict(ContentType='application/json')

    def getDeviceClassTemplates(rdata):
        return template_resp.list_templates

    def getInfo(rdata):
        t = rdata['uid'].split('/')[-1]
        return template_resp.templates[t]

    def getObjTemplates(rdata):
        return template_resp.obj_templates

    def addTemplate(rdata):
        return dict(
            result=dict(
                nodeConfig=dict(
                    uid='/zport/dmd/Devices/Server/TEST/rrdTemplates/TestAdd'
                )
            )
        )

    def addLocalRRDTemplate(rdata):
        return dict(
            result=dict(
                nodeConfig=dict(
                    uid='/zport/dmd/Devices/Server/TEST/test.example.com/DnsMonitor'
                )
            )
        )

    def getDataSourceTypes(rdata):
        return template_resp.ds_types

    def getThresholdTypes(rdata):
        return template_resp.threshold_types

    def copyTemplate(rdata):
        return template_resp.templates['LogicalVolume']

    def getDataSources(rdata):
        return template_resp.lv_data_sources

    def getDataSourceDetails(rdata):
        if rdata['uid'].endswith('status'):
            return template_resp.lv_ds_details
        elif rdata['uid'].endswith('disk'):
            return template_resp.fs_ds_details
        else:
            return template_resp.fail

    def getDataPoints(rdata):
        return template_resp.lv_data_points

    def getThresholds(rdata):
        return template_resp.fs_thresholds

    def getThresholdDetails(rdata):
        return template_resp.threshold_details

    def getGraphs(rdata):
        return template_resp.graphs_list

    def getGraphDefinition(rdata):
        return template_resp.graph_def

    def getDataPointDetails(rdata):
        if rdata['uid'].endswith('state'):
            return template_resp.lv_dp_details
        elif rdata['uid'].endswith('disk_percentUsed'):
            return template_resp.fs_dp_details
        elif rdata['uid'].endswith('disk_usedBlocks'):
            return template_resp.fs_dp_details_2
        else:
            return template_resp.no_points

    def getGraphPoints(rdata):
        return template_resp.graph_points

    if rdata['method'] in ['deleteTemplate', 'removeLocalRRDTemplate',
                           'addDataPointToGraph', 'addDataSource',
                           'deleteDataSource', 'addThreshold',
                           'removeThreshold', 'addGraphDefinition',
                           'addDataPoint', 'deleteDataPoint',
                           'addThreshold', 'removeThreshold', 'setInfo',
                           'setGraphDefinition', 'setGraphPointSequence',
                           'deleteGraphPoint', 'addThresholdToGraph']:
        resp_body = template_resp.success
    else:
        method = locals()[rdata['method']]
        resp_body = method(rdata['data'][0])

    return (200, resp_headers, json.dumps(resp_body))


def responses_callback(responses):
    responses.add_callback(
        responses.POST,
        '{0}/template_router'.format(url),
        callback=request_callback,
        content_type='application/json',
    )


class TestTemplateRouter(object):

    def test_template_router_init(self):
        tr = TemplateRouter(url, headers, True)
        assert tr.uid is None
        assert tr.properties is None

    def test_template_router_list_templates(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.list_device_class_templates('Server/TEST')
        assert len(resp) == 12
        assert resp == template_resp.list_templates_match

    def test_template_router_get_templates(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.get_device_class_templates('Server/TEST')
        assert len(resp) == 12
        assert isinstance(resp[0], ZenossTemplate)

    def test_template_router_get_object_templates(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.get_object_templates('Server/TEST/test.example.com')
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossTemplate)
        assert isinstance(resp[1], ZenossTemplate)

    def test_template_router_get_template(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.get_template('Devices', 'Device')
        assert isinstance(resp, ZenossTemplate)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/Device"

    def test_template_router_add_template(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.add_template('Servers/TEST', 'TestAdd')
        assert isinstance(resp, ZenossTemplate)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/TestAdd"

    def test_template_router_add_local_template(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.add_local_template('Servers/TEST/devices/test.example.com', 'DnsMonitor')
        assert isinstance(resp, ZenossTemplate)
        assert resp.uid == "Devices/Server/TEST/devices/test.example.com/DnsMonitor"

    def test_template_router_delete_template(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.delete_template('Servers/TEST', 'TestAdd')
        assert resp['success']

    def test_template_router_delete_local_template(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.delete_local_template('Server/TEST/devices/test.example.com', 'DnsMonitor')
        assert resp['success']

    def test_template_router_get_data_source_types(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.get_data_source_types()
        assert len(resp) == 18
        assert "HttpMonitor" in resp

    def test_template_router_get_threshold_types(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.get_threshold_types()
        assert len(resp) == 4
        assert "MinMaxThreshold" in resp

    def test_template_router_add_data_point_to_graph(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        resp = tr.add_data_point_to_graph('Data/Point', 'Graph/UID', True)
        assert resp['success']

    def test_template_router_zenosstemplate_copy(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.copy('Server')
        assert isinstance(resp, ZenossTemplate)

    def test_template_router_zenosstemplate_list_data_sources(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.list_data_sources()
        assert len(resp) == 1
        assert resp[0] == "Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status"

    def test_template_router_zenosstemplate_get_data_sources(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.get_data_sources()
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossDataSource)

    def test_template_router_zenosstemplate_get_data_source(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.get_data_source('status')
        assert isinstance(resp, ZenossDataSource)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status"

    def test_template_router_zenosstemplate_add_data_source(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.add_data_source('status', 'COMMAND')
        assert isinstance(resp, ZenossDataSource)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status"

    def test_template_router_zenosstemplate_delete_data_source(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.delete_data_source('status')
        assert resp['success']

    def test_temmplate_router_zenosstemplate_get_data_source_not_found(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        with pytest.raises(ZenossAPIClientError, message="Request failed: ObjectNotFoundException"):
            resp = zt.get_data_source('bad')

    def test_template_router_zenosstemplate_list_data_points(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.list_data_points()
        assert len(resp) == 2
        assert resp[0] == "Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state"

    def test_template_router_zenosstemplate_get_data_points(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        resp = zt.get_data_points()
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossDataPoint)

    def test_template_router_zenosstemplate_list_thresholds(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.list_thresholds()
        assert len(resp) == 2
        assert resp[0] == "Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used"

    def test_template_router_zenosstemplate_get_thresholds(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.get_thresholds()
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossThreshold)

    def test_template_router_zenosstemplate_get_threshold(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.get_threshold('90 percent used')
        assert isinstance(resp, ZenossThreshold)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used"

    def test_template_router_zenosstemplate_add_threshold(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.add_threshold('90 percent used', 'MinMaxThreshold', ['dp'])
        assert isinstance(resp, ZenossThreshold)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used"

    def test_template_router_zenosstemplate_delete_threshold(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.delete_threshold('90 percent used')
        assert resp['success']

    def test_template_router_zenosstemplate_list_graphs(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.list_graphs()
        assert len(resp) == 1
        assert resp[0] == "Devices/Server/TEST/rrdTemplates/FileSystem/graphDefs/Usage"

    def test_template_router_zenosstemplate_get_graphs(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.get_graphs()
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossGraph)

    def test_template_router_zenosstemplate_get_graph(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.get_graph('Usage')
        assert isinstance(resp, ZenossGraph)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/FileSystem/graphDefs/Usage"

    def test_template_router_zenosstemplate_add_graph(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        resp = zt.add_graph('Usage')
        assert isinstance(resp, ZenossGraph)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/FileSystem/graphDefs/Usage"

    def test_template_router_zenossdatasource_list_data_points(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        ds = zt.get_data_source('status')
        resp = ds.list_data_points()
        assert len(resp) == 2
        assert resp[0] == "Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state"

    def test_template_router_zenossdatasource_get_data_points(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        ds = zt.get_data_source('status')
        resp = ds.get_data_points()
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossDataPoint)

    def test_template_router_zenossdatasource_get_data_point(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        ds = zt.get_data_source('status')
        resp = ds.get_data_point('state')
        assert isinstance(resp, ZenossDataPoint)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state"

    def test_template_router_zenossdatasource_add_data_point(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        ds = zt.get_data_source('status')
        resp = ds.get_data_point('state')
        assert isinstance(resp, ZenossDataPoint)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state"

    def test_template_router_zenossdatasource_delete_data_point(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        ds = zt.get_data_source('status')
        resp = ds.delete_data_point('state')
        assert resp['success']

    def test_template_router_zenossdatasource_delete(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'LogicalVolume')
        ds = zt.get_data_source('status')
        resp = ds.delete()
        assert resp['success']

    def test_template_router_zenossdatapoint_set_threshold(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        ds = zt.get_data_source('disk')
        dp = ds.get_data_point('disk_percentUsed')
        resp = dp.set_threshold('90 percent used', 'MinMaxThreshold')
        assert isinstance(resp, ZenossThreshold)
        assert resp.uid == "Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used"

    def tet_template_router_zenossdatapoint_make_counter(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        ds = zt.get_data_source('disk')
        dp = ds.get_data_point('disk_percentUsed')
        dp.make_counter()

    def tet_template_router_zenossdatapoint_make_gauge(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        ds = zt.get_data_source('disk')
        dp = ds.get_data_point('disk_percentUsed')
        dp.make_gauge()

    def test_template_router_zenossdatapoint_delete(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        ds = zt.get_data_source('disk')
        dp = ds.get_data_point('disk_percentUsed')
        resp = dp.delete()
        assert resp['success']

    def test_template_router_zenossthreshold_set_max(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        threshold = zt.get_threshold('90 percent used')
        threshold.set_max(100)

    def test_template_router_zenossthreshold_set_min(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        threshold = zt.get_threshold('90 percent used')
        threshold.set_min(1)

    def test_template_router_zenossthreshold_delete(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        threshold = zt.get_threshold('90 percent used')
        resp = threshold.delete()
        assert resp['success']

    def test_template_router_zenossgraph_list_points(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        graph = zt.get_graph('Usage')
        resp = graph.list_points()
        assert len(resp) == 1
        assert resp[0] == "Devices/Server/TEST/rrdTemplates/FileSystem/graphDefs/Usage/graphPoints/Used"

    def test_template_router_zenossgraph_get_points(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        graph = zt.get_graph('Usage')
        resp = graph.get_points()
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossDataPoint)

    def test_template_router_zenossgraph_add_point(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        graph = zt.get_graph('Usage')
        resp = graph.add_point('disk', 'usedBlocks')
        assert resp['success']

    def test_template_router_zenossgraph_set_graph_properties(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        graph = zt.get_graph('Usage')
        resp = graph.set_graph_properties(dict(foo='bar'))
        assert resp['success']

    def test_template_router_zenossgraph_set_point_sequence(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        graph = zt.get_graph('Usage')
        resp = graph.set_point_sequence(['Used'])
        assert resp['success']

    def test_template_router_zenossgraph_delete_point(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        graph = zt.get_graph('Usage')
        resp = graph.delete_point('Used')
        assert resp['success']

    def test_template_router_zenossgraph_add_graph_threshold(self, responses):
        responses_callback(responses)

        tr = TemplateRouter(url, headers, True)
        zt = tr.get_template('Server/TEST', 'FileSystem')
        graph = zt.get_graph('Usage')
        resp = graph.add_graph_threshold('Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used')
        assert resp['success']
