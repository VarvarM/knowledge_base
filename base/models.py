from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()


class AccessLevelEnum(enum.Enum):
    read = "read"
    write = "write"


class NodeTypeEnum(enum.Enum):
    FEATURE = "FEATURE"
    HYPOTHESIS = "HYPOTHESIS"
    AND = "AND"
    OR = "OR"


class AttributeTypeEnum(enum.Enum):
    range = "range"
    discrete = "discrete"
    string = "string"


class ConnectionTypeEnum(enum.Enum):
    TRA = "TRA"
    RS = "RS"
    S = "S"
    SN = "SN"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)


class KnowledgeBase(Base):
    __tablename__ = "knowledge_bases"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)


class UserKBAccess(Base):
    __tablename__ = "user_kb_access"
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    kb_id = Column(Integer, ForeignKey('knowledge_bases.id'), primary_key=True)
    access_level = Column(Enum(AccessLevelEnum), nullable=False)


class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    kb_id = Column(Integer, ForeignKey('knowledge_bases.id'), nullable=False)
    name = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('kb_id', 'name'),)


class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey('sections.id'), nullable=False)
    name = Column(String(255), nullable=False)
    node_type = Column(Enum(NodeTypeEnum), nullable=False)


class Attribute(Base):
    __tablename__ = "attributes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(Enum(AttributeTypeEnum), nullable=False)
    value_area = Column(String, nullable=False)


class NodeAttribute(Base):
    __tablename__ = "node_attributes"
    node_id = Column(Integer, ForeignKey('nodes.id'), primary_key=True)
    attribute_id = Column(Integer, ForeignKey('attributes.id'), primary_key=True)
    activation_condition = Column(String)


class NodeConnection(Base):
    __tablename__ = "node_connections"
    source_node_id = Column(Integer, ForeignKey('nodes.id'), nullable=False, primary_key=True)
    target_node_id = Column(Integer, ForeignKey('nodes.id'), nullable=False, primary_key=True)
    connection_type = Column(Enum(ConnectionTypeEnum), nullable=False, primary_key=True)
