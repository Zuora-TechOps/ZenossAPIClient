tz = {
    "uuid": "93e16a10-d4c7-419f-93fa-4e5bc50ca076",
    "action": "DeviceManagementRouter",
    "result": {
        "data": "UTC",
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getTimeZone"
}

windows = {
    "uuid": "7b1aa255-096a-4818-bb53-3028beaa7572",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            {
                "niceRepeat": "Never",
                "startProdState": "Maintenance",
                "repeat": "Never",
                "occurrence": "1st",
                "startState": 300,
                "started": None,
                "skip": 1,
                "duration": "01:00:00",
                "enabled": False,
                "days": "Sunday",
                "name": "TestWindow",
                "start": 1510930800,
                "meta_type": "MaintenanceWindow",
                "startTime": "2017/11/17 15:00:00.000 UTC",
                "inspector_type": "MaintenanceWindow",
                "uid": "/zport/dmd/Devices/Server/TEST/maintenanceWindows/TestWindow",
                "id": "TestWindow",
                "description": ""
            },
            {
                "niceRepeat": "1st Friday of the month",
                "startProdState": "Maintenance",
                "repeat": "Monthly: day of week",
                "occurrence": "1st",
                "startState": 300,
                "started": None,
                "skip": 1,
                "duration": "01:00:00",
                "enabled": False,
                "days": "Friday",
                "name": "TestWindowRepeat",
                "start": 1510930800,
                "meta_type": "MaintenanceWindow",
                "startTime": "2017/11/17 15:00:00.000 UTC",
                "inspector_type": "MaintenanceWindow",
                "uid": "/zport/dmd/Devices/Server/TEST/maintenanceWindows/TestWindowRepeat",
                "id": "TestWindowRepeat",
                "description": ""
            },
            {
                "niceRepeat": "Never",
                "startProdState": "Maintenance",
                "repeat": "Never",
                "occurrence": "1st",
                "startState": 300,
                "started": None,
                "skip": 1,
                "duration": "01:00:00",
                "enabled": False,
                "days": "Sunday",
                "name": "TestAddWindow",
                "start": 1511204287.20076,
                "meta_type": "MaintenanceWindow",
                "startTime": "2017/11/20 18:58:07.000 UTC",
                "inspector_type": "MaintenanceWindow",
                "uid": "/zport/dmd/Devices/Server/TEST/maintenanceWindows/TestAddWindow",
                "id": "TestAddWindow",
                "description": ""
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getMaintWindows"
}

add_maint = {
    "uuid": "eba4e39b-cad1-4b53-ab86-d2a5f126a991",
    "action": "DeviceManagementRouter",
    "result": {
        "msg": "Maintenance Window TestAddWindow added successfully.",
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "addMaintWindow"
}

test_add = {
    "uuid": "5ed83a5d-bc49-46c6-b30d-3d7bac7bf4c3",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getMaintWindows"
}

delete_maint = {
    "uuid": "190220ac-e119-4923-b1f5-767d8138765f",
    "action": "DeviceManagementRouter",
    "result": {
        "data": None,
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "deleteMaintWindow"
}

update_maint = {
    "uuid": "c9e72e83-f061-45d6-9c8e-4cc11156fee2",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            {
                "niceRepeat": "Never",
                "startProdState": "Maintenance",
                "repeat": "Never",
                "occurrence": "2nd",
                "startState": 300,
                "started": None,
                "skip": 1,
                "duration": "01:30:00",
                "enabled": False,
                "days": "Monday",
                "name": "TestAddWindow",
                "start": 1511267400,
                "meta_type": "MaintenanceWindow",
                "startTime": "2017/11/21 12:30:00.000 UTC",
                "inspector_type": "MaintenanceWindow",
                "uid": "/zport/dmd/Devices/Server/TEST/maintenanceWindows/TestAddWindow",
                "id": "TestAddWindow",
                "description": ""
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "editMaintWindow"
}

user_commands = {
    "uuid": "9157db75-274a-4cec-b7ce-335ff7fce133",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            {
                "description": "Name to IP address lookup",
                "name": "DNS forward",
                "meta_type": "UserCommand",
                "command": "host ${device/id}",
                "inspector_type": "UserCommand",
                "id": "DNS forward",
                "uid": "/zport/dmd/userCommands/DNS forward"
            },
            {
                "description": "IP address to name lookup",
                "name": "DNS reverse",
                "meta_type": "UserCommand",
                "command": "host ${device/manageIp}",
                "inspector_type": "UserCommand",
                "id": "DNS reverse",
                "uid": "/zport/dmd/userCommands/DNS reverse"
            },
            {
                "description": "Is the device responding to ping?",
                "name": "ping",
                "meta_type": "UserCommand",
                "command": "${device/pingCommand} -c2 ${device/manageIp}",
                "inspector_type": "UserCommand",
                "id": "ping",
                "uid": "/zport/dmd/userCommands/ping"
            },
            {
                "description": "Display the OIDs available on a device",
                "name": "snmpwalk",
                "meta_type": "UserCommand",
                "command": "snmpwalk -${device/zSnmpVer} -c${device/zSnmpCommunity} ${device/snmpwalkPrefix}${here/manageIp} system",
                "inspector_type": "UserCommand",
                "id": "snmpwalk",
                "uid": "/zport/dmd/userCommands/snmpwalk"
            },
            {
                "description": "snmp version v3 Display the OIDs available on a device",
                "name": "snmpwalk_v3",
                "meta_type": "UserCommand",
                "command": "snmpwalk -${device/zSnmpVer} -l authPriv -a ${device/zSnmpAuthType} -x ${device/zSnmpPrivType} -A ${device/zSnmpAuthPassword} -X ${device/zSnmpPrivPassword} -u ${device/zSnmpSecurityName} ${device/snmpwalkPrefix}${here/manageIp}:${device/zSnmpPort} 1.3.6.1.2.1.25.2.3.1",
                "inspector_type": "UserCommand",
                "id": "snmpwalk_v3",
                "uid": "/zport/dmd/userCommands/snmpwalk_v3"
            },
            {
                "description": "Show the route to the device",
                "name": "traceroute",
                "meta_type": "UserCommand",
                "command": "${device/tracerouteCommand} -q 1 -w 2 ${device/manageIp}",
                "inspector_type": "UserCommand",
                "id": "traceroute",
                "uid": "/zport/dmd/userCommands/traceroute"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getUserCommands"
}

add_user_command = {
    "uuid": "cd50fa2c-4099-4e42-bd44-8a24d018b380",
    "action": "DeviceManagementRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "addUserCommand"
}

add_uc_bad_password = {
    "uuid": "859d530b-9a66-4a2e-8a9f-10e57a73de4d",
    "action": "DeviceManagementRouter",
    "result": {
        "msg": "Exception: Add new command failed. Incorrect or missing password.",
        "type": "exception",
        "success": False
    },
    "tid": 1,
    "type": "rpc",
    "method": "addUserCommand"
}

added_uc = {
    "uuid": "9157db75-274a-4cec-b7ce-335ff7fce133",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            {
                "description": "uname -a",
                "name": "uname_a",
                "meta_type": "UserCommand",
                "command": "uname -a",
                "inspector_type": "UserCommand",
                "id": "uname_a",
                "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/userCommands/uname_a"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getUserCommands"
}

delete_uc = {
    "uuid": "54aef422-46bd-4ea8-a32a-1ffc5cd18650",
    "action": "DeviceManagementRouter",
    "result": {
        "data": None,
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "deleteUserCommand"
}

update_uc = {
    "uuid": "f01f1c8f-abf9-4b4a-a4c2-5d4dfcaae876",
    "action": "DeviceManagementRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "updateUserCommand"
}

update_uc_bad_passwd = {
    "uuid": "658bf790-c4e9-4427-aa5c-e763281d8731",
    "action": "DeviceManagementRouter",
    "result": {
        "msg": "Exception: Update failed. Incorrect or missing password.",
        "type": "exception",
        "success": False
    },
    "tid": 1,
    "type": "rpc",
    "method": "updateUserCommand"
}

updated_uc = {
    "uuid": "9157db75-274a-4cec-b7ce-335ff7fce133",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            {
                "description": "uname -a",
                "name": "uname_a",
                "meta_type": "UserCommand",
                "command": "uname -a",
                "inspector_type": "UserCommand",
                "id": "uname_a",
                "uid": "/zport/dmd/Devices/Server/TEST/devices/test2.example.com/userCommands/uname_a"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getUserCommands"
}

user_list = {
    "uuid": "a4923782-2efc-48a1-a591-043b3d14c976",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            "admin",
            "ccuser",
            "lenny",
            "zenoss_system"
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getUserList"
}

roles_list = {
    "uuid": "dbd64697-73a5-402b-820d-fd01f9db4a05",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            "Manager",
            "ZenManager",
            "ZenOperator",
            "ZenUser"
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getRolesList"
}

admin_roles = {
    "uuid": "2fc85112-ca3b-4778-b3fe-54686c4a434e",
    "action": "DeviceManagementRouter",
    "result": {
        "data": [
            {
                "description": "",
                "name": "admin",
                "id": "admin",
                "meta_type": "AdministrativeRole",
                "role": "ZenManager",
                "inspector_type": "AdministrativeRole",
                "pager": "",
                "email": "",
                "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/adminRoles/admin"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getAdminRoles"
}

remove_admin = {
    "uuid": "76001a52-2f8e-42cd-b582-e9de5e9644b5",
    "action": "DeviceManagementRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "removeAdmin"
}

add_admin = {
    "uuid": "7a12bc91-0d66-4653-92eb-5813175a0ff0",
    "action": "DeviceManagementRouter",
    "result": {
        "msg": "New Administrator added successfully.",
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "addAdminRole"
}

update_admin = {
    "uuid": "cca5e9ec-32c2-4a0f-8659-ee006bf87bdc",
    "action": "DeviceManagementRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "updateAdminRole"
}

delete_admin = {
    "uuid": "1176f85f-1a27-4d8b-8c4a-e00b952e812b",
    "action": "DeviceManagementRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "removeAdmin"
}
