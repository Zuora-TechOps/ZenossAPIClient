# -*- coding: utf-8 -*-

"""
Zenoss evconsole_router
"""

from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers import ZenossRouter


class EventsRouter(ZenossRouter):
    """
    Class for interacting with Zenoss events.
    """

    def __init__(self, url, headers, ssl_verify):
        super(EventsRouter, self).__init__(url, headers, ssl_verify,
                                           'evconsole_router', 'EventsRouter')

        self.evid = None
        self.event_states_map = dict(
            New=0,
            Acknowledged=1,
            Suppressed=2,
            Closed=3,
            Cleared=4,
            Aged=6,
        )
        self.event_severity_map = dict(
            Critical=5,
            Error=4,
            Warning=3,
            Info=2,
            Debug=1,
            Clear=0,
        )

    def __repr__(self):
        if self.evid:
            identifier = "id {0}".format(self.evid)
        else:
            identifier = "at {0}".format(hex(id(self)))

        return '<{0} object {1}>'.format(
            type(self).__name__, identifier
        )

    def _query_events(self, limit=10, start=0, sort='lastTime', sort_dir='DESC',
                      params=None, exclude=None, keys=None,
                      context=None, archive=False):
        """
        Get a list of events based on query parameters.

        Some search parameter examples:

        Find New events:
            params=dict(eventState=[0])
        Find open events (in New or Acknowledged state):
            params=dict(eventState=[0,1])
        Find open events for Production servers:
            params=dict(eventState=[0,1], prodState=[1000])

        Other handy search keys: agent, count, DevicePriority, firstTime,
        lastTime, monitor, message, severity, summary

        Arguments:
            limit (int): Maximum number of events to get
            start (int): Minimum index of events to get
            sort (str): Sort key for events list
            sort_dir (str): Sort direction, ASC or DESC
            params (dict): Key/value pairs for filtering the events to include
            exclude (dict): Key/value pairs to filter out of the found events
            keys (list): List of keys to include in the return event data
            context (str): Device or device class uid as context for the query
            archive (bool): Search the events archive instead of active events

        Returns:
            dict(int, float, list(dict)): ::

            {
                'total': Total count of events matched by the query,
                'ts': Timestamp for the search,
                'events': List of events found,
            }

        """
        valid_params = {'agent',
                        'component',
                        'count',
                        'dedupid',
                        'device',
                        'deviceClass',
                        'deviceGroups',
                        'devicePriority',
                        'eventClass',
                        'eventGroup',
                        'eventKey',
                        'eventState',
                        'evid',
                        'facility',
                        'firstTime',
                        'ipAddress',
                        'lastTime',
                        'location',
                        'manager',
                        'message',
                        'ntevid',
                        'ownerId',
                        'priority',
                        'prodState',
                        'severity',
                        'stateChange',
                        'summary',
                        'systems'}

        if params:
            param_keys = set(params.keys())
            bad_params = param_keys.difference(valid_params)
            for bad in bad_params:
                params.pop(bad)

        events_data = self._router_request(
            self._make_request_data(
                'query',
                dict(
                    limit=limit,
                    start=start,
                    sort=sort,
                    dir=sort_dir,
                    params=params,
                    exclusion_filter=exclude,
                    keys=keys,
                    uid=context,
                    archive=archive,
                )
            )
        )

        return dict(
            ts=events_data['asof'],
            total=events_data['totalCount'],
            events=events_data['events'],
        )

    def _get_details_by_evid(self, evid):
        """
        Get the details of an event by the event ID.

        Arguments:
            evid (str): The event ID

        Returns:
            dict: Event details
        """
        event_data = self._router_request(
            self._make_request_data(
                'detail',
                dict(
                    evid=evid,
                )
            )
        )

        return event_data['event'][0]

    def _event_actions(self, action, evids=None, exclude_ids=None, params=None,
                      context=None, last_change=None, limit=None, timeout=60):
        """
        Close events by either passing a list of event ids or by a query.

        Arguments:
            action (str): The action to take on the event - close,
                ack, or reopen
            evids (list): List of event IDs to close
            exclude_ids (list): List of event IDs to exclude from the close
            params (dict): Key/value pairs for filtering the events to close
            context (str): Device or device class uid as context for the query
            last_change (float): Timestamp - only close events if there has
                been no change since this time
            limit (int): Maximum number of events to return in the query
            timeout (int): Number of seconds before the query times out
        """
        if action not in ['close', 'acknowledge', 'reopen']:
            raise ZenossAPIClientError("Unknown event action: {0}".format(action))

        self._router_request(
            self._make_request_data(
                action,
                dict(
                    evids=evids,
                    excludeIds=exclude_ids,
                    params=params,
                    uid=context,
                    asof=last_change,
                    limit=limit,
                    timeout=timeout,
                )
            )
        )

        return True

    def get_config(self):
        """
        Get the event handling configuration.

        Returns:
            list(dict):
        """
        config_data = self._router_request(
            self._make_request_data(
                'getConfig',
                dict(),
            )
        )

        return config_data['data']

    def update_config(self, config_values):
        """
        Update the Zenoss event handling configuration.

        Arguments:
            config_values (dict): Key/value pairs of the config
                values to change.
        """
        self._router_request(
            self._make_request_data(
                'setConfigValues',
                dict(values=config_values),
            )
        )

        return True

    def get_event_by_evid(self, evid):
        """
        Get an event by its event id

        Arguments:
            evid (str): The event id

        Returns:
            ZenossEvent:
        """
        event_data = self._get_details_by_evid(evid)

        return ZenossEvent(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            event_data,
        )

    def list_open_events(self, limit=10, start=0, sort='lastTime', sort_dir='DESC'):
        """
        Get a list of all open events (new or acknowledged state)

        Arguments:
            limit (int): Maximum number of events to return
            start (int): Minimum index of events to get
            sort (str): Sort key for events list
            sort_dir (str): Sort direction, ASC or DESC

        Returns:
            dict:
        """
        return self._query_events(
            limit=limit,
            start=start,
            sort=sort,
            sort_dir=sort_dir,
            params=dict(eventState=[0, 1], severity=[3, 4, 5])
        )

    def get_open_events(self, limit=10, start=0, sort='lastTime', sort_dir='DESC'):
        """
        Get all open events (new or acknowledged state)

        Arguments:
            limit (int): Maximum number of events to return
            start (int): Minimum index of events to get
            sort (str): Sort key for events list
            sort_dir (str): Sort direction, ASC or DESC

        Returns:
            list(ZenossEvent):
        """
        events_data = self._query_events(
            limit=limit,
            start=start,
            sort=sort,
            sort_dir=sort_dir,
            params=dict(eventState=[0, 1], severity=[3, 4, 5]),
            keys=['evid']
        )

        events = []
        for e in events_data['events']:
            evdetails = self._get_details_by_evid(e['evid'])
            events.append(
                ZenossEvent(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    evdetails,
                )
            )

        return events

    def list_open_production_events(self, limit=10, start=0, sort='lastTime',
                                    sort_dir='DESC'):
        """
        Get a list of all open events (new or acknowledged state) for devices
        with a production state of Production

        Arguments:
            limit (int): Maximum number of events to return
            start (int): Minimum index of events to get
            sort (str): Sort key for events list
            sort_dir (str): Sort direction, ASC or DESC

        Returns:
            dict:
        """
        return self._query_events(
            limit=limit,
            start=start,
            sort=sort,
            sort_dir=sort_dir,
            params=dict(eventState=[0, 1], prodState=[1000], severity=[3, 4, 5])
        )

    def get_open_production_events(self, limit=10, start=0, sort='lastTime',
                                   sort_dir='DESC'):
        """
        Get all open events (new or acknowledged state) for devices with a
        production state of Production

        Arguments:
            limit (int): Maximum number of events to return
            start (int): Minimum index of events to get
            sort (str): Sort key for events list
            sort_dir (str): Sort direction, ASC or DESC

        Returns:
            list(ZenossEvent):
        """
        events_data = self._query_events(
            limit=limit,
            start=start,
            sort=sort,
            sort_dir=sort_dir,
            params=dict(eventState=[0, 1], prodState=[1000], severity=[3, 4, 5]),
            keys=['evid']
        )

        events = []
        for e in events_data['events']:
            evdetails = self._get_details_by_evid(e['evid'])
            events.append(
                ZenossEvent(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    evdetails,
                )
            )

        return events

    def add_event(self, summary, device, severity, component=None,
                  event_class_key='', event_class='/Status', **kwargs):
        """
        Create a new Zenoss event.

        Arguments:
            summary (str): Summary for the new event
            device (str): Device ID for the new event
            component (str): Component UID for the new event
            severity (str): Severity to assign the new event, must be one of
                Critical, Error, Warning, Info, Debug, or Clear
            event_class_key (str): The Event Class Key to assign to the event
            event_class (str): Event Class for the event

        Returns:
            ZenossEvent:
        """
        if severity in self.event_severity_map:
            severity_num = self.event_severity_map[severity]
        else:
            severity_num = severity

        event_spec = dict(
            summary=summary,
            device=device,
            component=component,
            severity=severity,
            evclasskey=event_class_key,
            evclass=event_class,
            **kwargs
        )

        self._router_request(
            self._make_request_data(
                'add_event',
                event_spec,
            )
        )

        ev_filter = dict(
            summary=summary,
            device=[device],
            component=[component] if component else None,
            severity=severity_num,
            eventClassKey=event_class_key,
            **kwargs
        )

        event_data = self._query_events(
            limit=1,
            params=ev_filter,
            keys=['evid']
        )
        evid = event_data['events'][0]['evid']

        return self.get_event_by_evid(evid)

    def clear_heartbeats(self):
        """
        Clear all heartbeat events

        Returns:
            bool: True on success
        """
        self._router_request(
            self._make_request_data(
                'clear_heartbeats',
                dict(),
            )
        )

        return True

    def clear_heartbeat(self, collector, daemon):
        """
        Clear a heartbeat event for a specific daemon.

        Arguments:
            collector (str): Collector the daemon is running in,
                e.g. slvcollector
            daemon (str): Monitoring daemon to clear the heartbeat event
                for, e.g. zencommand
        """
        self._router_request(
            self._make_request_data(
                'clear_heartbeat',
                dict(
                    monitor=collector,
                    daemon=daemon,
                )
            )
        )

        return True


class ZenossEvent(EventsRouter):
    """
    Class for Zenoss event objects
    """

    def __init__(self, url, headers, ssl_verify, event_data):
        super(ZenossEvent, self).__init__(url, headers, ssl_verify)

        self.evid = event_data['evid']
        self.device_class = event_data['DeviceClass']
        self.device_groups = event_data['DeviceGroups']
        self.device_priority = event_data['DevicePriority']
        self.location = event_data['Location']
        self.systems = event_data['Systems']
        self.agent = event_data['agent']
        self.clearid = event_data['clearid']
        self.component = event_data['component']
        self.component_title = event_data['component_title']
        self.component_url = event_data['component_url']
        self.component_uuid = event_data['component_uuid']
        self.count = event_data['count']
        self.dedupid = event_data['dedupid']
        self.details = event_data['details']
        self.device = event_data['device']
        self.device_title = event_data['device_title']
        self.device_url = event_data['device_url']
        self.device_uuid = event_data['device_uuid']
        self.event_class = event_data['eventClass']
        self.event_class_key = event_data['eventClassKey']
        self.event_class_mapping = event_data['eventClassMapping']
        self.event_class_mapping_url = event_data['eventClassMapping_url']
        self.event_class_url = event_data['eventClass_url']
        self.event_group = event_data['eventGroup']
        self.event_key = event_data['eventKey']
        self.event_state = event_data['eventState']
        self.facility = event_data['facility']
        self.first_time = event_data['firstTime']
        self.id = event_data['id']
        self.ip_address = event_data['ipAddress']
        self.last_time = event_data['lastTime']
        self.log = event_data['log']
        self.message = event_data['message']
        self.collector = event_data['monitor']
        self.ntevid = event_data['ntevid']
        self.ownerid = event_data['ownerid']
        self.priority = event_data['priority']
        self.production_state = event_data['prodState']
        self.severity = event_data['severity']
        self.state_change = event_data['stateChange']
        self.summary = event_data['summary']

    def update_log(self, message):
        """
        Add an entry to the event's log

        Arguments:
            message (str): Log entry to add
        """
        self._router_request(
            self._make_request_data(
                'write_log',
                dict(
                    evid=self.evid,
                    message=message,
                )
            )
        )

        event_detail = self._get_details_by_evid(self.evid)
        self.log = event_detail['log']

        return True

    def close(self):
        """
        Close the event.
        """
        return self._event_actions('close', [self.evid])

    def ack(self):
        """
        Acknowledge the event.
        """
        return self._event_actions('acknowledge', [self.evid])

    def reopen(self):
        """
        Reopen (unacknowledge or unclose) the event.
        """
        return self._event_actions('reopen', [self.evid])
