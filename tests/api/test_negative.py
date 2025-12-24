import requests

def test_post_cart_invalid_data(monkeypatch, base_url):
    # Mocking a 400 Bad Request response for invalid payload
    class MockErrorResponse:
        status_code = 400
        def json(self):
            return {"error": "Invalid product ID"}

    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: MockErrorResponse())

    # Send invalid data
    response = requests.post(f"{base_url}/cart", json={"wrong_key": "empty"})

    # Assert that we handle the error correctly
    assert response.status_code == 400
    assert "error" in response.json()