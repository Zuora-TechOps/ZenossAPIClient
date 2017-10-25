# -*- coding: utf-8 -*-

"""
Zenoss jobs_router
"""

from zenossapi.routers import ZenossRouter


class JobsRouter(ZenossRouter):
    """
    Class for interacting with the Zenoss device router
    """

    def __init__(self, url, headers, ssl_verify):
        super(JobsRouter, self).__init__(url, headers, ssl_verify, 'jobs_router', 'JobsRouter')
        self.uuid = None

    def __repr__(self):
        if self.uuid:
            identifier = self.uuid
        else:
            identifier = hex(id(self))

        return '<{0} object at {1}>'.format(
            type(self).__name__, identifier
        )

    def _abort_jobs_by_uuid(self, jobs):
        """
        Aborts the jobs specified in the uuid list.

        Arguments:
            jobs (list): List of job uuids

        Returns:
            bool:
        """
        jobs_abort_response = self._router_request(
            self._make_request_data(
                'abort',
                dict(jobids=jobs),
            )
        )

        return True

    def _delete_jobs_by_uuid(self, jobs):
        """
        Deletes the jobs specified in the uuid list.

        Arguments:
            jobs (list): List of jobs uuids

        Returns:
            list: List of uuids deleted
        """
        deletes_response = self._router_request(
            self._make_request_data(
                'deleteJobs',
                dict(
                    jobids=jobs
                )
            )
        )

        if deletes_response is None:
            return []
        else:
            return deletes_response['deletedJobs']

    def list_jobs(self, start=0, limit=50, sort='scheduled', dir='DESC'):
        """
        List all Job Manager jobs, supports pagination.

        Arguments:
            start (int): Offset to start device list from, default 0
            limit (int): The number of results to return, default 50
            sort (str): Sort key for the list, default is 'scheduled'. Other
                sort keys are 'started, 'finished', 'status', 'type' and 'user'
            dir (str): Sort order, either 'ASC' or 'DESC', default is 'DESC'

        Returns:
            dict(int, dict(str, int, int, int, str, str, str, str, str)): ::

            {
                'total': (int) Total number of jobs,
                'jobs': {
                    'description': (str) Job description,
                    'finished': (int) Time the job finished in timestamp format,
                    'scheduled': (int) Time the job was scheduled in timestamp format,
                    'started': (int) Time the job started in timestamp format,
                    'status': (str) Status of the job,
                    'type': (str) Job type,
                    'uid': (str) JobManager UID - /zport/dmd/JobManager,
                    'user': (str) User who scheduled the job,
                    'uuid': (str) UUID of the job,
                }
            }

        """
        jobs_data = self._router_request(
            self._make_request_data(
                'getJobs',
                dict(
                    start=start,
                    limit=limit,
                    sort=sort,
                    dir=dir,
                    page=0,
                )
            )
        )

        return dict(
            total=jobs_data['totalCount'],
            jobs=jobs_data['jobs'],
        )

    def get_jobs(self, start=0, limit=50, sort='scheduled', dir='ASC'):
        """
        Get ZenossJob objects for Job Manager jobs. Supports pagination.

        Arguments:
            start (int): Offset to start device list from, default 0
            limit (int): The number of results to return, default 50
            sort (str): Sort key for the list, default is 'scheduled'. Other
                sort keys are 'started, 'finished', 'status', 'type' and 'user'
            dir (str): Sort order, either 'ASC' or 'DESC', default is 'ASC'

        Returns:
            list(ZenossJob):
        """
        jobs_data = self.list_jobs(start=start, limit=limit, sort=sort, dir=dir)

        jobs = []
        for job in jobs_data['jobs']:
            jobs.append(self.get_job(job['uuid']))

        return jobs

    def get_job(self, job):
        """
        Get a ZenossJob object by the job's uuid

        Arguments:
            job (str): uuid of the job

        Returns:
            ZenossJob:
        """
        job_data = self._router_request(
            self._make_request_data(
                'getInfo',
                dict(jobid=job)
            )
        )

        return ZenossJob(
            self.api_url,
            self.api_headers,
            self.ssl_verify,
            job_data['data']
        )


class ZenossJob(JobsRouter):
    """
    Class for Zenoss job objects
    """

    def __init__(self, url, headers, ssl_verify, job_data):
        super(ZenossJob, self).__init__(url, headers, ssl_verify)

        self.description = job_data['description']
        self.duration = job_data['duration']
        self.errors = job_data['errors']
        self.finished = job_data['finished']
        self.id = job_data['id']
        self.logfile = job_data['logfile']
        self.meta_type = job_data['meta_type']
        self.name = job_data['name']
        self.scheduled = job_data['scheduled']
        self.started = job_data['started']
        self.status = job_data['status']
        self.type = job_data['type']
        self.uid = job_data['uid']
        self.user = job_data['user']
        self.uuid = job_data['uuid']

    def abort(self):
        """
        Abort the job.

        Returns:
            bool:
        """
        return self._abort_jobs_by_uuid([self.uuid])

    def delete(self):
        """
        Delete the job.

        Returns:
            list: Job ID
        """
        return self._delete_jobs_by_uuid([self.uuid])

    def get_log(self):
        """
        Get the log for the job.

        Returns:
            dict(str, bool, list): ::

            {
                'logfile': Filesystem path of the log file,
                'maxLimit': True or False,
                'content': Log file lines
            }

        """
        return self._router_request(
            self._make_request_data(
                'detail',
                dict(
                    jobid=self.uuid,
                )
            )
        )

