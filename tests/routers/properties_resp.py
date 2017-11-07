local_props = {
    "uuid": "cde7624a-3b4d-4947-baac-1d45d8f55f47",
    "action": "PropertiesRouter",
    "result": {
        "totalCount": 2,
        "data": [
            {
                "category": "Misc",
                "description": "",
                "islocal": 1,
                "value": "[{\"user\":\"mmm_agent\",\"passwd\":\"1quf82swe3\",\"port\":\"7014\"},{\"user\":\"mmm_agent\",\"passwd\":\"1quf82swe3\",\"port\":\"7031\"}]",
                "label": "zMySQLConnectionString",
                "valueAsString": "[{\"user\":\"mmm_agent\",\"passwd\":\"1quf82swe3\",\"port\":\"7014\"},{\"user\":\"mmm_agent\",\"passwd\":\"1quf82swe3\",\"port\":\"7031\"}]",
                "id": "zMySQLConnectionString",
                "path": "/Server/TEST/devices/test.example.com",
                "type": "multilinecredentials",
                "options": []
            },
            {
                "category": "Windows",
                "description": "Authentication domain trusted by zWinRMUser",
                "islocal": 1,
                "value": "Westeros",
                "label": "Windows Trusted Realm",
                "valueAsString": "Westeros",
                "id": "zWinTrustedRealm",
                "path": "/Server/TEST/devices/test.example.com",
                "type": "string",
                "options": []
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getZenProperties"
}

get_prop = {
    "uuid": "cde7624a-3b4d-4947-baac-1d45d8f55f47",
    "action": "PropertiesRouter",
    "result": {
        "totalCount": 1,
        "data": [
            {
                "category": "Windows",
                "description": "Authentication domain trusted by zWinRMUser",
                "islocal": 0,
                "value": "",
                "label": "Windows Trusted Realm",
                "valueAsString": "",
                "id": "zWinTrustedRealm",
                "path": "/",
                "type": "string",
                "options": []
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getZenProperties"
}

get_local_prop = {
    "uuid": "cde7624a-3b4d-4947-baac-1d45d8f55f47",
    "action": "PropertiesRouter",
    "result": {
        "totalCount": 1,
        "data": [
            {
                "category": "Windows",
                "description": "Authentication domain trusted by zWinRMUser",
                "islocal": 1,
                "value": "Westeros",
                "label": "Windows Trusted Realm",
                "valueAsString": "Westeros",
                "id": "zWinTrustedRealm",
                "path": "/Server/TEST/devices/test.example.com",
                "type": "string",
                "options": []
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getZenProperties"
}

props = {
    "uuid": "bf7a06f5-e5c6-4864-bcc9-7b9e615a800f",
    "action": "PropertiesRouter",
    "result": {
        "totalCount": 4,
        "data": [
            {
                "category": "Misc",
                "description": "",
                "islocal": 0,
                "value": 300,
                "label": "zAggregatorCollectionInterval",
                "valueAsString": 300,
                "id": "zAggregatorCollectionInterval",
                "path": "/",
                "type": "int",
                "options": []
            },
            {
                "category": "Misc",
                "description": "Indicates whether to log changes.",
                "islocal": 0,
                "value": False,
                "label": "Log Collector Changes?",
                "valueAsString": False,
                "id": "zCollectorLogChanges",
                "path": "/",
                "type": "boolean",
                "options": []
            },
            {
                "category": "Misc",
                "description": "",
                "islocal": 0,
                "value": "",
                "label": "zMySQLConnectionString",
                "valueAsString": "",
                "id": "zMySQLConnectionString",
                "path": "/",
                "type": "multilinecredentials",
                "options": []
            },
            {
                "category": "Windows",
                "description": "Authentication domain trusted by zWinRMUser",
                "islocal": 0,
                "value": "",
                "label": "Windows Trusted Realm",
                "valueAsString": "",
                "id": "zWinTrustedRealm",
                "path": "/",
                "type": "string",
                "options": []
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getZenProperties"
}

custom_props = {
    "uuid": "0a65ae37-76d0-442e-bc31-623b453c9e17",
    "action": "PropertiesRouter",
    "result": {
        "totalCount": 1,
        "data": [
            {
                "islocal": 0,
                "value": "1900/01/01 00:00:00 US/Central",
                "label": None,
                "valueAsString": "1900/01/01 00:00:00 US/Central",
                "id": "cDateTest",
                "path": "/",
                "type": "date",
                "options": []
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getCustomProperties"
}

custom_local_props = {
    "uuid": "0a65ae37-76d0-442e-bc31-623b453c9e17",
    "action": "PropertiesRouter",
    "result": {
        "totalCount": 1,
        "data": [
            {
                "islocal": 1,
                "value": "2017/12/19 00:00:00 US/Pacific",
                "label": None,
                "valueAsString": "2017/12/19 00:00:00 US/Pacific",
                "id": "cDateTest",
                "path": "/Server/TEST/devices/test.example.com",
                "type": "date",
                "options": []
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getCustomProperties"
}

set_prop = {
    "uuid": "09ebdcae-5000-424a-a24a-955173feb650",
    "action": "PropertiesRouter",
    "result": {
        "data": {
            "path": "/Server/TEST/devices/test.example.com",
            "type": "string",
            "options": [],
            "value": "Westeros",
            "valueAsString": "Westeros"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "setZenProperty"
}

delete_prop = {
    "uuid": "980dd3fa-e425-4bdb-b362-6fea72f4d211",
    "action": "PropertiesRouter",
    "result": {
        "data": None,
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "deleteZenProperty"
}

set_custom_prop = {
    "uuid": "be1c91bb-055e-47a2-bff4-08ca3a049a0a",
    "action": "PropertiesRouter",
    "result": {
        "data": {
            "path": "/Server/TEST/devices/test.example.com",
            "type": "date",
            "options": [],
            "value": "2017/12/19 00:00:00 US/Pacific",
            "valueAsString": "2017/12/19 00:00:00 US/Pacific"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "setZenProperty"
}
