import psycopg2

# 连接数据库
conn = psycopg2.connect(database='testdb',
                        user='test',
                        password='Iluvatar123',
                        host='10.115.2.11',
                        port='5432')

job_name = 'superset.test_results'
job_date = '2022-06-01'
table_name = 'superset.test_results'
sql = "select image_name,sdk_url,build_type,node_name,to_char(to_timestamp(time_start),'yyyy-MM-dd'),test_result from {} " \
      "where test_name='{}' and " \
      "to_char(to_timestamp(time_start),'yyyy-MM-dd')='{}' limit 1". \
    format(table_name, job_name, job_date)
curs = conn.cursor()
curs.execute(sql)
data = curs.fetchall()
curs.close()

test_result_dict = dict()
test_result_dict.update({'image_name': data[0][0]})
test_result_dict.update({'sdk_url': data[0][1]})
test_result_dict.update({'build_type': data[0][2]})
test_result_dict.update({'node_name': data[0][3]})
test_result_dict.update({'time_start': data[0][4]})
test_result_dict.update({'test_result': data[0][5]})

# 关闭数据库
conn.close()
