from oslo_utils import uuidutils

from db.sqlalchemy.models import Subscribers
'''subscriber operation'''


def create_subscriber(context, values):
    db_session = context['db_session']
    subscriber = Subscribers()
    subscriber.update(values)
    # subscriber.created_at = timeutils.utcnow()
    # subscriber.updated_at = timeutils.utcnow()
    # subscriber.deleted_at = None
    # subscriber.deleted = 0
    # subscriber.sub_id = values['sub_id']
    # subscriber.topic = values['topic']
    # subscriber.protocol = values['protocol']
    # subscriber.endpoint = values['endpoint']
    # subscriber.extra_info = values['extra_info']
    subscriber.uuid = uuidutils.generate_uuid()
    db_session.add(subscriber)
    db_session.commit()


def update_subscriber(context, sub_id, values):
    db_session = context['db_session']
    db_session.query(Subscribers)\
        .filter(Subscribers.sub_id == sub_id)\
        .update(values)
    db_session.commit()


def delete_subscriber(context, sub_id, soft_delete=False):
    if soft_delete:
        return
    db_session = context['db_session']
    db_session.query(Subscribers)\
        .filter(Subscribers.sub_id == sub_id)\
        .delete()
    db_session.commit()


def subscriber_get_by_id(context, sub_id):
    db_session = context['db_session']
    sub = db_session.query(Subscribers).\
        filter(Subscribers.sub_id == sub_id)\
        .first()
    return sub


def subscribers_get_by_topic(context, topic):
    db_session = context['db_session']
    sub = db_session.query(Subscribers).\
        filter(Subscribers.topic == topic)\
        .all()
    return sub
