from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import Node, NodeConnection


def create_node_connections(source_id, target_id, conn_type):
    with engine.connect() as conn:
        source_check = conn.execute(select(Node).where(Node.id == source_id)).first()
        if not source_check:
            return "Source not found", 404
        target_check = conn.execute(select(Node).where(Node.id == target_id)).first()
        if not target_check:
            return "Target not found", 404
        connection_check = conn.execute(select(NodeConnection).where(
            (NodeConnection.source_node_id == source_id) & (NodeConnection.target_node_id == target_id))).first()
        if connection_check:
            return "Connection already exists", 409
        stmt = insert(NodeConnection).values(
            [
                {'source_node_id': source_id, 'target_node_id': target_id, 'connection_type': conn_type}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "Node connection created", 201


def read_node_connections():
    with engine.connect() as conn:
        query = select(NodeConnection).order_by(NodeConnection.source_node_id)
        users = [dict(row) for row in conn.execute(query).mappings()]
        return users


def update_node_connections(source_id, target_id, conn_type):
    with engine.connect() as conn:
        source_check = conn.execute(select(Node).where(Node.id == source_id)).first()
        if not source_check:
            return "Source not found", 404
        target_check = conn.execute(select(Node).where(Node.id == target_id)).first()
        if not target_check:
            return "Target not found", 404
        connection_check = conn.execute(select(NodeConnection).where(
            (NodeConnection.source_node_id == source_id) & (NodeConnection.target_node_id == target_id))).first()
        if not connection_check:
            return "Connection not found", 404
        stmt = update(NodeConnection).where(
            (NodeConnection.source_node_id == source_id) & (NodeConnection.target_node_id == target_id)).values(
            source_node_id=source_id, target_node_id=target_id, connection_type=conn_type)
        conn.execute(stmt)
        conn.commit()
        return 'Connection updated', 200


def delete_node_connections(source_id, target_id):
    with engine.connect() as conn:
        stmt = delete(NodeConnection).where(
            (NodeConnection.source_node_id == source_id) & (NodeConnection.target_node_id == target_id))
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount
