cat /docker_registry_password | docker login {registry_url} --username {registry_username} --password-stdin
cd {finally_project_code_path}
docker build -t {image_id} .
docker push {image_id}
