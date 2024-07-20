from fastapi import APIRouter, HTTPException
from base.queries.knowledge_bases import read_knowledge_bases, create_knowledge_bases, update_bases, delete_bases

router = APIRouter()


@router.get('/knowledge_bases')
def read_all_bases():
    bases = read_knowledge_bases()
    return {'bases': bases}


@router.post('/new_base')
def create_new_base(base: str, description: str = None):
    message, status_code = create_knowledge_bases(base, description)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/knowledge_bases/{base_id}')
def update_base(base_id: int, name: str, description: str = None):
    message, status_code = update_bases(base_id, name, description)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/knowledge_bases/{base_id}')
def delete_base(base_id: int):
    message, status_code = delete_bases(base_id)
    raise HTTPException(status_code=status_code, detail=message)
