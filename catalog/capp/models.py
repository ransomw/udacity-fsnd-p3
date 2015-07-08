from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text

import sqlalchemy.sql.functions as func

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(500), nullable=True)


class Category(Base):
    __tablename__ = 'category'
    id = Column(
        Integer, primary_key=True)
    name = Column(
        String(80), nullable=False, unique=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


class Item(Base):
    __tablename__ = 'item'
    id = Column(
        Integer, primary_key=True)
    # must be unique due to url scheme for edit/delete
    title = Column(String(80), unique=True)
    # todo: use Text type
    description = Column(String(250))
    category_id = Column(
        Integer, ForeignKey('category.id'), nullable=False)
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    last_update = Column(
        DateTime, server_default=func.now(),
        onupdate=func.now())

    @property
    def serialize(self):
        return {
            'cat_id': self.category_id,
            'description': self.description,
            'id': self.id,
            'title': self.title,
        }

engine = create_engine(
    'sqlite:///catalogapp.db')

Base.metadata.create_all(engine)
