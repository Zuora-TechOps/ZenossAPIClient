# -*- coding: utf-8 -*-

"""
Zenoss Events/IncidentManagementRouter
"""

from zenossapi.routers import ZenossRouter

__router__ = 'IncidentManagementRouter'


class IncidentManagementRouter(ZenossRouter):
    """
    Class for interacting with the Zenoss incidentmanagement router
    """

    def __init__(self, url, headers, ssl_verify):
        super(IncidentManagementRouter, self).__init__(url, headers, ssl_verify,
                                                       'Events/IncidentManagementRouter',
                                                       'IncidentManagementRouter')

    def __repr__(self):
        identifier = "at {0}".format(hex(id(self)))

        return '<{0} object {1}>'.format(
            type(self).__name__, identifier
        )

    def associate_incident_to_event(self, notification, incident, evids):
        """
        Associates an incident with a specific event ID.

        Arguments:
            notification (str): URI path to NotificationSubscriptions
            incident (str): The incident ID
            evids (list): The event IDs
        """
        self._router_request(
            self._make_request_data(
                'associateIncident',
                dict(
                    notification=notification,
                    number=incident,
                    evids=evids
                )
            )
        )
