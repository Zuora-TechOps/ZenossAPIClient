# -*- coding: utf-8 -*-

"""
Zenoss monitor_router
"""

from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers import ZenossRouter


class MonitorRouter(ZenossRouter):
    """
    Class for interacting with the Zenoss monitor router
    """

    def __init__(self, url, headers, ssl_verify):
        super(MonitorRouter, self).__init__(url, headers, ssl_verify,
                                           'monitor_router', 'MonitorRouter')
        self.id = None

    def __repr__(self):
        if self.id:
            identifier = self.id
        else:
            identifier = hex(id(self))

        return '<{0} object at {1}>'.format(
            type(self).__name__, identifier
        )

    def tree(self):
        """
        Returns the full tree of hubs and collectors

        Returns:
            list(dict):
        """
        return self._router_request(
            self._make_request_data(
                'getTree',
                data=dict(id='')
            )
        )

    def list_hubs(self):
        """
        Returns the list of configured zenhubs

        Returns:
            list(dict):
        """
        hubs_data = self.tree()
        hubs = []
        for hub in hubs_data:
            hubs.append(dict(name=hub['name'], uid=hub['uid'].replace('/zport/dmd/', '', 1)))

        return hubs

    def list_collectors(self):
        """
        Returns the list of configured collectors

        Returns:
            list(dict):
        """
        hubs_data = self.tree()
        collectors = []
        for hub in hubs_data:
            for collector in hub['children']:
                collectors.append(
                    dict(
                        name=collector['name'],
                        devcount=collector['devcount'],
                        hub=hub['name'],
                        uid=collector['uid'].replace('/zport/dmd/', '', 1)
                    )
                )

        return collectors

    def get_hubs(self):
        """
        Get the configured hubs as objects

        Returns:
            list(ZenossHub):
        """
        hubs_data = self.tree()
        hubs = []
        for hub in hubs_data:
            hubs.append(
                ZenossHub(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    hub
                )
            )

        return hubs

    def get_hub(self, name):
        """
        Get a ZenossHub object

        Arguments:
            name (str): Name of the hub to get

        Returns:
            ZenossHub:
        """
        hubs_data = self.tree()
        for hub in hubs_data:
            if hub['name'] == name:
                return ZenossHub(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    hub
                )

        return None


class ZenossHub(MonitorRouter):
    """
    Class for Zenoss hub objects
    """

    def __init__(self, url, headers, ssl_verify, hub_data):
        super(ZenossHub, self).__init__(url, headers, ssl_verify)

        self.uid = hub_data['uid'].replace('/zport/dmd/', '', 1)
        self.name = hub_data['name']
        self.text = hub_data['text']
        self.id = hub_data['id']
        self.devcount = hub_data['devcount']
        self.path = hub_data['path']
        self.ccbacked = hub_data['ccbacked']
        self.collectors = []

        for c in hub_data['children']:
            self.collectors.append(c['name'])

    def get_collectors(self):
        """
        Get the hub's collectors as objects.

        Returns:
             list(ZenossCollector):
        """
        collectors = []
        for c in self.collectors:
            cinfo = self._router_request(
                self._make_request_data(
                    'getInfo',
                    data=dict(
                        id=c
                    )
                )
            )
            collectors.append(
                ZenossCollector(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    cinfo['data']
                )
            )

        return collectors

    def get_collector(self, name):
        """
        Get a ZenossCollector object

        Arguments:
            name (str): Name of the collector to get

        Returns:
            ZenossCollector:
        """
        if name in self.collectors:
            cinfo = self._router_request(
                self._make_request_data(
                    'getInfo',
                    data=dict(
                        id=name
                    )
                )
            )
            return ZenossCollector(
                self.api_url,
                self.api_headers,
                self.ssl_verify,
                cinfo['data']
            )

        return None

    def add_collector(self, name, source=None, pool=None):
        """
        Add a new collector to the hub.

        Arguments:
            name (str): Name of the new collector
            source (str): Name of the existing collector to use as a template
            pool (str): The resource pool to place the collector in

        Returns:
            ZenossCollector:
        """
        if not source:
            raise ZenossAPIClientError("You must specify a collector to use as a template.")

        if not pool:
            raise ZenossAPIClientError("You must specify a resource pool for the collector.")

        collector_params = self._router_request(
            self._make_request_data(
                'addCollector',
                data=dict(
                    id=name,
                    sourceId=source,
                    hubId=self.name,
                    poolId=pool
                )
            )
        )

        collector_data = self._router_request(
            self._make_request_data(
                'getInfo',
                data=dict(
                    id=name
                )
            )
        )

        return ZenossCollector(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            collector_data=collector_data['data'],
            collector_params=collector_params
        )


class ZenossCollector(MonitorRouter):
    """
    Class for Zenoss collector objects
    """

    def __init__(self, url, headers, ssl_verify, collector_data, collector_params=None):
        super(ZenossCollector, self).__init__(url, headers, ssl_verify)

        self.uid = collector_data['uid'].replace('/zport/dmd/', '', 1)
        self.ccbacked = collector_data['ccbacked']
        self.name = collector_data['name']
        self.text = collector_data['text']
        self.devcount = collector_data['devcount']
        self.path = collector_data['path']
        self.id = collector_data['id']

        if not collector_params:
            collector_params = self._router_request(
                self._make_request_data(
                    'getCollector',
                    data=dict(
                        collectorString=self.name
                    )
                )
            )

        self.configCycleInterval = collector_params['data']['configCycleInterval']
        self.pingCycleInterval = collector_params['data']['pingCycleInterval']
        self.discoveryNetworks = collector_params['data']['discoveryNetworks']
        self.description = collector_params['data']['description']
        self.modelerCycleInterval = collector_params['data']['modelerCycleInterval']
        self.processCycleInterval = collector_params['data']['processCycleInterval']
        self.meta_type = collector_params['data']['meta_type']
        self.wmiqueryTimeout = collector_params['data']['wmiqueryTimeout']
        self.statusCycleInterval = collector_params['data']['statusCycleInterval']
        self.eventlogCycleInterval = collector_params['data']['eventlogCycleInterval']
        self.wmibatchSize = collector_params['data']['wmibatchSize']
        self.pingTimeOut = collector_params['data']['pingTimeOut']
        self.winCycleInterval = collector_params['data']['winCycleInterval']
        self.pingTries = collector_params['data']['pingTries']
        self.inspector_type = collector_params['data']['inspector_type']
        self.zenProcessParallelJobs = collector_params['data']['zenProcessParallelJobs']
