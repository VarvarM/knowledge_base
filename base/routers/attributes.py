from fastapi import APIRouter, HTTPException
from base.queries.attributes import create_attributes, read_attributes, update_attributes, delete_attributes
from base.models import AttributeTypeEnum

router = APIRouter()


@router.get('/attributes')
def read_all_attributes():
    attributes = read_attributes()
    return {'attributes': attributes}


@router.post('/new_attribute')
def create_new_attribute(name: str, type: AttributeTypeEnum, value_area: str):
    message, status_code = create_attributes(name, type, value_area)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/attributes/{attr_id}')
def update_attribute(attr_id: int, name: str, type: AttributeTypeEnum, value_area: str):
    message, status_code = update_attributes(attr_id, name, type, value_area)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/attributes/{attr_id}')
def delete_attribute(attr_id: int):
    message, status_code = delete_attributes(attr_id)
    raise HTTPException(status_code=status_code, detail=message)
