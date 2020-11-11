docker run -d \
  --name=execute_business_1_{execute_id}_code \
  -v /data/tristan/1/cache/dependency/java:/root/.m2 \
  -v {finally_project_code_path}:/source_code  \
  maven:3-alpine /bin/bash -c '{build_project_sh}'

docker logs -f execute_business_1_{execute_id}

docker rm execute_business_1_{execute_id}_code