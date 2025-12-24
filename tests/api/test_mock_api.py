import requests


def test_mock_api_workflow(monkeypatch, api_url):
    # 1. Mock GET /products
    monkeypatch.setattr(requests, "get", lambda url, **k: type('Mock', (), {
        'status_code': 200,
        'json': lambda: [{"id": 1, "name": "Phone"}]
    }) if "products" in url else type('Mock', (), {
        'status_code': 200,
        'json': lambda: [{"id": 1, "name": "Phone"}]  # Mock for /cart
    }))

    # 2. Mock POST /cart
    monkeypatch.setattr(requests, "post", lambda url, **k: type('Mock', (), {
        'status_code': 201,
        'json': lambda: {"message": "Added"}
    }))

    # Test Fetching
    products = requests.get(f"{api_url}/products")
    assert products.status_code == 200

    # Test Adding
    add_to_cart = requests.post(f"{api_url}/cart", json={"id": 1})
    assert add_to_cart.status_code == 201

    # Test Retrieving cart
    cart_items = requests.get(f"{api_url}/cart")
    assert len(cart_items.json()) > 0