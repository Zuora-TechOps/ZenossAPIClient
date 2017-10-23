import pytest
from zenossapi.apiclient import ZenossAPIClientAuthenticationError, ZenossAPIClientError
from zenossapi.routers import ZenossRouter

pytest_plugins = "pytest-responses"
url = 'https://zenoss/zport/dmd'
headers = dict(
    ContentType='application/json'
)


class TestBaseRouter(object):

    def test_routers_init(self):
        br = ZenossRouter(url, headers, True, 'test_router', 'TestRouter')
        assert br.api_url == url
        assert br.api_headers == headers
        assert br.ssl_verify
        assert br.api_endpoint == 'test_router'
        assert br.api_action == 'TestRouter'

    def test_routers_make_request_data(self):
        br = ZenossRouter(url, headers, True, 'test_router', 'TestRouter')

        expected = dict(
            action='TestRouter',
            method='TestMethod',
            data=[dict()],
            tid=1,
        )

        request_data = br._make_request_data(
            'TestMethod',
            dict(),
        )

        assert request_data == expected

    def test_routers_router_request(self, responses):
        responses.add(
            responses.POST,
            '{0}/test_router'.format(url),
            json={'result': {'success': True}}
        )

        br = ZenossRouter(url, headers, True, 'test_router', 'TestRouter')

        resp = br._router_request({'data': dict()})
        assert resp['success']

    def test_routers_router_request_login_failure(self, responses):
        responses.add(
            responses.POST,
            '{0}/test_router'.format(url),
            headers={'location': '{0}/login_form'.format(url)},
            status=302,
        )
        responses.add(
            responses.GET,
            '{0}/login_form'.format(url),
            body='',
        )

        br = ZenossRouter(url, headers, True, 'test_router', 'TestRouter')
        with pytest.raises(ZenossAPIClientAuthenticationError, message='API Login Failed'):
            resp = br._router_request({'data': dict()})

    def test_routers_router_request_failure(self, responses):
        responses.add(
            responses.POST,
            '{0}/test_router'.format(url),
            json={'result': {'success': False, 'msg': 'Test failure'}}
        )

        br = ZenossRouter(url, headers, True, 'test_router', 'TestRouter')
        with pytest.raises(ZenossAPIClientError, message='Request failed: Test failure'):
            resp = br._router_request({'data': dict()})

    def test_routers_router_request_no_data(self, responses):
        responses.add(
            responses.POST,
            '{0}/test_router'.format(url),
            json=dict()
        )

        br = ZenossRouter(url, headers, True, 'test_router', 'TestRouter')
        with pytest.raises(ZenossAPIClientError, message='Request failed, no response data returned'):
            resp = br._router_request({'data': dict()})

    def test_routers_router_request_not_ok_status(self, responses):
        responses.add(
            responses.POST,
            '{0}/test_router'.format(url),
            status=404
        )

        br = ZenossRouter(url, headers, True, 'test_router', 'TestRouter')
        with pytest.raises(ZenossAPIClientError, message='Request failed: 404 '):
            resp = br._router_request({'data': dict()})
