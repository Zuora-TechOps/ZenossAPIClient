success = {
    "uuid": "8bf7e570-67cd-4670-a37c-0999fd07f9bf",
    "action": "TemplateRouter",
    "result": {
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "detail"
}

fail = {
    "uuid": "89844ab9-b400-443b-8881-ad1be210f5ed",
    "action": "TemplateRouter",
    "result": {
        "msg": "ObjectNotFoundException",
        "type": "exception",
        "success": False
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataPointDetails"
}

no_points = {
    "uuid": "40558c6f-2d2d-4f80-9b9e-68215d7ad9a8",
    "action": "TemplateRouter",
    "result": {
        "data": [],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataPoints"
}

list_templates = {
    "uuid": "48b423d1-377d-489f-8cbf-b8b6008941e0",
    "action": "TemplateRouter",
    "result": [
        {
            "isOrganizer": True,
            "qtip": "",
            "leaf": False,
            "uid": "/zport/dmd/Devices/Server/TEST",
            "text": "Linux",
            "id": ".zport.dmd.Devices.Server.TEST",
            "iconCls": "",
            "path": "Devices/Server/TEST",
            "hidden": False,
            "children": [
                {
                    "isOrganizer": False,
                    "qtip": "",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/MySQLServer",
                    "text": "MySQLServer (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.MySQLServer",
                    "path": "Devices/Server/TEST/rrdTemplates/MySQLServer",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux file system monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem_NFS_Client",
                    "text": "FileSystem_NFS_Client (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.FileSystem_NFS_Client",
                    "path": "Devices/Server/TEST/rrdTemplates/FileSystem_NFS_Client",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Ethernet (and default) network interface monitoring for Linux via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/ethernetCsmacd",
                    "text": "ethernetCsmacd (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.ethernetCsmacd",
                    "path": "Devices/Server/TEST/rrdTemplates/ethernetCsmacd",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux hard disk (block device) monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/HardDisk",
                    "text": "HardDisk (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.HardDisk",
                    "path": "Devices/Server/TEST/rrdTemplates/HardDisk",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux LVM logical volume monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume",
                    "text": "LogicalVolume (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.LogicalVolume",
                    "path": "Devices/Server/TEST/rrdTemplates/LogicalVolume",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux LVM volume group monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/VolumeGroup",
                    "text": "VolumeGroup (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.VolumeGroup",
                    "path": "Devices/Server/TEST/rrdTemplates/VolumeGroup",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux process monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/OSProcess",
                    "text": "OSProcess (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.OSProcess",
                    "path": "Devices/Server/TEST/rrdTemplates/OSProcess",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/MegaRaid",
                    "text": "MegaRaid (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.MegaRaid",
                    "path": "Devices/Server/TEST/rrdTemplates/MegaRaid",
                    "iconCls": "tree-node-no-icon",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux file system monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem",
                    "text": "FileSystem (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.FileSystem",
                    "path": "Devices/Server/TEST/rrdTemplates/FileSystem",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux device monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/Device",
                    "text": "Device (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.Device",
                    "path": "Devices/Server/TEST/rrdTemplates/Device",
                    "iconCls": "tree-template-icon-bound",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux LVM physical volume monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/PhysicalVolume",
                    "text": "PhysicalVolume (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.PhysicalVolume",
                    "path": "Devices/Server/TEST/rrdTemplates/PhysicalVolume",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                },
                {
                    "isOrganizer": False,
                    "qtip": "Linux LVM snapshot volume monitoring via SSH.",
                    "hidden": False,
                    "leaf": True,
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/SnapshotVolume",
                    "text": "SnapshotVolume (Locally Defined)",
                    "id": "Devices.Server.TEST.rrdTemplates.SnapshotVolume",
                    "path": "Devices/Server/TEST/rrdTemplates/SnapshotVolume",
                    "iconCls": "tree-template-icon-component",
                    "children": [],
                    "uuid": None
                }
            ],
            "uuid": "c4d25bd5-7034-4286-bc4b-d6ad0ac501fb"
        }
    ],
    "tid": 1,
    "type": "rpc",
    "method": "getDeviceClassTemplates"
}

list_templates_match = [(u'Devices/Server/TEST/rrdTemplates/MySQLServer', u''),
                        (u'Devices/Server/TEST/rrdTemplates/FileSystem_NFS_Client',
                         u'Linux file system monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/ethernetCsmacd',
                         u'Ethernet (and default) network interface monitoring for Linux via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/HardDisk',
                         u'Linux hard disk (block device) monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/LogicalVolume',
                         u'Linux LVM logical volume monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/VolumeGroup',
                         u'Linux LVM volume group monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/OSProcess',
                         u'Linux process monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/MegaRaid', u''),
                        (u'Devices/Server/TEST/rrdTemplates/FileSystem',
                         u'Linux file system monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/Device',
                         u'Linux device monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/PhysicalVolume',
                         u'Linux LVM physical volume monitoring via SSH.'),
                        (u'Devices/Server/TEST/rrdTemplates/SnapshotVolume',
                         u'Linux LVM snapshot volume monitoring via SSH.')]

templates = {
    'MySQLServer': {
        "uuid": "6bae4016-f8ab-4559-a7c2-111cce1e274c",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "",
                "name": "MySQLServer",
                "text": "/Server/TEST",
                "id": "MySQLServer..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "ZenPacks.zenoss.MySqlMonitor.MySQLServer",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/MySQLServer"
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
    },
    'FileSystem_NFS_Client': {
        "uuid": "96919d08-b3d0-4797-81b1-b28e3a435c1b",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux file system monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux file system monitoring via SSH.",
                "name": "FileSystem_NFS_Client",
                "text": "/Server/TEST",
                "id": "FileSystem_NFS_Client..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "Products.ZenModel.FileSystem",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem_NFS_Client"
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
    },
    'ethernetCsmacd': {
        "uuid": "d0017709-10dd-4225-9450-56e300f7d806",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Ethernet (and default) network interface monitoring for Linux via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Ethernet (and default) network interface monitoring for Linux via SSH.",
                "name": "ethernetCsmacd",
                "text": "/Server/TEST",
                "id": "ethernetCsmacd..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "Products.ZenModel.IpInterface",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/ethernetCsmacd"
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
    },
    'HardDisk': {
        "uuid": "c2f74c42-7d4b-49f7-9ee7-c02b845b3923",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux hard disk (block device) monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux hard disk (block device) monitoring via SSH.",
                "name": "HardDisk",
                "text": "/Server/TEST",
                "id": "HardDisk..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "ZenPacks.zenoss.LinuxMonitor.HardDisk",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/HardDisk"
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
    },
    'LogicalVolume': {
        "uuid": "6a263783-75a7-42d5-b0ab-46ecf96f6b75",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux LVM logical volume monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux LVM logical volume monitoring via SSH.",
                "name": "LogicalVolume",
                "text": "/Server/TEST",
                "id": "LogicalVolume..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "ZenPacks.zenoss.LinuxMonitor.LogicalVolume",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume"
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
    },
    'VolumeGroup': {
        "uuid": "098c4d3f-b574-40bc-85a2-a876e4747ea3",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux LVM volume group monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux LVM volume group monitoring via SSH.",
                "name": "VolumeGroup",
                "text": "/Server/TEST",
                "id": "VolumeGroup..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "ZenPacks.zenoss.LinuxMonitor.VolumeGroup",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/VolumeGroup"
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
    },
    'OSProcess': {
        "uuid": "1fdd2401-b700-4fd1-a957-933631a1d1a2",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux process monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux process monitoring via SSH.",
                "name": "OSProcess",
                "text": "/Server/TEST",
                "id": "OSProcess..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "Products.ZenModel.OSProcess",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/OSProcess"
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
    },
    'MegaRaid': {
        "uuid": "58d74f54-c760-4e60-8ca6-983195cdd58b",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "",
                "name": "MegaRaid",
                "text": "/Server/TEST",
                "id": "MegaRaid..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "Products.ZenModel.Device",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-node-no-icon",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/MegaRaid"
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
    },
    'FileSystem': {
        "uuid": "09e5528b-3487-4e43-bb8e-951a196aa177",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux file system monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux file system monitoring via SSH.",
                "name": "FileSystem",
                "text": "/Server/TEST",
                "id": "FileSystem..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "Products.ZenModel.FileSystem",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem"
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
    },
    'Device': {
        "uuid": "5f526dbf-8d82-488e-a604-bf0f09a6ea21",
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
    },
    'PhysicalVolume': {
        "uuid": "afbe7c73-9919-49dc-b5f0-5f73bda9a622",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux LVM physical volume monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux LVM physical volume monitoring via SSH.",
                "name": "PhysicalVolume",
                "text": "/Server/TEST",
                "id": "PhysicalVolume..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "ZenPacks.zenoss.LinuxMonitor.PhysicalVolume",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/PhysicalVolume"
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
    },
    'SnapshotVolume': {
        "uuid": "a08e9298-9635-4fbf-9897-60eb482e99a2",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "Linux LVM snapshot volume monitoring via SSH.",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "Linux LVM snapshot volume monitoring via SSH.",
                "name": "SnapshotVolume",
                "text": "/Server/TEST",
                "id": "SnapshotVolume..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "ZenPacks.zenoss.LinuxMonitor.SnapshotVolume",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-component",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/SnapshotVolume"
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
    },
    'DnsMonitor': {
        "uuid": "0578b1b5-d628-4ded-b9ab-6e3ed6c1a06d",
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
    },
    'TestAdd': {
        "uuid": "0578b1b5-d628-4ded-b9ab-6e3ed6c1a06d",
        "action": "TemplateRouter",
        "result": {
            "data": {
                "qtip": "",
                "definition": "/Devices/Server/TEST",
                "hidden": False,
                "leaf": True,
                "description": "",
                "name": "TestAdd",
                "text": "/Server/TEST",
                "id": "TestAdd..Server.TEST",
                "meta_type": "RRDTemplate",
                "targetPythonClass": "Products.ZenModel.Device",
                "inspector_type": "RRDTemplate",
                "iconCls": "tree-template-icon-bound",
                "children": [],
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/TestAdd"
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
}

obj_templates = {
    "uuid": "39dfd607-b865-452c-8374-8f62b7ab18be",
    "action": "TemplateRouter",
    "result": {
        "data": [
            {
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
            {
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
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getObjTemplates"
}

ds_types = {
    "uuid": "24e9b489-738c-4f76-8888-708b8837ff6f",
    "action": "TemplateRouter",
    "result": {
        "data": [
            {
                "type": "ApacheMonitor"
            },
            {
                "type": "Built-In"
            },
            {
                "type": "COMMAND"
            },
            {
                "type": "DigMonitor"
            },
            {
                "type": "DnsMonitor"
            },
            {
                "type": "FtpMonitor"
            },
            {
                "type": "HttpMonitor"
            },
            {
                "type": "JMX"
            },
            {
                "type": "LDAPMonitor"
            },
            {
                "type": "MySqlMonitor"
            },
            {
                "type": "Oracle"
            },
            {
                "type": "PING"
            },
            {
                "type": "Python"
            },
            {
                "type": "SNMP"
            },
            {
                "type": "SQL"
            },
            {
                "type": "vCloudStatus"
            },
            {
                "type": "VMware vSphere"
            },
            {
                "type": "WebTx"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataSourceTypes"
}

threshold_types = {
    "uuid": "41877b7a-69ee-42f6-8517-293ba39ea6ea",
    "action": "TemplateRouter",
    "result": {
        "data": [
            {
                "type": "MinMaxThreshold"
            },
            {
                "type": "ValueChangeThreshold"
            },
            {
                "type": "CiscoStatus"
            },
            {
                "type": "PredictiveThreshold"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getThresholdTypes"
}

lv_data_sources = {
    "uuid": "0a426b20-d355-4839-b958-64ba0691145f",
    "action": "TemplateRouter",
    "result": {
        "data": [
            {
                "description": "Linux LVM logical volume monitoring via SSH.",
                "component": "${here/id}",
                "enabled": True,
                "inspector_type": "RRDDataSource",
                "name": "status",
                "source": "/usr/bin/env sudo lvs --noheadings -o vg_name,lv_name,lv_attr over SSH",
                "meta_type": "RRDDataSource",
                "newId": "status",
                "eventKey": "",
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status",
                "eventClass": "/Ignore",
                "type": "COMMAND",
                "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status",
                "severity": 0
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataSources"
}

lv_ds_details = {
    "uuid": "5c8e37c4-92de-49ea-976d-1c6081384925",
    "action": "TemplateRouter",
    "result": {
        "record": {
            "parser": "ZenPacks.zenoss.LinuxMonitor.parsers.linux.lvsstatus",
            "cycletime": 300,
            "description": "Linux LVM logical volume monitoring via SSH.",
            "availableParsers": [
                "Auto",
                "Cacti",
                "JSON",
                "Nagios",
                "ZenPacks.zenoss.LinuxMonitor.parsers.Standard",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.cpu",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.df",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.dfi",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.diskstats",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.ifconfig",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.lvsstatus",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.mem",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.ps",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.pvsstatus",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.pvvgstats",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.vgsstatus",
                "ps",
                "uptime"
            ],
            "component": "${here/id}",
            "commandTemplate": "/usr/bin/env sudo lvs --noheadings -o vg_name,lv_name,lv_attr",
            "usessh": "True",
            "enabled": True,
            "name": "status",
            "source": "/usr/bin/env sudo lvs --noheadings -o vg_name,lv_name,lv_attr over SSH",
            "meta_type": "RRDDataSource",
            "newId": "status",
            "eventKey": "",
            "testable": True,
            "inspector_type": "RRDDataSource",
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status",
            "eventClass": "/Ignore",
            "type": "COMMAND",
            "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status",
            "severity": 0
        },
        "form": {
            "items": [
                {
                    "items": [
                        {
                            "vtype": None,
                            "fieldLabel": "Name",
                            "xtype": "idfield",
                            "labelStyle": None,
                            "value": "status",
                            "name": "newId",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The name of this datasource' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Type",
                            "xtype": "displayfield",
                            "labelStyle": None,
                            "value": "COMMAND",
                            "name": "type",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "checked": True,
                            "xtype": "checkbox",
                            "labelStyle": "display:none",
                            "value": True,
                            "disabled": False,
                            "boxLabel": "Enabled",
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "enabled"
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Severity",
                            "xtype": "severity",
                            "labelStyle": None,
                            "value": 0,
                            "name": "severity",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Event Class",
                            "xtype": "eventclass",
                            "labelStyle": None,
                            "value": "/Ignore",
                            "name": "eventClass",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Cycle Time (seconds)",
                            "xtype": "numberfield",
                            "labelStyle": None,
                            "value": 300,
                            "disabled": False,
                            "decimalPrecision": 2,
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "cycletime"
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Parser",
                            "xtype": "parser",
                            "labelStyle": None,
                            "value": "ZenPacks.zenoss.LinuxMonitor.parsers.linux.lvsstatus",
                            "name": "parser",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "checked": "True",
                            "xtype": "checkbox",
                            "labelStyle": "display:none",
                            "value": "True",
                            "disabled": False,
                            "boxLabel": "Use SSH",
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "usessh"
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Component",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "${here/id}",
                            "name": "component",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Event Key",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "",
                            "name": "eventKey",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Command Template",
                            "xtype": "twocolumntextarea",
                            "labelStyle": None,
                            "value": "/usr/bin/env sudo lvs --noheadings -o vg_name,lv_name,lv_attr",
                            "name": "commandTemplate",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        }
                    ],
                    "xtype": "fieldset",
                    "title": None
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataSourceDetails"
}

fs_ds_details = {
    "uuid": "d3a91541-bd02-4871-a6d8-8cfc50ce0271",
    "action": "TemplateRouter",
    "result": {
        "record": {
            "parser": "ZenPacks.zenoss.LinuxMonitor.parsers.linux.df",
            "cycletime": 300,
            "description": "Linux file system monitoring via SSH.",
            "availableParsers": [
                "Auto",
                "Cacti",
                "JSON",
                "Nagios",
                "ZenPacks.zenoss.LinuxMonitor.parsers.Standard",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.cpu",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.df",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.dfi",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.diskstats",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.ifconfig",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.lvsstatus",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.mem",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.ps",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.pvsstatus",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.pvvgstats",
                "ZenPacks.zenoss.LinuxMonitor.parsers.linux.vgsstatus",
                "ps",
                "uptime"
            ],
            "component": "${here/id}",
            "commandTemplate": "/bin/sh -c 'export PATH=$$PATH:/bin:/sbin:/usr/bin:/usr/sbin; if command -v timeout > /dev/None 2>&1; then timeout 30 /usr/bin/env df -kP; else /usr/bin/env df -kP; fi'",
            "usessh": "True",
            "enabled": True,
            "name": "disk",
            "source": "/bin/sh -c 'export PATH=$$PATH:/bin:/sbin:/usr/bin:/usr/sbin; if command -v timeout > /dev/None 2>&1; then timeout 30 /usr/bin/env df -kP; else /usr/bin/env df -kP; fi' over SSH",
            "meta_type": "RRDDataSource",
            "newId": "disk",
            "eventKey": "",
            "testable": True,
            "inspector_type": "RRDDataSource",
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk",
            "eventClass": "/Ignore",
            "type": "COMMAND",
            "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk",
            "severity": 0
        },
        "form": {
            "items": [
                {
                    "items": [
                        {
                            "vtype": None,
                            "fieldLabel": "Name",
                            "xtype": "idfield",
                            "labelStyle": None,
                            "value": "disk",
                            "name": "newId",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The name of this datasource' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Type",
                            "xtype": "displayfield",
                            "labelStyle": None,
                            "value": "COMMAND",
                            "name": "type",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "checked": True,
                            "xtype": "checkbox",
                            "labelStyle": "display:none",
                            "value": True,
                            "disabled": False,
                            "boxLabel": "Enabled",
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "enabled"
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Severity",
                            "xtype": "severity",
                            "labelStyle": None,
                            "value": 0,
                            "name": "severity",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Event Class",
                            "xtype": "eventclass",
                            "labelStyle": None,
                            "value": "/Ignore",
                            "name": "eventClass",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Cycle Time (seconds)",
                            "xtype": "numberfield",
                            "labelStyle": None,
                            "value": 300,
                            "disabled": False,
                            "decimalPrecision": 2,
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "cycletime"
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Parser",
                            "xtype": "parser",
                            "labelStyle": None,
                            "value": "ZenPacks.zenoss.LinuxMonitor.parsers.linux.df",
                            "name": "parser",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "checked": "True",
                            "xtype": "checkbox",
                            "labelStyle": "display:none",
                            "value": "True",
                            "disabled": False,
                            "boxLabel": "Use SSH",
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "usessh"
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Component",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "${here/id}",
                            "name": "component",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Event Key",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "",
                            "name": "eventKey",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Command Template",
                            "xtype": "twocolumntextarea",
                            "labelStyle": None,
                            "value": "/bin/sh -c 'export PATH=$$PATH:/bin:/sbin:/usr/bin:/usr/sbin; if command -v timeout > /dev/None 2>&1; then timeout 30 /usr/bin/env df -kP; else /usr/bin/env df -kP; fi'",
                            "name": "commandTemplate",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        }
                    ],
                    "xtype": "fieldset",
                    "title": None
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataSourceDetails"
}

lv_data_points = {
    "uuid": "47b01edd-5278-490b-baec-dbd00102a4ba",
    "action": "TemplateRouter",
    "result": {
        "data": [
            {
                "isrow": True,
                "leaf": True,
                "description": "Linux LVM logical volume monitoring via SSH.",
                "rrdmin": "0",
                "availableRRDTypes": [
                    "COUNTER",
                    "GAUGE",
                    "DERIVE",
                    "ABSOLUTE"
                ],
                "name": "status.state",
                "rate": False,
                "meta_type": "RRDDataPoint",
                "newId": "state",
                "createCmd": "",
                "rrdtype": "GAUGE",
                "inspector_type": "RRDDataPoint",
                "rrdmax": None,
                "aliases": [
                    {
                        "description": "Linux LVM logical volume monitoring via SSH.",
                        "name": "lvm_lv_state__bool",
                        "meta_type": "RRDDataPointAlias",
                        "inspector_type": "RRDDataPointAlias",
                        "formula": "",
                        "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state/aliases/lvm_lv_state__bool",
                        "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state/aliases/lvm_lv_state__bool"
                    }
                ],
                "type": "GAUGE",
                "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state",
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state"
            },
            {
                "isrow": True,
                "leaf": True,
                "description": "Linux LVM logical volume monitoring via SSH.",
                "rrdmin": "0",
                "availableRRDTypes": [
                    "COUNTER",
                    "GAUGE",
                    "DERIVE",
                    "ABSOLUTE"
                ],
                "name": "status.health",
                "rate": False,
                "meta_type": "RRDDataPoint",
                "newId": "health",
                "createCmd": "",
                "rrdtype": "GAUGE",
                "inspector_type": "RRDDataPoint",
                "rrdmax": None,
                "aliases": [
                    {
                        "description": "Linux LVM logical volume monitoring via SSH.",
                        "name": "lvm_lv_health__bool",
                        "meta_type": "RRDDataPointAlias",
                        "inspector_type": "RRDDataPointAlias",
                        "formula": "",
                        "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/health/aliases/lvm_lv_health__bool",
                        "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/health/aliases/lvm_lv_health__bool"
                    }
                ],
                "type": "GAUGE",
                "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/health",
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/health"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataPoints"
}

fs_thresholds = {
    "uuid": "e6734cb3-38f5-4338-8862-acc9c58ebc4f",
    "action": "TemplateRouter",
    "result": {
        "data": [
            {
                "maxval": "90",
                "explanation": "",
                "description": "",
                "minval": "",
                "escalateCount": 0,
                "resolution": "",
                "dsnames": [
                    "disk_percentUsed"
                ],
                "enabled": True,
                "name": "90 percent used",
                "meta_type": "ThresholdClass",
                "newId": "90 percent used",
                "dataPoints": "disk_percentUsed",
                "inspector_type": "ThresholdClass",
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used",
                "eventClass": "/Perf/Filesystem",
                "type": "MinMaxThreshold",
                "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used",
                "severity": 3
            },
            {
                "maxval": "95",
                "explanation": "",
                "description": "",
                "minval": "",
                "escalateCount": 0,
                "resolution": "",
                "dsnames": [
                    "disk_percentUsed"
                ],
                "enabled": True,
                "name": "95 percent used",
                "meta_type": "ThresholdClass",
                "newId": "95 percent used",
                "dataPoints": "disk_percentUsed",
                "inspector_type": "ThresholdClass",
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/95 percent used",
                "eventClass": "/Perf/Filesystem",
                "type": "MinMaxThreshold",
                "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/95 percent used",
                "severity": 4
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getThresholds"
}

threshold_details = {
    "uuid": "386f7ba8-1c15-4820-889c-f6624a93b9fb",
    "action": "TemplateRouter",
    "result": {
        "record": {
            "maxval": "90",
            "explanation": "",
            "description": "",
            "minval": "",
            "escalateCount": 0,
            "resolution": "",
            "dsnames": [
                "disk_percentUsed"
            ],
            "enabled": True,
            "allDataPoints": [
                "disk_availBlocks",
                "disk_percentUsed",
                "disk_usedBlocks",
                "idisk_availableInodes",
                "idisk_percentInodesUsed",
                "idisk_totalInodes",
                "idisk_usedInodes"
            ],
            "name": "90 percent used",
            "meta_type": "ThresholdClass",
            "newId": "90 percent used",
            "dataPoints": "disk_percentUsed",
            "inspector_type": "ThresholdClass",
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used",
            "eventClass": "/Perf/Filesystem",
            "type": "MinMaxThreshold",
            "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/thresholds/90 percent used",
            "severity": 3
        },
        "form": {
            "items": [
                {
                    "items": [
                        {
                            "vtype": None,
                            "fieldLabel": "Name",
                            "xtype": "idfield",
                            "labelStyle": None,
                            "value": "90 percent used",
                            "name": "newId",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Description",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "",
                            "name": "description",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Type",
                            "xtype": "displayfield",
                            "labelStyle": None,
                            "value": "MinMaxThreshold",
                            "name": "type",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Explanation",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "",
                            "name": "explanation",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Resolution",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "",
                            "name": "resolution",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "DataPoints",
                            "xtype": "datapointitemselector",
                            "labelStyle": None,
                            "value": [
                                "disk_percentUsed"
                            ],
                            "name": "dsnames",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Severity",
                            "xtype": "severity",
                            "labelStyle": None,
                            "value": 3,
                            "name": "severity",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "checked": True,
                            "xtype": "checkbox",
                            "labelStyle": "display:none",
                            "value": True,
                            "disabled": False,
                            "boxLabel": "Enabled",
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "enabled"
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Minimum Value",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "",
                            "name": "minval",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Maximum Value",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "90",
                            "name": "maxval",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Event Class",
                            "xtype": "eventclass",
                            "labelStyle": None,
                            "value": "/Perf/Filesystem",
                            "name": "eventClass",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Escalate Count",
                            "xtype": "numberfield",
                            "labelStyle": None,
                            "value": 0,
                            "disabled": False,
                            "decimalPrecision": 2,
                            "allowBlank": True,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "name": "escalateCount"
                        }
                    ],
                    "xtype": "fieldset",
                    "title": None
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getThresholdDetails"
}

graphs_list = {
    "uuid": "21d7b974-1f77-4194-bc9b-827b7be8d28a",
    "action": "TemplateRouter",
    "result": [
        {
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/graphDefs/Usage",
            "sequence": 1,
            "fakeGraphCommands": "-F\n-E\n--disable-rrdtool-tag\n--height=500\n--width=500\n--lower-limit=0\n--rigid\n--vertical-label=bytes\n--base=1024\nDEF:Used-raw=rrdPath/disk_usedBlocks.rrd:ds0:AVERAGE\nCDEF:Used-rpn=Used-raw,__render_with_namespace__,*\nCDEF:Used=Used-rpn\nLINE1:Used-rpn#1f77b4:Used          \nGPRINT:Used-rpn:LAST:cur\\:%7.2lf%s\nGPRINT:Used-rpn:AVERAGE:avg\\:%7.2lf%s\\j",
            "height": 500,
            "miny": 0,
            "newId": "Usage",
            "id": "Usage",
            "maxy": -1,
            "autoscale": None,
            "log": False,
            "custom": "",
            "width": 500,
            "graphPoints": "Used",
            "units": "bytes",
            "hasSummary": True,
            "ceiling": None,
            "description": "",
            "base": True,
            "rrdVariables": [
                "Used-raw",
                "Used-rpn",
                "Used"
            ],
            "name": "Usage",
            "meta_type": "GraphDefinition",
            "inspector_type": "GraphDefinition"
        }
    ],
    "tid": 1,
    "type": "rpc",
    "method": "getGraphs"
}

graph_def = {
    "uuid": "f25cc8f6-4452-4846-b453-e2a190a8fb55",
    "action": "TemplateRouter",
    "result": {
        "data": {
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/graphDefs/Usage",
            "sequence": 1,
            "fakeGraphCommands": "-F\n-E\n--disable-rrdtool-tag\n--height=500\n--width=500\n--lower-limit=0\n--rigid\n--vertical-label=bytes\n--base=1024\nDEF:Used-raw=rrdPath/disk_usedBlocks.rrd:ds0:AVERAGE\nCDEF:Used-rpn=Used-raw,__render_with_namespace__,*\nCDEF:Used=Used-rpn\nLINE1:Used-rpn#1f77b4:Used          \nGPRINT:Used-rpn:LAST:cur\\:%7.2lf%s\nGPRINT:Used-rpn:AVERAGE:avg\\:%7.2lf%s\\j",
            "height": 500,
            "miny": 0,
            "newId": "Usage",
            "id": "Usage",
            "maxy": -1,
            "autoscale": None,
            "log": False,
            "custom": "",
            "width": 500,
            "graphPoints": "Used",
            "units": "bytes",
            "hasSummary": True,
            "ceiling": None,
            "description": "",
            "base": True,
            "rrdVariables": [
                "Used-raw",
                "Used-rpn",
                "Used"
            ],
            "name": "Usage",
            "meta_type": "GraphDefinition",
            "inspector_type": "GraphDefinition"
        },
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getGraphDefinition"
}

lv_dp_details = {
    "uuid": "28048a29-d8f3-47b2-bf9e-6fdba2f1fa81",
    "action": "TemplateRouter",
    "result": {
        "record": {
            "isrow": True,
            "leaf": True,
            "description": "Linux LVM logical volume monitoring via SSH.",
            "rrdmin": "0",
            "availableRRDTypes": [
                "COUNTER",
                "GAUGE",
                "DERIVE",
                "ABSOLUTE"
            ],
            "name": "status.state",
            "rate": False,
            "meta_type": "RRDDataPoint",
            "newId": "state",
            "createCmd": "",
            "rrdtype": "GAUGE",
            "inspector_type": "RRDDataPoint",
            "rrdmax": None,
            "aliases": [
                {
                    "description": "Linux LVM logical volume monitoring via SSH.",
                    "name": "lvm_lv_state__bool",
                    "meta_type": "RRDDataPointAlias",
                    "inspector_type": "RRDDataPointAlias",
                    "formula": "",
                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state/aliases/lvm_lv_state__bool",
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state/aliases/lvm_lv_state__bool"
                }
            ],
            "type": "GAUGE",
            "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state",
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state"
        },
        "form": {
            "items": [
                {
                    "items": [
                        {
                            "vtype": None,
                            "fieldLabel": "Name",
                            "xtype": "idfield",
                            "labelStyle": None,
                            "value": "state",
                            "name": "newId",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The name of this data point' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Description",
                            "xtype": "textarea",
                            "labelStyle": None,
                            "value": "Linux LVM logical volume monitoring via SSH.",
                            "name": "description",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The description of this data point' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Type",
                            "xtype": "rrdtype",
                            "labelStyle": None,
                            "value": "GAUGE",
                            "name": "rrdtype",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The type of data point we have' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Create Command",
                            "xtype": "textarea",
                            "labelStyle": None,
                            "value": "",
                            "name": "createCmd",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "RRD Minimum",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "0",
                            "name": "rrdmin",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "RRD Maximum",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": None,
                            "name": "rrdmax",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Alias",
                            "xtype": "alias",
                            "labelStyle": None,
                            "value": [
                                {
                                    "description": "Linux LVM logical volume monitoring via SSH.",
                                    "name": "lvm_lv_state__bool",
                                    "meta_type": "RRDDataPointAlias",
                                    "inspector_type": "RRDDataPointAlias",
                                    "formula": "",
                                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state/aliases/lvm_lv_state__bool",
                                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/LogicalVolume/datasources/status/datapoints/state/aliases/lvm_lv_state__bool"
                                }
                            ],
                            "name": "aliases",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        }
                    ],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataPointDetails"
}

fs_dp_details = {
    "uuid": "83efb7e2-065b-4b0b-9047-fc255e1fa0c5",
    "action": "TemplateRouter",
    "result": {
        "record": {
            "isrow": True,
            "leaf": True,
            "description": "Linux file system monitoring via SSH.",
            "rrdmin": "0",
            "availableRRDTypes": [
                "COUNTER",
                "GAUGE",
                "DERIVE",
                "ABSOLUTE"
            ],
            "name": "disk.percentUsed",
            "rate": False,
            "meta_type": "RRDDataPoint",
            "newId": "percentUsed",
            "createCmd": "",
            "rrdtype": "GAUGE",
            "inspector_type": "RRDDataPoint",
            "rrdmax": None,
            "aliases": [
                {
                    "description": "Linux file system monitoring via SSH.",
                    "name": "fs__pct",
                    "meta_type": "RRDDataPointAlias",
                    "inspector_type": "RRDDataPointAlias",
                    "formula": "",
                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs__pct",
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs__pct"
                },
                {
                    "description": "Linux file system monitoring via SSH.",
                    "name": "fs_used__pct",
                    "meta_type": "RRDDataPointAlias",
                    "inspector_type": "RRDDataPointAlias",
                    "formula": "",
                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs_used__pct",
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs_used__pct"
                }
            ],
            "type": "GAUGE",
            "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed",
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed"
        },
        "form": {
            "items": [
                {
                    "items": [
                        {
                            "vtype": None,
                            "fieldLabel": "Name",
                            "xtype": "idfield",
                            "labelStyle": None,
                            "value": "percentUsed",
                            "name": "newId",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The name of this data point' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Description",
                            "xtype": "textarea",
                            "labelStyle": None,
                            "value": "Linux file system monitoring via SSH.",
                            "name": "description",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The description of this data point' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Type",
                            "xtype": "rrdtype",
                            "labelStyle": None,
                            "value": "GAUGE",
                            "name": "rrdtype",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The type of data point we have' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Create Command",
                            "xtype": "textarea",
                            "labelStyle": None,
                            "value": "",
                            "name": "createCmd",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "RRD Minimum",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "0",
                            "name": "rrdmin",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "RRD Maximum",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": None,
                            "name": "rrdmax",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Alias",
                            "xtype": "alias",
                            "labelStyle": None,
                            "value": [
                                {
                                    "description": "Linux file system monitoring via SSH.",
                                    "name": "fs__pct",
                                    "meta_type": "RRDDataPointAlias",
                                    "inspector_type": "RRDDataPointAlias",
                                    "formula": "",
                                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs__pct",
                                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs__pct"
                                },
                                {
                                    "description": "Linux file system monitoring via SSH.",
                                    "name": "fs_used__pct",
                                    "meta_type": "RRDDataPointAlias",
                                    "inspector_type": "RRDDataPointAlias",
                                    "formula": "",
                                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs_used__pct",
                                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/percentUsed/aliases/fs_used__pct"
                                }
                            ],
                            "name": "aliases",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        }
                    ],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataPointDetails"
}

fs_dp_details_2 = {
    "uuid": "ba921802-4a6e-49cb-83cc-198b0f812d33",
    "action": "TemplateRouter",
    "result": {
        "record": {
            "isrow": True,
            "leaf": True,
            "description": "Linux file system monitoring via SSH.",
            "rrdmin": "0",
            "availableRRDTypes": [
                "COUNTER",
                "GAUGE",
                "DERIVE",
                "ABSOLUTE"
            ],
            "name": "disk.usedBlocks",
            "rate": False,
            "meta_type": "RRDDataPoint",
            "newId": "usedBlocks",
            "createCmd": "",
            "rrdtype": "GAUGE",
            "inspector_type": "RRDDataPoint",
            "rrdmax": None,
            "aliases": [
                {
                    "description": "Linux file system monitoring via SSH.",
                    "name": "fs_used__bytes",
                    "meta_type": "RRDDataPointAlias",
                    "inspector_type": "RRDDataPointAlias",
                    "formula": "${here/blockSize},*",
                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/fs_used__bytes",
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/fs_used__bytes"
                },
                {
                    "description": "Linux file system monitoring via SSH.",
                    "name": "usedFilesystemSpace__bytes",
                    "meta_type": "RRDDataPointAlias",
                    "inspector_type": "RRDDataPointAlias",
                    "formula": "${here/blockSize},*",
                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/usedFilesystemSpace__bytes",
                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/usedFilesystemSpace__bytes"
                }
            ],
            "type": "GAUGE",
            "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks",
            "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks"
        },
        "form": {
            "items": [
                {
                    "items": [
                        {
                            "vtype": None,
                            "fieldLabel": "Name",
                            "xtype": "idfield",
                            "labelStyle": None,
                            "value": "usedBlocks",
                            "name": "newId",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The name of this data point' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Description",
                            "xtype": "textarea",
                            "labelStyle": None,
                            "value": "Linux file system monitoring via SSH.",
                            "name": "description",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The description of this data point' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Type",
                            "xtype": "rrdtype",
                            "labelStyle": None,
                            "value": "GAUGE",
                            "name": "rrdtype",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='The type of data point we have' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Create Command",
                            "xtype": "textarea",
                            "labelStyle": None,
                            "value": "",
                            "name": "createCmd",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "RRD Minimum",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": "0",
                            "name": "rrdmin",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "RRD Maximum",
                            "xtype": "textfield",
                            "labelStyle": None,
                            "value": None,
                            "name": "rrdmax",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        },
                        {
                            "vtype": None,
                            "fieldLabel": "Alias",
                            "xtype": "alias",
                            "labelStyle": None,
                            "value": [
                                {
                                    "description": "Linux file system monitoring via SSH.",
                                    "name": "fs_used__bytes",
                                    "meta_type": "RRDDataPointAlias",
                                    "inspector_type": "RRDDataPointAlias",
                                    "formula": "${here/blockSize},*",
                                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/fs_used__bytes",
                                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/fs_used__bytes"
                                },
                                {
                                    "description": "Linux file system monitoring via SSH.",
                                    "name": "usedFilesystemSpace__bytes",
                                    "meta_type": "RRDDataPointAlias",
                                    "inspector_type": "RRDDataPointAlias",
                                    "formula": "${here/blockSize},*",
                                    "id": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/usedFilesystemSpace__bytes",
                                    "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/datasources/disk/datapoints/usedBlocks/aliases/usedFilesystemSpace__bytes"
                                }
                            ],
                            "name": "aliases",
                            "disabled": False,
                            "inputAttrTpl": " data-qtip='' ",
                            "anchor": "85%",
                            "allowBlank": True
                        }
                    ],
                    "xtype": "fieldset"
                }
            ]
        }
    },
    "tid": 1,
    "type": "rpc",
    "method": "getDataPointDetails"
}

graph_points = {
    "uuid": "0c05668d-f0ef-4979-b623-8bedf562f479",
    "action": "TemplateRouter",
    "result": {
        "data": [
            {
                "dpName": "disk_usedBlocks",
                "stacked": False,
                "description": "disk_usedBlocks",
                "name": "Used",
                "format": "%7.2lf%s",
                "color": "",
                "skipCalc": False,
                "limit": -1,
                "id": "Used",
                "lineWidth": 1,
                "meta_type": "DataPointGraphPoint",
                "newId": "Used",
                "lineType": "LINE",
                "rrdVariables": "None",
                "inspector_type": "DataPointGraphPoint",
                "cFunc": "AVERAGE",
                "rpn": "${here/blockSize},*",
                "type": "DataPoint",
                "legend": "${graphPoint/id}",
                "uid": "/zport/dmd/Devices/Server/TEST/rrdTemplates/FileSystem/graphDefs/Usage/graphPoints/Used"
            }
        ],
        "success": True
    },
    "tid": 1,
    "type": "rpc",
    "method": "getGraphPoints"
}
