#!bin/bash

apt update

cat <<EOF >/etc/hostname
controller0
EOF

hostname controller0
