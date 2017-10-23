import pytest
from zenossapi import apiclient as zapi
from zenossapi.routers.events import EventsRouter

host = 'zenoss'
user = 'admin'
password = 'zenoss'


class TestZenossClient(object):

    def test_client_init(self):
        zc = zapi.Client(host=host, user=user, password=password)
        assert zc.api_host == host
        assert zc.api_url == 'https://{0}/zport/dmd'.format(host)
        assert zc.api_user == user
        assert zc.ssl_verify

    def test_client_get_routers(self):
        zc = zapi.Client(host=host, user=user, password=password)
        zc.get_routers()

    def test_client_get_router(self):
        zc = zapi.Client(host=host, user=user, password=password)
        device_router = zc.get_router('events')
        assert isinstance(device_router, EventsRouter)
