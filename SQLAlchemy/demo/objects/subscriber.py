from db.api import create_db_session
from objects import base
from oslo_versionedobjects import fields
from db import api as db_api

db_session = create_db_session()
context = {'db_session': db_session}


class Subscriber(base.NotifierPersistentObject):
    VERSION = '1.0'

    fields = {
        'id': fields.IntegerField(read_only=True),
        'uuid': fields.UUIDField(),
        'sub_id': fields.StringField(nullable=True),
        'topic': fields.EnumField(nullable=True),
        'protocol': fields.EnumField(nullable=True),
        'endpoint': fields.StringField(),
        'extra_info': fields.StringField(),
    }

    def __init__(self, *args, **kwargs):
        super(Subscriber, self).__init__(*args, **kwargs)

    @staticmethod
    def create(self):
        values = dict()
        db_api.create_subscriber(context, values)
