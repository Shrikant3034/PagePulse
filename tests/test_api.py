from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["project"] == "Page Pulse"


def test_audit():
    response = client.post(
        "/audit",
        json={
            "url": "https://example.com"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True

    assert body["data"]["status_code"] == 200