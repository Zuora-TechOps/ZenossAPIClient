# -*- coding: utf-8 -*-

"""
Zenoss properties_router
"""

from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers import ZenossRouter


class PropertiesRouter(ZenossRouter):
    """
    Class for interacting with Zenoss properties.
    """

    def __init__(self, url, headers, ssl_verify):
        super(PropertiesRouter, self).__init__(url, headers, ssl_verify,
                                               'properties_router',
                                               'PropertiesRouter')

        self.id = None

    def __repr__(self):
        if self.id:
            identifier = "id {0}".format(self.id)
        else:
            identifier = "at {0}".format(hex(id(self)))

        return '<{0} object {1}>'.format(
            type(self).__name__, identifier
        )

    def _refresh(self, property_data):
        """
        Refresh the attributes of the object, e.g. after deleting a local copy.

        Arguments:
            property_data (dict): New attribute values
        """
        skip = ['api_action', 'api_endpoint', 'api_headers', 'api_url', 'ssl_verify']

        for pd in property_data:
            if pd in skip:
                continue
            setattr(self, pd, property_data[pd])

    def list_properties(self, uid, params=None, sort=None, sort_dir='ASC'):
        """
        Get a list of ZenProperties for the uid context.

        Arguments:
            uid (str): UID of the object to list properties for.
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
        properties_data = self._router_request(
            self._make_request_data(
                'getZenProperties',
                dict(
                    uid=uid,
                    params=params,
                    sort=sort,
                    dir=sort_dir,
                )
            )
        )

        return dict(
            total=properties_data['totalCount'],
            properties=properties_data['data'],
        )

    def get_properties(self, uid, params=None):
        """
        Get ZenossProperties objects for the properties of a uid context.

        Arguments:
            uid (str): UID of the object to get properties for.
            params (dict): Search parameters for filter the properties on.

        Returns:
            dict(int, list(ZenossProperty)): ::

            {
                'total': Total count of properties returned.
                'properties': List of ZenossProperty objects.
            }

        """
        properties_data = self.list_properties(uid, params=params)

        props = dict(
            total=properties_data['total'],
            properties=[]
        )
        for prop in properties_data['properties']:
            props['properties'].append(
                ZenossProperty(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    prop,
                )
            )

        return props

    def list_local_properties(self, uid):
        """
        Get a list of properties set locally to the specified UID.

        Arguments:
            uid (str): UID to get local properties for.

        Returns:
            dict(int, list(dict)): ::

            {
                'total': Total count of properties returned.
                'properties': List of properties found.
            }
        """
        return self.list_properties(uid, params=dict(islocal='1'))

    def get_local_properties(self, uid):
        """
        Get ZenossProperty objects for the local properties of a specified uid.

        Arguments:
            uid (str): UID to get local properties for.

        Returns:
            dict(int, list(ZenossProperty)): ::

            {
                'total': Total count of properties returned.
                'properties': List of ZenossProperty objects.
            }

        """
        properties_data = self.list_local_properties(uid)

        props = dict(
            total=properties_data['total'],
            properties=[]
        )
        for prop in properties_data['properties']:
            props['properties'].append(
                ZenossProperty(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    prop,
                )
            )

        return props

    def get_property(self, uid, zproperty):
        """
        Get a single ZenossProperty

        Arguments:
            uid (str): UID to get the property of.
            zproperty (str): ID of the property to get.

        Returns:
            ZenossProperty:
        """
        prop_data = self._router_request(
            self._make_request_data(
                'getZenProperties',
                dict(
                    uid=uid,
                    params=dict(
                        id=zproperty,
                    )
                )
            )
        )

        return ZenossProperty(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            prop_data['data'][0]
        )

    def list_custom_properties(self, uid, params=None, sort=None, sort_dir='ASC'):
        """
        Get a list of cProperties for the uid context.

        Arguments:
            uid (str): UID of the object to list properties for.
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
        properties_data = self._router_request(
            self._make_request_data(
                'getCustomProperties',
                dict(
                    uid=uid,
                    params=params,
                    sort=sort,
                    dir=sort_dir,
                )
            )
        )

        return dict(
            total=properties_data['totalCount'],
            properties=properties_data['data'],
        )

    def get_custom_properties(self, uid, params=None):
        """
        Get ZenossCustomProperties objects for the cProperties of a uid context.

        Arguments:
            uid (str): UID of the object to get properties for.
            params (dict): Search parameters for filter the properties on.

        Returns:
            dict(int, list(ZenossCustomProperty)): ::

            {
                'total': Total count of properties returned.
                'properties': List of ZenossCustomProperty objects.
            }

        """
        properties_data = self.list_custom_properties(uid, params=params)

        props = dict(
            total=properties_data['total'],
            properties=[]
        )
        for prop in properties_data['properties']:
            props['properties'].append(
                ZenossCustomProperty(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    prop,
                )
            )

        return props

    def get_custom_property(self, uid, cproperty):
        """
        Get a single ZenossCustomProperty

        Arguments:
            uid (str): UID to get the property of.
            cproperty (str): ID of the property to get.

        Returns:
            ZenossCustomProperty:
        """
        prop_data = self._router_request(
            self._make_request_data(
                'getCustomProperties',
                dict(
                    uid=uid,
                    params=dict(
                        id=cproperty,
                    )
                )
            )
        )

        return ZenossCustomProperty(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            prop_data['data'][0]
        )

    def set_property_value(self, uid, zproperty, value=None):
        """
        Sets (or updates) the local value of a property

        Arguments:
            value: The new value for the property, type varies by property.

        Returns:
            bool:
        """
        property_data = self._router_request(
            self._make_request_data(
                'setZenProperty',
                dict(
                    uid=uid,
                    zProperty=zproperty,
                    value=value,
                )
            )
        )

        return property_data['data']

    def delete_property(self, uid, zproperty):
        """
        Delete a ZenProperty.

        Arguments:
            uid (str): UID to delete the property from
            zproperty (str): ID of the property to delete.

        Returns:
            bool:
        """
        self._router_request(
            self._make_request_data(
                'deleteZenProperty',
                dict(
                    uid=uid,
                    zProperty=zproperty
                )
            )
        )

        return True


class ZenossProperty(PropertiesRouter):
    """
    Class for ZenProperties
    """

    def __init__(self, url, headers, ssl_verify, property_data):
        super(ZenossProperty, self).__init__(url, headers, ssl_verify)

        self.id = property_data['id']
        self.category = property_data['category']
        self.description = property_data['description']
        self.islocal = property_data['islocal']
        self.label = property_data['label']
        self.value = property_data['value']
        self.valueAsString = property_data['valueAsString']
        self.path = 'Devices{0}'.format(property_data['path'])
        self.type = property_data['type']
        self.options = []

    def set_value(self, path=None, value=None):
        """
        Sets (or updates) the local value of a property

        Arguments:
            path (str): UID of the node to set the property for.
            value (str): The new value for the property, type varies by property.

        Returns:
            bool:
        """
        if path:
            self.path = path

        property_data = self.set_property_value(self.path, self.id, value=value)

        self.value = property_data['value']
        self.valueAsString = property_data['valueAsString']
        self.islocal = '1'

        return True

    def delete(self):
        """
        Delete the local instance of a property.

        Returns:
            bool:
        """
        if self.islocal:
            self.delete_property(self.path, self.id)
            defprop = self.list_properties(self.path, params=dict(id=self.id))
            self._refresh(defprop['properties'][0])
            return True

        return False


class ZenossCustomProperty(PropertiesRouter):
    """
    Class for Zenoss CustomProperties
    """

    def __init__(self, url, headers, ssl_verify, property_data):
        super(ZenossCustomProperty, self).__init__(url, headers, ssl_verify)

        self.id = property_data['id']
        self.islocal = property_data['islocal']
        self.label = property_data['label']
        self.value = property_data['value']
        self.valueAsString = property_data['valueAsString']
        self.path = 'Devices{0}'.format(property_data['path'])
        self.type = property_data['type']
        self.options = property_data['options']

    def set_value(self, path=None, value=None):
        """
        Sets (or updates) the local value of a custom property

        Arguments:
            path (str): UID of the node to set the property for.
            value (str): The new value for the property, type varies by property.

        Returns:
            bool:
        """
        if path:
            self.path = path

        property_data = self.set_property_value(self.path, self.id, value=value)

        self.value = property_data['value']
        self.valueAsString = property_data['valueAsString']
        self.islocal = '1'

        return True

    def delete(self):
        """
        Delete the local instance of a property.

        Returns:
            bool:
        """
        if self.islocal:
            self.delete_property(self.path, self.id)
            defprop = self.list_custom_properties(self.path, params=dict(id=self.id))
            self._refresh(defprop['properties'][0])
            return True

        return False
