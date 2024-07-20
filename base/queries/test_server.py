from base.test_database import engine_test
from sqlalchemy import insert, select, update, delete, text
from base.models import User

query_test = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);
"""


def test_create():
    with engine_test.connect() as conn:
        conn.execute(text(query_test))
        conn.commit()
    print('Table created')


def insert_test(username):
    insert_query = """
    INSERT INTO users (username) VALUES (:username);
    """
    with engine_test.connect() as conn:
        conn.execute(text(insert_query), {"username": username})
        conn.commit()
    print(f"User '{username}' inserted successfully.")


def test_read():
    with engine_test.connect() as conn:
        res = conn.execute(text('SELECT * FROM users;'))
        print(f'{res.all()=}')


test_create()
insert_test("artem")
test_read()
