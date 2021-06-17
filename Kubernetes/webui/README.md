## Install webui for Kubernetes


deploy dashboard UI   
`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.2.0/aio/deploy/recommended.yaml`   

edit service from ClusterIP to NodePort   
`kubectl -n kubernetes-dashboard edit svc kubernetes-dashboard`   

create service account with admin role   
`kubectl create -f sa_cluster_admin.yaml`   

list the service account   
`kubectl -n kube-system get sa`   

get the token with admin role    
`kubectl -n kube-system describe sa admin-user`   

get the secret with admin role   
`kubectl -n kube-system describe secret admin-user-token-xxx`   

log in with the admin token   

[![webui](image)](.admin-token-webui-k8s.png)
