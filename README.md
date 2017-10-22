# Zenoss API Client

Python module for interacting with the Zenoss API an an object-oriented way.
Tested with Zenoss 5.2.x, no guarantees for earlier versions...

The philosophy here is to use objects to work with everything in the Zenoss API, and to try to normalize the various calls to the different routers.
Thus `get` methods will always return an object, `list` methods will return data.
All methods to add or create start with `create`, all remove or delete start with `delete`.
As much as possible the methods try to hide the idiosyncrasies of the JSON API, and to do the work for you, for example by letting you use a device name instead of having to provide the full device UID for every call.

## Using

```
from zenossapi import apiclient as zapi

zenoss_client = zapi.Client(host=<zenoss host>, user=<zenoss username>, password=<zenoss password>, ssl_verify=True)
events_router = zenoss_client.get_router('events')
```

Supports the Zenoss JobsRouter, DeviceRouter, TemplateRouter, and EventsRouter so far.
