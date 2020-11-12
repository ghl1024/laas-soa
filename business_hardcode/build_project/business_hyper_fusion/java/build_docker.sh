cat {docker_registry_password_path} | docker login {registry_url} --username {registry_username} --password-stdin
cd {finally_project_build_path}
rm -rf target/*-sources.jar
ls -alh target/
docker build -t {docker_image_id} .
docker push {docker_image_id}
