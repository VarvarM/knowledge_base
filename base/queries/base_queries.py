from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import KnowledgeBase


def create_knowledge_bases(base, description):
    with engine.connect() as conn:
        stmt = insert(KnowledgeBase).values(
            [
                {'name': base, 'description': description}
            ]
        )
        conn.execute(stmt)
        conn.commit()


def read_knowledge_bases():
    with engine.connect() as conn:
        query = select(KnowledgeBase).order_by(KnowledgeBase.id)
        bases = [dict(row) for row in conn.execute(query).mappings()]
        return bases


def update_bases(base_id, base_name, description):
    with engine.connect() as conn:
        stmt = update(KnowledgeBase).where(KnowledgeBase.id == base_id).values(name=base_name, description=description)
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount


def delete_bases(base_id):
    with engine.connect() as conn:
        stmt = delete(KnowledgeBase).where(KnowledgeBase.id == base_id)
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount
