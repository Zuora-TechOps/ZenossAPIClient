success = {
    "uuid": "8bf7e570-67cd-4670-a37c-0999fd07f9bf",
    "action": "EventsRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}

fail = {
    "uuid": "8bf7e570-67cd-4670-a37c-0999fd07f9bf",
    "action": "EventsRouter",
    "result": {
        "msg": "ServiceResponseError: Not Found",
        "type": "exception",
        "success": False
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}

events_query = {
    "uuid": "eadafce3-12ba-44ed-b1aa-e6ffdf6e98c6",
    "action": "EventsRouter",
    "result": {
        "totalCount": 50,
        "events": [
            {
                "prodState": "Production",
                "firstTime": 1505865565.822,
                "facility": None,
                "eventClassKey": "csm.sessionFailed",
                "agent": "zenpython",
                "dedupid": "test.example.com|test-01|/Status|ZenPacks.zenoss.NetAppMonitor.datasource_plugins.NetAppMonitorCmodeEventsDataSourcePlugin.NetAppMonitorCmodeEventsDataSourcePlugin|60|3",
                "Location": [
                    {
                        "uid": "/zport/dmd/Locations/Moon Base Alpha",
                        "name": "/Moon Base Alpha"
                    }
                ],
                "ownerid": "zenoss",
                "eventClass": {
                    "text": "/Status",
                    "uid": "/zport/dmd/Events/Status"
                },
                "id": "02420a11-0015-98b9-11e7-9d96ae351999",
                "DevicePriority": "Normal",
                "monitor": "localhost",
                "priority": None,
                "details": {
                    "node": [
                        "test-01"
                    ],
                    "recvtime": [
                        "1508797427"
                    ],
                    "zenoss.device.location": [
                        "/Moon Base Alpha"
                    ],
                    "zenoss.device.priority": [
                        "3"
                    ],
                    "zenoss.device.device_class": [
                        "/Storage/NetApp/C-Mode"
                    ],
                    "seq-num": [
                        "647604"
                    ],
                    "source": [
                        "CsmMpAgentThread"
                    ],
                    "manager": [
                        "13a1a22ff067"
                    ],
                    "message-name": [
                        "csm.sessionFailed"
                    ],
                    "resolution": [
                        "If you can reach the storage failover (SFO) partner of the target appliance, initiate a storage failover (takeover) of any aggregates on the target appliance. Then perform a 'sendhome' operation on these aggregates after the target appliance is operational again. Examine the network between the initiating appliance and the target appliance for problems. "
                    ],
                    "eventClassMapping": [
                        "/Status/failureNoFrames"
                    ],
                    "time": [
                        "1508797427"
                    ],
                    "zenoss.device.production_state": [
                        "1000"
                    ],
                    "zenoss.device.ip_address": [
                        "1.2.3.4"
                    ],
                    "event": [
                        "csm.sessionFailed: Cluster interconnect session (req=test-01:dblade, rsp=test-01:dblade, uniquifier=11055c3e278e5cc8) failed with record state ACTIVE and error CSM_CONNABORTED. "
                    ]
                },
                "DeviceClass": [
                    {
                        "uid": "/zport/dmd/Devices/Storage/NetApp/C-Mode",
                        "name": "/Storage/NetApp/C-Mode"
                    }
                ],
                "eventKey": "ZenPacks.zenoss.NetAppMonitor.datasource_plugins.NetAppMonitorCmodeEventsDataSourcePlugin.NetAppMonitorCmodeEventsDataSourcePlug",
                "evid": "02420a11-0015-98b9-11e7-9d96ae351999",
                "eventClassMapping": {
                    "uuid": "1337d66f-d5fa-4c3b-8198-bcfedf83d040",
                    "name": "failureNoFrames"
                },
                "component": {
                    "url": "/zport/dmd/goto?guid=08c40deb-1009-4634-a529-d66631391733",
                    "text": "test-01",
                    "uid": "/zport/dmd/Devices/Storage/NetApp/C-Mode/devices/test.example.com/systemnodes/test-01",
                    "uuid": "08c40deb-1009-4634-a529-d66631391733"
                },
                "clearid": None,
                "DeviceGroups": [],
                "eventGroup": None,
                "device": {
                    "url": "/zport/dmd/goto?guid=02e21618-b30a-47bf-8591-471c70570932",
                    "text": "test.example.com",
                    "uuid": "02e21618-b30a-47bf-8591-471c70570932",
                    "uid": "/zport/dmd/Devices/Storage/NetApp/C-Mode/devices/test.example.com"
                },
                "message": "csm.sessionFailed: Cluster interconnect session (req=test-01:dblade, rsp=test-01:dblade, uniquifier=11055c3e278e5cc8) failed with record state ACTIVE and error CSM_CONNABORTED. \nResolution: If you can reach the storage failover (SFO) partner of the target appliance, initiate a storage failover (takeover) of any aggregates on the target appliance. Then perform a 'sendhome' operation on these aggregates after the target appliance is operational again. Examine the network between the initiating appliance and the target appliance for problems. ",
                "severity": 3,
                "count": 66,
                "stateChange": 1507054918.83,
                "ntevid": None,
                "summary": "csm.sessionFailed: Cluster interconnect session (req=test-01:dblade, rsp=test-01:dblade, uniquifier=11055c3e278e5cc8) failed with record state ACTIVE and error CSM_CONNABORTED. ",
                "eventState": "Acknowledged",
                "lastTime": 1508797479.194,
                "ipAddress": [
                    "1.2.3.4"
                ],
                "Systems": []
            }
        ],
        "success": True,
        "asof": 1508797504.409547
    },
    "tid": 1,
    "type": "rpc",
    "method": "query"
}

events_query_evid = {
    "uuid": "eadafce3-12ba-44ed-b1aa-e6ffdf6e98c6",
    "action": "EventsRouter",
    "result": {
        "totalCount": 50,
        "events": [
            {
                "evid": "02420a11-0015-98b9-11e7-9d96ae351999"
            }
        ],
        "success": True,
        "asof": 1508797504.409547
    },
    "tid": 1,
    "type": "rpc",
    "method": "query"
}

event_detail = {
    "uuid": "23f0bbd9-b6a3-46bb-909f-aa53891dfbf5",
    "action": "EventsRouter",
    "result": {
        "event": [
            {
                "prodState": "Production",
                "firstTime": 1505865565.822,
                "device_uuid": "02e21618-b30a-47bf-8591-471c70570932",
                "eventClassKey": "smc.snapmir.unexpected.err",
                "agent": "zenpython",
                "dedupid": "test.example.com|test-01|/Status|ZenPacks.zenoss.NetAppMonitor.datasource_plugins.NetAppMonitorCmodeEventsDataSourcePlugin.NetAppMonitorCmodeEventsDataSourcePlugin|60|3",
                "Location": [
                    {
                        "uid": "/zport/dmd/Locations/Moon Base Alpha",
                        "name": "/Moon Base Alpha"
                    }
                ],
                "component_url": "/zport/dmd/goto?guid=08c40deb-1009-4634-a529-d66631391733",
                "ownerid": "zenoss",
                "eventClassMapping_url": "/zport/dmd/goto?guid=1337d66f-d5fa-4c3b-8198-bcfedf83d040",
                "eventClass": "/Status",
                "id": "02420a11-0015-98b9-11e7-9d96ae351999",
                "device_title": "test.example.com",
                "DevicePriority": "Normal",
                "log": [
                    [
                        "zenoss",
                        1507054918830,
                        "state changed to Acknowledged"
                    ]
                ],
                "facility": None,
                "eventClass_url": "/zport/dmd/Events/Status",
                "monitor": "localhost",
                "priority": None,
                "device_url": "/zport/dmd/goto?guid=02e21618-b30a-47bf-8591-471c70570932",
                "details": [
                    {
                        "key": "event",
                        "value": "smc.snapmir.unexpected.err: SnapMirror unexpected error 'Destination volume \"cg_name_wildcard\" was not found. It may have been moved.(Failed to get volume attributes for twoaggrdav.(Volume is not known or has been moved))'. Relationship UUID ' '. "
                    },
                    {
                        "key": "eventClassMapping",
                        "value": "/Status/failureNoFrames"
                    },
                    {
                        "key": "manager",
                        "value": "13a1a22ff067"
                    },
                    {
                        "key": "message-name",
                        "value": "smc.snapmir.unexpected.err"
                    },
                    {
                        "key": "node",
                        "value": "test-01"
                    },
                    {
                        "key": "recvtime",
                        "value": "1508798161"
                    },
                    {
                        "key": "resolution",
                        "value": "If the problem persists, contact NetApp technical support. "
                    },
                    {
                        "key": "seq-num",
                        "value": "647654"
                    },
                    {
                        "key": "source",
                        "value": "sm_logger_main"
                    },
                    {
                        "key": "time",
                        "value": "1508798161"
                    },
                    {
                        "key": "zenoss.device.device_class",
                        "value": "/Storage/NetApp/C-Mode"
                    },
                    {
                        "key": "zenoss.device.ip_address",
                        "value": "1.2.3.4"
                    },
                    {
                        "key": "zenoss.device.location",
                        "value": "/Moon Base Alpha"
                    },
                    {
                        "key": "zenoss.device.priority",
                        "value": "3"
                    },
                    {
                        "key": "zenoss.device.production_state",
                        "value": "1000"
                    }
                ],
                "DeviceClass": [
                    {
                        "uid": "/zport/dmd/Devices/Storage/NetApp/C-Mode",
                        "name": "/Storage/NetApp/C-Mode"
                    }
                ],
                "eventKey": "ZenPacks.zenoss.NetAppMonitor.datasource_plugins.NetAppMonitorCmodeEventsDataSourcePlugin.NetAppMonitorCmodeEventsDataSourcePlug",
                "evid": "02420a11-0015-98b9-11e7-9d96ae351999",
                "eventClassMapping": "failureNoFrames",
                "component": "test-01",
                "clearid": None,
                "DeviceGroups": [],
                "eventGroup": None,
                "device": "test.example.com",
                "Systems": [],
                "component_title": "test-01",
                "severity": 3,
                "count": 66,
                "stateChange": 1507054918.83,
                "ntevid": None,
                "summary": "smc.snapmir.unexpected.err: SnapMirror unexpected error 'Destination volume \"cg_name_wildcard\" was not found. It may have been moved.(Failed to get volume attributes for twoaggrdav.(Volume is not known or has been moved))'. Relationship UUID ' '. ",
                "message": "smc.snapmir.unexpected.err: SnapMirror unexpected error 'Destination volume \"cg_name_wildcard\" was not found. It may have been moved.(Failed to get volume attributes for twoaggrdav.(Volume is not known or has been moved))'. Relationship UUID ' '. \nResolution: If the problem persists, contact NetApp technical support. ",
                "eventState": "Acknowledged",
                "lastTime": 1508798199.186,
                "ipAddress": [
                    "1.2.3.4"
                ],
                "component_uuid": "08c40deb-1009-4634-a529-d66631391733"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}

events_config = {
    "uuid": "7f7109f2-1a6f-41f5-a12f-bbd95f280b9c",
    "action": "EventsRouter",
    "result": {
        "data": [
            {
                "xtype": "eventageseverity",
                "defaultValue": 4,
                "id": "event_age_disable_severity",
                "value": 4,
                "name": "Don't Age This Severity and Above"
            },
            {
                "defaultValue": False,
                "id": "event_age_severity_inclusive",
                "value": False,
                "xtype": "hidden"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getConfig"
}

add_event_evid_query = {
    "uuid": "6700ab59-c559-42ec-959b-ebc33bc52257",
    "action": "EventsRouter",
    "result": {
        "totalCount": 1,
        "events": [
            {
                "evid": "02420a11-000c-a561-11e7-ba9b510182b3",
            }
        ],
        "success": True,
        "asof": 1509056503.945677
    },
    "tid": 1,
    "type": "rpc",
    "method": "query"
}

add_event_detail = {
    "uuid": "c54074e8-af8b-4e40-a679-7dbe314709ed",
    "action": "EventsRouter",
    "result": {
        "event": [
            {
                "prodState": None,
                "firstTime": 1509056189.91,
                "device_uuid": None,
                "eventClassKey": None,
                "agent": None,
                "dedupid": "Heart of Gold|Arthur Dent|/Status|3|Out of Tea",
                "Location": [],
                "component_url": None,
                "ownerid": None,
                "eventClassMapping_url": None,
                "eventClass": "/Status",
                "id": "02420a11-000c-a561-11e7-ba9b510182b3",
                "device_title": "Heart of Gold",
                "DevicePriority": None,
                "log": [
                    [
                        "zenoss",
                        1509057815980,
                        "<p>Test log entry</p>"
                    ]
                ],
                "facility": None,
                "eventClass_url": "/zport/dmd/Events/Status",
                "monitor": None,
                "priority": None,
                "device_url": None,
                "details": [],
                "DeviceClass": [],
                "eventKey": "",
                "evid": "02420a11-000c-a561-11e7-ba9b510182b3",
                "eventClassMapping": None,
                "component": "Arthur Dent",
                "clearid": None,
                "DeviceGroups": [],
                "eventGroup": None,
                "device": "Heart of Gold",
                "Systems": [],
                "component_title": "Arthur Dent",
                "severity": 3,
                "count": 1,
                "stateChange": 1509056189.91,
                "ntevid": None,
                "summary": "Out of Tea",
                "message": "Out of Tea",
                "eventState": "New",
                "lastTime": 1509056189.91,
                "ipAddress": "",
                "component_uuid": None
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}
