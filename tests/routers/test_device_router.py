import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.device import DeviceRouter, ZenossDeviceClass, ZenossDevice, ZenossComponent
from zenossapi.routers.template import ZenossTemplate
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
        resp_body_template['result']['data'].extend([
            dict(name='Production', value=1000),
            dict(name='Maintenance', value=300),
        ])
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
        elif rdata['uid'] == "Devices/Server/TEST/devices/test.example.com/DnsMonitor":
            return resp_json.local_template
        elif rdata['uid'] == "Devices/Server/TEST/rrdTemplates/Device":
            return resp_json.device_template
        elif rdata['uid'] == "Devices/rrdTemplates/DnsMonitor":
            return resp_json.dns_template
        elif rdata['uid'] == "Devices/Server/rrdTemplates/Apache":
            return resp_json.apache_template
        elif rdata['uid'] == "Devices/Server/rrdTemplates/DigMonitor":
            return resp_json.dig_template
        else:
            return resp_json.not_found

    def getCollectors(rdata):
        return resp_json.collectors

    def getDeviceClasses(rdata):
        return resp_json.dev_classes

    def getGroups(rdata):
        return resp_json.groups

    def getSystems(rdata):
        return resp_json.systems

    def getDevices(rdata):
        return resp_json.devices

    def addDeviceClassNode(rdata):
        return resp_json.add_dc

    def addDevice(rdata):
        return resp_json.add_dev

    def getComponents(rdata):
        return resp_json.components

    def getUserCommands(rdata):
        return resp_json.uc

    def getLocalTemplates(rdata):
        return resp_json.local_templates

    def getTemplates(rdata):
        return resp_json.templates

    def getUnboundTemplates(rdata):
        return resp_json.ub_templates
    
    def getBoundTemplates(rdata):
        return resp_json.bound_templates

    def getOverridableTemplates(rdata):
        return resp_json.or_templates

    def moveDevices(rdata):
        return resp_json.move_dev

    def lockDevices(rdata):
        return resp_json.lock

    def resetIp(rdata):
        return resp_json.resetip

    def setProductionState(rdata):
        return resp_json.prod_state

    def setPriority(rdata):
        return resp_json.priority

    def setCollector(rdata):
        return resp_json.set_collector

    def remodel(rdata):
        return resp_json.remodel

    def setComponentsMonitored(rdata):
        return resp_json.monitored

    def lockComponents(rdata):
        return resp_json.lock_c

    def deleteComponents(rdata):
        return resp_json.delete_c

    if rdata['method'] in ['setBoundTemplates', 'bindOrUnbindTemplate',
                           'resetBoundTemplates', 'renameDevice',
                           'removeDevices']:
        resp_body = resp_json.success
    else:
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

    def test_device_router_list_groups(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        resp = dr.list_groups()
        assert len(resp) == 1
        assert resp[0] == "/TestGroup"

    def test_device_router_list_systems(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        resp = dr.list_systems()
        assert len(resp) == 1
        assert resp[0] == "/TestSystem"

    def test_device_router_get_device_class(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        resp = dr.get_device_class('Server/TEST')
        assert isinstance(resp, ZenossDeviceClass)

    def test_device_router_zenossdeviceclass_list_devices(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.list_devices()
        assert resp['total'] == 1
        assert resp['devices'][0]['name'] == "test.example.com"
        assert resp['devices'][0]['uid'] == "Devices/Server/TEST/devices/test.example.com"

    def test_device_router_zenossdeviceclass_get_devices(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.get_devices()
        assert len(resp['devices']) == 1
        assert isinstance(resp['devices'][0], ZenossDevice)

    def test_device_router_zenossdeviceclass_get_device(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.get_device('test.example.com')
        assert isinstance(resp, ZenossDevice)
        assert resp.uid == "Devices/Server/TEST/devices/test.example.com"

    def test_device_router_zenossdeviceclass_add_subclass(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.add_subclass('Foo')
        assert isinstance(resp, ZenossDeviceClass)

    def test_device_router_zenossdeviceclass_add_device(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        resp = dc.add_device('test2.example.com')
        assert resp == "721739ae-2b1d-4613-91e9-681f134a2c49"

    def test_device_router_zenossdevice_list_components(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_components()
        assert resp['total'] == 1
        assert resp['components'][0] == "hw/cpus/0"

    def test_device_router_zenossdevice_get_components(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_components()
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossComponent)

    def test_device_router_zenossdevice_get_component(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_component('hw/cpus/0')
        assert resp.uid == "Devices/Server/TEST/devices/test.example.com/hw/cpus/0"
        assert resp.meta_type == "CPU"
        assert resp.name == "0"

    def test_device_router_zenossdevice_list_user_commands(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_user_commands()
        assert len(resp) == 6
        assert resp[2]['name'] == "ping"

    def test_device_router_zenossdevice_list_local_templates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_local_templates()
        assert resp[0] == "DnsMonitor"

    def test_device_router_zenossdevice_get_local_templates(self, responses):
        responses.assert_all_requests_are_fired = False
        responses.add(
            responses.POST,
            '{0}/template_router'.format(url),
            json=resp_json.local_template,
            status=200,
        )
        responses.add_callback(
            responses.POST,
            '{0}/device_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_local_templates()
        assert isinstance(resp[0], ZenossTemplate)
        assert resp[0].uid == "Devices/Server/TEST/devices/test.example.com/DnsMonitor"

    def test_device_router_zenossdevice_list_active_templates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_active_templates()
        assert resp[0]['name'] == "Device"

    def test_device_router_zenossdevice_get_active_templates(self, responses):
        responses.assert_all_requests_are_fired = False
        responses.add_callback(
            responses.POST,
            '{0}/template_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        responses.add_callback(
            responses.POST,
            '{0}/device_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_active_templates()
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossTemplate)
        assert resp[0].uid == "Devices/Server/TEST/rrdTemplates/Device"

    def test_device_router_zenossdevice_list_unbound_templates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_unbound_templates()
        assert resp[0]['name'] == "Apache"

    def test_device_router_zenossdevice_get_unbound_templates(self, responses):
        responses.assert_all_requests_are_fired = False
        responses.add_callback(
            responses.POST,
            '{0}/template_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        responses.add_callback(
            responses.POST,
            '{0}/device_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_unbound_templates()
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossTemplate)
        assert resp[0].uid == "Devices/Server/rrdTemplates/Apache"
        assert resp[1].name == "DigMonitor"

    def test_device_router_zenossdevice_list_bound_templates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_bound_templates()
        assert resp[0]['name'] == "Device"
        
    def test_device_router_zenossdevice_get_bound_templates(self, responses):
        responses.assert_all_requests_are_fired = False
        responses.add_callback(
            responses.POST,
            '{0}/template_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        responses.add_callback(
            responses.POST,
            '{0}/device_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_bound_templates()
        assert len(resp) == 2
        assert isinstance(resp[0], ZenossTemplate)

    def test_device_router_zenossdevice_list_overridable_templates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.list_overridable_templates()
        assert resp[0]['name'] == "Device"

    def test_device_router_zenossdevice_get_overridable_templates(self, responses):
        responses.assert_all_requests_are_fired = False
        responses.add_callback(
            responses.POST,
            '{0}/template_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        responses.add_callback(
            responses.POST,
            '{0}/device_router'.format(url),
            callback=request_callback,
            content_type='application/json',
        )
        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.get_overridable_templates()
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossTemplate)

    def test_device_router_zenossdevice_set_bound_templates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.set_bound_templates(['Device'])

    def test_device_router_zenossdevice_bind_or_unbind_template(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.bind_or_unbind_template('Devices', 'DnsMonitor')

    def test_device_router_zenossdevice_reset_bound_templates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.reset_bound_templates()

    def test_device_router_zenossdevice_move(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.move('Server/TEST')

    def test_device_router_zenossdevice_reidentify(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.reidentify('test2.example.com')

    def test_device_router_zenossdevice_lock(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.lock(updates=True, deletion=True)
        assert resp == "Locked 1 devices."

    def test_device_router_zenossdevice_lock_for_updates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.lock_for_updates()
        assert resp == "Locked 1 devices."

    def test_device_router_zenossdevice_lock_for_deletion(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.lock_for_deletion()
        assert resp == "Locked 1 devices."

    def test_device_router_zenossdevice_reset_ip_address(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.reset_ip_address()
        assert resp == "Reset 1 IP addresses."

    def test_device_router_zenossdevice_set_production_state(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.set_production_state(300)
        assert resp == "Set 1 devices to Maintenance."

    def test_device_router_zenossdevice_set_priority(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.set_priority(3)
        assert resp == "Set 1 devices to Normal priority."

    def test_device_router_zenossdevice_set_collector(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.set_collector('localhost')
        assert resp == "bd320c54-4325-47a7-baaf-048a22c1a276"

    def test_device_router_zenossdevice_delete(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.delete('delete')
        assert resp

    def test_device_router_zenossdevice_remodel(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        resp = d.remodel()
        assert resp == "8735c0ba-0091-474d-8475-2ae4217aba32"

    def test_device_router_zenosscomponent_set_monitored(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        c = d.get_component('hw/cpus/0')
        resp = c.set_monitored(False)
        assert resp == "Set monitoring to False for 1 components."

    def test_device_router_zenosscomponent_lock(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        c = d.get_component('hw/cpus/0')
        resp = c.lock(updates=True, deletion=True)
        assert resp == "Locked 1 components."

    def test_device_router_zenosscomponent_lock_for_updates(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        c = d.get_component('hw/cpus/0')
        resp = c.lock_for_updates()
        assert resp == "Locked 1 components."

    def test_device_router_zenosscomponent_lock_for_deletion(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        c = d.get_component('hw/cpus/0')
        resp = c.lock_for_deletion()
        assert resp == "Locked 1 components."

    def test_device_router_zenosscomponent_delete(self, responses):
        responses_callback(responses)

        dr = DeviceRouter(url, headers, True)
        dc = dr.get_device_class('Server/TEST')
        d = dc.get_device('test.example.com')
        c = d.get_component('hw/cpus/0')
        resp = c.delete()
        assert resp == "Components deleted."
