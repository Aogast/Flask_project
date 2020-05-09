import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase, create_session


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telefon = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, nullable=True)
    surgeter = sqlalchemy.Column(sqlalchemy.String,
                              index=True, nullable=True)
    cv = sqlalchemy.Column(sqlalchemy.Integer,
                           index=True, nullable=True)
    kindofcook = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    amount = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    comment = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    time = sqlalchemy.Column(sqlalchemy.String, nullable=True)


