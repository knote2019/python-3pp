from sqlalchemy import create_engine

HOSTNAME = "192.168.99.100"
PORT = "3306"
DATABASE = "nova"
USERNAME = "root"
PASSWORD = "xxx"

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
    format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

engine = create_engine(DB_URI, encoding='utf-8', echo=True)
conn = engine.connect()

sql = "select * from hw_nic_devices"
result3 = conn.execute(sql).fetchall()
emp_json_list = [dict(zip(item.keys(), item)) for item in result3]

print(emp_json_list)
