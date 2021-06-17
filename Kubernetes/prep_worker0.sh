#!bin/bash

apt update

cat <<EOF >/etc/hostname
worker0
EOF

hostname worker0
