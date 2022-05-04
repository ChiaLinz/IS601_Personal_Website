def test_request_homepage_content(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'Home' in response.data