# Zenoss API Client

[![Documentation Status](https://readthedocs.org/projects/zenossapiclient/badge/)](http://zenossapiclient.readthedocs.io/en/latest/)

Python module for interacting with the Zenoss API an an object-oriented way.
Tested with Zenoss 5.2.x, no guarantees for earlier versions...

The philosophy here is to use objects to work with everything in the Zenoss API, and to try to normalize the various calls to the different routers.
Thus `get` methods will always return an object, `list` methods will return data.
All methods to add or create start with `add`, all remove or delete start with `delete`.
As much as possible the methods try to hide the idiosyncrasies of the JSON API, and to do the work for you, for example by letting you use a device name instead of having to provide the full device UID for every call.

## Installing

```
pip install ZenossAPIClient
```

## Using

```
In [1]: from zenossapi import apiclient as zapi

In [2]: zenoss_client = zapi.Client(host=<zenoss host>, user=<zenoss username>, password=<zenoss password>, ssl_verify=True)
In [3]: device_router = zenoss_client.get_router('device')
In [4]: device_class = device_router.get_device_class('Server/SSH/Linux')
In [5]: my_server = device_class.get_device('my.server.example.com')
In [6]: remodel_job = my_server.remodel()
In [7]: print remodel_job
9ba5c8d7-58de-4f18-96fe-d362841910d3
```

Supports the Zenoss JobsRouter, DeviceRouter, TemplateRouter, EventsRouter, and PropertiesRouter so far.
