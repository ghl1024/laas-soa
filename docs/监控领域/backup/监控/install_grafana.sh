# official doc address: https://grafana.com/grafana/download/7.2.2?platform=docker
# official docker image address: https://hub.docker.com/r/grafana/grafana
rm -rf /root/tistan/grafana/configs /root/tristan/grafana/data
mkdir -p /root/tistan/grafana/configs /root/tristan/grafana/data
chmod -R 777 /root/tristan/grafana/configs /root/tristan/grafana/data
# start grafana
# warning: mount just for /root directory
docker run -d \
  --name=grafana \
  --restart=always \
  -p 3000:3000 \
  -v /root/tristan/grafana/data:/var/lib/grafana \
  grafana/grafana:7.2.2
# also can update cofing by:   -v /tristan/grafana/configs/grafana.ini:/etc/grafana/grafana.ini \
# also can update icon by:   -v /tristan/grafana/configs/grafana_icon.svg:/usr/share/grafana/public/img/grafana_icon.svg \
# stop grafana
docker sotp grafana
# delete grafana
docker rm grafana
# monitor grafana running status
docker ps | grep grafana
# visit now the log of grafana
docker logs -f --tail=100 grafana