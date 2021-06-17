## Install Kubernetes via Kubeadm

1. use the prep scripts on the nodes   
2. for kubeadm install (VM's and Baremetal) use init scripts   

test on **Ubuntu 20.04.2 LTS**


### Deploying the Dashboard UI
https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/

### Configuring a cgroup driver
https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/

### Getting a Bearer Token
`kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get sa/admin-user -o jsonpath="{.secrets[0].name}") -o go-template="{{.data.token | base64decode}}"`
