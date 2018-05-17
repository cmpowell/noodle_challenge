""" Module for the details database object """

# coding=utf-8

from marshmallow_jsonapi import Schema, fields
from sqlalchemy import Column, String

from .entity import Entity, Base


class Detail(Entity, Base):
    """ Class to interact with the details table """
    __tablename__ = 'details'

    name = Column(String(256))

    def __init__(self, name, created_by):
        Entity.__init__(self, created_by)
        self.name = name

class DetailSchema(Schema):
    """ Schema definition for the details table """
    id = fields.Str(dump_only=True)
    name = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

    class Meta:
        type_ = 'details'
        strict = True
