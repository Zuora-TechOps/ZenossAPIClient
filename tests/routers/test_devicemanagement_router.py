import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.devicemanagement import DeviceManagementRouter, ZenossMaintenanceWindow, ZenossUserCommand, ZenossDeviceManagementAdmin
import devicemanagement_resp


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

    def getTimeZone(rdata):
        return devicemanagement_resp.tz

    def getMaintWindows(rdata):
        return devicemanagement_resp.windows

    def addMaintWindow(rdata):
        return devicemanagement_resp.add_maint

    def deleteMaintWindow(rdata):
        return devicemanagement_resp.delete_maint

    def editMaintWindow(rdata):
        return devicemanagement_resp.update_maint

    def getUserCommands(rdata):
        if rdata['uid'] == "Devices/Server/TEST/devices/test.example.com":
            return devicemanagement_resp.added_uc
        elif rdata['uid'] == "Devices/Server/TEST/devices/test2.example.com":
            return devicemanagement_resp.updated_uc
        else:
            return devicemanagement_resp.user_commands

    def addUserCommand(rdata):
        if rdata['password'] == "zenoss":
            return devicemanagement_resp.add_user_command
        else:
            return devicemanagement_resp.add_uc_bad_password

    def deleteUserCommand(rdata):
        return devicemanagement_resp.delete_uc

    def updateUserCommand(rdata):
        if rdata['params']['password'] == "zenoss":
            devicemanagement_resp.updated_uc['result']['data'][0]['description'] = rdata['params']['description']
            devicemanagement_resp.updated_uc['result']['data'][0]['command'] = rdata['params']['command']
            return devicemanagement_resp.update_uc
        else:
            return devicemanagement_resp.update_uc_bad_passwd

    def getUserList(rdata):
        return devicemanagement_resp.user_list

    def getRolesList(rdata):
        return devicemanagement_resp.roles_list

    def getAdminRoles(rdata):
        return devicemanagement_resp.admin_roles

    def addAdminRole(rdata):
        devicemanagement_resp.admin_roles['result']['data'].append(
            {
                "description": "",
                "name": "lenny",
                "id": "lenny",
                "meta_type": "AdministrativeRole",
                "role": "ZenUser",
                "inspector_type": "AdministrativeRole",
                "pager": "",
                "email": "lenny@example.com",
                "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/adminRoles/lenny"
            }
        )
        return devicemanagement_resp.add_admin

    def updateAdminRole(rdata):
        devicemanagement_resp.admin_roles['result']['data'][1]['role'] = rdata['params']['role']
        return devicemanagement_resp.update_admin

    def removeAdmin(rdata):
        devicemanagement_resp.admin_roles['result']['data'].pop(1)
        return devicemanagement_resp.delete_admin

    method = locals()[rdata['method']]
    resp_body = method(rdata['data'][0])

    return (200, resp_headers, json.dumps(resp_body))


def responses_callback(responses):
    responses.add_callback(
        responses.POST,
        '{0}/devicemanagement_router'.format(url),
        callback=request_callback,
        content_type='application/json',
    )


class TestDeviceManagementRouter(object):

    def test_devicemanagement_router_init(self):
        dmr = DeviceManagementRouter(url, headers, False)
        assert dmr.uid is None

    def test_devicemanagement_router_timezone(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.timezone()
        assert resp == "UTC"

    def test_devicemanagement_router_list_maintenance_windows(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.list_maintenance_windows('Server/TEST')
        assert len(resp) == 3
        assert resp[0]['name'] == "TestWindow"
        assert resp[0]['uid'] == "Devices/Server/TEST/maintenanceWindows/TestWindow"
        assert resp[1]['name'] == "TestWindowRepeat"
        assert resp[1]['uid'] == "Devices/Server/TEST/maintenanceWindows/TestWindowRepeat"

    def test_devicemanagement_router_get_maintenance_windows(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_maintenance_windows('Server/TEST')
        assert len(resp) == 3
        assert isinstance(resp[0], ZenossMaintenanceWindow)
        assert isinstance(resp[1], ZenossMaintenanceWindow)
        assert resp[0].name == "TestWindow"
        assert resp[1].name == "TestWindowRepeat"
        assert resp[0].repeat == "Never"
        assert resp[1].repeat == "Monthly: day of week"
        assert resp[0].parent == "Devices/Server/TEST"
        assert resp[1].parent == "Devices/Server/TEST"
        assert resp[0].startDate == "2017/11/17"
        assert resp[0].startHours == "15"
        assert resp[0].startMinutes == "00"
        assert resp[0].durationDays is None
        assert resp[0].durationHours == "01"
        assert resp[0].durationMinutes == "00"

    def test_devicemanagement_router_add_maintenance_window(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.add_maintenance_window('Server/TEST', 'TestAddWindow', '1511290393', '01:00:00')
        assert isinstance(resp, ZenossMaintenanceWindow)
        assert resp.name == "TestAddWindow"
        assert resp.parent == "Devices/Server/TEST"

    def test_devicemanagement_router_add_maintenance_window_bad_repeat(self):
        dmr = DeviceManagementRouter(url, headers, False)
        with pytest.raises(ZenossAPIClientError, message="Request failed: Invalid maintenance window repetition: Bogus"):
            resp = dmr.add_maintenance_window('Server/TEST', 'TestAddWindow', '1511290393', '01:00:00', repeat='Bogus')

    def test_devicemanagement_router_add_maintenance_window_bad_occurrence(self):
        dmr = DeviceManagementRouter(url, headers, False)
        with pytest.raises(ZenossAPIClientError, message="Request failed: Invalid maintenance window occurrence: Bogus"):
            resp = dmr.add_maintenance_window('Server/TEST', 'TestAddWindow', '1511290393', '01:00:00', occurrence='Bogus')

    def test_devicemanagement_router_add_maintenance_window_bad_days(self):
        dmr = DeviceManagementRouter(url, headers, False)
        with pytest.raises(ZenossAPIClientError, message="Request failed: Invalid maintenance window days: Bogus"):
            resp = dmr.add_maintenance_window('Server/TEST', 'TestAddWindow', '1511290393', '01:00:00', days='Bogus')

    def test_devicemanagement_router_list_user_commands(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.list_user_commands('Server/TEST')
        assert len(resp) == 6
        assert resp[0]['id'] == "DNS forward"
        assert resp[1]['id'] == "DNS reverse"
        assert resp[2]['id'] == "ping"
        assert resp[3]['id'] == "snmpwalk"
        assert resp[4]['id'] == "snmpwalk_v3"
        assert resp[5]['id'] == "traceroute"

    def test_devicemanagement_router_get_user_commands(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_user_commands('Server/TEST')
        assert len(resp) == 6
        assert resp[0].id == "DNS forward"
        assert resp[0].parent == "Devices/Server/TEST"
        assert resp[1].id == "DNS reverse"
        assert resp[1].parent == "Devices/Server/TEST"
        assert resp[2].id == "ping"
        assert resp[2].parent == "Devices/Server/TEST"
        assert resp[3].id == "snmpwalk"
        assert resp[3].parent == "Devices/Server/TEST"
        assert resp[4].id == "snmpwalk_v3"
        assert resp[4].parent == "Devices/Server/TEST"
        assert resp[5].id == "traceroute"
        assert resp[5].parent == "Devices/Server/TEST"

    def test_devicemanagement_router_get_user_command_by_id(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_user_command_by_id('Server/TEST', 'DNS forward')
        assert isinstance(resp, ZenossUserCommand)
        assert resp.id == "DNS forward"
        assert resp.description == "Name to IP address lookup"
        assert resp.meta_type == "UserCommand"
        assert resp.name == "DNS forward"
        assert resp.command == "host ${device/id}"
        assert resp.uid == "userCommands/DNS forward"
        assert resp.parent == "Devices/Server/TEST"

    def test_devicemanagement_router_get_user_command_by_name(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_user_command_by_name('Server/TEST', 'ping')
        assert isinstance(resp, ZenossUserCommand)
        assert resp.id == "ping"
        assert resp.description == "Is the device responding to ping?"
        assert resp.meta_type == "UserCommand"
        assert resp.name == "ping"
        assert resp.command == "${device/pingCommand} -c2 ${device/manageIp}"
        assert resp.uid == "userCommands/ping"
        assert resp.parent == "Devices/Server/TEST"

    def test_devicemanagement_router_add_user_command(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.add_user_command('Server/TEST/devices/test.example.com', 'uname_a', 'uname -a', 'uname -a', 'zenoss')
        assert isinstance(resp, ZenossUserCommand)
        assert resp.id == "uname_a"
        assert resp.command == "uname -a"

    def test_devicemanagement_router_add_user_command_bad_password(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        with pytest.raises(ZenossAPIClientError, message="Request failed: Exception: Add new command failed. Incorrect or missing password."):
            resp = dmr.add_user_command('Server/TEST/devices/test.example.com', 'uname_a', 'uname -a', 'uname -a', 'bogus')

    def test_devicemanagement_router_list_admin_users(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.list_users('Server/TEST/devices/test.example.com')
        assert len(resp) == 4
        assert resp == ['admin', 'ccuser', 'lenny', 'zenoss_system']

    def test_devicemanagement_router_list_available_roles(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.list_available_roles('Server/TEST/devices/test.example.com')
        assert len(resp) == 4
        assert resp == ['Manager', 'ZenManager', 'ZenOperator', 'ZenUser']

    def test_devicemanagement_router_list_admin_roles(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.list_admin_roles('Server/TEST/devices/test.example.com')
        assert len(resp) == 1
        assert resp[0]['name'] == "admin"

    def test_devicemanagement_router_get_admins(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_admins('Server/TEST/devices/test.example.com')
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossDeviceManagementAdmin)
        assert resp[0].uid == "Devices/Server/TEST/devices/test.example.com/adminRoles/admin"

    def test_devicemanagement_router_list_admins_by_role(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.list_admins_by_role('Server/TEST/devices/test.example.com', 'ZenManager')
        assert len(resp) == 1

    def test_devicemanagement_router_get_admins_by_role(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_admins_by_role('Server/TEST/devices/test.example.com', 'ZenManager')
        assert len(resp) == 1
        assert isinstance(resp[0], ZenossDeviceManagementAdmin)

    def test_devicemanagement_router_get_admin_by_name(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_admin_by_name('Server/TEST/devices/test.example.com', 'admin')
        assert isinstance(resp, ZenossDeviceManagementAdmin)
        assert resp.name == "admin"

    def test_devicemanagement_router_get_admin_by_id(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.get_admin_by_id('Server/TEST/devices/test.example.com', 'admin')
        assert isinstance(resp, ZenossDeviceManagementAdmin)
        assert resp.name == "admin"

    def test_devicemanagement_router_add_admin(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        resp = dmr.add_admin('Server/TEST/devices/test.example.com', 'lenny', 'ZenUser')
        assert isinstance(resp, ZenossDeviceManagementAdmin)
        assert resp.name == "lenny"
        assert resp.role == "ZenUser"
        assert resp.uid == "Devices/Server/TEST/devices/test.example.com/adminRoles/lenny"

    def test_devicemanagement_router_zenossmaintenancewindow_delete(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        mw = dmr.get_maintenance_window('Server/TEST', 'TestAddWindow')
        resp = mw.delete()
        assert resp['data'] is None

    def test_devicemanagement_router_zenossmaintenancewindow_update(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        mw = dmr.get_maintenance_window('Server/TEST', 'TestAddWindow')
        resp = mw.update(start_date='2017/11/21', start_hours='12', start_minutes='30', duration_minutes='30', occurrence='2nd', days='Monday')
        assert resp
        assert mw.duration == "01:30:00"
        assert mw.start == 1511267400
        assert mw.startTime == "2017/11/21 12:30:00.000 UTC"

    def test_devicemanagement_router_zenossmaintenancewindow_enable(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        mw = dmr.get_maintenance_window('Server/TEST', 'TestAddWindow')
        resp = mw.enable()
        assert resp
        assert mw.enabled

    def test_devicemanagement_router_zenossmaintenancewindow_disable(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        mw = dmr.get_maintenance_window('Server/TEST', 'TestAddWindow')
        mw.enabled = True
        resp = mw.disable()
        assert resp
        assert mw.enabled is False

    def test_devicemanagement_router_zenossusercommand_delete(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        uc = dmr.get_user_command_by_name('Server/TEST/devices/test.example.com', 'uname_a')
        resp = uc.delete()
        assert resp['data'] is None

    def test_devicemanagement_router_zenossusercommand_update(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        uc = dmr.get_user_command_by_name('Server/TEST/devices/test2.example.com', 'uname_a')
        resp = uc.update(description="Run uname -a command", password="zenoss")
        assert resp
        assert uc.description == "Run uname -a command"

    def test_devicemanagement_router_zenossusercommand_update_bad_passwd(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        uc = dmr.get_user_command_by_name('Server/TEST/devices/test2.example.com', 'uname_a')
        with pytest.raises(ZenossAPIClientError, message="Request failed: Exception: Update failed. Incorrect or missing password."):
            resp = uc.update(description="Run uname -a command", password="bogus")

    def test_devicemanagement_router_zenossdevicemanagementadmin_update(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        au = dmr.get_admin_by_name('Devices/Server/TEST/devices/test.example.com', 'lenny')
        resp = au.update('ZenManager')
        assert resp
        assert au.role == "ZenManager"

    def test_devicemanagement_router_zenossdevicemanagementadmin_delete(self, responses):
        responses_callback(responses)

        dmr = DeviceManagementRouter(url, headers, False)
        au = dmr.get_admin_by_name('Devices/Server/TEST/devices/test.example.com', 'lenny')
        resp = au.delete()
        au = dmr.get_admin_by_name('Devices/Server/TEST/devices/test.example.com', 'lenny')
        assert au is None
