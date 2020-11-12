cat {docker_registry_password_path} | docker login {registry_url} --username {registry_username} --password-stdin
cd {finally_project_build_path}
ls -alh {finally_project_build_path}/target/
docker build -t {image_id} .
docker push {image_id}
