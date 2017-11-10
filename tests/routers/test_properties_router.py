import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.properties import PropertiesRouter, ZenossProperty, ZenossCustomProperty
import properties_resp

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

    def getZenProperties(rdata):
        if rdata['params']:
            if 'id' in rdata['params']:
                if 'islocal' in rdata['params']:
                    return properties_resp.get_local_prop
                else:
                    return properties_resp.get_prop
            elif 'islocal' in rdata['params']:
                return properties_resp.local_props

        return properties_resp.props

    def getCustomProperties(rdata):
        if rdata['params'] and 'id' in rdata['params']:
            if 'islocal' in rdata['params']:
                return properties_resp.custom_local_props

        return properties_resp.custom_props

    def setZenProperty(rdata):
        if rdata['zProperty'] == "zWinTrustedRealm":
            return properties_resp.set_prop
        elif rdata['zProperty'] == "cDateTest":
            return properties_resp.set_custom_prop

    def deleteZenProperty(rdata):
        return properties_resp.delete_prop

    method = locals()[rdata['method']]
    resp_body = method(rdata['data'][0])

    return (200, resp_headers, json.dumps(resp_body))


def responses_callback(responses):
    responses.add_callback(
        responses.POST,
        '{0}/properties_router'.format(url),
        callback=request_callback,
        content_type='application/json',
    )


class TestPropertiesRouter(object):

    def test_properties_router_init(self):
        pr = PropertiesRouter(url, headers, True)
        assert pr.id is None

    def test_properties_router_list_properties(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.list_properties('test.example.com')
        assert props['total'] == 4
        assert len(props['properties']) == 4
        assert props['properties'][0]['id'] == "zAggregatorCollectionInterval"

    def test_properties_router_get_properties(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.get_properties('test.example.com')
        assert props['total'] == 4
        assert len(props['properties']) == 4
        assert isinstance(props['properties'][0], ZenossProperty)
        assert props['properties'][0].id == "zAggregatorCollectionInterval"

    def test_properties_router_list_local_properties(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.list_local_properties('test.example.com')
        assert props['total'] == 2
        assert len(props['properties']) == 2
        assert props['properties'][0]['id'] == "zMySQLConnectionString"

    def test_properties_router_get_local_properties(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.get_local_properties('test.example.com')
        assert props['total'] == 2
        assert len(props['properties']) == 2
        assert isinstance(props['properties'][0], ZenossProperty)
        assert props['properties'][0].id == "zMySQLConnectionString"

    def test_properties_router_get_property(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        prop = pr.get_property('test.example.com', 'zWinTrustedRealm')
        assert isinstance(prop, ZenossProperty)
        assert prop.id == 'zWinTrustedRealm'

    def test_properties_router_list_custom_properties(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.list_custom_properties('test.example.com')
        assert props['total'] == 1
        assert len(props['properties']) == 1
        assert props['properties'][0]['id'] == "cDateTest"
        assert props['properties'][0]['path'] == "/"

    def test_properties_router_get_custom_properties(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.get_custom_properties('test.example.com')
        assert props['total'] == 1
        assert len(props['properties']) == 1
        assert isinstance(props['properties'][0], ZenossCustomProperty)
        assert props['properties'][0].id == "cDateTest"

    def test_properties_router_get_custom_property(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        prop = pr.get_custom_property('test.example.com', 'cDateTest')
        assert isinstance(prop, ZenossCustomProperty)
        assert prop.id == "cDateTest"
        assert prop.path == "Devices/"

    def test_properties_router_set_property_value(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        prop = pr.set_property_value('test.example.com', 'zWinTrustedRealm', value='Westeros')
        assert prop['value'] == "Westeros"

    def test_properties_router_zenossproperty_set_value(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        prop = pr.get_property('test.example.com', 'zWinTrustedRealm')
        assert prop.id == "zWinTrustedRealm"
        assert prop.path == "Devices/"
        assert prop.set_value(path='Devices/Server/TEST/devices/test.example.com', value='Westeros')
        assert prop.value == "Westeros"
        assert prop.path == "Devices/Server/TEST/devices/test.example.com"

    def test_properties_router_zenossproperty_delete(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.get_properties('test.example.com', params=dict(id='zWinTrustedRealm', islocal=1))
        prop = props['properties'][0]
        assert prop.islocal == 1
        assert prop.value == "Westeros"
        assert prop.path == "Devices/Server/TEST/devices/test.example.com"
        assert prop.delete()
        assert prop.islocal == 0
        assert prop.id == "zWinTrustedRealm"
        assert prop.path == "/"

    def test_properties_router_zenossproperty_delete_non_local(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        prop = pr.get_property('test.example.com', 'zWinTrustedRealm')
        assert prop.islocal == 0
        assert not prop.delete()

    def test_properties_router_zenosscustomproperty_set_value(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.get_custom_properties('test.example.com')
        prop = props['properties'][0]
        assert prop.id == "cDateTest"
        assert prop.value == "1900/01/01 00:00:00 US/Central"
        assert prop.path == "Devices/"
        assert prop.set_value(path='Devices/Server/TEST/devices/test.example.com', value="2017/12/19 00:00:00 US/Pacific")
        assert prop.value == "2017/12/19 00:00:00 US/Pacific"
        assert prop.path == "Devices/Server/TEST/devices/test.example.com"

    def test_properties_router_zenosscustomproperty_delete(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.get_custom_properties('test.example.com', params=dict(id='cDateTest', islocal=1))
        prop = props['properties'][0]
        assert prop.islocal == 1
        assert prop.path == "Devices/Server/TEST/devices/test.example.com"
        assert prop.value == "2017/12/19 00:00:00 US/Pacific"
        assert prop.delete()
        assert prop.islocal == 0
        assert prop.path == "/"
        assert prop.value == "1900/01/01 00:00:00 US/Central"

    def test_properties_router_zenosscustomproperty_delete_non_local(self, responses):
        responses_callback(responses)

        pr = PropertiesRouter(url, headers, True)
        props = pr.get_custom_properties('test.example.com')
        prop = props['properties'][0]
        assert prop.islocal == 0
        assert not prop.delete()
