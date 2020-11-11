docker run -it \
  --name=exe1cute_business_1_{execute_id} \
  -v {build_project_sh_path}:/build_project.sh \
  -v /data/tristan/1/cache/java:/root/.m2 \
  -v {finally_project_code_path}:/source_code  \
  -v {finally_project_build_path}:/source_code/target   \
  maven:3-alpine /build_project.sh