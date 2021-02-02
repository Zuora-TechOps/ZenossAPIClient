import pytest
from zenossapi import apiclient as zapi
from zenossapi.routers.events import EventsRouter

host = 'https://zenoss'
user = 'admin'
password = 'zenoss'
collection_zone = 'cz1'
api_key = 'a594730e-293c-4d32-915e-edf43aa9bae8'


class TestZenossClient(object):

    def test_client_init(self):
        zc = zapi.Client(host=host, user=user, password=password)
        assert zc.api_url == '{0}/zport/dmd'.format(host)
        assert 'authorization' in zc.api_headers
        assert zc.ssl_verify

        zc = zapi.Client(host=host, collection_zone=collection_zone, api_key=api_key)
        assert zc.api_url == '{0}/{1}/zport/dmd'.format(host, collection_zone)
        assert 'z-api-key' in zc.api_headers
        assert zc.ssl_verify

    def test_client_get_routers(self):
        zc = zapi.Client(host=host, user=user, password=password)
        zc.get_routers()

    def test_client_get_router(self):
        zc = zapi.Client(host=host, user=user, password=password)
        device_router = zc.get_router('events')
        assert isinstance(device_router, EventsRouter)
