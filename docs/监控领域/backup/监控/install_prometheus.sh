# offficial doc address: https://prometheus.io/download/
wget https://github.com/prometheus/prometheus/releases/download/v2.22.0/prometheus-2.22.0.linux-amd64.tar.gz
# unpack compress package
tar -zvxf prometheus-2.22.0.linux-amd64.tar.gz
# start prometheus
cd prometheus-2.22.0.linux-amd64
# debug mode running
#./prometheus --web.enable-lifecycle
# backend mode runnig
nohup ./prometheus --web.enable-lifecycle >prometheus.log 2>&1 &
# stop the prometheus process
kill $(ps aux | grep 'prometheus' | awk '{print $2}')
# monitroing node_exporter running status
ps aux | grep prometheus
# visit now the log of node_exporter
tail -f 100 prometheus.log
# reload prometheus config when prometheus running
curl -X POST http://localhost:9090/-/reload
