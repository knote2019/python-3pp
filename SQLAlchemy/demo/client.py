import time

from sqlalchemy.orm import sessionmaker

from db.api import get_db_base, create_db_engine, create_subscriber, subscriber_get_by_id, update_subscriber

if __name__ == '__main__':
    # init_db()
    ctxt = dict()
    db_username = 'root'
    db_password = 'cloudxxxx'
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

    Base = get_db_base()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    db_session = Session()

    api_ctxt = dict()
    api_ctxt.update({'db_session': db_session})

    subscriber_dict = dict()
    subscriber_dict.update({
        'sub_id': 1,
        'topic': 'Openstack',
        'protocol': 'HTTPS',
        'endpoint': 'https://192.168.0.10',
        'extra_info': ''
    })
    create_subscriber(api_ctxt, subscriber_dict)

    sub = subscriber_get_by_id(api_ctxt, 1)
    print(sub)

    time.sleep(3)

    subscriber_update_dict = dict()
    subscriber_update_dict.update({'topic': 'Alarm'})
    update_subscriber(api_ctxt, 1, subscriber_update_dict)

    sub2 = subscriber_get_by_id(api_ctxt, 1)
    print(sub2)

    pass
