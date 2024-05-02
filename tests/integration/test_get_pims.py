def test_get_model(client):
    response = client.get("/api/model/get-pims")
    assert response.status_code == 200