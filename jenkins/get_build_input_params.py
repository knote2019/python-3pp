import jenkins
import time

jenkins_client = jenkins.Jenkins('http://10.150.9.97:8080',
                                 username='pub.ci',
                                 password='xxxxxx')

job_name = 'tf_resnet50_cuda10'
lastCompletedBuild_number = jenkins_client.get_job_info(
    job_name)['lastCompletedBuild']['number']

job_info = jenkins_client.get_job_info(job_name)
build_info = jenkins_client.get_build_info(job_name,
                                           lastCompletedBuild_number,
                                           depth=3)

timestamp = build_info['timestamp']
t1 = time.localtime(timestamp / 1000)
t2 = time.strftime('%Y-%m-%d %H:%M:%S', t1)
print(t2)

job_build_parameters = dict()
for action in build_info['actions']:
    if action:
        for k, v in action.items():
            if v == 'hudson.model.ParametersAction':
                for param_items in action['parameters']:
                    if param_items:
                        param_name = ''
                        param_value = ''
                        for pk, pv in param_items.items():
                            if 'name' in pk:
                                param_name = pv
                            if 'value' in pk:
                                param_value = pv
                        job_build_parameters.update({param_name: param_value})

print(job_build_parameters)
