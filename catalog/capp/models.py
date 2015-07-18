from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text

import sqlalchemy.sql.functions as func

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

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

    def __str__(self):
        return self.name

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
    category = relationship(Category, cascade="delete")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    last_update = Column(
        DateTime, server_default=func.now(),
        onupdate=func.now())

    @validates('description')
    def validate_description(self, key, description):
        if description == '':
            raise ValueError(
                "may not have empty description")
        return description

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

# ??? is it appropriate to initialize a DB session here?
# I want to use the same session in both the view and view_helper
# modules but avoid circular imports
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
