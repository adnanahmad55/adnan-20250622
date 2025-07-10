from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)

    workspaces = relationship("Workspace", back_populates="user")


class Workspace(Base):
    __tablename__ = "workspace"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(Text)
    progress = Column(Integer)
    priority_keywords = Column(ARRAY(Text))
    root_node = Column(String)

    user = relationship("User", back_populates="workspaces")
    modules = relationship("Module", back_populates="workspace")


class Module(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey("workspace.id"))
    epic = Column(String)
    completed_resources = Column(ARRAY(Text))
    explorations = Column(ARRAY(Text))
    is_completed = Column(Boolean, default=False)
    tag = Column(String)

    workspace = relationship("Workspace", back_populates="modules")
