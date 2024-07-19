from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import Section, KnowledgeBase


def create_sections(kb_id, name):
    with engine.connect() as conn:
        base_check = conn.execute(select(KnowledgeBase).where(KnowledgeBase.id == kb_id)).first()
        if not base_check:
            return "Base not found", 404
        section_check = conn.execute(select(Section).where((Section.kb_id == kb_id) & (Section.name == name))).first()
        if section_check:
            return "Section already exists", 409
        stmt = insert(Section).values(
            [
                {'kb_id': kb_id, 'name': name}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "Section created", 201


def read_sections():
    with engine.connect() as conn:
        query = select(Section).order_by(Section.id)
        users = [dict(row) for row in conn.execute(query).mappings()]
        return users


def update_sections(sec_id, kb_id, name):
    with engine.connect() as conn:
        base_check = conn.execute(select(KnowledgeBase).where(KnowledgeBase.id == kb_id)).first()
        if not base_check:
            return "Base not found", 404
        section_check = conn.execute(select(Section).where(Section.id == sec_id)).first()
        if not section_check:
            return "Section not found", 404
        stmt = update(Section).where(Section.id == sec_id).values(kb_id=kb_id, name=name)
        conn.execute(stmt)
        conn.commit()
        return 'Section updated', 200


def delete_sections(sec_id):
    with engine.connect() as conn:
        stmt = delete(Section).where(Section.id == sec_id)
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount
