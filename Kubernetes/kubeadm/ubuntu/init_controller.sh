#!bin/bash

echo 'disable firewall'
ufw disable

echo 'disable swap'
swapoff -a; sed -i '/swap/d' /etc/fstab

echo 'Update sysctl settings for Kubernetes networking'
cat >>/etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system

echo 'install docker'
{
  apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  apt update
  apt install -y docker-ce containerd.io
}

echo 'Add Apt repository'
{
  curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
  echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
}

echo 'Install Kubernetes components'
apt update && apt install -y kubeadm kubelet kubectl

echo 'Initialize Kubernetes Cluster'
IP=$(hostname -I | head -c 12)
kubeadm init --apiserver-advertise-address=$IP --pod-network-cidr=172.16.0.0/16  --ignore-preflight-errors=all
# to change from cgroups to systemd use --config or use the script
# kubeadm init --config kubeadm-config.yaml

echo 'deloy calico'
kubectl --kubeconfig=/etc/kubernetes/admin.conf create -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml



#### To start using your cluster, you need to run the following as a regular user:
#  mkdir -p $HOME/.kube
#  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
#  sudo chown $(id -u):$(id -g) $HOME/.kube/config

#### Alternatively, if you are the root user, you can run:
# export KUBECONFIG=/etc/kubernetes/admin.conf