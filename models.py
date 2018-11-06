from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    character = Column(String, nullable=False)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actors = relationship('Actor', secondary='actor_roles')

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    roles = relationship('Role', secondary='actor_roles')

class ActorRole(Base):
    __tablename__ = "actor_roles"
    role_id= Column(Integer, ForeignKey('roles.id'),primary_key=True)
    actor_id = Column(Integer, ForeignKey('actors.id'),primary_key=True)




engine = create_engine('sqlite:///movies.db')
Base.metadata.create_all(engine)
