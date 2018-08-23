

def test_can_create_event(app, auth):
    """Asserts an event can be created via API"""
    event_data = {"name": "Puggies Convention", "date": "2018-09-09"}
    with app.test_client() as client:
        created = client.post('/api/v1/event/', json=event_data, headers=auth)
        assert created.status_code == 201


def test_can_list_event(app):
    """Asserts event can be listed"""
    with app.test_client() as client:
        events = client.get('/api/v1/event/')
        assert events.status_code == 200
        assert 'events' in events.json
