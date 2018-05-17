""" Module for the products database object """

# coding=utf-8

from marshmallow_jsonapi import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .entity import Entity, Base
from .detail import DetailSchema


association_table = Table('products_details', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('detail_id', Integer, ForeignKey('details.id'))
)

class Product(Entity, Base):
    """ Class to interact with the products table """
    __tablename__ = 'products'

    name = Column(String(256))
    details = relationship('Detail', secondary=association_table, backref='products')

    def __init__(self, name, created_by):
        Entity.__init__(self, created_by)
        self.name = name

class ProductSchema(Schema):
    """ Schema definition for the products table """
    id = fields.Str(dump_only=True)
    name = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

    details = fields.Relationship(
        include_data=True,
        many=True,
        type_='details',
        include_resource_linkage=True,
        schema=DetailSchema()
    )

    class Meta:
        type_ = 'products'
        strict = True
