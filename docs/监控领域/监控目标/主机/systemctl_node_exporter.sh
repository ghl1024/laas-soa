#!/bin/bash

echo "systemctl_node_exporter.sh"
kill $(ps aux | grep /root/node_exporter | awk '{print $2}')
systemctl status node_exporter
systemctl stop node_exporter
tee /etc/systemd/system/node_exporter.service <<-'EOF'
[Unit]
Description=Node Exporter
After=network.target

[Service]
Type=simple
ExecStart=/root/node_exporter --web.listen-address=0.0.0.0:9100

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl start  node_exporter
systemctl status node_exporter
systemctl enable node_exporter