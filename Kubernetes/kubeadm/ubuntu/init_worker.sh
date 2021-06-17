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