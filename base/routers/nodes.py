from fastapi import APIRouter, HTTPException
from base.queries.nodes import create_nodes, read_nodes, update_nodes, delete_nodes
from base.models import NodeTypeEnum

router = APIRouter()


@router.get('/nodes')
def read_all_nodes():
    nodes = read_nodes()
    return {'nodes': nodes}


@router.post('/new_node')
def create_new_node(sec_id: int, name: str, node_type: NodeTypeEnum):
    message, status_code = create_nodes(sec_id, name, node_type)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/nodes/{node_id}')
def update_node(node_id: int, sec_id: int, name: str, node_type: NodeTypeEnum):
    message, status_code = update_nodes(node_id, sec_id, name, node_type)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/nodes/{node_id}')
def delete_node(node_id: int):
    message, status_code = delete_nodes(node_id)
    raise HTTPException(status_code=status_code, detail=message)
