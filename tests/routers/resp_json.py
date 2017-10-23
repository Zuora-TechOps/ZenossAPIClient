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

add_dev = {
    "uuid": "d18bb6b3-023b-407f-9775-a9fbcaa49901",
    "action": "DeviceRouter",
    "result": {
        "new_jobs": [
            {
                "uuid": "721739ae-2b1d-4613-91e9-681f134a2c49",
                "description": "Create test2.example.com under /Server/TEST",
                "uid": "/zport/dmd/JobManager"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "addDevice"
}

uc = {
    "uuid": "b93045d7-409b-4d2e-9acf-e9c1dd0fdcb2",
    "action": "DeviceRouter",
    "result": [
        {
            "id": "DNS forward",
            "description": "Name to IP address lookup",
            "uid": "/zport/dmd/userCommands/DNS forward"
        },
        {
            "id": "DNS reverse",
            "description": "IP address to name lookup",
            "uid": "/zport/dmd/userCommands/DNS reverse"
        },
        {
            "id": "ping",
            "description": "Is the device responding to ping?",
            "uid": "/zport/dmd/userCommands/ping"
        },
        {
            "id": "snmpwalk",
            "description": "Display the OIDs available on a device",
            "uid": "/zport/dmd/userCommands/snmpwalk"
        },
        {
            "id": "snmpwalk_v3",
            "description": "snmp version v3 Display the OIDs available on a device",
            "uid": "/zport/dmd/userCommands/snmpwalk_v3"
        },
        {
            "id": "traceroute",
            "description": "Show the route to the device",
            "uid": "/zport/dmd/userCommands/traceroute"
        }
    ],
    "tid": 1,
    "type": "rpc",
    "method": "getUserCommands"
}

local_templates = {
    "uuid": "c68b8966-2653-4491-9555-be78255a2585",
    "action": "DeviceRouter",
    "result": {
        "data": [
            {
                "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/DnsMonitor",
                "label": "DnsMonitor (Locally Defined)"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getLocalTemplates"
}

local_template = {
    "uuid": "966435e6-2c93-482d-be23-8ea20fbd5f6d",
    "action": "TemplateRouter",
    "result": {
        "data": {
            "qtip": "Perform a DNS forward lookup of the device name and check to see that it resolves to the device's manageIp",
            "definition": "/Devices/Server/TEST/devices/test.example.com",
            "hidden": False,
            "leaf": True,
            "description": "Perform a DNS forward lookup of the device name and check to see that it resolves to the device's manageIp",
            "name": "DnsMonitor",
            "text": "/Server/TEST/test.example.com",
            "id": "DnsMonitor..Server.TEST.test.example.com",
            "meta_type": "RRDTemplate",
            "targetPythonClass": "Products.ZenModel.Device",
            "inspector_type": "RRDTemplate",
            "iconCls": "tree-template-icon-bound",
            "children": [],
            "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/DnsMonitor"
        },
        "success": True,
        "form": {
            "items": [
                {
                    "items": [],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

templates = {
    "uuid": "0398d95e-dc4b-45ee-8327-881169e8193e",
    "action": "DeviceRouter",
    "result": [
        {
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/Device",
            "path": "/Server/TEST",
            "leaf": True,
            "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/Device",
            "text": "Device (/Server/TEST)"
        },
        {
            "uid": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/DnsMonitor",
            "path": "Locally Defined",
            "leaf": True,
            "id": "/zport/dmd/Devices/Server/TEST/devices/test.example.com/DnsMonitor",
            "text": "DnsMonitor (Locally Defined)"
        }
    ],
    "tid": 1,
    "type": "rpc",
    "method": "getTemplates"
}

dns_template = {
    "uuid": "d11158e2-1a57-44cc-b301-64f38edb4829",
    "action": "TemplateRouter",
    "result": {
        "data": {
            "qtip": "Perform a DNS forward lookup of the device name and check to see that it resolves to the device's manageIp",
            "definition": "/Devices",
            "hidden": False,
            "leaf": True,
            "description": "Perform a DNS forward lookup of the device name and check to see that it resolves to the device's manageIp",
            "name": "DnsMonitor",
            "text": "/",
            "id": "DnsMonitor..",
            "meta_type": "RRDTemplate",
            "targetPythonClass": "Products.ZenModel.Device",
            "inspector_type": "RRDTemplate",
            "iconCls": "tree-node-no-icon",
            "children": [],
            "uid": "/zport/dmd/Devices/rrdTemplates/DnsMonitor"
        },
        "success": True,
        "form": {
            "items": [
                {
                    "items": [],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

device_template = {
    "uuid": "75f49b81-f655-4425-a5a9-e166483b1641",
    "action": "TemplateRouter",
    "result": {
        "data": {
            "qtip": "Linux device monitoring via SSH.",
            "definition": "/Devices/Server/TEST",
            "hidden": False,
            "leaf": True,
            "description": "Linux device monitoring via SSH.",
            "name": "Device",
            "text": "/Server/TEST",
            "id": "Device..Server.TEST",
            "meta_type": "RRDTemplate",
            "targetPythonClass": "Products.ZenModel.Device",
            "inspector_type": "RRDTemplate",
            "iconCls": "tree-template-icon-bound",
            "children": [],
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/Device"
        },
        "success": True,
        "form": {
            "items": [
                {
                    "items": [],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

ub_templates = {
    "uuid": "15131180-9037-4b7b-a9cc-fb754ab7978e",
    "action": "DeviceRouter",
    "result": {
        "data": [
            [
                "Apache",
                "Apache (/Server)"
            ],
            [
                "DigMonitor",
                "DigMonitor (/Server)"
            ]
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getUnboundTemplates"
}

apache_template = {
    "uuid": "88c860ce-5141-4947-a9e3-61533fcdf09c",
    "action": "TemplateRouter",
    "result": {
        "data": {
            "qtip": "Apache metrics via mod_status",
            "definition": "/Devices/Server",
            "hidden": False,
            "leaf": True,
            "description": "Apache metrics via mod_status",
            "name": "Apache",
            "text": "/Server",
            "id": "Apache..Server",
            "meta_type": "RRDTemplate",
            "targetPythonClass": "Products.ZenModel.Device",
            "inspector_type": "RRDTemplate",
            "iconCls": "tree-node-no-icon",
            "children": [],
            "uid": "/zport/dmd/Devices/Server/rrdTemplates/Apache"
        },
        "success": True,
        "form": {
            "items": [
                {
                    "items": [],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

dig_template = {
    "uuid": "19a53446-490f-48f9-a12c-7f1aa7949f91",
    "action": "TemplateRouter",
    "result": {
        "data": {
            "qtip": "DNS query time template with 30 second threshold",
            "definition": "/Devices/Server",
            "hidden": False,
            "leaf": True,
            "description": "DNS query time template with 30 second threshold",
            "name": "DigMonitor",
            "text": "/Server",
            "id": "DigMonitor..Server",
            "meta_type": "RRDTemplate",
            "targetPythonClass": "Products.ZenModel.Device",
            "inspector_type": "RRDTemplate",
            "iconCls": "tree-node-no-icon",
            "children": [],
            "uid": "/zport/dmd/Devices/Server/rrdTemplates/DigMonitor"
        },
        "success": True,
        "form": {
            "items": [
                {
                    "items": [],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getInfo"
}

bound_templates = {
    "uuid": "1ba75e4e-5702-4820-96a7-fe2d3e4b859a",
    "action": "DeviceRouter",
    "result": {
        "data": [
            [
                "Device",
                "Device (/Server/TEST)"
            ],
            [
                "DnsMonitor",
                "DnsMonitor (/Server/TEST/test.example.com)"
            ]
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getBoundTemplates"
}

or_templates = {
    "uuid": "de5fd36b-8f0c-487a-9cc1-4a8ba7444bd9",
    "action": "DeviceRouter",
    "result": {
        "data": [
            {
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/Device",
                "label": "Device (/Server/TEST)"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getOverridableTemplates"
}
