## Install Elasticsearch with Docker

Elasticsearch is also available as Docker images. The images use [centos:7](https://hub.docker.com/_/centos/) as the base image.

A list of all published Docker images and tags is available at [www.docker.elastic.co](https://www.docker.elastic.co/). The source files are in [Github](https://github.com/elastic/elasticsearch/blob/7.5/distribution/docker).

These images are free to use under the Elastic license. They contain open source and free commercial features and access to paid commercial features. [Start a 30-day trial](https://www.elastic.co/guide/en/kibana/7.5/managing-licenses.html) to try out all of the paid commercial features. See the [Subscriptions](https://www.elastic.co/subscriptions) page for information about Elastic license levels.

### Pulling the image

Obtaining Elasticsearch for Docker is as simple as issuing a `docker pull` command against the Elastic Docker registry.

```sh
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.5.2
```

Alternatively, you can download other Docker images that contain only features available under the Apache 2.0 license. To download the images, go to [www.docker.elastic.co](https://www.docker.elastic.co/).

### Starting a single node cluster with Docker

To start a single-node Elasticsearch cluster for development or testing, specify [single-node discovery](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/bootstrap-checks.html#single-node-discovery) to bypass the [bootstrap checks](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/bootstrap-checks.html):

```sh
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.5.2
```

### Starting a multi-node cluster with Docker Compose

To get a three-node Elasticsearch cluster up and running in Docker, you can use Docker Compose:

1. Create a `docker-compose.yml` file:

```yaml
version: '2.2'
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.5.2
    container_name: es01
    environment:
      - node.name=es01
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es02,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - elastic
  es02:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.5.2
    container_name: es02
    environment:
      - node.name=es02
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es01,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data02:/usr/share/elasticsearch/data
    networks:
      - elastic
  es03:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.5.2
    container_name: es03
    environment:
      - node.name=es03
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es01,es02
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data03:/usr/share/elasticsearch/data
    networks:
      - elastic

volumes:
  data01:
    driver: local
  data02:
    driver: local
  data03:
    driver: local

networks:
  elastic:
    driver: bridge
```

This sample Docker Compose file brings up a three-node Elasticsearch cluster. Node `es01` listens on `localhost:9200` and `es02` and `es03` talk to `es01` over a Docker network.

Please note that this configuration exposes port 9200 on all network interfaces, and given how Docker manipulates `iptables` on Linux, this means that your Elasticsearch cluster is publically accessible, potentially ignoring any firewall settings. If you don’t want to expose port 9200 and instead use a reverse proxy, replace `9200:9200` with `127.0.0.1:9200:9200` in the docker-compose.yml file. Elasticsearch will then only be accessible from the host machine itself.

The [Docker named volumes](https://docs.docker.com/storage/volumes) `data01`, `data02`, and `data03` store the node data directories so the data persists across restarts. If they don’t already exist, `docker-compose` creates them when you bring up the cluster.

1. Make sure Docker Engine is allotted at least 4GiB of memory. In Docker Desktop, you configure resource usage on the Advanced tab in Preference (macOS) or Settings (Windows).

   Docker Compose is not pre-installed with Docker on Linux. See docs.docker.com for installation instructions: [Install Compose on Linux](https://docs.docker.com/compose/install)

2. Run `docker-compose` to bring up the cluster:

   ```sh
   docker-compose up
   ```

3. Submit a `_cat/nodes` request to see that the nodes are up and running:

   ```sh
   curl -X GET "localhost:9200/_cat/nodes?v&pretty"
   ```

Log messages go to the console and are handled by the configured Docker logging driver. By default you can access logs with `docker logs`.

To stop the cluster, run `docker-compose down`. The data in the Docker volumes is preserved and loaded when you restart the cluster with `docker-compose up`. To **delete the data volumes** when you bring down the cluster, specify the `-v` option: `docker-compose down -v`.

#### Start a multi-node cluster with TLS enabled

See [Encrypting communications in an Elasticsearch Docker Container](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/configuring-tls-docker.html) and [Run the Elastic Stack in Docker with TLS enabled](https://www.elastic.co/guide/en/elastic-stack-get-started/7.5/get-started-docker.html#get-started-docker-tls).

### Using the Docker images in production

The following requirements and recommendations apply when running Elasticsearch in Docker in production.

#### Set `vm.max_map_count` to at least `262144`

The `vm.max_map_count` kernel setting must be set to at least `262144` for production use.

How you set `vm.max_map_count` depends on your platform:

- Linux

  The `vm.max_map_count` setting should be set permanently in `/etc/sysctl.conf`:

  ```sh
  grep vm.max_map_count /etc/sysctl.conf
  vm.max_map_count=262144
  ```

  To apply the setting on a live system, run:

  ```sh
  sysctl -w vm.max_map_count=262144
  ```

- macOS with [Docker for Mac](https://docs.docker.com/docker-for-mac)

  The `vm.max_map_count` setting must be set within the xhyve virtual machine:

  1. From the command line, run:

     ```sh
     screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty
     ```

  2. Press enter and use`sysctl` to configure `vm.max_map_count`:

     ```sh
     sysctl -w vm.max_map_count=262144
     ```

  3. To exit the `screen` session, type `Ctrl a d`.

- Windows and macOS with [Docker Desktop](https://www.docker.com/products/docker-desktop)

  The `vm.max_map_count` setting must be set via docker-machine:

  ```sh
  docker-machine ssh
  sudo sysctl -w vm.max_map_count=262144
  ```

#### Configuration files must be readable by the `elasticsearch` user

By default, Elasticsearch runs inside the container as user `elasticsearch` using uid:gid `1000:1000`.

One exception is [Openshift](https://docs.openshift.com/container-platform/3.6/creating_images/guidelines.html#openshift-specific-guidelines), which runs containers using an arbitrarily assigned user ID. Openshift presents persistent volumes with the gid set to `0`, which works without any adjustments.

If you are bind-mounting a local directory or file, it must be readable by the `elasticsearch` user. In addition, this user must have write access to the [data and log dirs](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/path-settings.html). A good strategy is to grant group access to gid `1000` or `0` for the local directory.

For example, to prepare a local directory for storing data through a bind-mount:

```sh
mkdir esdatadir
chmod g+rwx esdatadir
chgrp 1000 esdatadir
```

As a last resort, you can force the container to mutate the ownership of any bind-mounts used for the [data and log dirs](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/path-settings.html) through the environment variable `TAKE_FILE_OWNERSHIP`. When you do this, they will be owned by uid:gid `1000:0`, which provides the required read/write access to the Elasticsearch process.

#### Increase ulimits for nofile and nproc

Increased ulimits for [nofile](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/setting-system-settings.html) and [nproc](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/max-number-threads-check.html) must be available for the Elasticsearch containers. Verify the [init system](https://github.com/moby/moby/tree/ea4d1243953e6b652082305a9c3cda8656edab26/contrib/init) for the Docker daemon sets them to acceptable values.

To check the Docker daemon defaults for ulimits, run:

```sh
docker run --rm centos:7 /bin/bash -c 'ulimit -Hn && ulimit -Sn && ulimit -Hu && ulimit -Su'
```

If needed, adjust them in the Daemon or override them per container. For example, when using `docker run`, set:

```sh
--ulimit nofile=65535:65535
```

#### Disable swapping

Swapping needs to be disabled for performance and node stability. For information about ways to do this, see [Disable swapping](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/setup-configuration-memory.html).

If you opt for the `bootstrap.memory_lock: true` approach, you also need to define the `memlock: true` ulimit in the [Docker Daemon](https://docs.docker.com/engine/reference/commandline/dockerd/#default-ulimits), or explicitly set for the container as shown in the [sample compose file](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/docker.html#docker-compose-file). When using `docker run`, you can specify:

```
-e "bootstrap.memory_lock=true" --ulimit memlock=-1:-1
```

#### Randomize published ports

The image [exposes](https://docs.docker.com/engine/reference/builder/#/expose) TCP ports 9200 and 9300. For production clusters, randomizing the published ports with `--publish-all` is recommended, unless you are pinning one container per host.

#### Set the heap size

Use the `ES_JAVA_OPTS` environment variable to set the heap size. For example, to use 16GB, specify `-e ES_JAVA_OPTS="-Xms16g -Xmx16g"` with `docker run`.

You must [configure the heap size](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/heap-size.html) even if you are [limiting memory access](https://docs.docker.com/config/containers/resource_constraints/#limit-a-containers-access-to-memory) to the container.

#### Pin deployments to a specific image version

Pin your deployments to a specific version of the Elasticsearch Docker image. For example `docker.elastic.co/elasticsearch/elasticsearch:7.5.2`.

#### Always bind data volumes

You should use a volume bound on `/usr/share/elasticsearch/data` for the following reasons:

1. The data of your Elasticsearch node won’t be lost if the container is killed
2. Elasticsearch is I/O sensitive and the Docker storage driver is not ideal for fast I/O
3. It allows the use of advanced [Docker volume plugins](https://docs.docker.com/engine/extend/plugins/#volume-plugins)

#### Avoid using `loop-lvm` mode

If you are using the devicemapper storage driver, do not use the default `loop-lvm` mode. Configure docker-engine to use [direct-lvm](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/#configure-docker-with-devicemapper).

#### Centralize your logs

Consider centralizing your logs by using a different [logging driver](https://docs.docker.com/engine/admin/logging/overview/). Also note that the default json-file logging driver is not ideally suited for production use.

### Configuring Elasticsearch with Docker

When you run in Docker, the [Elasticsearch configuration files](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/settings.html#config-files-location) are loaded from `/usr/share/elasticsearch/config/`.

To use custom configuration files, you [bind-mount the files](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/docker.html#docker-config-bind-mount) over the configuration files in the image.

You can set individual Elasticsearch configuration parameters using Docker environment variables. The [sample compose file](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/docker.html#docker-compose-file) and the [single-node example](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/docker.html#docker-cli-run-dev-mode) use this method.

You can also override the default command for the image to pass Elasticsearch configuration parameters as command line options. For example:

```sh
docker run <various parameters> bin/elasticsearch -Ecluster.name=mynewclustername
```

While bind-mounting your configuration files is usually the preferred method in production, you can also [create a custom Docker image](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/docker.html#_c_customized_image) that contains your configuration.

#### Mounting Elasticsearch configuration files

Create custom config files and bind-mount them over the corresponding files in the Docker image. For example, to bind-mount `custom_elasticsearch.yml` with `docker run`, specify:

```sh
-v full_path_to/custom_elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml
```

The container **runs Elasticsearch as user `elasticsearch` using** uid:gid `1000:1000`**. Bind mounted host directories and files must be accessible by this user, and the data and log directories must be writable by this user.

#### Using custom Docker images

In some environments, it might make more sense to prepare a custom image that contains your configuration. A `Dockerfile` to achieve this might be as simple as:

```sh
FROM docker.elastic.co/elasticsearch/elasticsearch:7.5.2
COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/
```

You could then build and run the image with:

```sh
docker build --tag=elasticsearch-custom .
docker run -ti -v /usr/share/elasticsearch/data elasticsearch-custom
```

Some plugins require additional security permissions. You must explicitly accept them either by:

- Attaching a `tty` when you run the Docker image and allowing the permissions when prompted.
- Inspecting the security permissions and accepting them (if appropriate) by adding the `--batch` flag to the plugin install command.

See [Plugin management](https://www.elastic.co/guide/en/elasticsearch/plugins/7.5/_other_command_line_parameters.html) for more information.

### Next steps

You now have a test Elasticsearch environment set up. Before you start serious development or go into production with Elasticsearch, you must do some additional setup:

- Learn how to [configure Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/settings.html).
- Configure [important Elasticsearch settings](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/important-settings.html).
- Configure [important system settings](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/system-config.html).