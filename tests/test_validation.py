from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_invalid_url():

    response = client.post(
        "/audit",
        json={
            "url": "abc"
        }
    )

    assert response.status_code == 422