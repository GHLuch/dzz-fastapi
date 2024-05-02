def test_create_model(client):
    response = client.get("/api/model/get-models")
    assert response.status_code == 200
    models = response.json()["models"]
    print(models)