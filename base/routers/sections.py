from fastapi import APIRouter, HTTPException
from base.queries.sections import create_sections, read_sections, update_sections, delete_sections

router = APIRouter()


@router.get('/sections')
def read_all_sections():
    sections = read_sections()
    return {'sections': sections}


@router.post('/new_section')
def create_new_section(kb_id: int, name: str):
    message, status_code = create_sections(kb_id, name)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/sections/{sec_id}')
def update_section(sec_id: int, kb_id: int, name: str):
    message, status_code = update_sections(sec_id, kb_id, name)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/sections/{sec_id}')
def delete_section(sec_id: int):
    message, status_code = delete_sections(sec_id)
    raise HTTPException(status_code=status_code, detail=message)
