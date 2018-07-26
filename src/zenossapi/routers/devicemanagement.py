# -*- coding: utf-8 -*-

"""
Zenoss devicemanagement_router
"""

from datetime import datetime as dt
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers import ZenossRouter

__router__ = 'DeviceManagementRouter'


class DeviceManagementRouter(ZenossRouter):
    """
    Class for interacting with the Zenoss devicemanagement router
    """

    def __init__(self, url, headers, ssl_verify):
        super(DeviceManagementRouter, self).__init__(url, headers, ssl_verify,
                                                     'devicemanagement_router',
                                                     'DeviceManagementRouter')
        self.uid = None

    def __repr__(self):
        if self.uid:
            identifier = self.uid
        else:
            identifier = hex(id(self))

        return '<{0} object at {1}>'.format(
            type(self).__name__, identifier
        )

    def timezone(self):
        """
        Returns the configured timezone.

        Returns:
            str:
        """
        tz_data = self._router_request(
            self._make_request_data(
                'getTimeZone',
                data=dict()
            )
        )

        return tz_data['data']

    def list_maintenance_windows(self, uid):
        """
        Returns the list of maintenance windows configured for a device
        or device class.

        Arguments:
            uid (str): The UID of the device or device class

        Returns:
            list(dict):
        """
        uid = self._check_uid(uid)

        mw_data = self._router_request(
            self._make_request_data(
                'getMaintWindows',
                data=dict(
                    uid=uid
                )
            )
        )

        for mw in mw_data['data']:
            mw['uid'] = mw['uid'].replace('/zport/dmd/', '', 1)

        return mw_data['data']

    def get_maintenance_windows(self, uid):
        """
        Returns a list of ZenossMaintenanceWindow objects for the
        maintenance windows configured for a device or device class

        Arguments:
            uid (str): The UID of the device or device class

        Returns:
            list(ZenossMaintenanceWindow):
        """
        mw_data = self.list_maintenance_windows(uid)
        windows = []
        for mw in mw_data:
            windows.append(
                ZenossMaintenanceWindow(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    mw,
                    parent=self._check_uid(uid),
                )
            )

        return windows

    def get_maintenance_window(self, uid, name):
        """
        Get a maintenance window object for the named window.

        Arguments:
            uid (str): The UID of the device or device class
            name (str): Name of the maintenance window

        Returns:
            ZenossMaintenanceWindow:
        """
        mw_data = self.list_maintenance_windows(uid)

        for mw in mw_data:
            if mw['name'] == name:
                return ZenossMaintenanceWindow(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    mw,
                    parent=self._check_uid(uid),
                )

        return None

    def add_maintenance_window(self, uid, name, start, duration, enabled=False, start_state=300, repeat='Never', occurrence='1st', days='Sunday'):
        """
        Add a new maintenance window for device or device class.

        Arguments:
            uid (str): The UID of the device or device class
            start (str): Window start time in UNIX epoch timestamp format,
                e.g. "1511290393"
            duration (str): Duration of the window in HH:MM:SS format
            start_state (int): Production state for the maintenance window,
                default is 300 (Maintenance)
            repeat (str): Maintenance window repeat interval, default is
                'Never'. Other valid choices are: 'Daily', 'Every Weekday',
                'Weekly', 'Monthly: day of month', 'Monthly: day of week'
            occurrence (str): For 'Monthly: day of week' repeats, options are
                '1st', '2nd', '3rd', '4th', '5th', 'Last'
            days (str): For 'Monthly: day of week' repeats, options are
                'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday'

        Returns:
            ZenossMaintenanceWindow:
        """
        if repeat not in ['Never', 'Daily', 'Every Weekday', 'Weekly',
                          'Monthly: day of month', 'Monthly: day of week']:
            raise ZenossAPIClientError(
                'Invalid maintenance window repetition: {0}'.format(repeat))

        if occurrence not in ['1st', '2nd', '3rd', '4th', '5th', 'Last']:
            raise ZenossAPIClientError(
                'Invalid maintenance window occurrence: {0}'.format(occurrence))

        if days not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                        'Saturday', 'Sunday']:
            raise ZenossAPIClientError(
                'Invalid maintenance window days: {0}'.format(days))

        self._router_request(
            self._make_request_data(
                'addMaintWindow',
                data=dict(
                    params=dict(
                        uid=uid,
                        name=name,
                        start=start,
                        duration=duration,
                        enabled=enabled,
                        startState=start_state,
                        repeat=repeat,
                        occurrence=occurrence,
                        days=days,
                    )
                )
            )
        )

        return self.get_maintenance_window(uid, name)

    def list_user_commands(self, uid):
        """
        Get the list of user commands configured for a device or device class.

        Arguments:
            uid (str): The UID of the device or device class

        Returns:
            list(dict):
        """
        uid = self._check_uid(uid)

        uc_data = self._router_request(
            self._make_request_data(
                'getUserCommands',
                data=dict(
                    uid=uid,
                )
            )
        )

        return uc_data['data']

    def get_user_commands(self, uid):
        """
        Get a list of user commands objects configured for a device
        or device class.

        Arguments:
            uid (str): The UID of the device or device class

        Returns:
            list(ZenossUserCommand):
        """
        uc_data = self.list_user_commands(uid)
        user_commands = []
        for uc in uc_data:
            user_commands.append(
                ZenossUserCommand(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    uc,
                    parent=self._check_uid(uid)
                )
            )

        return user_commands

    def get_user_command_by_id(self, uid, command_id):
        """
        Get a configured user command by its id

        Arguments:
            uid (str): The UID of the device or device class
            command_id (str): The ID of the user command
        """
        uc_data = self.list_user_commands(uid)
        for uc in uc_data:
            if uc['id'] == command_id:
                return ZenossUserCommand(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    uc,
                    parent=self._check_uid(uid)
                )

        return None

    def get_user_command_by_name(self, uid, command_name):
        """
        Get a configured user command by its id

        Arguments:
            uid (str): The UID of the device or device class
            command_name (str): The name of the user command
        """
        uc_data = self.list_user_commands(uid)
        for uc in uc_data:
            if uc['name'] == command_name:
                return ZenossUserCommand(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    uc,
                    parent=self._check_uid(uid)
                )

        return None

    def add_user_command(self, uid, name, description, command, password):
        """
        Add a new user command to a device or device class.

        Arguments:
            uid (str): The UID of the device or device class
            name (str): Name for the new command
            description (str): Description of the new command
            command (str): Command line of the new command, can include TALES
                expressions
            password (str): Password of the user adding the command.
        """
        uid = self._check_uid(uid)
        self._router_request(
            self._make_request_data(
                'addUserCommand',
                data=dict(
                    uid=uid,
                    name=name,
                    description=description,
                    command=command,
                    password=password
                )
            )
        )

        return self.get_user_command_by_name(uid, name)

    def list_users(self, uid):
        """
        List the users available to associate with a device or device class.

        Arguments:
            uid (str): the UID of the device or device class

        Returns:
            list(str):
        """
        uid = self._check_uid(uid)
        user_data = self._router_request(
            self._make_request_data(
                'getUserList',
                data=dict(
                    uid=uid
                )
            )
        )
        return user_data['data']

    def list_available_roles(self, uid):
        """
        List the admin roles available to associate with a device or device class.

        Arguments:
            uid (str): The UID of the device or device class

        Returns:
            list(str):
        """
        uid = self._check_uid(uid)
        role_data = self._router_request(
            self._make_request_data(
                'getRolesList',
                data=dict(
                    uid=uid
                )
            )
        )

        return role_data['data']

    def list_admin_roles(self, uid):
        """
        List the admin roles associated with a device or device class.

        Arguments:
            uid (str): The UID of the device or device class

        Returns:
            list(dict):
        """
        uid = self._check_uid(uid)
        role_data = self._router_request(
            self._make_request_data(
                'getAdminRoles',
                data=dict(
                    uid=uid
                )
            )
        )

        for r in role_data['data']:
            r['uid'] = r['uid'].replace('/zport/dmd/', '', 1)

        return role_data['data']

    def get_admins(self, uid):
        """
        Get ZenossDeviceManagementAdmin objects for the configured admin
        users for a device or device class.

        Arguments:
            uid (str): The UID of the device or device class

        Returns:
            list(ZenossDeviceManagementAdmin):
        """
        admin_data = self.list_admin_roles(uid)
        admins = []
        for admin in admin_data:
            admins.append(
                ZenossDeviceManagementAdmin(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    admin
                )
            )

        return admins

    def list_admins_by_role(self, uid, role):
        """
        List configured admin users for a device or device class by role.

        Arguments:
            uid (str): The UID of the device or device class
            role (str): The role to filter on

        Returns:
            list(dict):
        """
        admin_data = self.list_admin_roles(uid)
        admins = []
        for admin in admin_data:
            if admin['role'] == role:
                admins.append(admin)

        return admins

    def get_admins_by_role(self, uid, role):
        """
        Get ZenossDeviceManagementAdmin objects for the configured admin users
        of a device or device class by role.

        Arguments:
            uid (str): The UID of the device or device class
            role (str): The role to filter on

        Returns:
            list(ZenossDeviceManagementAdmin):
        """
        admin_data = self.list_admin_roles(uid)
        admins = []
        for admin in admin_data:
            if admin['role'] == role:
                admins.append(
                    ZenossDeviceManagementAdmin(
                        self.api_url,
                        self.api_headers,
                        self.ssl_verify,
                        admin
                    )
                )

        return admins

    def get_admin_by_name(self, uid, name):
        """
        Get an admin user for a device or device class by name.

        Arguments:
            uid (str): The UID of the device or device class
            name (str): The name of the admin user

        Returns:
            ZenossDeviceManagementAdmin:
        """
        admin_data = self.list_admin_roles(uid)
        for admin in admin_data:
            if admin['name'] == name:
                return ZenossDeviceManagementAdmin(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    admin
                )

        return None

    def get_admin_by_id(self, uid, admin_id):
        """
        Get and admin user for a device or device class by id.

        Arguments:
            uid (str): The UID of the device or device class
            admin_id (str): The ID of the admin user

        Returns:
            ZenossDeviceManagementAdmin:
        """
        admin_data = self.list_admin_roles(uid)
        for admin in admin_data:
            if admin['id'] == admin_id:
                return ZenossDeviceManagementAdmin(
                    self.api_url,
                    self.api_headers,
                    self.ssl_verify,
                    admin
                )

        return None

    def add_admin(self, uid, name, role=None):
        """
        Add an admin user to a device or device class.

        Arguments:
            uid (str): The UID of the device or device class
            name (str): The name of the user to add
            role (str): The role to associate with the user for this
                device or device class

        Returns:
            ZenossDeviceManagementAdmin:
        """
        uid = self._check_uid(uid)
        self._router_request(
            self._make_request_data(
                'addAdminRole',
                data=dict(
                    params=dict(
                        uid=uid,
                        name=name,
                        role=role,
                    )
                )
            )
        )

        return self.get_admin_by_name(uid, name)


class ZenossMaintenanceWindow(DeviceManagementRouter):
    """
    Class for Zenoss maintenance window objects
    """

    def __init__(self, url, headers, ssl_verify, window_data, parent=None):
        super(ZenossMaintenanceWindow, self).__init__(url, headers, ssl_verify)

        self.uid = window_data['uid'].replace('/zport/dmd/', '', 1)
        self.id = window_data['id']
        self.name = window_data['name']
        self.description = window_data['description']
        self.meta_type = window_data['meta_type']
        self.inspector_type = window_data['inspector_type']
        self.startState = window_data['startState']
        self.startProdState = window_data['startProdState']
        self.enabled = window_data['enabled']
        self.started = window_data['started']
        self.start = window_data['start']
        self.startTime = window_data['startTime']
        self.duration = window_data['duration']
        self.skip = window_data['skip']
        self.repeat = window_data['repeat']
        self.niceRepeat = window_data['niceRepeat']
        self.occurrence = window_data['occurrence']
        self.days = window_data['days']
        self.parent = parent

        self.startDate, start_ts, tz = self.startTime.split()
        self.startHours, self.startMinutes = start_ts.split(':')[:2]
        duration_parts = self.duration.split()
        if len(duration_parts) > 1:
            self.durationDays = duration_parts[0]
        else:
            self.durationDays = None
        self.durationHours, self.durationMinutes = duration_parts[-1].split(':')[:2]

    def _build_update_params(self, params):
        """
        Build the params dict for updating a maintenance window

        Arguments:
            params (dict): The update parameters as a dict

        Returns:
            dict:
        """

    def delete(self):
        """
        Delete a maintenance window from a device or device class.

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'deleteMaintWindow',
                data=dict(
                    uid=self.parent,
                    id=self.id,
                )
            )
        )

    def update(self, start_timestamp=None, start_datetime=None, start_date=None,
               start_hours=None, start_minutes=None, duration_days=None,
               duration_time=None, duration_hours=None, duration_minutes=None,
               production_state=None, enabled=None, repeat=None,
               occurrence=None, days=None):
        """
        Update the settings for a maintenance window, with flexible options for
        specifying the start date/time and duration.

        Arguments:
            start_timestamp (float): Start date and time in UNIX timestamp format
            start_datetime (datetime): Start date and time as a datetime.datetime object
            start_date (str): Start date as a string
            start_hours (str): Start hours as a string
            start_minutes (str): Start minutes as a string
            duration_days (str): Duration days
            duration_time (str): Duration time in "HH:MM" format
            duration_hours (str): Duration hours
            duration_minutes (str): Duration minutes
            production_state (int): Production state for the window
            enabled (bool): Enabled state of the window
            occurrence (str): Repeat occurrence
            days (str): Repeat days

        Returns:
            bool:
        """
        new_params = dict()
        if start_timestamp:
            new_start = dt.fromtimestamp(start_timestamp)
            new_params['startDate'] = str(new_start.date())
            new_params['startHours'] = str(new_start.hour)
            new_params['startMinutes'] = str(new_start.minute)
        elif start_datetime:
            new_params['startDate'] = str(start_datetime.date())
            new_params['startHours'] = str(start_datetime.hour)
            new_params['startMinutes'] = str(start_datetime.minute)
        if start_date:
            new_params['startDate'] = start_date
        if start_hours:
            new_params['startHours'] = start_hours
        if start_minutes:
            new_params['startMinutes'] = start_minutes

        new_params['durationDays'] = duration_days
        if duration_time:
            new_params['durationHours'], new_params['durationMinutes'] = duration_time.split(':')[:2]
        if duration_hours:
            new_params['durationHours'] = duration_hours
        if duration_minutes:
            new_params['durationMinutes'] = duration_minutes

        update_resp = self._router_request(
            self._make_request_data(
                'editMaintWindow',
                data=dict(
                    params=dict(
                        uid=self.parent,
                        id=self.id,
                        startDate=new_params.get('startDate', self.startDate),
                        startHours=new_params.get('startHours', self.startHours),
                        startMinutes=new_params.get('startMinutes', self.startMinutes),
                        durationDays=new_params.get('durationDays', self.durationDays),
                        durationHours=new_params.get('durationHours', self.durationHours),
                        durationMinutes=new_params.get('durationMinutes', self.durationMinutes),
                        startProductionState=production_state if production_state else self.startProdState,
                        repeat=repeat if repeat else self.repeat,
                        enabled=enabled if enabled else self.enabled,
                        occurrence=occurrence if occurrence else self.occurrence,
                        days=days if days else self.days
                    )
                )
            )
        )

        self.__init__(self.api_url, self.api_headers, self.ssl_verify, update_resp['data'][0], parent=self.parent)

        return True

    def enable(self):
        """
        Set maintenance window to enabled.

        Returns:
            bool:
        """
        if not self.enabled:
            self._router_request(
                self._make_request_data(
                    'editMaintWindow',
                    data=dict(
                        params=dict(
                            uid=self.parent,
                            id=self.id,
                            startDate=self.startDate,
                            startHours=self.startHours,
                            startMinutes=self.startMinutes,
                            durationDays=self.durationDays,
                            durationHours=self.durationHours,
                            startProductionState=self.startProdState,
                            repeat=self.repeat,
                            enabled=True,
                            occurrence=self.occurrence,
                            days=self.days,
                        )
                    )
                )
            )
            self.enabled = True

        return True

    def disable(self):
        """
        Set maintenance window to disabled.

        Returns:
            bool:
        """
        if self.enabled:
            self._router_request(
                self._make_request_data(
                    'editMaintWindow',
                    data=dict(
                        uid=self.parent,
                        id=self.id,
                        params=dict(
                            startDate=self.startDate,
                            startHours=self.startHours,
                            startMinutes=self.startMinutes,
                            durationDays=self.durationDays,
                            durationHours=self.durationHours,
                            startProductionState=self.startProdState,
                            repeat=self.repeat,
                            enabled=False,
                            occurrence=self.occurrence,
                            days=self.days,
                        )
                    )
                )
            )
            self.enabled = False

        return True


class ZenossUserCommand(DeviceManagementRouter):
    """
    Class for Zenoss user command objects
    """

    def __init__(self, url, headers, ssl_verify, command_data, parent=None):
        super(ZenossUserCommand, self).__init__(url, headers, ssl_verify)

        self.description = command_data['description']
        self.name = command_data['name']
        self.meta_type = command_data['meta_type']
        self.command = command_data['command']
        self.inspector_type = command_data['inspector_type']
        self.id = command_data['id']
        self.uid = command_data['uid'].replace('/zport/dmd/', '', 1)
        self.parent = parent

    def delete(self):
        """
        Delete a user command for a device or device class.

        Returns:
            dict:
        """
        return self._router_request(
            self._make_request_data(
                'deleteUserCommand',
                data=dict(
                    uid=self.parent,
                    id=self.id
                )
            )
        )

    def update(self, description=None, command=None, password=None):
        """
        Update a user command.

        Arguments:
            description (str): Description of the user command
            command (str): Command line of the command
            password (str): Password of the user updating the command.
        """
        self._router_request(
            self._make_request_data(
                'updateUserCommand',
                data=dict(
                    params=dict(
                        uid=self.parent,
                        id=self.id,
                        description=description if description else self.description,
                        command=command if command else self.command,
                        password=password,
                    )
                )
            )
        )

        uc_data = self.list_user_commands(self.parent)
        for uc in uc_data:
            if uc['id'] == self.id:
                self.__init__(self.api_url, self.api_headers, self.ssl_verify, uc, parent=self.parent)

        return True


class ZenossDeviceManagementAdmin(DeviceManagementRouter):
    """
    Class for Zenoss user command objects
    """

    def __init__(self, url, headers, ssl_verify, admin_data):
        super(ZenossDeviceManagementAdmin, self).__init__(url, headers, ssl_verify)

        self.uid = admin_data['uid'].replace('/zport/dmd/', '', 1)
        self.name = admin_data['name']
        self.id = admin_data['id']
        self.meta_type = admin_data['meta_type']
        self.role = admin_data['role']
        self.inspector_type = admin_data['inspector_type']
        self.pager = admin_data['pager']
        self.email=admin_data['email']

    def update(self, role):
        """
        Update the admin user's role.

        Arguments:
            role (str): New role for the user

        Returns:
            bool:
        """
        self._router_request(
            self._make_request_data(
                'updateAdminRole',
                data=dict(
                    params=dict(
                        uid=self.uid,
                        name=self.name,
                        role=role
                    )
                )
            )
        )

        self.role = role

        return True

    def delete(self):
        """
        Delete an admin user from a device or device class.

        :return:
        """
        return self._router_request(
            self._make_request_data(
                'removeAdmin',
                data=dict(
                    uid=self.uid,
                    id=self.id,
                )
            )
        )
