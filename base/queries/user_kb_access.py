from base.database import engine
from sqlalchemy import insert, select, update, delete
from base.models import UserKBAccess, User, KnowledgeBase


def create_accesses(user_id, kb_id, access_level):
    with engine.connect() as conn:
        user_check = conn.execute(select(User).where(User.id == user_id)).first()
        if not user_check:
            return "User not found", 404
        base_check = conn.execute(select(KnowledgeBase).where(KnowledgeBase.id == kb_id)).first()
        if not base_check:
            return "Base not found", 404
        access_check = conn.execute(select(UserKBAccess).where((UserKBAccess.user_id == user_id) & (UserKBAccess.kb_id == kb_id))).first()
        if access_check:
            return "Access already exists", 409
        stmt = insert(UserKBAccess).values(
            [
                {'user_id': user_id, 'kb_id': kb_id, 'access_level': access_level}
            ]
        )
        conn.execute(stmt)
        conn.commit()
        return "Access created", 201


def read_user_kb_accesses():
    with engine.connect() as conn:
        query = select(UserKBAccess).order_by(UserKBAccess.user_id)
        bases = [dict(row) for row in conn.execute(query).mappings()]
        return bases


def update_accesses(user_id, kb_id, access_level):
    with engine.connect() as conn:
        stmt = update(UserKBAccess).where((UserKBAccess.user_id == user_id) & (UserKBAccess.kb_id == kb_id)).values(
            access_level=access_level)
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount


def delete_accesses(user_id, kb_id):
    with engine.connect() as conn:
        stmt = delete(UserKBAccess).where((UserKBAccess.user_id == user_id) & (UserKBAccess.kb_id == kb_id))
        res = conn.execute(stmt)
        conn.commit()
        return res.rowcount

# print(create_accesses(1, 1, 'read'))
