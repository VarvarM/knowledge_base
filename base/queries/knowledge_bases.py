from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import KnowledgeBase, Section, UserKBAccess


def create_knowledge_bases(base, description):
    with engine.connect() as conn:
        name_check = conn.execute(select(KnowledgeBase).where(KnowledgeBase.name == base)).first()
        if name_check:
            return "Knowledge base already exists", 409
        stmt = insert(KnowledgeBase).values(
            [
                {'name': base, 'description': description}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "Knowledge base created", 201


def read_knowledge_bases():
    with engine.connect() as conn:
        query = select(KnowledgeBase).order_by(KnowledgeBase.id)
        bases = [dict(row) for row in conn.execute(query).mappings()]
        return bases


def update_bases(base_id, base_name, description):
    with engine.connect() as conn:
        base_check = conn.execute(select(KnowledgeBase).where(KnowledgeBase.id == base_id)).first()
        if not base_check:
            return "Knowledge base not found", 404
        existing_base = conn.execute(select(KnowledgeBase).where(KnowledgeBase.name == base_name)).first()
        if existing_base and existing_base.id != base_id:
            return "Knowledge base name already taken", 400
        stmt = update(KnowledgeBase).where(KnowledgeBase.id == base_id).values(name=base_name, description=description)
        conn.execute(stmt)
        conn.commit()
        return "Knowledge base updated", 200


def delete_bases(base_id):
    with engine.connect() as conn:
        base_check = conn.execute(select(KnowledgeBase).where(KnowledgeBase.id == base_id)).first()
        if not base_check:
            return "Knowledge base not found", 404
        conn.execute(delete(Section).where(Section.kb_id == base_id))
        conn.execute(delete(UserKBAccess).where(UserKBAccess.kb_id == base_id))
        stmt = delete(KnowledgeBase).where(KnowledgeBase.id == base_id)
        conn.execute(stmt)
        conn.commit()
        return "Knowledge base deleted", 200
