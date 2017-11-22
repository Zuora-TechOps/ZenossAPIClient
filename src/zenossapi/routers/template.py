# -*- coding: utf-8 -*-

"""
Zenoss template_router
"""

from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers import ZenossRouter


class TemplateRouter(ZenossRouter):
    """
    Class for interacting with the Zenoss template router
    """

    def __init__(self, url, headers, ssl_verify):
        super(TemplateRouter, self).__init__(url, headers, ssl_verify, 'template_router', 'TemplateRouter')
        self.uid = None
        self.properties = None

    def __repr__(self):
        if self.uid:
            identifier = self.uid
        else:
            identifier = hex(id(self))

        return '<{0} object at {1}>'.format(
            type(self).__name__, identifier
        )

    def _get_properties(self, zobject):
        """
        Gets the properties of an object.

        Arguments:
            zobject (str): The uid of the Zenoss object (device, component,
                           etc.) to get the properties of

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'getInfo',
                dict(uid=zobject)
            )
        )

    def _get_template_by_uid(self, template_uid):
        """
        Gets a template by its full UID

        Arguments:
            template_uid (str): UID of the template

        Returns:
            ZenossTemplate:
        """
        template_data = self._router_request(
            self._make_request_data(
                'getInfo',
                dict(uid=template_uid)
            )
        )
        return ZenossTemplate(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            template_data['data']
        )

    def _get_data_source_by_uid(self, datasource_uid):
        """
        Get a data source by its full UID.

        Arguments:
            datasource_uid (str): UID of the data source to get

        Returns:
            ZenossDataSource:
        """
        data_source_data = self._router_request(
            self._make_request_data(
                'getDataSourceDetails',
                dict(uid=datasource_uid),
            )
        )
        return ZenossDataSource(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            data_source_data['record']
        )

    def _get_data_point_by_uid(self, datapoint_uid):
        """
        Get a data point by its full UID.

        Arguments:
            datapoint_uid (str): UID of the data point to get details for

        Returns:
            ZenossDataPoint:
        """
        dp_data = self._router_request(
            self._make_request_data(
                'getDataPointDetails',
                dict(uid=datapoint_uid),
            )
        )
        return ZenossDataPoint(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            dp_data['record']
        )

    def _get_threshold_by_uid(self, threshold_uid):
        """
        Gets a threshold by its full UID

        Arguments:
            threshold_uid (str): UID of the template

        Returns:
            ZenossThreshold:
        """
        threshold_data = self._router_request(
            self._make_request_data(
                'getThresholdDetails',
                dict(uid=threshold_uid)
            )
        )

        return ZenossThreshold(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            threshold_data['record']
        )

    def _get_graph_by_uid(self, graph_uid):
        """
        Get a graph by its full UID.

        Arguments:
            graph_uid (str): UID of the graph to get the definition of

        Returns:
            ZenossGraph:
        """
        graph_data = self._router_request(
            self._make_request_data(
                'getGraphDefinition',
                dict(uid=graph_uid),
            )
        )

        return ZenossGraph(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            graph_data['data']
        )

    def _find_templates_in_tree(self, templates_data):
        """
        Works through the dict structure returned by the Zenoss API for
        template queries and returns the defined templates from it.

        Arguments:
            templates_data (dict): Templates data returned by the API

        Returns:
            list:
        """
        templates = []
        for node in templates_data['children']:
            if node['leaf']:
                if node['text'].find("Locally Defined") > -1:
                    templates.append((node['uid'].replace('/zport/dmd/', '', 1), node['qtip']))
            else:
                templates.extend(self._find_templates_in_tree(node))

        return templates

    def _set_properties(self, properties):
        """
        Sets arbitrary properties of any object.

        Arguments:
            properties (dict): Properties and values to set

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'setInfo',
                properties
            )
        )

    def set_properties(self, properties):
        """
        Sets properties of an object.

        Arguments:
            properties (dict): Properties and values to set
        """
        if not isinstance(properties, dict):
            raise ZenossAPIClientError('Type error: Properties to set for {} must be a dict'.format(type(self).__name__))

        if not self.uid:
            return

        data = properties
        data['uid'] = self.uid
        properties_result = self._set_properties(data)
        for prop in properties:
            if getattr(self, prop, False):
                setattr(self, prop, properties[prop])
            elif getattr(self, 'properties', False) and prop in self.properties:
                self.properties[prop] = properties[prop]

        return properties_result

    def get_all_templates(self):
        """
        Returns all defined templates.

        Returns:
            list(ZenossTemplate):
        """
        templates_data = self._router_request(
            self.get_device_class_templates(
                device_class='Devices'
            )
        )

        templates = []
        found_templates = self._find_templates_in_tree(templates_data[0])
        for t in found_templates:
            templates.append(
                self._get_template_by_uid(t[0])
            )
        return templates

    def list_all_templates(self):
        """
        Returns all defined templates as a list of tuples containing the
        template UID and description.

        Returns:
            list(ZenossTemplate):
        """
        templates_data = self._router_request(
            self.get_device_class_templates(
                device_class='Devices'
            )
        )

        templates = []
        found_templates = self._find_templates_in_tree(templates_data[0])
        for t in found_templates:
            templates.append(t)
        return templates

    def get_device_class_templates(self, device_class):
        """
        Gets the defined templates for a device class

        Arguments:
            device_class (str): Device class to get templates for

        Returns:
            list(ZenossTemplate):
        """
        templates_data = self._router_request(
            self._make_request_data(
                'getDeviceClassTemplates',
                dict(id=device_class),
            )
        )

        templates = []
        found_templates = self._find_templates_in_tree(templates_data[0])
        for t in found_templates:
            templates.append(
                self._get_template_by_uid(t[0])
            )
        return templates

    def list_device_class_templates(self, device_class):
        """
        Returns the defined templates for a device class as a list of
        tuples containing the template UID and description.

        Arguments:
            device_class (str): Device class to list templates for

        Returns:
            list(str):
        """
        if not device_class.startswith('Devices'):
            if device_class.startswith('/'):
                device_class = 'Devices{0}'.format(device_class)
            else:
                device_class = 'Devices/{0}'.format(device_class)
        templates_data = self._router_request(
            self._make_request_data(
                'getDeviceClassTemplates',
                dict(id=device_class),
            )
        )

        templates = []
        found_templates = self._find_templates_in_tree(templates_data[0])
        for t in found_templates:
            templates.append(t)
        return templates

    def get_object_templates(self, zenoss_object):
        """
        Gets the templates bound to a specific object
        (monitored resource or component)

        Arguments:
            zenoss_object (str): The uid of the object, e.g.
                        Devices/Server/Zuora/Aspose/devices/10.aspose.prod.slv.zuora

        Returns:
            list(ZenossTemplate):
        """
        if not zenoss_object.startswith('Devices'):
            if zenoss_object.startswith('/'):
                zenoss_object = 'Devices{0}'.format(zenoss_object)
            else:
                zenoss_object = 'Devices/{0}'.format(zenoss_object)

        templates_data = self._router_request(
            self._make_request_data(
                'getObjTemplates',
                dict(uid=zenoss_object),
            )
        )

        templates = []
        found_templates = templates_data['data']
        for t in found_templates:
            templates.append(
                self._get_template_by_uid(t['uid'].replace('/zport/dmd/', '', 1))
            )
        return templates

    def get_template(self, device_class, template):
        """
        Get a Zenoss template

        Arguments:
            device_class (str): Name of the device class where the template is defined
            template (str): Name of the template to get

        Returns:
            ZenossTemplate:
        """
        # Check to see if this is a local template instead of a device class
        # template
        if "devices" in device_class:
            template_uid = '{0}/{1}'.format(device_class, template)
        else:
            template_uid = '{0}/rrdTemplates/{1}'.format(device_class, template)

        return self._get_template_by_uid(template_uid)

    def add_template(self, target, name):
        """
        Adds a template to a device class.

        Arguments:
            target (str): The uid of the target device class
            name (str): Unique name of the template to add

        Returns:
            ZenossTemplate:
        """
        if not target.startswith('Devices'):
            if target.startswith('/'):
                target = 'Devices{0}'.format(target)
            else:
                target = 'Devices/{0}'.format(target)

        if not target.endswith('rrdTemplates'):
            target = target + '/rrdTemplates'

        template_data = self._router_request(
            self._make_request_data(
                'addTemplate',
                dict(
                    id=name,
                    targetUid=target,
                )
            )
        )

        return self._get_template_by_uid(template_data['nodeConfig']['uid'].replace('/zport/dmd/', '', 1))

    def delete_template(self, device_class, template):
        """
        Removes a template.

        Arguments:
            device_class (str): Name of the device class where the template is defined
            template (str): Name of the template to remove

        Returns:
             dict:
        """
        if not device_class.startswith('Devices'):
            if device_class.startswith('/'):
                device_class = 'Devices{0}'.format(device_class)
            else:
                device_class = 'Devices/{0}'.format(device_class)

        template_uid = '{0}/rrdTemplates/{1}'.format(device_class, template)
        return self._router_request(
            self._make_request_data(
                'deleteTemplate',
                dict(uid=template_uid),
            )
        )

    def add_local_template(self, zenoss_object, name):
        """
        Adds a local template to an object.

        Arguments:
             zenoss_object (str): Uid of the object to add the local template to
             name (str): Unique name for the new local template

         Returns:
             ZenossTemplate:
        """
        if not zenoss_object.startswith('Devices'):
            if zenoss_object.startswith('/'):
                zenoss_object = 'Devices{0}'.format(zenoss_object)
            else:
                zenoss_object = 'Devices/{0}'.format(zenoss_object)

        template_data = self._router_request(
            self._make_request_data(
                'addLocalRRDTemplate',
                dict(
                    uid=zenoss_object,
                    templateName=name,
                )
            )
        )

        return self._get_template_by_uid(template_data['nodeConfig']['uid'].replace('/zport/dmd/', '', 1))

    def delete_local_template(self, zenoss_object, name):
        """
        Builds the request data for deleting a local template to an object.

        Arguments:
             object (str): Uid of the object to remove the local template from
             name (str): Unique name of the new local template

         Returns:
             dict:
        """
        if not zenoss_object.startswith('Devices'):
            if zenoss_object.startswith('/'):
                zenoss_object = 'Devices{0}'.format(zenoss_object)
            else:
                zenoss_object = 'Devices/{0}'.format(zenoss_object)

        return self._router_request(
            self._make_request_data(
                'removeLocalRRDTemplate',
                dict(
                    uid=zenoss_object,
                    templateName=name,
                )
            )
        )

    def get_data_source_types(self):
        """
        Gets the list of available data source types.

        Returns:
            list:
        """
        ds_types_data = self._router_request(
            self._make_request_data(
                'getDataSourceTypes',
                dict(query=''),
            )
        )
        data_source_types = []
        for ds_type in ds_types_data['data']:
            data_source_types.append(ds_type['type'])

        return data_source_types

    def get_threshold_types(self):
        """
        Gets the list of available threshold types.

        Returns:
            list:
        """
        threshold_types_data = self._router_request(
            self._make_request_data(
                'getThresholdTypes',
                dict()
            )
        )
        threshold_types = []
        for threshold_type in threshold_types_data['data']:
            threshold_types.append(threshold_type['type'])

        return threshold_types

    def add_data_point_to_graph(self, datapoint, graph, include_thresholds=False):
        """
        Adds a data point to a graph.

        Arguments:
            datapoint (str): Uid of the data point to add
            graph (str): Uid of the graph to add the data point to
            include_thresholds (bool): Set to True to include the related
                                       thresholds for the data point

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'addDataPointToGraph',
                dict(
                    dataPointUid=datapoint,
                    graphUid=graph,
                    includeThresholds=include_thresholds,
                )
            )
        )


class ZenossTemplate(TemplateRouter):
    """
    Class for Zenoss Template objects
    """

    def __init__(self, url, headers, ssl_verify, template_data):
        super(ZenossTemplate, self).__init__(url, headers, ssl_verify)

        self.definition = template_data.setdefault('definition', None)
        self.description = template_data.setdefault('description', None)
        self.hidden = template_data.setdefault('hidden', False)
        self.iconCls = template_data.setdefault('iconCls', None)
        self.id = template_data.setdefault('id', None)
        self.inspector_type = template_data.setdefault('inspector_type', None)
        self.leaf = template_data.setdefault('leaf', True)
        self.meta_type = template_data.setdefault('meta_type', 'RRDTemplate')
        self.name = template_data['name']
        self.qtip = template_data.setdefault('qtip', None)
        self.targetPythonClass = template_data.setdefault('targetPythonClass', None)
        self.text = template_data.setdefault('text', None)

        if 'uid' in template_data:
            self.uid = template_data['uid'].replace('/zport/dmd/', '', 1)
        else:
            self.uid = None

    def copy(self, target):
        """
        Copy a template to another device or device class.

        Arguments:
            target (str): Uid of the device or device class to copy to

        Returns:
            ZenossTemplate:
        """
        if not target.endswith('rrdTemplates'):
            target = target + '/rrdTemplates'
        template_data = self._router_request(
            self._make_request_data(
                'copyTemplate',
                dict(
                    uid=self.uid,
                    targetUid=target,
                )
            )
        )
        return ZenossTemplate(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            template_data['data']
        )

    def delete(self):
        """
        Removes a template.

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'deleteTemplate',
                dict(uid=self.uid),
            )
        )

    def get_data_sources(self):
        """
        Gets data sources configured for a template.

        Returns:
            list(ZenossDataSource):
        """
        ds_data = self._router_request(
            self._make_request_data(
                'getDataSources',
                dict(uid=self.uid),
            )
        )
        datasources = []
        for ds in ds_data['data']:
            datasources.append(
                ZenossDataSource(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    ds
                )
            )
        return datasources

    def list_data_sources(self):
        """
        Rerturns data sources configured for a template as a list.

        Returns:
            list(str):
        """
        ds_data = self._router_request(
            self._make_request_data(
                'getDataSources',
                dict(uid=self.uid),
            )
        )
        datasources = []
        for ds in ds_data['data']:
            datasources.append(ds['uid'].replace('/zport/dmd/', '', 1))

        return datasources

    def get_data_source(self, datasource):
        """
        Get a particular data source.

        Arguments:
            datasource (str): Name of the data source to get

        Returns:
            ZenossDataSource:
        """
        datasource_uid = '{}/datasources/{}'.format(self.uid, datasource)

        return self._get_data_source_by_uid(datasource_uid)

    def add_data_source(self, datasource, type):
        """
        Adds a data source to a template.

        Arguments:
            datasource (str): Name of the new data source
            type (str): Type of the new data source, must be one of the types
                        returned by get_data_source_types()

        Returns:
            ZenossDataSource:
        """
        response_data = self._router_request(
            self._make_request_data(
                'addDataSource',
                dict(
                    templateUid=self.uid,
                    name=datasource,
                    type=type,
                )
            )
        )
        return self._get_data_source_by_uid(
            '{}/datasources/{}'.format(self.uid, datasource)
        )

    def delete_data_source(self, datasource):
        """
        Deletes a data source from a template.

        Arguments:
            datasource (str): Name the data source to remove

        Returns:
            dict:
        """
        datasource_uid = '{}/datasources/{}'.format(self.uid, datasource)
        return self._router_request(
            self._make_request_data(
                'deleteDataSource',
                dict(uid=datasource_uid),
            )
        )

    def get_data_points(self):
        """
        Get all the data points in a template.

        Returns:
            list(ZenossDataPoint):
        """
        dp_data = self._router_request(
            self._make_request_data(
                'getDataPoints',
                dict(uid=self.uid)
            )
        )

        datapoints = []
        for dp in dp_data['data']:
            datapoints.append(
                ZenossDataPoint(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    dp
                )
            )
        return datapoints

    def list_data_points(self):
        """
        Returns all the data points in a template as a list.

        Returns:
            list(str):
        """
        dp_data = self._router_request(
            self._make_request_data(
                'getDataPoints',
                dict(uid=self.uid)
            )
        )

        datapoints = []
        for dp in dp_data['data']:
            datapoints.append(dp['uid'].replace('/zport/dmd/', '', 1))

        return datapoints

    def get_thresholds(self):
        """
        Gets the thresholds of a template.

        Returns:
            list(ZenossThresholds):
        """
        threshold_data = self._router_request(
            self._make_request_data(
                'getThresholds',
                dict(uid=self.uid),
            )
        )

        thresholds = []
        for t in threshold_data['data']:
            thresholds.append(
                ZenossThreshold(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    t
                )
            )

        return thresholds

    def list_thresholds(self):
        """
        Returns the thresholds of a template as a list.

        Returns:
            list(str):
        """
        threshold_data = self._router_request(
            self._make_request_data(
                'getThresholds',
                dict(uid=self.uid),
            )
        )

        thresholds = []
        for t in threshold_data['data']:
            thresholds.append(t['uid'].replace('/zport/dmd/', '', 1))

        return thresholds

    def get_threshold(self, threshold):
        """
        Get a particular threshold.

        Arguments:
            threshold (str): Name of the threshold to get details on

        Returns:
            ZenossThreshold:
        """
        threshold_uid = '{}/thresholds/{}'.format(self.uid, threshold)
        return self._get_threshold_by_uid(threshold_uid)

    def add_threshold(self, threshold, threshold_type, datapoints):
        """
        Adds a threshold to a template.

        Arguments:
            threshold (str): Name of the new threshold
            threshold_type (str): Type of the new threshold, must be one of the types
                        returned by get_threshold_types()
            datapoints (list): List of datapoints to select for the threshold

        Returns:
            ZenossThreshold:
        """
        if not isinstance(datapoints, list):
            raise ZenossAPIClientError('Type error: datapoints to add to a threshold must be a list')

        response_data = self._router_request(
            self._make_request_data(
                'addThreshold',
                dict(
                    uid=self.uid,
                    thresholdId=threshold,
                    thresholdType=threshold_type,
                    dataPoints=datapoints,
                )
            )
        )

        return self._get_threshold_by_uid(
            '{}/thresholds/{}'.format(self.uid, threshold)
        )

    def delete_threshold(self, threshold):
        """
        Deletes a threshold.

        Arguments:
            threshold (str): Name of the threshold to remove

        Returns:
            dict:
        """
        threshold_uid = '{}/thresholds/{}'.format(self.uid, threshold)
        return self._router_request(
            self._make_request_data(
                'removeThreshold',
                dict(uid=threshold_uid),
            )
        )

    def get_graphs(self):
        """
        Get the graphs defined for a template.

        Returns:
            list(ZenossGraph):
        """
        graphs_data = self._router_request(
            self._make_request_data(
                'getGraphs',
                dict(uid=self.uid),
            )
        )

        graphs = []
        for g in graphs_data:
            graphs.append(
                ZenossGraph(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    g
                )
            )
        return graphs

    def list_graphs(self):
        """
        Returns the graphs defined for a template as a list.

        Returns:
            list(str):
        """
        graphs_data = self._router_request(
            self._make_request_data(
                'getGraphs',
                dict(uid=self.uid),
            )
        )

        graphs = []
        for g in graphs_data:
            graphs.append(g['uid'].replace('/zport/dmd/', '', 1))

        return graphs

    def get_graph(self, graph):
        """
        Get a particular graph.

        Arguments:
            graph (str): Name of the graph to get the definition of

        Returns:
            ZenossGraph:
        """
        graph_uid = '{}/graphDefs/{}'.format(self.uid, graph)

        return self._get_graph_by_uid(graph_uid)

    def add_graph(self, graph):
        """
        Add a new graph to a template.

        Arguments:
            graph (str): Name for the new graph

        Returns:
            ZenossGraph:
        """
        response_data = self._router_request(
            self._make_request_data(
                'addGraphDefinition',
                dict(
                    templateUid=self.uid,
                    graphDefinitionId=graph,
                )
            )
        )

        return self._get_graph_by_uid(
            '{}/graphDefs/{}'.format(self.uid, graph)
        )

    def delete_graph(self, graph):
        """
        Delete a particular graph.

        Arguments:
            graph (str): The name of the graph to delete.

        Returns:
            dict:
        """
        graph_uid = '{0}/graphDefs/{1}'.format(self.uid, graph)

        return self._router_request(
            self._make_request_data(
                'deleteGraphDefinition',
                data=dict(
                    uid=graph_uid,
                )
            )
        )


class ZenossDataSource(TemplateRouter):
    """
    Class for Zenoss template data sources
    """

    def __init__(self, url, headers, ssl_verify, ds_data):
        super(ZenossDataSource, self).__init__(url, headers, ssl_verify)

        uid = ds_data.pop('uid')
        self.uid = uid.replace('/zport/dmd/', '', 1)
        self.name = ds_data.pop('name')
        self.id = ds_data.pop('id')
        self.eventClass = ds_data.pop('eventClass')
        self.eventKey = ds_data.pop('eventKey')
        self.severity = ds_data.pop('severity')
        self.type = ds_data.pop('type')
        self.component = ds_data.pop('component')
        self.properties = ds_data
        self.parent = self.uid.split('/datasources/')[0]

    def delete(self):
        """
        Deletes a data source from a template.

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'deleteDataSource',
                dict(uid=self.uid),
            )
        )

    def get_data_points(self):
        """
        Get all the data points for a datasource.

        Returns:
            list(ZenossDataPoint):
        """
        dp_data = self._router_request(
            self._make_request_data(
                'getDataPoints',
                dict(uid=self.parent)
            )
        )

        datapoints = []
        for dp in dp_data['data']:
            if dp['name'].startswith(self.name):
                datapoints.append(
                    ZenossDataPoint(
                        self.api_url,
                        self.api_headers,
                        self.ssl_verify,
                        dp
                    )
                )
        return datapoints

    def list_data_points(self):
        """
        Returns all the data points for a datasource as a list.

        Returns:
            list(str):
        """
        dp_data = self._router_request(
            self._make_request_data(
                'getDataPoints',
                dict(uid=self.parent)
            )
        )

        datapoints = []
        for dp in dp_data['data']:
            if dp['name'].startswith(self.name):
                datapoints.append(dp['uid'].replace('/zport/dmd/', '', 1))

        return datapoints

    def get_data_point(self, datapoint):
        """
        Get a particular data point.

        Arguments:
            datapoint (str): Name of the data point to get details for

        Returns:
            ZenossDataPoint:
        """
        datapoint_uid = '{}/datapoints/{}'.format(self.uid, datapoint)

        return self._get_data_point_by_uid(datapoint_uid)

    def add_data_point(self, datapoint):
        """
        Adds a data point to a data source.

        Arguments:
            datapoint (str): Name of the new data point

        Returns:
            ZenossDataPoint:
        """
        response_data = self._router_request(
            self._make_request_data(
                'addDataPoint',
                dict(
                    dataSourceUid=self.uid,
                    name=datapoint,
                )
            )
        )

        return self._get_data_point_by_uid(
            '{}/datapoints/{}'.format(self.uid, datapoint)
        )

    def delete_data_point(self, datapoint):
        """
        Deletes a data point from a template.

        Arguments:
            datapoint (str): Name of the data point to remove

        Returns:
            dict:
        """
        datapoint_uid = '{}/datapoints/{}'.format(self.uid, datapoint)
        return self._router_request(
            self._make_request_data(
                'deleteDataPoint',
                dict(uid=datapoint_uid),
            )
        )


class ZenossDataPoint(TemplateRouter):
    """
    Class for Zenoss data points
    """

    def __init__(self, url, headers, ssl_verify, dp_data):
        super(ZenossDataPoint, self).__init__(url, headers, ssl_verify)

        self.isrow = dp_data['isrow']
        self.leaf = dp_data['leaf']
        self.description = dp_data['description']
        self.rrdmin = dp_data['rrdmin']
        self.name = dp_data['name']
        self.rate = dp_data['rate']
        self.newId = dp_data['newId']
        self.createCmd = dp_data['createCmd']
        self.rrdtype = dp_data['rrdtype']
        self.rrdmax = dp_data['rrdmax']
        self.aliases = dp_data['aliases']
        self.type = dp_data['type']
        self.id = dp_data['id']
        self.uid = dp_data['uid'].replace('/zport/dmd/', '', 1)
        self.parent = self.uid.split('/datapoints/')[0]

    def set_threshold(self, threshold, threshold_type):
        """
        Adds a threshold for the data point

        Arguments:
            threshold (str): Name of the threshold to add
            threshold_type (str): Type of the new threshold, must be one of the
                        types returned by get_threshold_types()

        Returns:
            ZenossThreshold:
        """
        template = self.uid.split('/datasources/')[0]

        response_data = self._router_request(
            self._make_request_data(
                'addThreshold',
                dict(
                    uid=template,
                    thresholdId=threshold,
                    thresholdType=threshold_type,
                    dataPoints=[self.uid],
                )
            )
        )

        return self._get_threshold_by_uid(
            '{}/thresholds/{}'.format(self.uid, threshold)
        )

    def make_counter(self):
        """
        Sets the RRD Type of the data point to COUNTER

        Returns:
            bool:
        """
        self.set_properties(dict(rrdtype='COUNTER'))
        self.rrdtype = 'COUNTER'

        return True

    def make_gauge(self):
        """
        Sets the RRD Type of the data point to GAUGE

        Returns:
            bool:
        """
        self.set_properties(dict(rrdtype='GAUGE'))
        self.rrdtype = 'GAUGE'

        return True

    def add_to_graph(self, graph, include_thresholds=False):
        """
        Adds a data point to a graph.

        Arguments:
            graph (str): Name of the graph to add the data point to
            include_thresholds (bool): Set to True to include the related
                                       thresholds for the data point

        Returns:
            dict:
        """
        graph_uid = '{0}/graphDefs/{1}'.format(self.uid.split('/datasources/')[0], graph)
        return self.add_data_point_to_graph(self.uid, graph_uid, include_thresholds)

    def delete(self):
        """
        Deletes a data point from a template.

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'deleteDataPoint',
                dict(uid=self.uid),
            )
        )


class ZenossThreshold(TemplateRouter):
    """
    Class for Zenoss thresholds
    """

    def __init__(self, url, headers, ssl_verify, threshold_data):
        super(ZenossThreshold, self).__init__(url, headers, ssl_verify)

        self.description = threshold_data.pop('description')
        self.enabled = threshold_data.pop('enabled')
        self.name = threshold_data.pop('name')
        self.dataPoints = threshold_data.pop('dataPoints')
        self.eventClass = threshold_data.pop('eventClass')
        self.type = threshold_data.pop('type')
        self.id = threshold_data.pop('id')
        self.severity = threshold_data.pop('severity')
        uid = threshold_data.pop('uid')
        self.uid = uid.replace('/zport/dmd/', '', 1)
        self.parent = self.uid.split('/thresholds/')[0]
        self.properties = threshold_data

    def set_max(self, maxval):
        """
        Sets the threshold value for a MinMaxThreshold checking the max
        value of a data point.

        Arguments:
            maxval (str): Maximum value for the data point before alerting

        Returns:
            bool:
        """
        self.set_properties(dict(maxval=maxval))
        self.properties['maxval'] = maxval

        return True

    def set_min(self, minval):
        """
        Sets the threshold value for a MinMaxThreshold checking the minimum
        value of a data point.

        Arguments:
            minval (str): Minimum value for the data point before alerting

        Returns:
            bool:
        """
        self.set_properties(dict(minval=minval))
        self.properties['minval'] = minval

        return True

    def delete(self):
        """
        Deletes a threshold.

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'removeThreshold',
                dict(uid=self.uid),
            )
        )


class ZenossGraph(TemplateRouter):
    """
    Class for Zenoss graphs
    """

    def __init__(self, url, headers, ssl_verify, graph_data):
        super(ZenossGraph, self).__init__(url, headers, ssl_verify)

        self.sequence = graph_data['sequence']
        self.height = graph_data['height']
        self.miny = graph_data['miny']
        self.id = graph_data['id']
        self.maxy = graph_data['maxy']
        self.autoscale = graph_data['autoscale']
        self.log = graph_data['log']
        self.custom = graph_data['custom']
        self.width = graph_data['width']
        self.graphPoints = graph_data['graphPoints']
        self.rrdVariables = graph_data['rrdVariables']
        self.units = graph_data['units']
        self.hasSummary = graph_data['hasSummary']
        self.ceiling = graph_data['ceiling']
        self.description = graph_data['description']
        self.base = graph_data['base']
        self.name = graph_data['name']
        self.uid = graph_data['uid'].replace('/zport/dmd/', '', 1)
        self.parent = self.uid.split('/graphDefs/')[0]

    def delete(self):
        """
        Delete the graph.

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'deleteGraphDefinition',
                data=dict(
                    uid=self.uid,
                )
            )
        )

    def get_points(self):
        """
        Gets the data points of a graph.

        Returns:
            list(ZenossDataPoint):
        """
        points_data = self._router_request(
            self._make_request_data(
                'getGraphPoints',
                dict(uid=self.uid,)
            )
        )

        points = []
        for p in points_data['data']:
            point_datasource = p['dpName'].split('_')[0]
            points.append(
                self._get_data_point_by_uid('{0}/datasources/{1}/datapoints/{2}'.format(self.parent, point_datasource, p['dpName']))
            )
        return points

    def list_points(self):
        """
        Returns the data points of a graph as a list.

        Returns:
            list(str):
        """
        points_data = self._router_request(
            self._make_request_data(
                'getGraphPoints',
                dict(uid=self.uid,)
            )
        )

        points = []
        for p in points_data['data']:
            points.append(p['uid'].replace('/zport/dmd/', '', 1))

        return points

    def add_point(self, datasource, datapoint, include_thresholds=False):
        """
        Adds a data point to a graph.

        Arguments:
            datasource (str): Name of the data source holding the data point
            datapoint (str): Name of the data point to add
            include_thresholds (bool): Set to True to include the related
                                       thresholds for the data point

        Returns:
            dict:
        """
        datapoint_uid = '{0}/datasources/{1}/datapoints/{2}'.format(self.parent, datasource, datapoint)
        return self.add_data_point_to_graph(datapoint_uid, self.uid, include_thresholds)

    def set_graph_properties(self, properties):
        """
        Set the properties for a graph.

        Arguments:
            properties (dict): Properties and values to set

        Returns:
            dict:
        """
        data = dict(uid=self.uid)
        data.update(properties)
        response_data = self._router_request(
            self._make_request_data(
                'setGraphDefinition',
                data,
            )
        )
        for prop in properties:
            if getattr(self, prop, False):
                setattr(self, prop, properties[prop])

        return response_data

    def set_zero_baseline(self):
        """
        Set the minimum value of a graph display to zero. By default
        Zenoss graph scale is dynamic, meaning the display
        can be skewed because the minimum value isn't fixed.
        """
        return self.set_graph_properties(
            properties=dict(miny=0),
        )

    def set_point_sequence(self, datapoints):
        """
        Sets the order of data points in a graph.

        Arguments:
            datapoints (list): List of data point names in the desired order

        Returns:
            dict:
        """
        if not isinstance(datapoints, list):
            raise ZenossAPIClientError('Type error: Sequence of datapoints must be a list')

        graph_points = []
        for p in datapoints:
            graph_points.append('{}/graphPoints/{}'.format(self.uid, p))

        return self._router_request(
            self._make_request_data(
                'setGraphPointSequence',
                dict(uids=graph_points)
            )
        )

    def delete_point(self, datapoint):
        """
        Deletes a data point from a graph.

        Arguments:
            datapoint (str): Name of the data point to remove

        Returns:
            dict:
        """
        response_data = self._router_request(
            self._make_request_data(
                'deleteGraphPoint',
                dict(uid='{}/graphPoints/{}'.format(self.uid, datapoint))
            )
        )

        graph_data = self._router_request(
            self._make_request_data(
                'getGraphDefinition',
                dict(uid=self.uid)
            )
        )

        self.graphPoints = graph_data['data']['graphPoints']
        self.rrdVariables = graph_data['data']['rrdVariables']

        return response_data

    def add_graph_threshold(self, threshold):
        """
        Adds a threshold to a graph.

        Arguments:
            threshold (str): Uid of the threshold to add

        Returns:
            dict:
        """
        response_data = self._router_request(
            self._make_request_data(
                'addThresholdToGraph',
                dict(
                    graphUid=self.uid,
                    thresholdUid=threshold,
                )
            )
        )

        graph_data = self._router_request(
            self._make_request_data(
                'getGraphDefinition',
                dict(uid=self.uid)
            )
        )

        self.graphPoints = graph_data['data']['graphPoints']

        return response_data
