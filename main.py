from dotenv import load_dotenv
from fastapi import FastAPI
from base.routers import users, knowledge_bases, user_kb_access, sections, nodes, node_attributes, node_connections, \
    attributes

load_dotenv()
app = FastAPI()

app.include_router(users.router)
app.include_router(knowledge_bases.router)
app.include_router(user_kb_access.router)
app.include_router(sections.router)
app.include_router(nodes.router)
app.include_router(node_attributes.router)
app.include_router(node_connections.router)
app.include_router(attributes.router)
