docker run -d \
  --name=execute_business_1_{execute_id}_image \
  -v {finally_project_code_path}/target:target  \
  -v {docker_registry_password_path}:docker_registry_password  \
  docker /bin/bash -c '{build_docker_sh}'

docker logs -f execute_business_1_{execute_id}_image

docker rm execute_business_1_{execute_id}_image