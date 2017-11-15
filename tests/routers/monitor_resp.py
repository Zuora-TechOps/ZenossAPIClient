tree = {
    "uuid": "b2781216-19ca-46d6-b4dc-2dbdf75e3909",
    "action": "MonitorRouter",
    "result": [
        {
            "leaf": False,
            "name": "localhost",
            "text": "localhost",
            "id": ".zport.dmd.Monitors.Hub.localhost",
            "devcount": 0,
            "path": "/zport/dmd/Monitors/Hub/localhost",
            "ccbacked": False,
            "type": "hub",
            "children": [
                {
                    "ccbacked": True,
                    "leaf": False,
                    "name": "localhost",
                    "text": "localhost",
                    "children": [],
                    "devcount": 0,
                    "path": "/zport/dmd/Monitors/Performance/localhost",
                    "type": "collector",
                    "id": ".zport.dmd.Monitors.Performance.localhost",
                    "uid": "/zport/dmd/Monitors/Performance/localhost"
                }
            ],
            "uid": "/zport/dmd/Monitors/Hub/localhost"
        },
        {
            "leaf": False,
            "name": "testhub",
            "text": "testhub",
            "id": ".zport.dmd.Monitors.Hub.testhub",
            "devcount": 0,
            "path": "/zport/dmd/Monitors/Hub/testhub",
            "ccbacked": False,
            "type": "hub",
            "children": [
                {
                    "ccbacked": True,
                    "leaf": False,
                    "name": "testcollector",
                    "text": "testcollector",
                    "children": [],
                    "devcount": 179,
                    "path": "/zport/dmd/Monitors/Performance/testcollector",
                    "type": "collector",
                    "id": ".zport.dmd.Monitors.Performance.testcollector",
                    "uid": "/zport/dmd/Monitors/Performance/testcollector"
                }
            ],
            "uid": "/zport/dmd/Monitors/Hub/testhub"
        }
    ],
    "tid": 1,
    "type": "rpc",
    "method": "getTree"
}

testcollector = {
    "uuid": "0de03747-255e-4efb-ac1b-d4b59dc3d277",
    "action": "MonitorRouter",
    "result": {
        "data": {
            "ccbacked": True,
            "leaf": False,
            "name": "testcollector",
            "text": "testcollector",
            "children": [],
            "devcount": 179,
            "path": "/zport/dmd/Monitors/Performance/testcollector",
            "type": "collector",
            "id": ".zport.dmd.Monitors.Performance.testcollector",
            "uid": "/zport/dmd/Monitors/Performance/testcollector"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

newcollector = {
    "uuid": "0de03747-255e-4efb-ac1b-d4b59dc3d277",
    "action": "MonitorRouter",
    "result": {
        "data": {
            "ccbacked": True,
            "leaf": False,
            "name": "newcollector",
            "text": "newcollector",
            "children": [],
            "devcount": 0,
            "path": "/zport/dmd/Monitors/Performance/newcollector",
            "type": "collector",
            "id": ".zport.dmd.Monitors.Performance.newcollector",
            "uid": "/zport/dmd/Monitors/Performance/newcollector"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

params = {
    "uuid": "418de426-356d-4535-b679-3ac4ac4360c4",
    "action": "MonitorRouter",
    "result": {
        "data": {
            "configCycleInterval": 360,
            "pingCycleInterval": 60,
            "discoveryNetworks": "",
            "description": "",
            "modelerCycleInterval": 720,
            "processCycleInterval": 180,
            "meta_type": "PerformanceConf",
            "wmiqueryTimeout": 100,
            "statusCycleInterval": 60,
            "eventlogCycleInterval": 60,
            "name": "testcollector",
            "wmibatchSize": 10,
            "pingTimeOut": 1.5,
            "winCycleInterval": 60,
            "pingTries": 2,
            "inspector_type": "PerformanceConf",
            "zenProcessParallelJobs": 10,
            "id": "testcollector",
            "uid": "/zport/dmd/Monitors/Performance/testcollector"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getCollector"
}

add = {
    "uuid": "1a539847-a89c-4047-9385-4ff697ec8195",
    "action": "MonitorRouter",
    "result": {
        "data": {
            "configCycleInterval": 360,
            "pingCycleInterval": 60,
            "discoveryNetworks": "",
            "description": "",
            "modelerCycleInterval": 720,
            "processCycleInterval": 180,
            "meta_type": "PerformanceConf",
            "wmiqueryTimeout": 100,
            "statusCycleInterval": 60,
            "eventlogCycleInterval": 60,
            "name": "newcollector",
            "wmibatchSize": 10,
            "pingTimeOut": 1.5,
            "winCycleInterval": 60,
            "pingTries": 2,
            "inspector_type": "PerformanceConf",
            "zenProcessParallelJobs": 10,
            "id": "newcollector",
            "uid": "/zport/dmd/Monitors/Performance/newcollector"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "addCollector"
}
