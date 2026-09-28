from unittest.mock import MagicMock
from src.database.models import User


def test_create_user(client, user, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)

    response = client.post(
        "/api/auth/signup",
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    if "user" in data:
        assert data["user"]["email"] == user.get("email")
    else:
        assert data["email"] == user.get("email")


def test_repeat_create_user(client, user):
    response = client.post(
        "/api/auth/signup",
        json=user,
    )
    assert response.status_code == 409, response.text
    data = response.json()
    assert "detail" in data


def test_login_user_not_confirmed(client, user):
    response = client.post(
        "/api/auth/login",
        data={"username": user.get("email"), "password": user.get("password")},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] in ["Email not confirmed", "Invalid email"]


def test_login_user(client, user, session):
    current_user = session.query(User).filter(User.email == user.get("email")).first()
    current_user.confirmed = True
    session.commit()

    response = client.post(
        "/api/auth/login",
        data={"username": user.get("email"), "password": user.get("password")},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client, user):
    response = client.post(
        "/api/auth/login",
        data={"username": user.get("email"), "password": "wrongpassword"},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] in ["Invalid password", "Invalid email"]


def test_login_wrong_email(client, user):
    response = client.post(
        "/api/auth/login",
        data={"username": "wrongemail@example.com", "password": user.get("password")},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] in ["Invalid email", "Invalid password"]
