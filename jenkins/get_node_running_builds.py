import re
from six.moves.urllib.parse import urlparse
import jenkins

jenkins_client = jenkins.Jenkins('http://10.150.9.97:8080',
                                 username='pub.ci',
                                 password='xxxxxx')
user = jenkins_client.get_whoami()
version = jenkins_client.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


# 参考: running_builds = jenkins_client.get_running_builds()
def get_node_running_builds(node_name):
    builds = []
    try:
        info = jenkins_client.get_node_info(node_name, depth=2)
        for executor in info['executors']:
            executable = executor['currentExecutable']
            if executable and 'number' in executable:
                executor_number = executor['number']
                build_number = executable['number']
                url = executable['url']
                m = re.search(r'/job/([^/]+)/.*', urlparse(url).path)
                job_name = m.group(1)
                builds.append({
                    'name': job_name,
                    'number': build_number,
                    'url': url,
                    'node': node_name,
                    'executor': executor_number
                })
    except Exception as e:
        print("get_node_running_builds ERROR: {}".format(e))
    return builds


node_name = '218_chip'
running_builds = get_node_running_builds(node_name)

print(running_builds)
