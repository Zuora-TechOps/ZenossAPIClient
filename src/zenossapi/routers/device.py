# -*- coding: utf-8 -*-

"""
Zenoss device_router
"""

import re
import warnings
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers import ZenossRouter
from zenossapi.routers.properties import PropertiesRouter
from zenossapi.routers.template import TemplateRouter


class DeviceRouter(ZenossRouter):
    """
    Class for interacting with the Zenoss device router
    """

    def __init__(self, url, headers, ssl_verify):
        super(DeviceRouter, self).__init__(url, headers, ssl_verify,
                                           'device_router', 'DeviceRouter')
        self.uid = None
        self.properties = None
        self.prod_states_by_value = {}
        self.prod_states_by_name = {}
        self.priorities_by_value = {}
        self.priorities_by_name = {}

        prod_states_data = self._router_request(
            self._make_request_data(
                'getProductionStates',
                dict(),
            )
        )
        for state in prod_states_data['data']:
            self.prod_states_by_name[state['name']] = state['value']
            self.prod_states_by_value[state['value']] = state['name']

        priority_data = self._router_request(
            self._make_request_data(
                'getPriorities',
                dict(),
            )
        )
        for p in priority_data['data']:
            self.priorities_by_name[p['name']] = p['value']
            self.priorities_by_value[p['value']] = p['name']

    def __repr__(self):
        if self.uid:
            identifier = self.uid
        else:
            identifier = hex(id(self))

        return '<{0} object at {1}>'.format(
            type(self).__name__, identifier
        )

    def _find_nodes_in_tree(self, tree_data):
        """
        Works through the dict structure returned by the Zenoss API for
        a device class tree and returns the nodes.

        Arguments:
            tree_data (dict): Templates data returned by the API

        Returns:
            list:
        """
        tree = []
        for node in tree_data['children']:
            node_children = self._find_nodes_in_tree(node)
            tree.append(
                dict(
                    uid=node['path'],
                    children=node_children
                )
            )

        return tree

    def _get_info_by_uid(self, uid):
        """
        Get object properties by the full UID

        Arguments:
            uid (str): UID for the object

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'getInfo',
                dict(uid=uid),
            )
        )

    def _get_device_by_uid(self, device_uid):
        """
        Get a device by its full UID

        Arguments:
            device_uid (str): The uid of the device to get

        Returns:
            ZenossDevice:
        """
        device_data = self._get_info_by_uid(device_uid)

        return ZenossDevice(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            device_data['data']
        )

    def _move_devices_by_uid(self, devices, device_class):
        """
        Move the devices in the list to a new device class.

        Arguments:
            devices (list): List of device uids to move
            device_class (str): Target device class for the move

        Returns:
            list(dict(str, str)): List of Job manager info for each device move ::

            [{
                'uuid': Job manager uuid for the device move,
                'description': Description of the move job,
            }]

        """
        if not isinstance(devices, list):
            raise ZenossAPIClientError(
                'Type error: devices to move must be a list')

        move_job_data = self._router_request(
            self._make_request_data(
                'moveDevices',
                dict(
                    uids=devices,
                    target=device_class,
                ),
            )
        )
        move_jobs = []
        for mj in move_job_data['new_jobs']:
            move_jobs.append(dict(
                uuid=mj['uuid'],
                description=mj['description']
            ))

        return move_jobs

    def _add_device_class(self, new_class, parent,
                          description='', connection_info=None):
        """
        Add a new device class under a parent path

        Arguments:
            new_class (str): Name of the device class to add
            parent (str): Device class to place the new class under
            description (str): Description for the new class
            connection_info (list): zProperties that are the credentials for
                accessing this device class, e.g. zCommandUsername,
                zCommandPassword

        Returns:
            ZenossDeviceClass:
        """
        response_data = self._router_request(
            self._make_request_data(
                'addDeviceClassNode',
                dict(
                    type='organizer',
                    contextUid=parent,
                    id=new_class,
                    description=description,
                    connectionInfo=connection_info,
                )
            )
        )

        dc_data = self._get_info_by_uid(response_data['nodeConfig']['path'])
        return ZenossDeviceClass(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            dc_data['data']
        )

    def _lock_devices_by_uid(self, devices, updates=False, deletion=False,
                             send_event=False):
        """
        Lock devices from changes.

        Arguments:
            devices (list): Uids of the devices to lock
            updates (bool): Lock devices from updates
            deletion (bool): Lock devices from deletion
            send_event (bool): Send an event when an action is blocked by locking

        Returns:
            str: Response message
        """
        response_data = self._router_request(
            self._make_request_data(
                'lockDevices',
                dict(
                    uids=devices,
                    hashcheck='',
                    updates=updates,
                    deletion=deletion,
                    sendEvent=send_event,
                )
            )
        )

        return response_data['msg']

    def _reset_device_ip_addresses_by_uid(self, devices, ip_address=''):
        """
        Reset IP addresses of devices, either by DNS lookup or manually
        specified address

        Arguments:
            devices (list): Uids of devices to reset IP address for
            ip_address (str): IP address to set device to
        """
        response_data = self._router_request(
            self._make_request_data(
                'resetIp',
                dict(
                    uids=devices,
                    hashcheck='',
                    ip=ip_address,
                )
            )
        )

        return response_data['msg']

    def _set_production_state_by_uids(self, devices, production_state):
        """
        Sets the production state of a list of devices.

        Arguments:
            devices (list): Uids of devices to set production state for
            production_state (int): Numeric value of production state to set

        Returns:
            str: Response message
        """
        if production_state not in self.prod_states_by_value:
            raise ZenossAPIClientError(
                'Production state {0} is not a valid option'.format(
                    production_state))

        response_data = self._router_request(
            self._make_request_data(
                'setProductionState',
                dict(
                    uids=devices,
                    hashcheck='',
                    prodState=production_state,
                )
            )
        )

        return response_data['msg']

    def _set_priority_by_uids(self, devices, priority):
        """
        Sets the priority of a list of devices

        Arguments:
            devices (list): Uids of devices to set priority for
            priority (int): Numeric value of priority to set

        Returns:
            str: Response message
        """
        if priority not in self.priorities_by_value:
            raise ZenossAPIClientError(
                "Priority {0} is not a valid option".format(
                    priority
                )
            )

        response_data = self._router_request(
            self._make_request_data(
                'setPriority',
                dict(
                    uids=devices,
                    hashcheck='',
                    priority=priority,
                )
            )
        )

        return response_data['msg']

    def _set_collector_by_uids(self, devices, collector):
        """
        Sets the collector for a list of devices.

        Arguments:
            devices (list): Uids of the devices to set collector for
            collector (str): The collector to set devices to use

        Returns:
            list(dict(str, str)): List of Job manager info for each device move ::

            [{
                'uuid': Job manager uuid for the device move
                'description': Description of the move job
            }]

        """
        collector_job_data = self._router_request(
            self._make_request_data(
                'setCollector',
                dict(
                    uids=devices,
                    hashcheck='',
                    collector=collector,
                )
            )
        )

        return dict(
            uuid=collector_job_data['new_jobs']['uuid'],
            description=collector_job_data['new_jobs']['description']
        )

    def _delete_devices_by_uid(self, devices, action, del_events=False,
                               del_perf=False):
        """
        Remove a list of devices from their organizer UID, or delete them
        from Zenoss altogether.

        Arguments:
            devices (list): Uids of devices to remove/delete
            action (str): 'remove' to remove the devices from their organizer,
                'delete' to delete them from Zenoss
            del_events (bool): Remove all events for the devices
            del_perf (bool): Remove all perf data for the devices

        Returns:
            dict:
        """
        if action not in ['remove', 'delete']:
            raise ZenossAPIClientError(
                "Delete action must be either 'remove' or 'delete'"
            )

        response_data = self._router_request(
            self._make_request_data(
                'removeDevices',
                dict(
                    uids=devices,
                    hashcheck='',
                    action=action,
                    del_events=del_events,
                    del_perf=del_perf,
                )
            )
        )

        return response_data

    def _set_components_monitored_by_uids(self, components, monitor=True):
        """
        Sets the monitored state for a list of components.

        Arguments:
            components (list): Uids of the components to update
            monitor (bool): True to monitor, False to stop monitoring

        Returns:
            str: Response message
        """
        response_data = self._router_request(
            self._make_request_data(
                'setComponentsMonitored',
                dict(
                    uids=components,
                    hashcheck='',
                    monitor=monitor,
                )
            )
        )

        return response_data['msg']

    def _lock_components_by_uid(self, components, updates=False, deletion=False,
                                send_event=False):
        """
        Lock devices from changes.

        Arguments:
            components (list): Uids of the components to lock
            updates (bool): Lock components from updates
            deletion (bool): Lock components from deletion
            send_event (bool): Send an event when an action is blocked by locking

        Returns:
            str: Response message
        """
        response_data = self._router_request(
            self._make_request_data(
                'lockComponents',
                dict(
                    uids=components,
                    hashcheck='',
                    updates=updates,
                    deletion=deletion,
                    sendEvent=send_event,
                )
            )
        )

        return response_data['msg']

    def _delete_components_by_uid(self, components):
        """
        Deletes a list of components from a device.

        Arguments:
            components (list): Uids of the components to delete

        Returns:
            str: Response message
        """
        response_data = self._router_request(
            self._make_request_data(
                'deleteComponents',
                dict(
                    uids=components,
                    hashcheck=''
                )
            )
        )

        return response_data['msg']

    def get_tree(self, device_class):
        """
        Get the tree structure of a device class.

        Arguments:
            device_class (str): Device class to use as the top of the tree

        Returns:
            dict:
        """
        tree_data = self._router_request(
            self._make_request_data(
                'getTree',
                dict(id=device_class)
            )
        )

        return self._find_nodes_in_tree(tree_data[0])

    def list_collectors(self):
        """
        Get the list of collectors.

        Returns:
            list:
        """
        return self._router_request(
            self._make_request_data(
                'getCollectors',
                dict(),
            )
        )

    def list_device_classes(self):
        """
        Get the list of all device classes.

        Returns:
            list:
        """
        device_classes_data = self._router_request(
            self._make_request_data(
                'getDeviceClasses',
                dict(),
            )
        )

        dc_list = []
        for dc in device_classes_data['deviceClasses']:
            if len(dc['name']) == 0 or dc['name'] == '/':
                continue
            dc_list.append('Devices{0}'.format(dc['name']))

        return dc_list

    def list_systems(self):
        """
        Get the list of all systems.

        Returns:
            list:
        """
        systems_data = self._router_request(
            self._make_request_data(
                'getSystems',
                dict(),
            )
        )

        systems = []
        for s in systems_data['systems']:
            systems.append(s['name'])

        return systems

    def list_groups(self):
        """
        Get the list of all groups.

        Returns:
            list:
        """
        groups_data = self._router_request(
            self._make_request_data(
                'getGroups',
                dict(),
            )
        )

        groups = []
        for g in groups_data['groups']:
            groups.append(g['name'])

        return groups

    def list_locations(self):
        """
        Get the list of all locations.

        Returns:
            list:
        """
        location_data = self._router_request(
            self._make_request_data(
                'getLocations',
                dict(),
            )
        )

        loci = []
        for l in location_data['locations']:
            loci.append(l['name'])

        return loci

    def get_device_class(self, device_class):
        """
        Get a device class

        Arguments:
            device_class (str): The name of the device class

        Returns:
            ZenossDeviceClass:
        """
        if not device_class.startswith('Devices'):
            if device_class.startswith('/'):
                device_class = 'Devices{0}'.format(device_class)
            else:
                device_class = 'Devices/{0}'.format(device_class)

        dc_data = self._get_info_by_uid(device_class)

        return ZenossDeviceClass(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            dc_data['data']
        )


class ZenossDeviceClass(DeviceRouter):
    """
    Class for Zenoss device class objects
    """

    def __init__(self, url, headers, ssl_verify, device_class_data):
        super(ZenossDeviceClass, self).__init__(url, headers, ssl_verify)

        self.uid = device_class_data['uid'].replace('/zport/dmd/', '', 1)
        self.name = device_class_data['name']
        self.severity = device_class_data['severity']
        self.id = device_class_data['id']
        self.description = device_class_data['description']
        self.connectionInfo = device_class_data['connectionInfo']
        self.events = device_class_data['events']

    def list_devices(self, params=None, keys=None, start=0, limit=50,
                     sort='name', dir='ASC'):
        """
        List the devices contained in a device class. Supports pagination.

        Arguments:
            params (dict): Key/value filters for the search, options are
                name, ipAddress, deviceClass, or productionState
            keys (list): List of keys to return for the devices found
            start (int): Offset to start device list from, default 0
            limit (int): The number of results to return, default 50
            sort (str): Sort key for the list, default is 'name'
            dir (str): Sort order, either 'ASC' or 'DESC', default is 'ASC'

        Returns:
            dict:
        """
        if not keys:
            keys = [
                'name',
                'uid',
                'ipAddressString',
                'collector',
                'productionState',
                'priority',
                'location',
                'groups',
                'events'
            ]

        device_data = self._router_request(
            self._make_request_data(
                'getDevices',
                dict(
                    uid=self.uid,
                    params=params,
                    keys=keys,
                    start=start,
                    limit=limit,
                    sort=sort,
                    dir=dir,
                )
            )
        )

        device_list = dict(
            total=device_data['totalCount'],
            hash=device_data['hash'],
            devices=[],
        )
        for device in device_data['devices']:
            devinfo = dict()
            for key in keys:
                if key == "uid":
                    devinfo['uid'] = device['uid'].replace('/zport/dmd/', '', 1)
                elif key == "location":
                    if device['location']:
                        devinfo['location'] = device['location']['name']
                    else:
                        devinfo['location'] = None
                else:
                    devinfo[key] = device[key]
            device_list['devices'].append(devinfo)

        return device_list

    def get_devices(self, params=None, start=0, limit=50, sort='name',
                    dir='ASC'):
        """
        Get the devices contained in a device class. Supports pagination.

        Arguments:
            params (dict): Key/value filters for the search, options are
                name, ipAddress, deviceClass, or productionState
            start (int): Offset to start device list from, default 0
            limit (int): The number of results to return, default 50
            sort (str): Sort key for the list, default is 'name'
            dir (str): Sort order, either 'ASC' or 'DESC', default is 'ASC'

        Returns:
            dict(int, str, list(ZenossDevice)): ::

            {
                'total': Total number of devices found
                 'hash': Hashcheck to determine if any devices have changed,
                 'devices': ZenossDevice objects,
            }

        """
        device_data = self._router_request(
            self._make_request_data(
                'getDevices',
                dict(
                    uid=self.uid,
                    params=params,
                    start=start,
                    limit=limit,
                    sort=sort,
                    dir=dir,
                )
            )
        )

        device_list = dict(
            total=device_data['totalCount'],
            hash=device_data['hash'],
            devices=[]
        )
        for device in device_data['devices']:
            device_list['devices'].append(self._get_device_by_uid(
                device['uid'].replace('/zport/dmd/', '', 1)))

        return device_list

    def get_device(self, device_name):
        """
        Get a device from the device class

        Arguments:
            device_name (str): The name of the device to get

        Returns:
            ZenossDevice:
        """
        device_uid = '{0}/devices/{1}'.format(self.uid, device_name)
        return self._get_device_by_uid(device_uid)

    def add_subclass(self, name, description='', connection_info=None):
        """
        Add a new subclass to the device class.

        Arguments:
            name (str): Name of the new subclass
            description (str): Description for the new subclass
            connection_info (list): zProperties that represent the credentials
                for access in the subclass
        """
        return self._add_device_class(name, self.uid, description,
                                      connection_info)

    def add_device(self, device_name, title='', ip_address='', location=None,
                   systems=None, groups=None, model=False,
                   collector='localhost', production_state=500, comments='',
                   priority=3, snmp_community='', snmp_port=161, rack_slot='',
                   hw_manufacturer='', hw_product_name='', os_manufacturer='',
                   os_product_name='', asset_tag='', serial_number='',
                   windows_user='', windows_password='', zcommand_user='',
                   zcommand_password='', configuration_properties=None,
                   custom_properties=None):
        """
        Add a new device to the device class.

        Arguments:
            device_name (str): Name of the new device, will be the device id
            title (str): Optional title for the device, default is to match
                the device_name
            ip_address (str): Ip address for the device, default is to derive
                this from DNS based on device_name
            location (str): Location for the device
            systems (list[(str)]: List of systems for the device
            groups (list[(str)]: List of groups for the device
            model (bool): Set to True to model the device automatically after
                creation
            collector (str): Collector to use for the device
            production_state (int): Numerical production state for the device,
                default is 500 (Pre-Production)
            comments (str): Comments for the device
            priority (int): Numerical priority for the device, default
                is 3 (Normal)
            snmp_community (str): SNMP community string for the device
            snmp_port (int): SNMP port for the device
            rack_slot (str): Rack slot description
            hw_manufacturer (str): Hardware manufacturer name, default is to
                derive by modeling
            hw_product_name (str): Hardware product name, default is to
                derive by modeling
            os_manufacturer (str): Operating system developer, default is to
                derive by modeling
            os_product_name (str): Operating system name, default is to
                derive by modeling
            asset_tag (str): Device's inventory asset tag
            serial_number (str): Device's serial number
            windows_user (str): Username for Windows device monitoring
            windows_password (str): Password for the windows_user
            zcommand_user (str): Username for SSH-based monitoring user
            zcommand_password (str): Password for the zcommand_user
            configuration_properties (dict): Key/value pairs for setting
                Configuration Properties for the device
            custom_properties (dict): Key/value pairs for setting Custom
                Properties for the device

        Returns:
            str: ID of the add device job
        """
        if not configuration_properties:
            configuration_properties = dict()
        if not custom_properties:
            custom_properties = dict()
        if not systems:
            systems = []
        if not groups:
            groups = []

        job_data = self._router_request(
            self._make_request_data(
                'addDevice',
                dict(
                    deviceName=device_name,
                    deviceClass=self.uid.replace('Devices', ''),
                    title=title,
                    snmpCommunity=snmp_community,
                    snmpPort=snmp_port,
                    manageIp=ip_address,
                    locationPath='Locations/{0}'.format(location),
                    systemPaths=systems,
                    groupPaths=groups,
                    model=model,
                    collector=collector,
                    rackSlot=rack_slot,
                    productionState=production_state,
                    comments=comments,
                    hwManufacturer=hw_manufacturer,
                    hwProductName=hw_product_name,
                    osManufacturer=os_manufacturer,
                    osProductName=os_product_name,
                    priority=priority,
                    tag=asset_tag,
                    serialNumber=serial_number,
                    zWinUser=windows_user,
                    zWinPassword=windows_password,
                    zCommandPassword=zcommand_password,
                    zCommandUsername=zcommand_user,
                    zProperties=configuration_properties,
                    cProperties=custom_properties,
                )
            )
        )

        return job_data['new_jobs'][0]['uuid']

    def list_properties(self, params=None, sort=None, sort_dir='ASC'):
        """
        List the configuration properties for the device class

        Arguments:
            params (dict): Search parameters to filter the properties list on.
            sort (str): Sort key for the properties list.
            sort_dir (str): Sort direction, either ASC or DESC

        Returns:
            dict(int, list(dict)): ::

            {
                'total': Total count of properties returned.
                'properties': List of properties found.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.list_properties(self.uid, params=params, sort=sort,
                                  sort_dir=sort_dir)

    def list_local_properties(self):
        """
        List the locally defined configuration properties for the device class

        Returns:
            dict(int, list(dict)): ::

            {
                'total': Total count of properties returned.
                'properties': List of properties found.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.list_local_properties(self.uid)

    def list_custom_properties(self):
        """
        List the custom properties for the device class

        Returns:
            dict(int, list(dict)): ::

            {
                'total': Total count of properties returned.
                'properties': List of properties found.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.list_custom_properties(self.uid)

    def get_properties(self, params=None):
        """
        Get the configuration properties for the device class

        Arguments:
            params (dict): Search parameters for filter the properties on.

        Returns:
            dict(int, list(ZenossProperty)): ::

            {
                'total': Total count of properties returned.
                'properties': List of ZenossProperty objects.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_properties(self.uid, params=params)

    def get_property(self, zproperty):
        """
        Get a configuration property

        Arguments:
            zproperty (str): The id of the property to get

        Returns:
            ZenossProperty:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_property(self.uid, zproperty)

    def get_custom_properties(self, params=None):
        """
        Get the cProperties for the device class

        Arguments:
            params (dict): Search parameters for filter the properties on.

        Returns:
            dict(int, list(ZenossCustomProperty)): ::

            {
                'total': Total count of properties returned.
                'properties': List of ZenossCustomProperty objects.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_custom_properties(self.uid, params=params)

    def get_custom_property(self, cproperty):
        """
        Get a custom property for the device class

        Arguments:
            cproperty (str): ID of the property to get.

        Returns:
            ZenossCustomProperty:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_custom_property(self.uid, cproperty)

    def set_property(self, zproperty, value=None):
        """
        Set the value of a configuration property

        Arguments:
            zproperty (str): The id of the property to set a value for
            value (str): The value to set for the property

        Returns:
            bool:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.set_property_value(self.uid, zproperty, value=value)

    def delete_property(self, zproperty):
        """
        Delete the locally set value of a property for a device class

        Arguments:
            zproperty (str): ID of the property to delete.

        Returns:
            bool:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.delete_property(self.uid, zproperty)


class ZenossDevice(DeviceRouter):
    """
    Class for Zenoss device objects
    """

    def __init__(self, url, headers, ssl_verify, device_data):
        super(ZenossDevice, self).__init__(url, headers, ssl_verify)

        unneeded_props = ['class_label', 'class_plural_label',
                          'class_plural_short_label', 'class_short_label',
                          'deviceClass', 'inspector_type',
                          'ipAddress', 'meta_type', 'priorityLabel',
                          'productionStateLabel', 'pythonClass', 'uuid', ]

        default_props = ['collector', 'comments', 'description', 'device',
                         'deviceConnectionInfo', 'events', 'firstSeen',
                         'groups', 'icon', 'id', 'hwManufacturer', 'hwModel',
                         'lastChanged', 'lastCollected', 'links', 'locking',
                         'memory', 'name', 'osManufacturer', 'osModel',
                         'priority', 'productionState', 'rackSlot',
                         'serialNumber', 'severity', 'snmpAgent',
                         'snmpCommunity', 'snmpContact', 'snmpDescr',
                         'snmpLocation', 'snmpSysName', 'snmpVersion',
                         'sshLink', 'status', 'systems',
                         'tagNumber', 'uptime', ]

        for i in unneeded_props:
            if i in device_data:
                device_data.pop(i)

        uid = device_data.pop('uid')
        self.uid = uid.replace('/zport/dmd/', '', 1)

        location = device_data.pop('location')
        if location:
            self.location = location['name']
        else:
            self.location = None

        self.ip_address = device_data.pop('ipAddressString')

        for prop in default_props:
            setattr(self, prop, device_data.pop(prop))

        self.properties = device_data
        self.parent = self.uid.split('/devices/')[0]

    def list_components(self, meta_type=None, start=0, limit=50, sort='name',
                        dir='ASC', keys=None, name=None):
        """
        Get a list of all the components on a device. Supports pagination.

        Arguments:
            meta_type (str): Meta type of components to list
            start (int): Offset to start device list from, default 0
            limit (int): The number of results to return, default 50
            sort (str): Sort key for the list, default is 'name'
            dir (str): Sort order, either 'ASC' or 'DESC', default is 'ASC'
            keys (list): Keys to include in the returned data
            name (str): Regular expression pattern to filter on, requries
                the keys parameter

        Returns:
            dict(int, str, list): ::

            {
                'total': Total number of components found.
                'hash': Hash check to determine if components have changed
                'components': List of components found
            }

        """
        if name and not keys:
            warnings.warn("Filtering by name also requires a list of keys", UserWarning)
            name = None

        components_data = self._router_request(
            self._make_request_data(
                'getComponents',
                dict(
                    uid='/zport/dmd/{0}'.format(self.uid),
                    meta_type=meta_type,
                    start=start,
                    limit=limit,
                    sort=sort,
                    dir=dir,
                    keys=keys,
                    name=name,
                )
            )
        )

        components_list = dict(
            total=components_data['totalCount'],
            hash=components_data['hash'],
            components=[],
        )

        for c in components_data['data']:
            components_list['components'].append(
                c['uid'].split('/{0}/'.format(self.id))[-1])

        return components_list

    def get_components(self, meta_type=None, start=0, limit=50, sort='name',
                       dir='ASC'):
        """
        Get component objects for all components on the device.
        Supports Pagination.

        Arguments:
            meta_type (str): Meta type of components to list
            start (int): Offset to start device list from, default 0
            limit (int): The number of results to return, default 50
            sort (str): Sort key for the list, default is 'name'
            dir (str): Sort order, either 'ASC' or 'DESC', default is 'ASC'

        Returns:
            list(ZenossComponent):
        """
        components_list = self.list_components(meta_type=meta_type, start=start,
                                               limit=limit, sort=sort, dir=dir)

        components = []
        for component in components_list['components']:
            c_info = self._get_info_by_uid(
                '{0}/{1}'.format(self.uid, component))
            components.append(
                ZenossComponent(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    c_info['data']
                )
            )

        return components

    def get_component(self, component):
        """
        Get a component object.

        Arguments:
            component (str): Name of the component, e.g. 'hw/cpus/0'

        Returns:
            ZenossComponent:
        """
        c_info = self._get_info_by_uid('{0}/{1}'.format(self.uid, component))

        return ZenossComponent(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            c_info['data']
        )

    def list_user_commands(self):
        """
        Get the list of user commands for a device.

        Returns:
            dict(str, str): ::

            {
                name: Name of the user command
                description: Command description
            }

        """
        uc_data = self._router_request(
            self._make_request_data(
                'getUserCommands',
                dict(uid=self.uid),
            )
        )

        user_commands = []
        for uc in uc_data:
            user_commands.append(
                dict(
                    name=uc['id'],
                    description=uc['description']
                ))

        return user_commands

    def list_local_templates(self):
        """
        Get the list of monitoring templates defined locally on a device.

        Returns:
            list:
        """
        lt_data = self._router_request(
            self._make_request_data(
                'getLocalTemplates',
                dict(
                    uid=self.uid,
                    query='',
                ),
            )
        )

        local_templates = []
        for lt in lt_data['data']:
            local_templates.append(lt['uid'].split('/')[-1])

        return local_templates

    def get_local_templates(self):
        """
        Get ZenossTemplate objects for all locally defined templates.

        Returns:
            list(ZenossTemplate):
        """
        lt_list = self.list_local_templates()

        local_templates = []
        tr = TemplateRouter(self.api_url, self.api_headers, self.ssl_verify)
        for lt in lt_list:
            local_templates.append(
                tr._get_template_by_uid('{0}/{1}'.format(self.uid, lt))
            )

        return local_templates

    def add_local_template(self, template):
        """
        Add a local template to the device.

        Arguments:
            template (str): Name of the new local template
        """
        self._router_request(
            self._make_request_data(
                'addLocalTemplate',
                dict(
                    deviceUid=self.uid,
                    templateId=template,
                )
            )
        )

        return True

    def delete_local_template(self, template):
        """
        Remove a local template from the device.

        Arguments:
            template (str): Name of the template to remove
        """
        self._router_request(
            self._make_request_data(
                'removeLocalTemplate',
                dict(
                    deviceUid=self.uid,
                    templateId=template,
                )
            )
        )

        return True

    def list_active_templates(self):
        """
        Get the list of templates active on a device, both bound and local.

        Returns:
            list(dict(str, str)): ::

            {
                'name': Template name,
                'label': Display label for the template,
            }

        """
        templates_data = self._router_request(
            self._make_request_data(
                'getTemplates',
                dict(id=self.uid),
            )
        )

        templates = []
        for t in templates_data:
            templates.append(dict(
                name=t['uid'].split('/')[-1],
                label=t['text'])
            )

        return templates

    def get_active_templates(self):
        """
        Get ZenossTemplate objects for all active templates on a device.

        Returns:
            list(ZenossTemplate):
        """
        templates_data = self._router_request(
            self._make_request_data(
                'getTemplates',
                dict(id=self.uid),
            )
        )

        templates = []
        tr = TemplateRouter(self.api_url, self.api_headers, self.ssl_verify)
        for t in templates_data:
            tuid = t['uid'].replace('/zport/dmd/', '', 1)
            templates.append(
                tr._get_template_by_uid(tuid)
            )

        return templates

    def list_unbound_templates(self):
        """
        Get the list of available templates that are not bound to the device.

        Returns:
            list(dict(str, str)): ::

            {
                'name': Template name,
                'label': Display label for the template,
            }

        """
        templates_data = self._router_request(
            self._make_request_data(
                'getUnboundTemplates',
                dict(uid=self.uid),
            )
        )

        templates = []
        for t in templates_data['data']:
            templates.append(dict(
                name=t[0],
                label=t[1]
            ))

        return templates

    def get_unbound_templates(self):
        """
        Get ZenossTemplate objects for available templates that are not bound
        to the device.

        Returns:
            list(ZenossTemplate):
        """
        ut_list = self.list_unbound_templates()
        find_path = re.compile('\((\/.*)\)')
        templates = []
        tr = TemplateRouter(self.api_url, self.api_headers, self.ssl_verify)
        for t in ut_list:
            m = re.search(find_path, t['label'])
            if m:
                if m.groups()[0] == "/":
                    path = ''
                else:
                    path = m.groups()[0]
                uid = 'Devices{0}/rrdTemplates/{1}'.format(path, t['name'])
                templates.append(
                    tr._get_template_by_uid(uid)
                )

        return templates

    def list_bound_templates(self):
        """
        Get the list of templates bound to a device, does not include
        local templates.

        Returns:
            list(dict(str, str)): ::

            {
                'name': Template name,
                'label': Display label for the template,
            }

        """
        templates_data = self._router_request(
            self._make_request_data(
                'getBoundTemplates',
                dict(uid=self.uid),
            )
        )

        templates = []
        for t in templates_data['data']:
            templates.append(dict(
                name=t[0],
                label=t[1]
            ))

        return templates

    def get_bound_templates(self):
        """
        Get ZenossTemplate objects templates that are bound to the device.

        Returns:
            list(ZenosTemplate):
        """
        bt_list = self.list_bound_templates()
        find_path = re.compile('\((\/.*)\)')
        templates = []
        tr = TemplateRouter(self.api_url, self.api_headers, self.ssl_verify)
        for t in bt_list:
            m = re.search(find_path, t['label'])
            if m:
                if m.groups()[0] == "/":
                    path = ''
                else:
                    path = m.groups()[0]
                if path.endswith(self.name):
                    path = path.replace(self.name,
                                        'devices/{0}'.format(self.name))
                    uid = 'Devices{0}/{1}'.format(path, t['name'])
                else:
                    uid = 'Devices{0}/rrdTemplates/{1}'.format(path, t['name'])
                templates.append(
                    tr._get_template_by_uid(uid)
                )

        return templates

    def list_overridable_templates(self):
        """
        Get the list of available templates on a device that can be overridden.

        Returns:
            list(dict(str, str)): ::

            {
                'name': Template name,
                'label': Display label for the template,
            }

        """
        template_data = self._router_request(
            self._make_request_data(
                'getOverridableTemplates',
                dict(
                    uid=self.uid,
                    query='',
                ),
            )
        )

        templates = []
        for t in template_data['data']:
            templates.append(dict(
                name=t['uid'].split('/')[-1],
                label=t['label'])
            )

        return templates

    def get_overridable_templates(self):
        """
        Get ZenossTemplate objects for templates that can be overridden.

        Returns:
            list(ZenossTemplate):
        """
        template_data = self._router_request(
            self._make_request_data(
                'getOverridableTemplates',
                dict(
                    uid=self.uid,
                    query='',
                )
            )
        )

        templates = []
        tr = TemplateRouter(self.api_url, self.api_headers, self.ssl_verify)
        for t in template_data['data']:
            templates.append(
                tr._get_template_by_uid(t['uid'].replace('/zport/dmd/', '', 1))
            )

        return templates

    def set_bound_templates(self, templates):
        """
        Set a list of templates as bound to a device.

        Arguments:
            templates (list): List of template names
        """
        self._router_request(
            self._make_request_data(
                'setBoundTemplates',
                dict(
                    uid=self.uid,
                    templateIds=templates,
                )
            )
        )

        return True

    def bind_or_unbind_template(self, path, template):
        """
        Binds a template to the device if it's unbound, or unbinds it if
        it's bound.

        Arguments:
            path (str): Template's path, as given in the display label
            template (str): Name of the template to bind/unbind
        """
        self._router_request(
            self._make_request_data(
                'bindOrUnbindTemplate',
                dict(
                    uid=self.uid,
                    templateUid='Devices{0}/rrdtemplates/{1}'.format(path,
                                                                     template)
                )
            )
        )

        return True

    def reset_bound_templates(self):
        """
        Remove all bound templates from device.
        """
        self._router_request(
            self._make_request_data(
                'resetBoundTemplates',
                dict(uid=self.uid)
            )
        )

        return True

    def move(self, device_class):
        """
        Move the device to a different device class

        Arguments:
            device_class (str): Name of the device class to move the device into

        Returns:
            str: uuid of the Job Manager job for the move
        """
        job_data = self._move_devices_by_uid([self.uid], device_class)
        return job_data[0]['uuid']

    def reidentify(self, new_id):
        """
        Change the device's id in Zenoss. Note that changing the device id will
        cause the loss of all graph data for the device.

        Arguments:
            new_id (str): New ID for the device
        """
        return_data = self._router_request(
            self._make_request_data(
                'renameDevice',
                dict(
                    uid=self.uid,
                    newId=new_id,
                ),
            )
        )

        self.id = new_id
        self.name = new_id
        self.uid = '{0}/devices/{1}'.format(self.parent, self.uid)

        return True

    def lock(self, updates=False, deletion=False, send_event=False):
        """
        Lock the device for changes.

        Arguments:
            updates (bool): Lock for updates
            deletion (bool): Lock for deletion
            send_event (bool): Send an event when an action is blocked by locking

        Returns:
            str: Response message
        """
        return self._lock_devices_by_uid([self.uid], updates=updates,
                                         deletion=deletion,
                                         send_event=send_event)

    def lock_for_updates(self, send_event=False):
        """
        Lock the device for updates.

        Arguments:
            send_event (bool): Send an event when updates are blocked by locking

        Returns:
            str: Response message
        """
        return self.lock(updates=True, send_event=send_event)

    def lock_for_deletion(self, send_event=False):
        """
        Lock the device for updates.

        Arguments:
            send_event (bool): Send an event when deletion is blocked by locking

        Returns:
            str: Response message
        """
        return self.lock(deletion=True, send_event=send_event)

    def reset_ip_address(self, ip_address=''):
        """
        Reset the IP address of the device to ip_address if specified or to the
        result of a DNS lookup if not.

        Arguments:
            ip_address (str): IP address to set device to

        Returns:
            str: Response message
        """
        return self._reset_device_ip_addresses_by_uid([self.uid],
                                                      ip_address=ip_address)

    def set_production_state(self, production_state):
        """
        Set the production state for the device.

        Arguments:
            production_state (int): Numeric value for the desired production
                state.

        Returns:
            str: Response message
        """
        message = self._set_production_state_by_uids([self.uid],
                                                     production_state)
        self.productionState = production_state
        return message

    def set_priority(self, priority):
        """
        Set the priority for the device.

        Arguments:
            priority (int): Numeric value for the desired priority

        Returns:
            str: Reponse message
        """
        message = self._set_priority_by_uids([self.uid], priority)
        self.priority = priority
        return message

    def set_collector(self, collector):
        """
        Set the collector for the device.

        Arguments:
            collector (str): The collector to use for the device

        Returns:
            str: uuid of the Job Manager job for the change
        """
        job_data = self._set_collector_by_uids([self.uid], collector)
        return job_data['uuid']

    def delete(self, action, del_events=False, del_perf=True):
        """
        Remove a device from its organizer, or delete it from Zenoss altogether.

        Arguments:
            action (str): 'remove' to remove the devices from their organizer,
                'delete' to delete them from Zenoss
            del_events (bool): Remove all events for the devices
            del_perf (bool): Remove all perf data for the devices

        Returns:
            bool:
        """
        self._delete_devices_by_uid([self.uid], action, del_events, del_perf)

        return True

    def remodel(self):
        """
        Remodel the device.

        Returns:
            str: uuid of the Job Manager job for the remodel
        """
        response_data = self._router_request(
            self._make_request_data(
                'remodel',
                dict(deviceUid=self.uid)
            )
        )

        return response_data['jobId']

    def list_properties(self, params=None, sort=None, sort_dir='ASC'):
        """
        List the configuration properties for the device

        Arguments:
            params (dict): Search parameters to filter the properties list on.
            sort (str): Sort key for the properties list.
            sort_dir (str): Sort direction, either ASC or DESC

        Returns:
            dict(int, list(dict)): ::

            {
                'total': Total count of properties returned.
                'properties': List of properties found.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.list_properties(self.uid, params=params, sort=sort,
                                  sort_dir=sort_dir)

    def list_local_properties(self):
        """
        List the locally defined configuration properties for the device

        Returns:
            dict(int, list(dict)): ::

            {
                'total': Total count of properties returned.
                'properties': List of properties found.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.list_local_properties(self.uid)

    def list_custom_properties(self):
        """
        List the custom properties for the device

        Returns:
            dict(int, list(dict)): ::

            {
                'total': Total count of properties returned.
                'properties': List of properties found.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.list_custom_properties(self.uid)

    def get_properties(self, params=None):
        """
        Get the configuration properties for the device

        Arguments:
            params (dict): Search parameters for filter the properties on.

        Returns:
            dict(int, list(ZenossProperty)): ::

            {
                'total': Total count of properties returned.
                'properties': List of ZenossProperty objects.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_properties(self.uid, params=params)

    def get_property(self, zproperty):
        """
        Get a configuration property

        Arguments:
            zproperty (str): The id of the property to get

        Returns:
            ZenossProperty:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_property(self.uid, zproperty)

    def get_custom_properties(self, params=None):
        """
        Get the cProperties for the device

        Arguments:
            params (dict): Search parameters for filter the properties on.

        Returns:
            dict(int, list(ZenossCustomProperty)): ::

            {
                'total': Total count of properties returned.
                'properties': List of ZenossCustomProperty objects.
            }

        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_custom_properties(self.uid, params=params)

    def get_custom_property(self, cproperty):
        """
        Get a custom property for the device

        Arguments:
            cproperty (str): ID of the property to get.

        Returns:
            ZenossCustomProperty:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.get_custom_property(self.uid, cproperty)

    def set_property(self, zproperty, value=None):
        """
        Set the value of a configuration property

        Arguments:
            zproperty (str): The id of the property to set a value for
            value (str): The value to set for the property

        Returns:
            bool:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.set_property_value(self.uid, zproperty, value=value)

    def delete_property(self, zproperty):
        """
        Delete the locally set value of a property for a device

        Arguments:
            zproperty (str): ID of the property to delete.

        Returns:
            bool:
        """
        pr = PropertiesRouter(self.api_url, self.api_headers, self.ssl_verify)
        return pr.delete_property(self.uid, zproperty)


class ZenossComponent(DeviceRouter):
    """
    Class for Zenoss component objects
    """

    def __init__(self, url, headers, ssl_verify, device_data):
        super(ZenossComponent, self).__init__(url, headers, ssl_verify)

        unneeded_props = ['class_label', 'class_plural_label',
                          'class_plural_short_label', 'class_short_label',
                          'inspector_type', 'uuid']

        for i in unneeded_props:
            if i in device_data:
                device_data.pop(i)

        uid = device_data.pop('uid')
        self.uid = uid.replace('/zport/dmd/', '', 1)
        self.description = device_data.pop('description')
        self.device = device_data.pop('device')
        self.deviceName = device_data.pop('deviceName')
        self.events = device_data.pop('events')
        self.icon = device_data.pop('icon')
        self.id = device_data.pop('id')
        self.locking = device_data.pop('locking')
        self.meta_type = device_data.pop('meta_type')
        self.monitor = device_data.pop('monitor')
        self.monitored = device_data.pop('monitored')
        self.name = device_data.pop('name')
        self.pingStatus = device_data.pop('pingStatus')
        self.severity = device_data.pop('severity')
        self.status = device_data.pop('status')
        self.usesMonitorAttribute = device_data.pop('usesMonitorAttribute')

        self.properties = device_data
        dev_path = self.uid.split('/{0}/'.format(self.device))[0]
        self.parent = '{0}/{1}'.format(dev_path, self.device)

    def set_monitored(self, monitor=True):
        """
        Sets the monitored state for the component.

        Arguments:
            monitor (bool): True to monitor, False to stop monitoring

        Returns:
            str: Response message
        """
        return self._set_components_monitored_by_uids([self.uid], monitor)

    def lock(self, updates=False, deletion=False, send_event=False):
        """
        Lock the component for changes.

        Arguments:
            updates (bool): Lock for updates
            deletion (bool): Lock for deletion
            send_event (bool): Send an event when an action is blocked by locking

        Returns:
            str: Response message
        """
        return self._lock_components_by_uid([self.uid], updates=updates,
                                            deletion=deletion,
                                            send_event=send_event)

    def lock_for_updates(self, send_event=False):
        """
        Lock the component for updates.

        Arguments:
            send_event (bool): Send an event when updates are blocked by locking

        Returns:
            str: Response message
        """
        return self.lock(updates=True, send_event=send_event)

    def lock_for_deletion(self, send_event=False):
        """
        Lock the component for updates.

        Arguments:
            send_event (bool): Send an event when deletion is blocked by locking

        Returns:
            str: Response message
        """
        return self.lock(deletion=True, send_event=send_event)

    def delete(self):
        """
        Delete the component.

        Returns:
            str: Response message
        """
        return self._delete_components_by_uid([self.uid])
