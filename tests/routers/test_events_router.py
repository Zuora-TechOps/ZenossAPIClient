import json
import pytest
from zenossapi.apiclient import ZenossAPIClientError
from zenossapi.routers.events import EventsRouter, ZenossEvent
import events_resp

pytest_plugins = "pytest-responses"
url = 'https://zenoss/zport/dmd'
headers = dict(
    ContentType='application/json'
)


def request_callback(request):
    rdata = json.loads(request.body)
    resp_headers = dict(ContentType='application/json')

    def query(rdata):
        if rdata['keys'] and rdata['keys'][0] == "evid":
            if 'params' in rdata and 'summary' in rdata['params'] and rdata['params']['summary'] == "Out of Tea":
                return events_resp.add_event_evid_query
            else:
                return events_resp.events_query_evid
        else:
            return events_resp.events_query

    def detail(rdata):
        if rdata['evid'] == "02420a11-0015-98b9-11e7-9d96ae351999":
            return events_resp.event_detail
        elif rdata['evid'] == "02420a11-000c-a561-11e7-ba9b510182b3":
            return events_resp.add_event_detail
        else:
            return events_resp.fail

    def getConfig(rdata):
        return events_resp.events_config

    if rdata['method'] in ['close', 'acknowledge', 'reopen',
                           'setConfigValues', 'add_event',
                           'clear_heartbeats', 'clear_heartbeat',
                           'write_log']:
        resp_body = events_resp.success
    else:
        method = locals()[rdata['method']]
        resp_body = method(rdata['data'][0])

    return (200, resp_headers, json.dumps(resp_body))


def responses_callback(responses):
    responses.add_callback(
        responses.POST,
        '{0}/evconsole_router'.format(url),
        callback=request_callback,
        content_type='application/json',
    )


class TestEventsRouter(object):

    def test_events_router_init(self):
        er = EventsRouter(url, headers, True)
        assert er.evid is None
        assert isinstance(er.event_states_map, dict)
        assert er.event_states_map['Acknowledged'] == 1
        assert isinstance(er.event_severity_map, dict)
        assert er.event_severity_map['Critical'] == 5

    def test_events_router_query_events(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er._query_events(limit=2)
        assert resp['total'] == 50
        assert resp['ts'] == 1508797504.409547
        assert len(resp['events']) == 1
        assert resp['events'][0]['eventState'] == "Acknowledged"

    def test_events_router_get_details_by_evid(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er._get_details_by_evid("02420a11-0015-98b9-11e7-9d96ae351999")
        assert resp['agent'] == "zenpython"
        assert resp['device_uuid'] == "02e21618-b30a-47bf-8591-471c70570932"

    def test_events_router_get_details_by_evid_not_found(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        with pytest.raises(
            ZenossAPIClientError,
            match="Request failed: ServiceResponseError: Not Found"
        ):
            resp = er._get_details_by_evid(
                "02420a11-0015-98b9-11e7-9d96ae35199f"
            )

    def test_events_router_event_actions(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er._event_actions('acknowledge', evids=["02420a11-0015-98b9-11e7-9d96ae351999"])

    def test_events_router_event_actions_invalid(self):
        er = EventsRouter(url, headers, True)
        with pytest.raises(
            ZenossAPIClientError,
            match="Unknown event action: terminate"
        ):
            er._event_actions('terminate')

    def test_events_router_get_config(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.get_config()
        assert len(resp) == 2
        assert resp[0]['id'] == "event_age_disable_severity"

    def test_events_router_update_config(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.update_config(dict(event_age_disable_severity=3))
        assert resp

    def test_events_router_get_event_by_evid(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.get_event_by_evid("02420a11-0015-98b9-11e7-9d96ae351999")
        assert isinstance(resp, ZenossEvent)
        assert resp.evid == "02420a11-0015-98b9-11e7-9d96ae351999"

    def test_events_router_list_open_events(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.list_open_events()
        assert len(resp['events']) == 1
        assert resp['total'] == 50
        assert resp['events'][0]['evid'] == "02420a11-0015-98b9-11e7-9d96ae351999"

    def test_events_router_get_open_events(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.get_open_events()
        assert isinstance(resp[0], ZenossEvent)

    def test_events_router_list_open_production_events(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.list_open_production_events()
        assert len(resp['events']) == 1
        assert resp['total'] == 50
        assert resp['events'][0]['evid'] == "02420a11-0015-98b9-11e7-9d96ae351999"

    def test_events_router_get_open_production_events(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.get_open_production_events()
        assert isinstance(resp[0], ZenossEvent)

    def test_events_router_add_event(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.add_event(
            "Out of Tea",
            "Heart of Gold",
            3,
            component="Arthur Dent"
        )
        assert isinstance(resp, ZenossEvent)
        assert resp.evid == "02420a11-000c-a561-11e7-ba9b510182b3"

    def test_events_router_add_event_retry(self, responses):
        # First response, adding the event.
        responses.add(
            responses.POST,
            '{0}/evconsole_router'.format(url),
            json=events_resp.success
        )

        # Second response, event not fully created.
        responses.add(
            responses.POST,
            '{0}/evconsole_router'.format(url),
            json=events_resp.success
        )

        # Third response, event now created.
        responses.add(
            responses.POST,
            '{0}/evconsole_router'.format(url),
            json=events_resp.add_event_evid_query
        )

        # Finally, event detail
        responses.add(
            responses.POST,
            '{0}/evconsole_router'.format(url),
            json=events_resp.add_event_detail
        )

        er = EventsRouter(url, headers, True)
        resp = er.add_event(
            "Out of Tea",
            "Heart of Gold",
            3,
            component="Arthur Dent"
        )
        assert isinstance(resp, ZenossEvent)
        assert resp.evid == "02420a11-000c-a561-11e7-ba9b510182b3"

    def test_events_router_clear_heartbeats(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.clear_heartbeats()
        assert resp

    def test_events_router_clear_heartbeat(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        resp = er.clear_heartbeat(
            collector='localhost',
            daemon='zenpython'
        )
        assert resp

    def test_events_router_zenossevent_update_log(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        ev = er.get_event_by_evid("02420a11-000c-a561-11e7-ba9b510182b3")
        ev.log = []
        ev.update_log('Test log entry')
        assert len(ev.log) == 1
        assert ev.log[0][0] == "zenoss"

    def test_events_router_zenossevent_close(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        ev = er.get_event_by_evid("02420a11-000c-a561-11e7-ba9b510182b3")
        resp = ev.close()
        assert resp

    def test_events_router_zenossevent_ack(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        ev = er.get_event_by_evid("02420a11-000c-a561-11e7-ba9b510182b3")
        resp = ev.ack()
        assert resp

    def test_events_router_zenossevent_reopen(self, responses):
        responses_callback(responses)

        er = EventsRouter(url, headers, True)
        ev = er.get_event_by_evid("02420a11-000c-a561-11e7-ba9b510182b3")
        resp = ev.reopen()
        assert resp
