import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.jobs import JobsRouter, ZenossJob
import jobs_resp

pytest_plugins = "pytest-responses"
url = 'https://zenoss/zport/dmd'
headers = dict(
    ContentType='application/json'
)


def request_callback(request):
    rdata = json.loads(request.body)
    resp_headers = dict(ContentType='application/json')

    def getJobs(rdata):
        return jobs_resp.get_jobs

    def getInfo(rdata):
        if rdata['jobid'] == "721739ae-2b1d-4613-91e9-681f134a2c49":
            return jobs_resp.job1
        elif rdata['jobid'] == "9ba5c8d7-58de-4f18-96fe-d362841910d3":
            return jobs_resp.job2
        else:
            fail = jobs_resp.fail
            fail['result']['msg'] = "NoSuchJobException: {0}".format(rdata['jobid'])
            return fail

    def detail(rdata):
        if rdata['jobid'] == "721739ae-2b1d-4613-91e9-681f134a2c49":
            return jobs_resp.nolog
        elif rdata['jobid'] == "9ba5c8d7-58de-4f18-96fe-d362841910d3":
            return jobs_resp.detail

    method = locals()[rdata['method']]
    resp_body = method(rdata['data'][0])

    return (200, resp_headers, json.dumps(resp_body))


def responses_callback(responses):
    responses.add_callback(
        responses.POST,
        '{0}/jobs_router'.format(url),
        callback=request_callback,
        content_type='application/json',
    )


class TestJobsRouter(object):

    def test_jobs_router_init(self):
        jr = JobsRouter(url, headers, True)
        assert jr.uuid is None

    def test_jobs_router_list_jobs(self, responses):
        responses_callback(responses)

        jr = JobsRouter(url, headers, True)
        resp = jr.list_jobs()
        assert resp['total'] == 585
        assert len(resp['jobs']) == 2

    def test_jobs_router_get_jobs(self, responses):
        responses_callback(responses)

        jr = JobsRouter(url, headers, True)
        resp = jr.get_jobs()
        assert isinstance(resp[0], ZenossJob)

    def test_jobs_router_get_job(self, responses):
        responses_callback(responses)

        jr = JobsRouter(url, headers, True)
        resp = jr.get_job('721739ae-2b1d-4613-91e9-681f134a2c49')
        assert isinstance(resp, ZenossJob)
        assert resp.id == "721739ae-2b1d-4613-91e9-681f134a2c49"
        assert resp.status == "PENDING"

    def test_jobs_router_get_job_not_found(self, responses):
        responses_callback(responses)

        jr = JobsRouter(url, headers, True)
        with pytest.raises(ZenossAPIClientError, message="Request failed: NoSuchJobException: 0a39a730-9d41-48fb-878e-a5cbbbc1116a"):
            resp = jr.get_job('0a39a730-9d41-48fb-878e-a5cbbbc1116a')

    def test_jobs_router_get_log(self, responses):
        responses_callback(responses)

        jr = JobsRouter(url, headers, True)
        job = jr.get_job('9ba5c8d7-58de-4f18-96fe-d362841910d3')
        resp = job.get_log()
        assert resp['logfile'] == "/opt/zenoss/log/jobs/9ba5c8d7-58de-4f18-96fe-d362841910d3.log"
        assert len(resp['content']) == 29

    def test_jobs_router_get_log_no_log(self, responses):
        responses_callback(responses)

        jr = JobsRouter(url, headers, True)
        job = jr.get_job('721739ae-2b1d-4613-91e9-681f134a2c49')
        resp = job.get_log()
        assert resp['logfile'] == "The log file for this job either does not exist or cannot be accessed."
