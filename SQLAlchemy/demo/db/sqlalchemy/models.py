from oslo_db.sqlalchemy import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Index, Integer, Enum, String, schema, Text)

_BASE = declarative_base()


def get_db_base_with_tables():
    return _BASE


class _NotifierBase(models.ModelBase, models.TimestampMixin,
                    models.SoftDeleteMixin):
    pass


class Subscribers(_BASE, _NotifierBase):

    __tablename__ = 'subscribers'
    __table_args__ = (
        schema.UniqueConstraint("sub_id",
                                "deleted",
                                name="uniq_subscribers0sub_id0deleted"),
        Index('subscribers_uuid_idx', 'uuid', unique=True),
    )

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    sub_id = Column(Integer, nullable=False)
    topic = Column(Enum('Openstack', 'Infrastructure', 'Alarm'),
                   nullable=False)
    protocol = Column(Enum('HTTPS', 'SNMPv3'), nullable=False)
    endpoint = Column(String(255), nullable=False)
    extra_info = Column(Text())
