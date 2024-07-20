from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import NodeAttribute, Node, Attribute


def create_node_attributes(node_id, attr_id, condition):
    with engine.connect() as conn:
        node_check = conn.execute(select(Node).where(Node.id == node_id)).first()
        if not node_check:
            return "Node not found", 404
        attr_check = conn.execute(select(Attribute).where(Attribute.id == attr_id)).first()
        if not attr_check:
            return "Attribute not found", 404
        node_attr_check = conn.execute(select(NodeAttribute).where(
            (NodeAttribute.node_id == node_id) & (NodeAttribute.attribute_id == attr_id))).first()
        if node_attr_check:
            return "Node attribute already exists", 409
        stmt = insert(NodeAttribute).values(
            [
                {'node_id': node_id, 'attribute_id': attr_id, 'activation_condition': condition}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "Node attribute created", 201


def read_node_attributes():
    with engine.connect() as conn:
        query = select(NodeAttribute).order_by(NodeAttribute.node_id)
        users = [dict(row) for row in conn.execute(query).mappings()]
        return users


def update_node_attributes(node_id, attr_id, condition):
    with engine.connect() as conn:
        node_check = conn.execute(select(Node).where(Node.id == node_id)).first()
        if not node_check:
            return "Node not found", 404
        attr_check = conn.execute(select(Attribute).where(Attribute.id == attr_id)).first()
        if not attr_check:
            return "Attribute not found", 404
        node_attr_check = conn.execute(select(NodeAttribute).where(
            (NodeAttribute.node_id == node_id) & (NodeAttribute.attribute_id == attr_id))).first()
        if not node_attr_check:
            return "Node attribute not found", 404
        stmt = update(NodeAttribute).where(
            (NodeAttribute.node_id == node_id) & (NodeAttribute.attribute_id == attr_id)).values(
            node_id=node_id, attribute_id=attr_id, activation_condition=condition)
        conn.execute(stmt)
        conn.commit()
        return 'Node attribute updated', 200


def delete_node_attributes(node_id, attr_id):
    with engine.connect() as conn:
        stmt = delete(NodeAttribute).where(
            (NodeAttribute.node_id == node_id) & (NodeAttribute.attribute_id == attr_id)).returning(
            NodeAttribute.node_id)
        res = conn.execute(stmt).scalar()
        if not res:
            return "Node attribute not found", 404
        conn.commit()
        return 'Node attribute deleted', 200
