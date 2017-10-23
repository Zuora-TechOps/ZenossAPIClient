not_found = {
    "uuid": "6662b00f-daec-4d54-a853-deec1867f1fd",
    "action": "DeviceRouter",
    "result": {
        "msg": "ObjectNotFoundException: Cannot find \"Devices/Server/TEST\". KeyError: 'TEST'",
        "type": "exception",
        "success": False
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

dc_info = {
    "uuid": "58c48961-7b6a-46f1-913e-a1c750fb84d6",
    "action": "DeviceRouter",
    "result": {
        "disabled": False,
        "data": {
            "connectionInfo": [
                "zCommandUsername, zCommandPassword"
            ],
            "uuid": "32d1d98b-e352-433b-b93e-c994cc7b9c44",
            "name": "TEST",
            "severity": "clear",
            "id": "TEST",
            "meta_type": "DeviceClass",
            "inspector_type": "DeviceClass",
            "uid": "/zport/dmd/Devices/Server/TEST",
            "events": {
                "info": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "clear": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "warning": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "critical": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "error": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "debug": {
                    "count": 0,
                    "acknowledged_count": 0
                }
            },
            "description": "TEST"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

collectors = {
    "uuid": "b9f0e31c-b2d7-4655-9438-11f861cdf69f",
    "action": "DeviceRouter",
    "result": [
        "localhost",
    ],
    "tid": 1,
    "type": "rpc",
    "method": "getCollectors"
}

dev_classes = {
    "uuid": "27f2f802-46cd-4691-acd8-f8988e114873",
    "action": "DeviceRouter",
    "result": {
        "totalCount": 120,
        "deviceClasses": [
            {
                "name": ""
            },
            {
                "name": "/"
            },
            {
                "name": "/Server"
            },
            {
                "name": "/Server/SSH"
            },
            {
                "name": "/Server/SSH/AIX"
            },
            {
                "name": "/Server/SSH/AIX/IBM_PowerVM"
            },
            {
                "name": "/Server/SSH/HP-UX"
            },
            {
                "name": "/Server/SSH/HP-UX/Itanium"
            },
            {
                "name": "/Server/SSH/Linux"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDeviceClasses"
}

loci = {
    "uuid": "53806094-d692-447c-badf-a3e2d788fd47",
    "action": "DeviceRouter",
    "result": {
        "totalCount": 5,
        "locations": [
            {
                "name": "/Moon Base Alpha"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getLocations"
}

devices = {
    "uuid": "e942d0b0-e7b0-4769-a6a7-9e7d948bfe0f",
    "action": "DeviceRouter",
    "result": {
        "totalCount": 1,
        "hash": "1",
        "success": True,
        "devices": [
            {
                "ipAddressString": "1.2.3.4",
                "serialNumber": "1234",
                "pythonClass": "ZenPacks.zenoss.LinuxMonitor.LinuxDevice",
                "hwManufacturer": {
                    "uid": "/zport/dmd/Manufacturers/VMware",
                    "name": "VMware"
                },
                "collector": "localhost",
                "osModel": {
                    "uid": "/zport/dmd/Manufacturers/Unknown/products/CentOS release 6.9 (Final)",
                    "name": "CentOS release 6.9 (Final)"
                },
                "productionState": 1000,
                "systems": [],
                "priority": 3,
                "hwModel": {
                    "uid": "/zport/dmd/Manufacturers/VMware/products/VMware Virtual Platform",
                    "name": "VMware Virtual Platform"
                },
                "tagNumber": "",
                "osManufacturer": {
                    "uid": "/zport/dmd/Manufacturers/Unknown",
                    "name": "Unknown"
                },
                "location": {
                    "uid": "/zport/dmd/Locations/Moon Base Alpha",
                    "name": "/Moon Base Alpha",
                    "uuid": "d800ed1e-e162-4b64-a2aa-94d9d1a44996"
                },
                "groups": [],
                "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com",
                "ipAddress": 1234567890,
                "events": {
                    "info": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "clear": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "warning": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "critical": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "error": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "debug": {
                        "count": 0,
                        "acknowledged_count": 0
                    }
                },
                "name": "test.example.com"
            }
        ]
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDevices"
}

dev_info = {
    "uuid": "f007f1b3-b1cc-402b-ac5f-f029f8fdddd7",
    "action": "DeviceRouter",
    "result": {
        "disabled": False,
        "data": {
            "productionState": 1000,
            "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com",
            "links": "<a href=\"/zport/dmd/Devices/vSphere/devices/vcenter.example.com/vms/VirtualMachine_vm-1\">Virtual Machine 'test' on vcenter.example.com</a>",
            "snmpContact": "",
            "osModel": {
                "description": "",
                "name": "CentOS release 6.9 (Final)",
                "meta_type": "SoftwareClass",
                "inspector_type": "SoftwareClass",
                "id": "CentOS release 6.9 (Final)",
                "uid": "/zport/dmd/Manufacturers/Unknown/products/CentOS release 6.9 (Final)"
            },
            "hwModel": {
                "description": "",
                "name": "VMware Virtual Platform",
                "meta_type": "HardwareClass",
                "inspector_type": "HardwareClass",
                "id": "VMware Virtual Platform",
                "uid": "/zport/dmd/Manufacturers/VMware/products/VMware Virtual Platform"
            },
            "osManufacturer": {
                "description": "",
                "name": "Unknown",
                "meta_type": "Manufacturer",
                "inspector_type": "Manufacturer",
                "id": "Unknown",
                "uid": "/zport/dmd/Manufacturers/Unknown"
            },
            "deviceClass": {
                "connectionInfo": [
                    "zCommandUsername, zCommandPassword"
                ],
                "uuid": "32d1d98b-e352-433b-b93e-c994cc7b9c44",
                "name": "TEST",
                "severity": "clear",
                "id": "TEST",
                "meta_type": "DeviceClass",
                "inspector_type": "DeviceClass",
                "uid": "/zport/dmd/Devices/Server/TEST",
                "events": {
                    "info": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "clear": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "warning": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "critical": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "error": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "debug": {
                        "count": 0,
                        "acknowledged_count": 0
                    }
                },
                "description": "TEST"
            },
            "hwManufacturer": {
                "description": "",
                "name": "VMware",
                "meta_type": "Manufacturer",
                "inspector_type": "Manufacturer",
                "id": "VMware",
                "uid": "/zport/dmd/Manufacturers/VMware"
            },
            "snmpVersion": "v3",
            "collector": "localhost",
            "id": "test.example.com",
            "deviceConnectionInfo": "",
            "uptime": "40d:14h:01m:00s",
            "severity": "clear",
            "locking": {
                "updates": False,
                "deletion": False,
                "events": False
            },
            "comments": "",
            "name": "test.example.com",
            "priority": 3,
            "snmpCommunity": "public",
            "location": {
                "uid": "/zport/dmd/Locations/Moon Base Alpha",
                "name": "/Moon Base Alpha",
                "uuid": "8f37ea37-ee7e-4198-afed-bc8507bbf05b"
            },
            "memory": {
                "ram": "15.6GB",
                "swap": "8.0GB"
            },
            "icon": "/zport/dmd/img/icons/server-linux.png",
            "priorityLabel": "Normal",
            "lastCollected": 1508763898.349612,
            "events": {
                "info": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "clear": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "warning": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "critical": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "error": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "debug": {
                    "count": 0,
                    "acknowledged_count": 0
                }
            },
            "systems": [],
            "status": True,
            "ipAddressString": "1.2.3.4",
            "description": "TEST",
            "snmpDescr": "",
            "groups": [],
            "device": "test.example.com",
            "sshLink": "ssh://zenoss@1.2.3.4",
            "firstSeen": 1506874671.273677,
            "snmpSysName": "",
            "pythonClass": "Products.ZenModel.Device",
            "lastChanged": 1508763892.047559,
            "productionStateLabel": "Production",
            "serialNumber": "1234",
            "uuid": "8c6e927e-1bd7-48b9-b2b3-88fbdc137cc3",
            "tagNumber": "",
            "meta_type": "Device",
            "inspector_type": "Device",
            "snmpLocation": "",
            "snmpAgent": "",
            "ipAddress": 1234567890,
            "rackSlot": ""
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

components = {
    "uuid": "e884358d-587f-4292-be10-1a69572902be",
    "action": "DeviceRouter",
    "result": {
        "totalCount": 1,
        "hash": "1",
        "success": True,
        "data": [
            {
                "deviceName": "test.example.com",
                "uid": "/zport/dmd/Devices/Server/TEST/test.example.com/hw/cpus/0",
                "icon": "/zport/dmd/img/icons/noicon.png",
                "product": {
                    "description": "",
                    "name": "AuthenticAMD AMD Opteron(TM) Processor 6274",
                    "meta_type": "HardwareClass",
                    "inspector_type": "HardwareClass",
                    "id": "AuthenticAMD AMD Opteron(TM) Processor 6274",
                    "uid": "/zport/dmd/Manufacturers/AuthenticAMD/products/AuthenticAMD AMD Opteron(TM) Processor 6274"
                },
                "voltage": 0,
                "clockspeed": 2199.999,
                "id": "0",
                "extspeed": 0,
                "cacheSizeL2": 2048,
                "severity": "clear",
                "cacheSizeL1": 0,
                "locking": {
                    "updates": False,
                    "deletion": False,
                    "events": False
                },
                "name": "0",
                "manufacturer": {
                    "description": "",
                    "name": "AuthenticAMD",
                    "meta_type": "Manufacturer",
                    "inspector_type": "Manufacturer",
                    "id": "AuthenticAMD",
                    "uid": "/zport/dmd/Manufacturers/AuthenticAMD"
                },
                "events": {
                    "info": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "clear": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "warning": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "critical": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "error": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "debug": {
                        "count": 0,
                        "acknowledged_count": 0
                    }
                },
                "status": "Up",
                "usesMonitorAttribute": False,
                "description": "TEST",
                "device": {
                    "productionState": 1000,
                    "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com",
                    "links": "<a href=\"/zport/dmd/Devices/vSphere/devices/vcenter.example.com/vms/VirtualMachine_vm-1\">Virtual Machine 'test' on vcenter.example.com</a>",
                    "snmpContact": "",
                    "osModel": {
                        "description": "",
                        "name": "CentOS release 6.9 (Final)",
                        "meta_type": "SoftwareClass",
                        "inspector_type": "SoftwareClass",
                        "id": "CentOS release 6.9 (Final)",
                        "uid": "/zport/dmd/Manufacturers/Unknown/products/CentOS release 6.9 (Final)"
                    },
                    "hwModel": {
                        "description": "",
                        "name": "VMware Virtual Platform",
                        "meta_type": "HardwareClass",
                        "inspector_type": "HardwareClass",
                        "id": "VMware Virtual Platform",
                        "uid": "/zport/dmd/Manufacturers/VMware/products/VMware Virtual Platform"
                    },
                    "osManufacturer": {
                        "description": "",
                        "name": "Unknown",
                        "meta_type": "Manufacturer",
                        "inspector_type": "Manufacturer",
                        "id": "Unknown",
                        "uid": "/zport/dmd/Manufacturers/Unknown"
                    },
                    "deviceClass": {
                        "connectionInfo": [
                            "zCommandUsername, zCommandPassword"
                        ],
                        "uuid": "32d1d98b-e352-433b-b93e-c994cc7b9c44",
                        "name": "TEST",
                        "severity": "clear",
                        "id": "TEST",
                        "meta_type": "DeviceClass",
                        "inspector_type": "DeviceClass",
                        "uid": "/zport/dmd/Devices/Server/TEST",
                        "events": {
                            "info": {
                                "count": 0,
                                "acknowledged_count": 0
                            },
                            "clear": {
                                "count": 0,
                                "acknowledged_count": 0
                            },
                            "warning": {
                                "count": 0,
                                "acknowledged_count": 0
                            },
                            "critical": {
                                "count": 0,
                                "acknowledged_count": 0
                            },
                            "error": {
                                "count": 0,
                                "acknowledged_count": 0
                            },
                            "debug": {
                                "count": 0,
                                "acknowledged_count": 0
                            }
                        },
                        "description": "TEST"
                    },
                    "hwManufacturer": {
                        "description": "",
                        "name": "VMware",
                        "meta_type": "Manufacturer",
                        "inspector_type": "Manufacturer",
                        "id": "VMware",
                        "uid": "/zport/dmd/Manufacturers/VMware"
                    },
                    "snmpVersion": "v3",
                    "collector": "localhost",
                    "id": "test.example.com",
                    "deviceConnectionInfo": "",
                    "uptime": "40d:14h:31m:00s",
                    "severity": "clear",
                    "locking": {
                        "updates": False,
                        "deletion": False,
                        "events": False
                    },
                    "comments": "",
                    "name": "test.example.com",
                    "priority": 3,
                    "snmpCommunity": "public",
                    "location": {
                        "uid": "/zport/dmd/Locations/Moon Base Alpha",
                        "name": "/Moon Base Alpha",
                        "uuid": "8f37ea37-ee7e-4198-afed-bc8507bbf05b"
                    },
                    "memory": {
                        "ram": "15.6GB",
                        "swap": "8.0GB"
                    },
                    "icon": "/zport/dmd/img/icons/server-linux.png",
                    "priorityLabel": "Normal",
                    "lastCollected": 1508763898.349612,
                    "events": {
                        "info": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "clear": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "warning": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "critical": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "error": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "debug": {
                            "count": 0,
                            "acknowledged_count": 0
                        }
                    },
                    "systems": [],
                    "status": True,
                    "ipAddressString": "1.2.3.4",
                    "description": "TEST",
                    "snmpDescr": "",
                    "groups": [],
                    "device": "test.example.com",
                    "sshLink": "ssh://zenoss@1.2.3.4",
                    "firstSeen": 1506874671.273677,
                    "snmpSysName": "",
                    "pythonClass": "Products.ZenModel.Device",
                    "lastChanged": 1508763892.047559,
                    "productionStateLabel": "Production",
                    "serialNumber": "1234",
                    "uuid": "8c6e927e-1bd7-48b9-b2b3-88fbdc137cc3",
                    "tagNumber": "",
                    "meta_type": "Device",
                    "inspector_type": "Device",
                    "snmpLocation": "",
                    "snmpAgent": "",
                    "ipAddress": 1234567890,
                    "rackSlot": ""
                },
                "monitored": "",
                "monitor": False,
                "pingStatus": "Up",
                "socket": "0",
                "uuid": "283a7620-a18c-4b20-a6e1-08f4639c8321",
                "meta_type": "CPU",
                "inspector_type": "CPU"
            }
        ]
    },
    "tid": 1,
    "type": "rpc",
    "method": "getComponents"
}

component_info = {
    "uuid": "4f8f0256-1677-43d7-90c2-d42d4e8dc451",
    "action": "DeviceRouter",
    "result": {
        "disabled": False,
        "data": {
            "deviceName": "test.example.com",
            "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/hw/cpus/0",
            "icon": "/zport/dmd/img/icons/noicon.png",
            "product": {
                "description": "",
                "name": "AuthenticAMD AMD Opteron(TM) Processor 6274",
                "meta_type": "HardwareClass",
                "inspector_type": "HardwareClass",
                "id": "AuthenticAMD AMD Opteron(TM) Processor 6274",
                "uid": "/zport/dmd/Manufacturers/AuthenticAMD/products/AuthenticAMD AMD Opteron(TM) Processor 6274"
            },
            "voltage": 0,
            "clockspeed": 2199.999,
            "id": "0",
            "extspeed": 0,
            "cacheSizeL2": 2048,
            "severity": "clear",
            "cacheSizeL1": 0,
            "locking": {
                "updates": False,
                "deletion": False,
                "events": False
            },
            "name": "0",
            "manufacturer": {
                "description": "",
                "name": "AuthenticAMD",
                "meta_type": "Manufacturer",
                "inspector_type": "Manufacturer",
                "id": "AuthenticAMD",
                "uid": "/zport/dmd/Manufacturers/AuthenticAMD"
            },
            "events": {
                "info": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "clear": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "warning": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "critical": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "error": {
                    "count": 0,
                    "acknowledged_count": 0
                },
                "debug": {
                    "count": 0,
                    "acknowledged_count": 0
                }
            },
            "status": "Up",
            "usesMonitorAttribute": False,
            "description": "TEST",
            "device": {
                "productionState": 1000,
                "uid": "/zport/dmd/Devices/Server/Zuora/TEST/test.example.com",
                "links": "<a href=\"/zport/dmd/Devices/vSphere/devices/vcenter.example.com/vms/VirtualMachine_vm-1\">Virtual Machine 'test' on vcenter.example.com</a>",
                "snmpContact": "",
                "osModel": {
                    "description": "",
                    "name": "CentOS release 6.9 (Final)",
                    "meta_type": "SoftwareClass",
                    "inspector_type": "SoftwareClass",
                    "id": "CentOS release 6.9 (Final)",
                    "uid": "/zport/dmd/Manufacturers/Unknown/products/CentOS release 6.9 (Final)"
                },
                "hwModel": {
                    "description": "",
                    "name": "VMware Virtual Platform",
                    "meta_type": "HardwareClass",
                    "inspector_type": "HardwareClass",
                    "id": "VMware Virtual Platform",
                    "uid": "/zport/dmd/Manufacturers/VMware/products/VMware Virtual Platform"
                },
                "osManufacturer": {
                    "description": "",
                    "name": "Unknown",
                    "meta_type": "Manufacturer",
                    "inspector_type": "Manufacturer",
                    "id": "Unknown",
                    "uid": "/zport/dmd/Manufacturers/Unknown"
                },
                "deviceClass": {
                    "connectionInfo": [
                        "zCommandUsername, zCommandPassword"
                    ],
                    "uuid": "32d1d98b-e352-433b-b93e-c994cc7b9c44",
                    "name": "TEST",
                    "severity": "clear",
                    "id": "TEST",
                    "meta_type": "DeviceClass",
                    "inspector_type": "DeviceClass",
                    "uid": "/zport/dmd/Devices/Server/TEST",
                    "events": {
                        "info": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "clear": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "warning": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "critical": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "error": {
                            "count": 0,
                            "acknowledged_count": 0
                        },
                        "debug": {
                            "count": 0,
                            "acknowledged_count": 0
                        }
                    },
                    "description": "ActiveMQ Servers"
                },
                "hwManufacturer": {
                    "description": "",
                    "name": "VMware",
                    "meta_type": "Manufacturer",
                    "inspector_type": "Manufacturer",
                    "id": "VMware",
                    "uid": "/zport/dmd/Manufacturers/VMware"
                },
                "snmpVersion": "v3",
                "collector": "localhost",
                "id": "test.example.com",
                "deviceConnectionInfo": "",
                "uptime": "40d:14h:41m:00s",
                "severity": "clear",
                "locking": {
                    "updates": False,
                    "deletion": False,
                    "events": False
                },
                "comments": "",
                "name": "test.example.com",
                "priority": 3,
                "snmpCommunity": "public",
                "location": {
                    "uid": "/zport/dmd/Locations/Moon Base Alpha",
                    "name": "/Moon Base Alpha",
                    "uuid": "8f37ea37-ee7e-4198-afed-bc8507bbf05b"
                },
                "memory": {
                    "ram": "15.6GB",
                    "swap": "8.0GB"
                },
                "icon": "/zport/dmd/img/icons/server-linux.png",
                "priorityLabel": "Normal",
                "lastCollected": 1508763898.349612,
                "events": {
                    "info": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "clear": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "warning": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "critical": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "error": {
                        "count": 0,
                        "acknowledged_count": 0
                    },
                    "debug": {
                        "count": 0,
                        "acknowledged_count": 0
                    }
                },
                "systems": [],
                "status": True,
                "ipAddressString": "1.2.3.4",
                "description": "TEST",
                "snmpDescr": "",
                "groups": [],
                "device": "test.example.com",
                "sshLink": "ssh://zenoss@1.2.3.4",
                "firstSeen": 1506874671.273677,
                "snmpSysName": "",
                "pythonClass": "Products.ZenModel.Device",
                "lastChanged": 1508763892.047559,
                "productionStateLabel": "Production",
                "serialNumber": "1234",
                "uuid": "8c6e927e-1bd7-48b9-b2b3-88fbdc137cc3",
                "tagNumber": "",
                "meta_type": "Device",
                "inspector_type": "Device",
                "snmpLocation": "",
                "snmpAgent": "",
                "ipAddress": 1234567890,
                "rackSlot": ""
            },
            "monitored": "",
            "monitor": False,
            "pingStatus": "Up",
            "socket": "0",
            "uuid": "283a7620-a18c-4b20-a6e1-08f4639c8321",
            "meta_type": "CPU",
            "inspector_type": "CPU"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}
