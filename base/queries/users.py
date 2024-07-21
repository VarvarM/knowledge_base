from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import User, UserKBAccess


def create_users(user):
    with engine.connect() as conn:
        name_check = conn.execute(select(User).where(User.username == user)).first()
        if name_check:
            return "User already exists", 409
        stmt = insert(User).values(
            [
                {'username': user}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "User created", 201


def read_users():
    with engine.connect() as conn:
        query = select(User).order_by(User.id)
        users = [dict(row) for row in conn.execute(query).mappings()]
        return users


def update_users(user_id, new_username):
    with engine.connect() as conn:
        user_check = conn.execute(select(User).where(User.id == user_id)).first()
        if not user_check:
            return "User not found", 404
        existing_user = conn.execute(select(User).where(User.username == new_username)).first()
        if existing_user and existing_user.id != user_id:
            return "Username already taken", 400
        stmt = update(User).where(User.id == user_id).values(username=new_username)
        conn.execute(stmt)
        conn.commit()
        return "User updated", 200


def delete_users(user_id):
    with engine.connect() as conn:
        user_check = conn.execute(select(User).where(User.id == user_id)).first()
        if not user_check:
            return "User not found", 404
        conn.execute(delete(UserKBAccess).where(UserKBAccess.user_id == user_id))
        stmt = delete(User).where(User.id == user_id)
        conn.execute(stmt)
        conn.commit()
        return "User deleted", 200
