from fastapi import APIRouter, HTTPException
from base.queries.node_connections import create_node_connections, read_node_connections, \
    update_node_connections, delete_node_connections
from base.models import ConnectionTypeEnum

router = APIRouter()


@router.get('/node_connections')
def read_all_node_connections():
    connections = read_node_connections()
    return {'connections': connections}


@router.post('/new_connection')
def create_new_node_connection(source_id: int, target_id: int, conn_type: ConnectionTypeEnum):
    message, status_code = create_node_connections(source_id, target_id, conn_type)
    raise HTTPException(status_code=status_code, detail=message)


@router.put('/node_connections/{source_id}')
def update_node_connection(source_id: int, target_id: int, conn_type: ConnectionTypeEnum):
    message, status_code = update_node_connections(source_id, target_id, conn_type)
    raise HTTPException(status_code=status_code, detail=message)


@router.delete('/node_connections/{source_id}')
def delete_node_connection(source_id: int, target_id: int):
    message, status_code = delete_node_connections(source_id, target_id)
    raise HTTPException(status_code=status_code, detail=message)
