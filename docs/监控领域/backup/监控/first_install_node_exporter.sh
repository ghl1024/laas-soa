# official repo address: https://github.com/prometheus/node_exporter/releases
wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz
tar -zvxf node_exporter-1.0.1.linux-amd64.tar.gz
cp node_exporter-1.0.1.linux-amd64/node_exporter node_exporter
# debug mode running
#./node_exporter-1.0.1.linux-amd64/node_exporter
# backend mode running
nohup  ~/node_exporter > node_exporter.log 2>&1 &
# now, you can visit the url: http://<YOUR-SERVER-IP>:9100  to visit the last metric period of node info
# if you cann't visit the url, pleace check th firewall and process is still runnig status
# monitroing node_exporter running status
ps aux | grep node_exporter
# visit now the log of node_exporter
tail -f 100 node_exporter.log
# stop the node_exporter process
kill $(ps aux | grep 'node_exporter' | awk '{print $2}')
