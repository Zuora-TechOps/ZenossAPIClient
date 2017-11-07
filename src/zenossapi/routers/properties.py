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
            identifier = "id {0}".format(self.evid)
        else:
            identifier = "at {0}".format(hex(id(self)))

        return '<{0} object {1}>'.format(
            type(self).__name__, identifier
        )

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


class ZenossProperty(PropertiesRouter):
    """
    Class for ZenProperties
    """

    def __init__(self, url, headers, ssl_verify, property_data):
        super(ZenossProperty, self).__init__(url, headers, ssl_verify)

        self.id = property_data['id']
        self.category = property_data['category']
        self.description = property_data['description']
        self.isLocal = property_data['isLocal']
        self.label = property_data['label']
        self.value = property_data['value']
        self.valueAsString = property_data['valueAsString']
        self.path = property_data['path']
        self.type = property_data['type']
        self.options = []

    def set_value(self, value=None):
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
                    uid=self.path,
                    zProperty=self.id,
                    value=value,
                )
            )
        )

        self.value = property_data['data']['value']
        self.valueAsString = property_data['data']['valueAsString']

        return True
