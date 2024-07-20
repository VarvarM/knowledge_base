from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import Node, Section, NodeAttribute, NodeConnection


def create_nodes(sec_id, name, node_type):
    with engine.connect() as conn:
        section_check = conn.execute(select(Section).where(Section.id == sec_id)).first()
        if not section_check:
            return "Section not found", 404
        stmt = insert(Node).values(
            [
                {'section_id': sec_id, 'name': name, 'node_type': node_type}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "Node created", 201


def read_nodes():
    with engine.connect() as conn:
        query = select(Node).order_by(Node.id)
        users = [dict(row) for row in conn.execute(query).mappings()]
        return users


def update_nodes(node_id, sec_id, name, node_type):
    with engine.connect() as conn:
        node_check = conn.execute(select(Node).where(Node.id == node_id)).first()
        if not node_check:
            return "Node not found", 404
        section_check = conn.execute(select(Section).where(Section.id == sec_id)).first()
        if not section_check:
            return "Section not found", 404
        stmt = update(Node).where(Node.id == node_id).values(section_id=sec_id, name=name, node_type=node_type)
        conn.execute(stmt)
        conn.commit()
        return 'Node updated', 200


def delete_nodes(node_id):
    with engine.connect() as conn:
        node_check = conn.execute(select(Node).where(Node.id == node_id)).first()
        if not node_check:
            return "Node not found", 404
        conn.execute(delete(NodeConnection).where(NodeConnection.source_node_id == node_id))
        conn.execute(delete(NodeConnection).where(NodeConnection.target_node_id == node_id))
        conn.execute(delete(NodeAttribute).where(NodeAttribute.node_id == node_id))
        stmt = delete(Node).where(Node.id == node_id)
        conn.execute(stmt)
        conn.commit()
        return "Node deleted", 200
