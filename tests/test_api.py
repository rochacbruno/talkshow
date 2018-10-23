def test_can_create_event(client, auth):
    """Asserts an event can be created via API"""
    event_data = {"name": "Puggies Convention", "date": "2018-09-09"}
    created = client.post('/api/v1/event/', json=event_data, headers=auth)
    assert created.status_code == 201


def test_can_list_event(client):
    """Asserts event can be listed"""
    events = client.get('/api/v1/event/')
    assert events.status_code == 200
    assert 'events' in events.json


def test_can_get_event_create(client):
    events = client.get('/api/v1/event/puggies-convention')
    assert events.status_code == 200


def test_can_create_proposal_in_event(client, app):
    proposal_event_data = {"name": "Emma Smith ",
                           "email": "emma_smith@mail.com",
                           "title": "Tutorial Flask",
                           "description": "A simple base app as "
                                          "example of Flask Architecture"}
    events = client.post(f"/api/v1/event/{app.db['events'].find_one()['_id']}",
                         json=proposal_event_data)
    assert events.status_code == 201
    assert 'proposal created' in events.json
