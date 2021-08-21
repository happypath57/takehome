# encoding: utf-8
from sqlalchemy import Column, DateTime, Integer, MetaData, SmallInteger, String, Table
from sqlalchemy.dialects.postgresql import TIMESTAMP

metadata = MetaData()


t_letter = Table(
    'letter', metadata,
    Column('id', Integer, nullable=False),
    Column('main_id', Integer),
    Column('letter', String(255)),
    Column('state', SmallInteger),
    Column('created_at', TIMESTAMP(True, 6)),
    Column('updated_at', TIMESTAMP(True, 6)),
    schema='ocr'
)


t_picture = Table(
    'picture', metadata,
    Column('id', Integer, nullable=False),
    Column('url', String(255)),
    Column('file', String(255)),
    Column('state', SmallInteger),
    Column('created_at', TIMESTAMP(True, 6)),
    Column('updated_at', TIMESTAMP(True, 6)),
    Column('filename', String(255)),
    schema='ocr'
)
