from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username="user", email="user@mail.com", password="minhasenha")
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == "user@mail.com"))

    assert result.username == "user"
