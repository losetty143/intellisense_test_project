"""
This Code is for getting deployment name, image name and Deployment updated time for the deployments present in Kubernetes cluster. 
This code will give you all the deployments that been created under any name space. You just have to update the 
name space details and you will get the data in the table format.
"""
from kubernetes import client, config
from prettytable import PrettyTable
config.load_kube_config()
apis_api = client.AppsV1Api()
resp = apis_api.list_namespaced_deployment('sock-shop')
deps = resp.items
dep_name = [deployment.metadata.name for deployment in deps]
image_name = [deployment.spec.template.spec.containers[0].image for deployment in deps]
deployment_time = [deployment.status.conditions[0].last_update_time for deployment in deps]
#print(dep_name)
#print(image_name)
#print(deployment_time)
#print(list(zip(dep_name,image_name,deployment_time)))
t = PrettyTable(['Deployment_Name','Image','Deployment_updated_Time'])
for i in range(len(deps)):
    t.add_row(list(zip(dep_name,image_name,deployment_time))[i])
print(t)