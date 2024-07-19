from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import Attribute


def create_attributes(name, type, value_area):
    with engine.connect() as conn:
        stmt = insert(Attribute).values(
            [
                {'name': name, 'type': type, 'value_area': value_area}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "Attribute created", 201


def read_attributes():
    with engine.connect() as conn:
        query = select(Attribute).order_by(Attribute.id)
        users = [dict(row) for row in conn.execute(query).mappings()]
        return users


def update_attributes(attr_id, name, type, value_area):
    with engine.connect() as conn:
        attr_check = conn.execute(select(Attribute).where(Attribute.id == attr_id)).first()
        if not attr_check:
            return "Attribute not found", 404
        stmt = update(Attribute).where(Attribute.id == attr_id).values(name=name, type=type, value_area=value_area)
        conn.execute(stmt)
        conn.commit()
        return 'Attribute updated', 200


def delete_attributes(attr_id):
    with engine.connect() as conn:
        stmt = delete(Attribute).where(Attribute.id == attr_id)
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount
