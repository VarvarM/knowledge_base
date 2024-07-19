from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from base.models import AccessLevelEnum, NodeTypeEnum, ConnectionTypeEnum
from base.database import SessionLocal
from base.queries.user_queries import read_users, update_users, delete_users, create_users
from base.queries.base_queries import create_knowledge_bases, update_bases, delete_bases, read_knowledge_bases
from base.queries.user_kb_access import create_accesses, read_user_kb_accesses, update_accesses, delete_accesses
from base.queries.sections_queries import create_sections, read_sections, update_sections, delete_sections
from base.queries.nodes_queries import create_nodes, read_nodes, update_nodes, delete_nodes
from base.queries.node_connections_queries import create_node_connections, read_node_connections, \
    update_node_connections, delete_node_connections

load_dotenv()
app = FastAPI()


# Зависимость для получения сессии базы данных
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get('/users')
def read_all_users():
    users = read_users()
    return {'users': users}


@app.post('/new_user')
def create_new_user(user: str):
    create_users(user)
    return {'ok': 'True'}


@app.put('/users/{user_id}')
def update_user(user_id: int, username: str):
    res = update_users(user_id, username)
    if res == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {'ok': 'True'}


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    res = delete_users(user_id)
    if res == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {'ok': 'True'}


@app.get('/knowledge_bases')
def read_all_bases():
    bases = read_knowledge_bases()
    return {'bases': bases}


@app.post('/new_base')
def create_new_base(base: str, description: str = None):
    create_knowledge_bases(base, description)
    return {'ok': 'True'}


@app.put('/knowledge_bases/{base_id}')
def update_base(base_id: int, name: str, description: str = None):
    res = update_bases(base_id, name, description)
    if res == 0:
        raise HTTPException(status_code=404, detail="Base not found")
    return {'ok': 'True'}


@app.delete('/knowledge_bases/{base_id}')
def delete_base(base_id: int):
    res = delete_bases(base_id)
    if res == 0:
        raise HTTPException(status_code=404, detail="Base not found")
    return {'ok': 'True'}


@app.get('/user_kb_access')
def read_all_accesses():
    accesses = read_user_kb_accesses()
    return {'accesses': accesses}


@app.post('/new_access')
def create_new_access(user_id: int, kb_id: int, access_level: AccessLevelEnum):
    message, status_code = create_accesses(user_id, kb_id, access_level)
    raise HTTPException(status_code=status_code, detail=message)


@app.put('/user_kb_access/{user_id}')
def update_access(user_id: int, kb_id: int, access_level: AccessLevelEnum):
    res = update_accesses(user_id, kb_id, access_level)
    if res == 0:
        raise HTTPException(status_code=404, detail="Access not found")
    return {'ok': 'True'}


@app.delete('/user_kb_access/{user_id}')
def delete_access(user_id: int, kb_id: int):
    res = delete_accesses(user_id, kb_id)
    if res == 0:
        raise HTTPException(status_code=404, detail="Access not found")
    return {'ok': 'True'}


@app.get('/sections')
def read_all_sections():
    sections = read_sections()
    return {'sections': sections}


@app.post('/new_section')
def create_new_section(kb_id: int, name: str):
    message, status_code = create_sections(kb_id, name)
    raise HTTPException(status_code=status_code, detail=message)


@app.put('/sections/{sec_id}')
def update_section(sec_id: int, kb_id: int, name: str):
    message, status_code = update_sections(sec_id, kb_id, name)
    raise HTTPException(status_code=status_code, detail=message)


@app.delete('/sections/{sec_id}')
def delete_section(sec_id: int):
    res = delete_sections(sec_id)
    if res == 0:
        raise HTTPException(status_code=404, detail="Section not found")
    return {'ok': 'True'}


@app.get('/nodes')
def read_all_nodes():
    nodes = read_nodes()
    return {'nodes': nodes}


@app.post('/new_node')
def create_new_node(sec_id: int, name: str, node_type: NodeTypeEnum):
    message, status_code = create_nodes(sec_id, name, node_type)
    raise HTTPException(status_code=status_code, detail=message)


@app.put('/nodes/{node_id}')
def update_node(node_id: int, sec_id: int, name: str, node_type: NodeTypeEnum):
    message, status_code = update_nodes(node_id, sec_id, name, node_type)
    raise HTTPException(status_code=status_code, detail=message)


@app.delete('/nodes/{node_id}')
def delete_node(node_id: int):
    res = delete_nodes(node_id)
    if res == 0:
        raise HTTPException(status_code=404, detail="Node not found")
    return {'ok': 'True'}


@app.get('/node_connections')
def read_all_node_connections():
    connections = read_node_connections()
    return {'connections': connections}


@app.post('/new_connection')
def create_new_node_connection(source_id: int, target_id: int, conn_type: ConnectionTypeEnum):
    message, status_code = create_node_connections(source_id, target_id, conn_type)
    raise HTTPException(status_code=status_code, detail=message)


@app.put('/node_connections/{source_id}')
def update_node_connection(source_id: int, target_id: int, conn_type: ConnectionTypeEnum):
    message, status_code = update_node_connections(source_id, target_id, conn_type)
    raise HTTPException(status_code=status_code, detail=message)


@app.delete('/node_connections/{source_id}')
def delete_node(source_id: int, target_id: int):
    res = delete_node_connections(source_id, target_id)
    if res == 0:
        raise HTTPException(status_code=404, detail="Connection not found")
    return {'ok': 'True'}
