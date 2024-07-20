from fastapi import APIRouter, HTTPException
from base.queries.users import read_users, create_users, update_users, delete_users

router = APIRouter()


@router.get('/users')
def read_all_users():
    users = read_users()
    return {'users': users}


@router.post('/new_user')
def create_new_user(user: str):
    message, status_code = create_users(user)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/users/{user_id}')
def update_user(user_id: int, username: str):
    message, status_code = update_users(user_id, username)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/users/{user_id}')
def delete_user(user_id: int):
    message, status_code = delete_users(user_id)
    raise HTTPException(status_code=status_code, detail=message)
