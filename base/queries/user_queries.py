from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import User


def create_users(user):
    with engine.connect() as conn:
        stmt = insert(User).values(
            [
                {'username': user}
            ]
        )
        conn.execute(stmt)
        conn.commit()


def read_users():
    with engine.connect() as conn:
        query = select(User).order_by(User.id)
        users = [dict(row) for row in conn.execute(query).mappings()]
        return users


def update_users(user_id, new_username):
    with engine.connect() as conn:
        stmt = update(User).where(User.id == user_id).values(username=new_username)
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount


def delete_users(user_id):
    with engine.connect() as conn:
        stmt = delete(User).where(User.id == user_id)
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount
