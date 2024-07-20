from fastapi import APIRouter, HTTPException
from base.queries.node_attributes import create_node_attributes, read_node_attributes, update_node_attributes, \
    delete_node_attributes

router = APIRouter()


@router.get('/node_attributes')
def read_all_node_attributes():
    node_attributes = read_node_attributes()
    return {'node_attributes': node_attributes}


@router.post('/new_node_attribute')
def create_new_node_attribute(node_id: int, attr_id: int, condition: str = None):
    message, status_code = create_node_attributes(node_id, attr_id, condition)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/node_attributes/{node_id}')
def update_node_attribute(node_id: int, attr_id: int, condition: str = None):
    message, status_code = update_node_attributes(node_id, attr_id, condition)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/node_attributes/{node_id}')
def delete_node_attribute(node_id: int, attr_id: int):
    message, status_code = delete_node_attributes(node_id, attr_id)
    raise HTTPException(status_code=status_code, detail=message)
