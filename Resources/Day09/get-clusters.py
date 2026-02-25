# from kubernetes import client, config

# def get_clusters():
#     config.load_kube_config()

#     v1= client.Corev1Api()
    
#     ret = v1.list_clusterrolebinding_for_all_namespaces(watch=false)
    
#     for i in ret.items:
#         print("%s\t%s\t%s" % (i.metadata.name, i.subjects[0].name, i.role_ref.name))

# if __name__ == '__main__':
#     get_clusters()
################################################################
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
    # print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

print(v1)