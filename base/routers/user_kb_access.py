from fastapi import APIRouter, HTTPException
from base.queries.user_kb_access import read_user_kb_accesses, create_accesses, update_accesses, delete_accesses
from base.models import AccessLevelEnum

router = APIRouter()


@router.get('/user_kb_access')
def read_all_accesses():
    accesses = read_user_kb_accesses()
    return {'accesses': accesses}


@router.post('/new_access')
def create_new_access(user_id: int, kb_id: int, access_level: AccessLevelEnum):
    message, status_code = create_accesses(user_id, kb_id, access_level)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/user_kb_access/{user_id}')
def update_access(user_id: int, kb_id: int, access_level: AccessLevelEnum):
    message, status_code = update_accesses(user_id, kb_id, access_level)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/user_kb_access/{user_id}')
def delete_access(user_id: int, kb_id: int):
    message, status_code = delete_accesses(user_id, kb_id)
    raise HTTPException(status_code=status_code, detail=message)
