tee /etc/systemd/system/node_exporter.service <<-'EOF'
[Unit]
Description=Node Exporter
After=network.target

[Service]
Type=simple
ExecStart=/root/node_exporter

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl start  node_exporter
systemctl status node_exporter
systemctl enable node_exporter