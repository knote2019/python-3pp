from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.sqlalchemy import models
from db.sqlalchemy import api as IMPL


def get_db_base():
    return models.get_db_base_with_tables()


def create_db_engine(context, **kwargs):
    db_username = context['db_username']
    db_password = context['db_password']
    db_host = context['db_host']
    db_port = context['db_port']
    db_name = context['db_name']
    engine_conn = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        db_username, db_password, db_host, db_port, db_name)
    # todo: kwargs
    db_engine = create_engine(engine_conn)
    return db_engine


def create_db_session():
    ctxt = dict()
    db_username = 'root'
    db_password = 'kmh198706,.'
    db_host = '127.0.0.1'
    db_port = '13306'
    db_name = 'notifier'
    ctxt.update({
        'db_username': db_username,
        'db_password': db_password,
        'db_host': db_host,
        'db_port': db_port,
        'db_name': db_name
    })
    engine = create_db_engine(ctxt)
    session = sessionmaker(bind=engine)
    return session


'''subscriber operation'''


def create_subscriber(context, values):
    return IMPL.create_subscriber(context, values)


def update_subscriber(context, sub_id, values):
    return IMPL.update_subscriber(context, sub_id, values)


def delete_subscriber(context, sub_id, soft_delete=False):
    return IMPL.delete_subscriber(context, sub_id, soft_delete)


def subscriber_get_by_id(context, sub_id):
    return IMPL.subscriber_get_by_id(context, sub_id)


def subscribers_get_by_topic(context, topic):
    return IMPL.subscribers_get_by_topic(context, topic)
