docker run -it \
  --name=exe1cute_business_1_{execute_id} \
  -v {build_project_sh_path}:/build_project.sh \
  -v /data/tristan/1/cache/dependency/java:/root/.m2 \
  -v {finally_project_code_path}:/source_code  \
  maven:3-alpine /bin/bash -c '{build_project_sh}'