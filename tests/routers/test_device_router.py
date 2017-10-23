import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.device import DeviceRouter, ZenossDeviceClass, ZenossDevice, ZenossComponent
import resp_json

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

    def getProductionStates(rdata):
        resp_body_template['result']['data'].append(dict(name='Production', value=1000))
        return resp_body_template

    def getPriorities(rdata):
        resp_body_template['result']['data'].append(dict(name='Normal', value=3))
        return resp_body_template

    def getInfo(rdata):
        if rdata['uid'] == "Devices/Server/TEST":
            return resp_json.dc_info
        elif rdata['uid'] == "Devices/Server/TEST/devices/test.example.com":
            return resp_json.dev_info
        elif rdata['uid'] == "Devices/Server/TEST/devices/test.example.com/hw/cpus/0":
            return resp_json.component_info
        else:
            return resp_json.not_found

    def getCollectors(rdata):
        return resp_json.collectors

    def getDeviceClasses(rdata):
        return resp_json.dev_classes

    def getDevices(rdata):
        return resp_json.devices

    def getComponents(rdata):
        return resp_json.components

    method = locals()[rdata['method']]
    resp_body = method(rdata['data'][0])

    return (200, resp_headers, json.dumps(resp_body))


def responses_callback(responses):
    responses.add_callback(
        responses.POST,
        '{0}/device_router'.format(url),
        callback=request_callback,
        content_type='application/json',
    )


class TestDeviceRouter(object):

    def test_device_router_init(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        assert dr.uid is None
        assert dr.properties is None
        assert dr.prod_states_by_value[1000] == "Production"
        assert dr.prod_states_by_name['Production'] == 1000
        assert dr.priorities_by_value[3] == "Normal"
        assert dr.priorities_by_name['Normal'] == 3

    def test_device_router_get_info_by_uid(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        resp = dr._get_info_by_uid('Devices/Server/TEST')
        assert resp['data']['name'] == "TEST"

    def test_device_router_get_info_by_uid_not_found(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        with pytest.raises(ZenossAPIClientError, message="Request failed: ObjectNotFoundException: Cannot find \"Devices/Server/TEST\". KeyError: 'TEST'"):
            resp = dr._get_info_by_uid('Devices/Server/NOTFOUND')

    def test_device_router_list_collectors(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        resp = dr.list_collectors()
        assert resp[0] == "localhost"

    def test_device_router_list_device_classes(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        resp = dr.list_device_classes()
        assert len(resp) == 7
        assert resp[-1] == "Devices/Server/SSH/Linux"

    def test_device_router_get_device_class(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        resp = dr.get_device_class('Server/TEST')
        assert isinstance(resp, ZenossDeviceClass)

    def test_device_router_list_devices(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.list_devices()
        assert resp['total'] == 1
        assert resp['devices'][0]['name'] == "test.example.com"
        assert resp['devices'][0]['uid'] == "Devices/Server/TEST/devices/test.example.com"

    def test_device_router_get_devices(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.get_devices()
        assert len(resp['devices']) == 1
        assert isinstance(resp['devices'][0], ZenossDevice)

    def test_device_router_get_device(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.get_device('test.example.com')
        assert isinstance(resp, ZenossDevice)
        assert resp.uid == "Devices/Server/TEST/devices/test.example.com"

    def test_device_router_list_components(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_components()
        assert resp['total'] == 1
        assert resp['components'][0] == "hw/cpus/0"

    def test_device_router_get_components(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_components()
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossComponent)

    def test_device_router_get_component(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_component('hw/cpus/0')
        assert resp.uid == "Devices/Server/TEST/devices/test.example.com/hw/cpus/0"
        assert resp.meta_type == "CPU"
        assert resp.name == "0"
