import os

#only tested on windows

os.system("kubectl delete -f k8sconfig.yaml")
os.system("kubectl apply -f k8sconfig.yaml")
