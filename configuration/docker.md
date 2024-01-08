# Docker and Kubernetes

## Docker

### What are Containers?

Applications that are packaged together with their configuration and dependencies.

Containers are used to:

- Share applications
- Post applications for review
- Test different instances of an application
- Handle parts of a complex architecture separately

Think of requirements.txt
Containers are use cases between VMs and venvs.

It's like packing up part of your computer and giving it to someone else.

Common problem, not everyone's computer is set up quite the same. So, even though it might work correctly on your personal computer it might not work correctly on theirs.

Allows them to run the application inside a small snapshot of your computer.

Can also run a small database inside of a container and connect to that database within another application.

### Set up Docker

Docker is an easy way to package and run applications in containers.
Within a container, the application is isolated from all other processes on the host machine.

- Docker daemon - manages running containers on a host machine called the Docker HOst.
- Docker CLI - the command line tool to interact with Docker Daemon
- Docker Desktop - a GUI to interact with the daemon
- Docker Hub - the central repository for downloading containers

Docker supports running client tools and daemon on different machines.
Allows you to manage containers on a remote server as easily as if they're on your own workstation.

#### Installing Docker

Read the [Getting started guide](https://docs.docker.com/get-started/)

##### What is a container?

A sandboxed process running on a host machine that is isolated from all other processes running on that host machine.

- runnable instance of an image - you can create, start, stop, move, or delete a container using the Docker API or CLI.
- can be run on local machines, virtual machines, or deployed to the cloud.
- Is portable (and can be run on any os)
- Is isolated from other containers and runs its own software, binaries, configurations, etc.

##### What is an image?

A running container uses an isolated filesystem, provided by an image, and the image must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc.

The image also contains other configurations for the container, such as environment variables, a default command to run, and other metadata.

---

Download and install Docker according to operating system.

- Windows - [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)
- Linux - [https://docs.docker.com/desktop/install/linux-install/](https://docs.docker.com/desktop/install/linux-install/)

---

Run your first container:

- Open the Docker desktop app.
- Select the search bar at the top
- type hello-world

- click Run

To do it from the command line:

- Open a terminal window and type `docker`
- Type `docker run hello-world` and press Enter

### Docker web apps

Docker is an open-source tool used to build, deploy, run, update, and manage containers.

Sharing image in docker requires:

- requirements.txt
- Dockerfile (Docker Image)

Docker web app - uploading a container to a server people can connect to remotely.

### Docker Images

Docker images are the building blocks of Docker containers.
A Docker image contains the application code, data files, configuration files, libraries, and other dependencies needed to run an application.

#### Docker images and image layers

Think of a Docker image as a template from which Docker containers are created and executed. Each image is composed of multiple layers - adding or removing files from the previous layer.

Each layer represents a specific set of changes made to the image and is composed based on the instructions in a Dockerfile.

The Dockerfile define how the images should be built.

The purpose of having multiple layers is to keep the final images as small as possible. You do this by reusing layers in multiple images - and to speed up the process of building containers, as Docker has to rebuild only the layers that have changed.

#### How to build a Docker image

The key to packaging your own application as a Docker image is to have a Dockerfile.

The Dockerfile acts as your sources of truth or instruction manual: it specifies how Docker should build the image and contains a series of commands to build the image.

A common process is to start with a base image such as Debian Linux or Python 3.10, install the libraries your application requires, then copy the application and any related files into the image.

A Dockerfile for a python application:

`FROM python:3.9`
This line says that you're starting from the Python 3.9 base image.

`COPY *.py setup.cfg LICENSE README.md requirements.txt /app/`

`WORKDIR /app`

This command says to copy all of the application's files to a folder inside the container named `/app` and make it the current working directory.

`RUN pip install - r requirements.txt`

`RUN python setup.py install`

These two lines of code run the Python commands to install the libraries required by the app. When that step is complete, build and install the app inside the container.

`EXPOSE 8000`

`CMD [ "/usr/local/bin/my-application" ]`

This command tells Docker what executable should run when the container starts and that the container will listen for network connections on port 8000

**Tip** To build this image from the Dockerfile, use the command: `docker build`.
If the build is successful, Docker outputs the ID of the new image, which you can then use to start a container.

#### Image names, tags, and IDs

tags and ids are used to reference Docker images. The ID is a random string of numbers and letters. Can assign any number of tags to the image in addition to the ID.

Most images are tagged wth the author's Github username, the name of the application, and a version number.

**Tip** Tag the most recent version of an image with `latest` in addition to a version number.

```
csmith/my-docker-image:1.0

csmith/my-docker-image:latest

sha256:abc123def456
```

`csmith` is the name of the author, `my-docker-image` is the image name, `1.0` is the version number, and `sha256:abc123def456` represents the image ID.

#### How to Manage Images

Docker caches images on a disk. Therefore, you don't need to grab them or rebuild them every time you need them. This saves a lot of time.

Some Docker CLI commands you can use:

- `docker image ls` - This command lists the images cached locally
- `docker image tag` - This command applies tags to a local image
- `docker image pull` - This command fetches an image from a remote repository
- `docker image push` - This command sends a local image to a remote repository
- `docker image rm` - This command removes an image from the cache
- `docker image prune` - This command removes all unused images to reclaim disk space.

### Using Multiple Containers

The idea behind microservices is to take a large application and break it up into smaller, more tangible, independent parts of the application that are self-contained.

This allows each part of the application to be better maintained.
Use multiple containers to test the entirety of the application to ensure everything runs smoothly.

#### Starting multiple containers

You need to run multiple `docker run` commands.

Starting two containers that work together once they find each other by name:

As a programmer, you've been asked to set up a WordPress blog, which requires a database to store its content. You create and start two containers, `wordpress` and `db` using the following command:

```
$ docker run -d --name db --restart always \
	-v db_data:/var/lib/mysql -p 3306 -p 33060 \
	-e MYSQL_ROOT_PASSWORD=somewordpress \
	-e MYSQL_DATABASE=wordpress \
	-e MYSQL_USER=wordpress \
	-e MYSQL_PASSWORD=wordpress \
	mariadb:10
```

This command starts the `mariadb` database, determines a storage volume, and sets the initial password for the WordPress user. It declares two network ports open to other containers, but it is not shown on the host machine.

Now, start the WordPress container using the following command:

```
$ docker run -d --name wordpress --restart always \
	-v wp_data:/var/www/html -p 80:80 \
	-e WORDPRESS_DB_HOST=db \
	-e WORDPRESS_DB_USER=wordpress \
	-e WORDPRESS_DB_PASSWORD=wordpress \
	-e WORDPRESS_DB_NAME=wordpress \
	wordpress:latest
```

**Note** The environment variable `WORDPRESS_DB_HOST` is set to `db` on the third line. This is needed to refer to another container. Docker provides domain name system (DNS) services that allow containers to find each other by their name.

#### Networking with multiple containers

Imagine several customers using the same application. Created multiple containers, one for each customer.

Docker allows you to create private networks for a container or groups of containers. These private containers are able to discover each other, but no other networks will be able to find the private containers you've started.

Modifying the wordpress and `db` containers by putting them on a private network:

First, stop and delete both containers:

```
$ docker stop wordpress && docker rm wordpress
$ docker stop db && docker rm db
```

Then create a private network for both containers to use:

```
$ docker network create myblog
<really long complicate id>
```

Once the containers are on private networks, restart them with the additional option `-network myblog`

```
$ docker run -d --name db --restart always \
	-v db_data:/var/lib/mysql -p 3306 -p 33060 \
	-e MYSQL_ROOT_PASSWORD=somewordpress \
	-e MYSQL_DATABASE=wordpress \
	-e MYSQL_USER=wordpress \
	-e MYSQL_PASSWORD=wordpress \
	--network myblog \
	mariadb:10

$ docker run -d --name wordpress --restart always \
	-v wp_data:/var/www/html -p 80:80 \
	-e WORDPRESS_DB_HOST=db \
	-e WORDPRESS_DB_USER=wordpress \
	-e WORDPRESS_DB_PASSWORD=wordpress \
	-e WORDPRESS_DB_NAME=wordpress \
	--network myblog \
	wordpress:latest
```

It's good practice to verify that containers on other networks can't access the private networks you created.
Start a new container and attempt to find the private containers you created.

```
$ docker run -it debian:latest

root@7240f1e3ddab:/# ping db.myblog

ping: db.myblog: Name or service not known
```

#### Docker Compose

Docker Compose is an optional tool, provided by Docker, that makes using multiple containers easy.

Docker Compose allows you to define a multiple-container setup in a single YAML format, called a Compose file.

The Compose file communicates with Docker and identifies the containers you need and how you should configure them. The containers in a Compose file are called services.

Using Compose to recreate the private networks from the `wordpress` and `db` example:

1. Create an empty folder and save the file below as `docker-compose.yml`

   ```yml
   version: '3.3'
   services:
   	db:
   		image: mariadb:10
   		volumes:
   			- db_data:/var/lib/mysql
   		restart: always
   		environment:
   			- MYSQL_ROOT_PASSWORD=somewordpress
   			- MYSQL_DATABASE=wordpress
   			- MYSQL_USER=wordpress
   			- MYSQL_PASSWORD=wordpress
   		networks:
   			- myblog
   		expose:
   			- 3306
   			- 33060
   wordpress:
   	image: wordpress:latest
   	volumes:
   		- wp_data:/var/www/html
   	ports:
   		- 80:80
   	networks:
   		- myblog
   	restart: always
   	environment:
   		- WORDPRESS_DB_HOST=db
   		- WORDPRESS_DB_USER=wordpress
   		- WORDPRESS_DB_PASSWORD=wordpress
   		- WORDPRESS_DB_NAME=wordpress
    volumes:
   	db_data:
   	wp_data:
   networks:
   	myblog:
   ```

2. Run the command `docker compose up`. This pulls up the images, creates two empty data volumes, and starts both services.

The Compose file grants you control over how each service is configured:

- Choosing the image
- Setting environment variables
- Mounting storage volumes
- Exposing network ports

**Tip** You can also express any option you pass to the `docker run` command as YAML in a Compose file.

A helpful third party tool is [Composerize](https://www.composerize.com/)

Compose has additional commands when working with a single or multiple containers. Let’s look at some examples:

- docker compose pull: This fetches the latest image for each service.
- docker compose up: This creates the containers and starts the service.
- docker compose down: This stops the service and deletes the container.
- docker compose logs: This displays the console logs from the container.

### Container and artifact registry

Container registry is a storage location for container images, organized for efficient access.

Repository is a container registry that also manages container images and associated artifacts.

Artifact is a byproduct of the software development process.
Allows you to distribute your code so others can use it.

An artifact has a specific purpose or use.

Container registries in the cloud:

- Azure Container Registry
- AWS Elastic Container Registry
- Google Container Registry

### Docker and GCP

Docker and Google Cloud Platform are two types of technologies that complement each other, allowing programmers to build, deploy, and manage containerized applications in the cloud.

#### Google Cloud Platform

GCP is a composition of all the cloud services provided by Google:

- Virtual Machines
- Containers
- Computing
- Hosting
- Storage
- Databases
- Tools
- Identity management

#### How to run Docker containers in GCP

You can run containers two ways.

Start a virtual machine with Docker installed on it. Use the docker run command to create a container and start it. This is the same process for running Docker on any other host machine.

Or.

Use a service called Cloud Run. This is a serverless platform managed by Google and allows you to launch containers without worrying about managing the underlying infrastructure.

Cloud Run is that it allows you to deploy code written in any programming language if you can put the code into a container.

#### Use Cloud Run to Deploy Containers in GCP

1. Open [Cloud Run](https://console.cloud.google.com/run?enableapi=true&_ga=2.103152064.1978640569.1689869801-335443466.1689535280)

2. Click **Create service** to display the form.

In the form:

1. Select **Deploy one revision from an existing container image**
2. Below the **Container image URL** text box, select **Test with a sample container**
3. From the **Region** drop-down menu, select the region in which you want the service located
4. Below **Authentication**, select **Allow unauthenticated invocations**
5. Click **Create** to deploy the sample container image to Cloud Run and wait for the deployment to finish

**Tip** Cloud Run helps keep costs down by only charging you for the central processing unit time while the container is running. It's unlike running Docker on a virtual machine, for which you must keep the virtual machine on at all times - running up your bill.

### Build artifact testing

No matter what code you write, you'll need to test it. You want to create a product that is free of errors and bugs.

Testing build artifacts and troubleshooting within your tests are great ways to ensure the quality of your work.

#### Build artifacts

Items that you create during the build process. Your main artifact is your docker container, if you're working within a Dockerized application.

All other items that you generate during the Docker image build process are also considered build artifacts.

- Libraries
- Documentation
- Static files
- Configuration files
- Scripts

#### Build artifacts in Docker

Build artifacts play a crucial role in software development in Docker.
Must test before deployment to ensure you catch and correct all issues, defects, and errors.

**Tip** It's important to check that Docker built the container itself correctly if you are testing your code with a containerized application.

Types of software testing to execute with Docker containers:

- Unit tests - There are small, granular tests written by the developer to test individual functions in the code. In Docker, unit tests are un directly on your codebase before the Docker image is built, ensuring the code is working as expected before being packaged.

- Integration tests: Testing an application or microservice in conjunction with the other services on which it relies.
  In a Dockerized environment, integration tests are run after the docker image is built and the container is running, testing how different components operate together inside the Docker container.

- End-to-end tests: This type of testing simulates the behavior of a real user (e.g. by opening the browser and navigating through several pages). E2E tests are run against the fully deployed docker container, checking that the entire application stack with its various components and services functions correctly as a whole.

- Performance tests: This type of testing identifies bottlenecks. Performance tests are run against the fully deployed Docker container and test various stresses and loads to ensure the application performs at expectations

#### How to test a Docker container

Automated testing often requires supplying configuration files, data files, and test tools to the application you want to test, which unfortunately increases the size of your container.

Instead, you can build a container just for testing, using your output artifact as a base image.

Let's say a Python application uses pytest as a unit testing framework and Sphix to generate documentation. YOu can reuse your application container and build a new image that includes the tools on top.

```
FROM myapp:latest
RUN pip install pytest pydoc
WORKDIR /opt/myapp
CMD pytest .
```

This part shows that you have a container that has both the application and the test framework in it.

```
docker run -it myapp:test
```

You can mount data files for input or configuration as a volume when you create your test container:

```
docker run -it -v ./testdata:/data myapp:test
```

What to do if test fails.

Troubleshoot it.
First, oen the shell inside the failed container and see if you can identify the problem. If the container is still running, use the docker exec command and the container ID.

```
docker exec -it c47da2b409a1 /bin/sh
```

## Kubernetes

### Kubernetes Overview

Kubernetes, abbreviated as K8s, is an open-source platform that gives programmers the power to orchestrate containers.

Containers used and named in K8s are deployed as pods in the cloud. A pod is a logical group of one or more containers that are scheduled and run together on a single worker node, a host, within a Kubernetes cluster.

They share the same namespace on the network and IP address and resources.

Kubernetes:

- Is scalable - add more clones, and update all at once
- Can be rolled back
- Allows access to information
- Provides more access permissions - allows automated load balancing

Imagine Docker as a shipping container that lets you package each application and its dependencies in a separate crate within a container.
Kubernetes is the port orchestrating how the containers and packages are handled.

The learning curve is steep.

### Kubernetes Principles

Kubernetes is an open-sourced container orchestration platform that automates the deployment, scaling, and management of containerized applications.
Provides developers with a framework to easily run distributed systems.

A container is self-contained, relying only on the Linux kernel. Once the container is build, then additional libraries can be added. In addition, containerized applications are not meant to change to different environments after they are built.

In terms of run time, each container needs to implement APIs to help the platform manage the application in the most efficient way possible.
All APIs must be public, as there should be no hidden or private APIs.
In addition, APIs should be declarative meaning the programmer should be able to communicate their desired end result, allowing Kubernetes to find and implement a solution.

#### Declarative configuration

In this approach, developers specify the desired state, but they do not explicitly define how to achieve or reach the desired state. More focused on what the state should be.
The system will determine the most efficient and reliable way to achieve the desired state. These configuration assets are stored in a revision control system and track changes over time.

To use declarative configuration in Kubernetes, create a manifest that describes the desired of an application. Then the control plane will determine how to direct nodes in the cluster to achieve the desired state.

#### The control plane

The Kubernetes control plane is responsible for making decisions about the entire cluster and desired state and for ensuring the cluster's components work together.

Components of the control plane include:

- etcd
  Used as backing store for all cluster data as a distributed database. This key-value store is highly available and designed to run on multiple nodes
- API server
  Acts as the front-end for developers and other components interacting with the cluster. Responsible for ensuring requests to the API are properly authenticated and authorized.
- Scheduler
  A component of the control plane where pods are assigned to run on particular nodes in the cluster.
- Controller manager
  Hosts multiple Kubernetes controllers. Each controller continuously monitors the current state of the cluster and works towards achieving the desired state
- Cloud controller manager
  Embeds cloud-specific control logic. It acts as the interface between Kubernetes and a specific cloud provider, managing the cloud's resources.

### Installing Kubernetes

Kubernetes is not something you download. You decide on the installation type you need based on your programming requirements.

#### Download Docker

#### Enable Kubernetes

1. From the Docker Dashboard, select **Settings**
2. Select **Kubernetes** from the left sidebar
3. Select the checkbox next to **Enable Kubernetes**
4. Select **Apply & Restart** to save the settings
5. Select **Install** to complete the installation process

The Kubernetes server runs as containers and installs the `/usr/local/bin/kubect1` command on your machine.

It's typically the most common way that developers use Kubernetes since Docker Desktop has built-in support for it.

### Pods

In Kubernetes, a **container** is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and system tools.

In the context of Kubernetes, containers are the smallest units of deployment that are scheduled and managed. They are encapsulated within **Pods** which are the fundamental deployment units in a Kubernetes cluster. A Pod can contain one or more containers that need to run together on the same host and share the same network and storage resources, allowing them to communicate with each other using localhost.

#### Pods as logical host

A pod can run one or more closely-related containers which share the same network and storage context. This shared context is much like what you would find on a physical or virtual machine.

- **Tightly coupled containers:** When multiple containers within a Pod are considered tightly coupled.This allows them to exchange data and information efficiently without the need for complex networking configurations.

- **Shared network namespace:** Containers within the same Pod share the same network namespace. Makes it easier for them to communicate using standard inter-process communication mechanisms.

- **Shared storage context:** They can access the same volumes or storage resources. This facilitates data sharing among the containers within the Pod, further enhancing their collaboration.

- **Co-location and co-scheduling:** Ensures that containers can efficiently communicate with each other within the same network and storage context.

- **Ephemeral nature:** Can be easily created or terminated, or replaced based on scaling requirements or resource constraints. However, all containers within the Pod are treated as a single unit in terms of scheduling and lifecycle management.

#### Pods in action

Consider being a dev in charge of a webapp that includes a main web server and a helper component for log processing. The server interacts with the log processor to handle, analyze, and store data in real-time. These two components need to be tightly integrated and should communicate with each other efficiently.

This is where you would use a Pod to encapsulate both the server and log processor containers. They share the same network namespace and share the same storage volumes. This allows the web server to generate logs and the log processor to access and process these logs efficiently.

If the Pod needs to be rescheduled or if it fails, both containers would be dealt with together, maintaining their coupled relationship. The Pod abstracts away the details of the host machine and the underlying infrastructure, allowing you to focus on managing your application.

#### Advantages of Pods

- **Facilitating co-location:** Pods allow multiple containers to be co-located on the same host machine. This is particularly useful for closely related components that need to work together, such as an application and its helper components.
  By running these components in the same Pod, they can be scheduled onto the same machine and managed as a single entity.

- **Enabling data sharing:** Share an IP address and port space. Allows data to be easily exchanged between containers, and allows data to persist beyond the life of a single container, which can be useful for applications that require persistent data storage.

- **Simplifying inter-container communication:** The shared network namespace also simplifies inter-container communication.

#### Single container vs multiple containers

**Single-container pods** typically only contain the primary application or service that the Pod is meant to run. They are straightforward and are commonly used when you have a simple application that requires no additional sidecar containers or closely related helper components.

**Multi-container Pods** have containers that are meant to work together and complement each other's functionalities. Multi-container Pods are appropriate in various scenarios:

- **Sidecar pattern:** The main container represents the primary application, while additional sidecar containers provide supporting features like logging, monitoring, or authentication. The sidecar containers enhance and extend the capabilities of the main application without modifying its code.

- **Proxy patterns:** Can use use a proxy container as an intermediary between the main application container and the external world. Handles tasks like load balancing, caching, or SSL termination, offloading these responsibilities from the main application container.

- **Adapter pattern:** An adaptor container that performs data format conversions or protocol translations. This allows main container to focus solely on its core functionality without worrying about the intricacies of data exchange formats.

- **Shared data and dependencies:** suitable for applications that require data sharing or have interdependent components.

**Tip**
Use a single-container Pod when you have a simple application that does not require additional containers, or when you want to isolate different applications or services for easier management and scaling.

Use multi-container Pods when you have closely related components that need to work together, such as those following the sidecar pattern. This is useful for tasks like logging, monitoring, or enhancing the main application's capabilities without modifying its code. Multi-container Pods are also appropriate for scenarios where multiple containers need to share data or dependencies efficiently.

#### Key terms

- Pod lifecycle: Pods have specific lifecycle phases, starting from "Pending" when they are being scheduled, to "Running" when all containers are up and running, "Succeeded" when all containers successfully terminate, and "Failed" if any container within the Pod fails to run. Pods can also be in a "ContainerCreating" state if one or more containers are being created.

- Pod templates: Pod templates define the specification for creating new Pods. They are used in higher-level controllers like ReplicaSets, Deployments, and StatefulSets to ensure the desired state of the Pods.

- Pod affinity and anti-affinity: Pod affinity and anti-affinity rules define the scheduling preferences and restrictions for Pods. They allow you to influence the co-location or separation of Pods based on labels and other attributes.

- Pod autoscaling: Kubernetes provides Horizontal Pod Autoscaler (HPA) functionality that automatically scales the number of replicas (Pods) based on resource usage or custom metrics.

- Pod security policies: Pod security policies are used to control the security-related aspects of Pods, such as their access to certain host resources, usage of privileged containers, and more.

- Init containers: Init containers are additional containers that run and complete before the main application containers start. They are useful for performing initialization tasks, such as database schema setup or preloading data.

- Pod eviction and disruption: Pods can be evicted from nodes due to resource constraints or node failures. Understanding Pod eviction behavior is important for managing application reliability.

- Pod health probes: Kubernetes supports different types of health probes (liveness, readiness, and startup probes) to check the health of containers within a Pod. These probes help Kubernetes decide whether a Pod is considered healthy and ready to receive traffic.

- Taints and tolerations: Taints are applied to nodes to repel Pods, while tolerations are set on Pods to allow them to be scheduled on tainted nodes.

- Pod DNS: Pods are assigned a unique hostname and IP address. They can communicate with each other using their hostname or service names. Kubernetes provides internal DNS resolution for easy communication between Pods.

- Pod annotations and labels: Annotations and labels can be attached to Pods to provide metadata or facilitate Pod selection for various purposes like monitoring, logging, or routing.

#### Pods and Python

Here is some example code of how to create, read, update, and delete a Pod using Python.

```py
from kubernetes import client, config

# Load the Kubernetes configuration from the default location
config.load_kube_config()

# Alternatively, you can load configuration from a specific file
# config.load_kube_config()

# Initialize the Kubernetes client
v1 = client.CoreV1Api()

# Define the Pod details
pod_name = 'example-pod'
container_name = 'example-container
image_name = 'nginx:latest'
port = 80

# Create a Pod
def create_pod(namespace, name, container_name, image, port):
	container = client.V1Container(
		name=container_name,
		image=image,
		ports=[client.V1ContainerPOrt(container_port=port)],
	)

	pod_spec = client.V1PodSpec(containers=[container])
	pod_template = client.V1PodTemplateSpec(
		metadata=client.V1ObjectMeta(labels={'app': name}), spec=pod_spec
	)

	pod = client.V1Pod(
		api_version='v1',
		kind='Pod',
		metadata=client.v1ObjectMeta(name=name),
		spec=pod_spec,
	)

	try:
		response = v1.create_namespaced_pod(namespace, pod)
		print('Pod created successfully.')
		return response
	except Exception as e:
		print('Error creating Pod:', e)

# Read a Pod
def get_pod(namespace, name):
	try:
		response = v1.read_namespaced_pod(name, namespace)
		print('Pod details:', response)
	except Exception as e:
		print('Error getting Pod:', e)

# Update a Pod (e.g., change the container image)
def update_pod(namespace, name, image):
	try:
		response = v1.read_namespaced_pod(name, namespace)
		response.spec.containers[0].image = image

		updated_pod = v1.replace_namespaced_pod(name, namespace, response)
		print('Pod updated successfully.')
		return updated_pod
	except Exception as e:
		print('Error updating Pod:', e)

# Delete a Pod
def delete_pod(namespace, name):
	try:
		response = v1.delete_namespaced_pod(name, namespace)
		print('Pod deleted successfully.')
	except Exception as e:
		print('Error deleting Pod:', e)

if __name__ == '__main__':
	namespace = 'default'

	# Create a Pod
	create_pod(namespace, pod_name, container_name, image_name, port)

	# Read a Pod
	get_pod(namespace, pod_name)

	# Update a Pod
	new_image_name = 'nginx:1.19'
	update_pod(namespace, pod_name, new_image_name)

	# Read the updated Pod
	get_pod(namespace, pod_name)

	# Delete the Pod
	delete_pod(namespace, pod_name)
```

### Services

Services offer an abstraction layer over Pods. They provide a stable virtual IP and a DNS name for each set of related Pods (like caching layer or database) and these remain constant regardless of the changes in the underlying Pods.

So your web server only needs to know this Service ID or DNS name, saving it from the ordeal of tracking and updating numerous changing Pod IPs.

They also set up load balancing automatically.

#### Types of Services

...

### Deployment

A Deployment is like your application's manager. It's responsible for keeping your application up and running smoothly, even under heavy load or during updates. It ensures your application, encapsulated in Pods, always has the desired number of instances or 'replicas' running.

It's like a blueprint for application's Pods. Contains a **Pod Template Spec** defining what each Pod of your application should look like, including the container specifications, labels and other parameters. The Deployment uses this template to create and update Pods.

Also manages a **ReplicaSet**, a lower level resource that makes sure the specified number of identical Pods are always running. The Deployment sets the desired state, such as the number of replicas, and the ReplicaSet ensure that the current state matches the desired state.
If a Pod fails or is deleted, the ReplicaSet automatically creates new ones.

Deployments support **rolling updates and rollbacks**.

#### Powerful features

Deployments not only help maintain high availability and scalability, but they also provide several powerful features:

- **Declarative updates:** You just specify the desired state of your application and the Deployment ensures that this state is achieved. If there are any differences between current and desired state, K8s automatically reconciles them.

- **Scaling:** You can easily adjust the number of replicas in your Deployment to handle increased or decreased loads. For example, you might want to scale up during peak traffic times and scale down during off-peak hours.

- **History and revision control:** Keep track of changes made to the desired state, providing you with a revision history. useful for debugging, auditing, and rolling back to specific versions.

Typically definded using a YAML file:

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
	app: example-app
  template:
    metadata:
	labels:
	  app: example-app
	spec:
	containers:
	- name: example-container
		image: example-image:latest
		ports:
		- containerPort: 80
```

This Deployment specifies that it should maintain three replicas of the `example-container` Pod template.
The Pods are labeled with `app: example-app`, and the container runs an image tagged as `example-image:latest` on port 80.

The default rolling update strategy will be used for any updates to this Deployment.

#### Deployments and Python

```py
from kubernetes import client, config

def create_deployment(api_instance, namespace, deployment_name, image, replicas):
	# Define the Deployment manifest with the desired number of replicas and container image.
	deployment_manifest = {
    	"apiVersion": "apps/v1",
    	"kind": "Deployment",
    	"metadata": {"name": deployment_name},
    	"spec": {
        	"replicas": replicas,
        	"selector": {"matchLabels": {"app": deployment_name}},
        	"template": {
            	"metadata": {"labels": {"app": deployment_name}},
            	"spec": {
                	"containers": [
                    	{"name": deployment_name, "image": image, "ports": [{"containerPort": 80}]}
                	]
            	},
        	},
    	},
	}

	# Create the Deployment using the Kubernetes API.
	api_response = api_instance.create_namespaced_deployment(
    	body=deployment_manifest,
    	namespace=namespace,
	)
	print(f"Deployment '{deployment_name}' created. Status: {api_response.status}")

def update_deployment_image(api_instance, namespace, deployment_name, new_image):
	# Get the existing Deployment.
	deployment = api_instance.read_namespaced_deployment(deployment_name, namespace)

	# Update the container image in the Deployment.
	deployment.spec.template.spec.containers[0].image = new_image

	# Patch the Deployment with the updated image.
	api_response = api_instance.patch_namespaced_deployment(
    	name=deployment_name,
    	namespace=namespace,
    	body=deployment
	)
	print(f"Deployment '{deployment_name}' updated. Status: {api_response.status}")

def delete_deployment(api_instance, namespace, deployment_name):
	# Delete the Deployment using the Kubernetes API.
	api_response = api_instance.delete_namespaced_deployment(
    	name=deployment_name,
    	namespace=namespace,
    	body=client.V1DeleteOptions(
        	propagation_policy="Foreground",
        	grace_period_seconds=5,
    	)
	)
	print(f"Deployment '{deployment_name}' deleted. Status: {api_response.status}")


if __name__ == "__main__":
	# Load Kubernetes configuration (if running in-cluster, this might not be necessary)
	config.load_kube_config()

	# Create an instance of the Kubernetes API client for Deployments
	v1 = client.AppsV1Api()

	# Define the namespace where the Deployment will be created
	namespace = "default"

	# Example: Create a new Deployment
	create_deployment(v1, namespace, "example-deployment", image="nginx:latest", replicas=3)

	# Example: Update the image of the Deployment
	update_deployment_image(v1, namespace, "example-deployment", new_image="nginx:1.19.10")

	# Example: Delete the Deployment
	delete_deployment(v1, namespace, "example-deployment")
```

#### Additional learning points

Beyond the fundamental concepts, you should be aware of a few additional features and best practices related to Kubernetes Deployments.

- A fresh start: While the default update strategy is rolling updates, Kubernetes also supports a "Recreate" strategy. In the "Recreate" strategy, all existing Pods are terminated before new Pods are created. This strategy may lead to brief periods of downtime during updates but can be useful in specific scenarios where a clean restart is necessary.

- Don’t get stuck: Deployments have a progressDeadlineSeconds field, which sets the maximum time (in seconds) allowed for a rolling update to make progress. If progress stalls beyond this duration, the update is considered failed. This field helps prevent deployments from getting stuck in a partially updated state. Likewise, the minReadySeconds field specifies the minimum time Kubernetes should wait after a Pod becomes ready before proceeding with the next update. This can help ensure the new Pods are fully functional and ready to handle traffic before more updates are made.

- Press pause: Deployments can be paused and resumed to temporarily halt the progress of rolling updates. This feature is helpful when investigating issues or performing maintenance tasks. Pausing a Deployment prevents further updates until it is explicitly resumed.

- It’s alive!: Deployments can utilize liveness and readiness probes to enhance the health management of Pods. Liveness probes determine if a Pod is still alive and running correctly, while readiness probes determine if a Pod is ready to accept traffic. These probes help Kubernetes decide whether to consider a Pod as healthy or not during rolling updates and scaling operations.

If you want to learn more about Kubernetes Deployments and their components, you can explore the provided resources below.

[Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
[Managing Resources](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/)
[Kubernetes ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
[Declarative Application Management in Kubernetes](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/)
[Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

[Rolling Back a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment)

## Deploying Containers to GCP

### Kubernetes on GCP

Kubernetes can be used:

- On a computer
- Directly on GCE
- On GCP using GKE

GKE provides a web-based interface for immediate visibility.
Also handles security and updates.

As usual compare the advantages and disadvantages of the cloud services providers.

### Create a Kubernetes cluster on GCP

A Kubernetes cluster is a fundamental construct within Kubernetes.
It enables the deployment, coordination, and operation of containerised applications at scale.

A cluster is a group of machines grouped to work together, but not necessarily all doing the same tasks.
In a Kubernetes cluster, virtual machines are coordinated to execute all of the functions needed to process requests, such as servinga a web application, running a database, or solving big-data problems.

Each cluster consists of at least one cluster control plane machine, a server that manages multiple nodes. YOu sumbit all of your work to the control plane, and the control plane distributes the work to the node or nodes where it will run.
These worker nodes are virtual machine instances running the Kubernetes processes necessary to make them part of the cluster. They can be in a single zone or spread out all over the world. Depending on the use case, one node might be used for data processing and another for hosting a web server. EAch of these nodes is made up of pods, which are assigned by the control plane. Each pod is made up of one or more containers that work together to execute necessary functions.

#### Setup

- Create a valid CGP account and access to the Google Cloud Console.
- Create a GCP project where yo will deploy your Kubernetes cluster.
- Enable billing for your GCP project to use Google Kubernetes Engine (GKE) as this may involve charges for the resources you use.
- Create a service account for GKE with the necessary permissions to manage resources in your GCP project.
- Install the Google Cloud SDK on your local machine. It provides the necessary tools and commands to interact with GCP resources.
- Install kubectl on your local machine. kubectl is a command-line tool used to interact with Kubernetes clusters.
- Configure firewall rules to allow necessary network traffic to and from your cluster.

#### Creating a GKE Cluster using Google Cloud Console

As you get started working with Kubernetes clusters on Google Cloud Platform (GCP), the first thing to do is create a cluster to work with. Here are the steps to creating a standard cluster:

1.  Log in to Google Cloud Console: Go to https://console.cloud.google.com/ and log in with your Google Cloud account.

2.  Open Google Kubernetes Engine (GKE). In the left-hand navigation menu, select Kubernetes Engine, and then Clusters.

3.  Click Create Cluster to create a new Kubernetes cluster. By default, this will take you to Autopilot cluster. For these instructions, we are setting up a standard cluster, so click Switch to Standard Cluster. For more information on the difference between Standard and Autopilot, see
    Compare GKE Autopilot and Standard
    .

4.  Configure cluster basics. Enter a unique cluster name for your GKE cluster.

5.  Choose a Location type. Zonal is for creating a cluster within a single zone. When selecting this, you will also need to select the zone where your cluster's control plane will run.

Regional is for multi-zone deployment. Deployment across a larger area means higher availability to users. When selecting a regional cluster, you’ll also need to choose the region. By default, three zones will be selected within the chosen region, or you can manually select the zones if you wish.

6.  Configure the node pool. In the Node pool section, specify the desired node count for the initial number of nodes in the default node pool depending on the needs of your application on your Kubernetes cluster. For production clusters, the recommended minimum is usually three nodes.

The maximum number of nodes will depend on the type of application, the expected amount of traffic, and your budget. A maximum of five to ten nodes is a good start while you get a feel for what's needed. As you configure the node pool, there's a cost estimator on the right side of the screen that estimates how much you will pay per month. You can also look over the
GKE pricing for Standard mode
. If you don’t set a maximum that suits your budget, and demand for your application rises sharply, you could get an expensive wake-up call.

Once you have configured the node pool, you can enable Autoscaling by checking the box for Enable cluster autoscaler. Once enabled, Autoscaler will automatically adjust the number of nodes based on resource utilization up to the maximum number of nodes you set for the Node pool.

Finally, choose the machine type for your nodes. There are four machine families:

General purpose machines are suitable for most workloads. These machines balance performance with price.

Compute-optimized machines provide high performance for intensive workloads like artificial intelligence and machine learning, entertainment streaming, and game servers

Memory-optimized machines offer the highest memory configurations. These machines process large data sets in memory in use cases like Big Data analytics.

Accelerator-optimized machines are for very demanding workloads like machine learning (ML) training and inference, in which a neural network makes deductions about new data based on what it has already learned.

For more details on choosing machine families or specific types, see
Choosing the right machine family and type
.

7.  Choose any optional configurations needed. Based on your projects’ specific requirements, you can expand the Node pool section to configure advanced settings including boot disk size, preemptible nodes, node labels, and node locations.

You can also enable networking and security features based on the data governance laws and the level of security you need to maintain for your data. In the Networking section, you can choose the VPC network and subnetwork where your cluster's nodes will be placed. You can also enable Private cluster mode to hide the cluster's master endpoint from the public internet. For pod-level firewall rules, you can define network tags and network policies.

8.  Click the Create button to start creating the GKE cluster.

9.  Wait for cluster creation. GKE will begin creating your cluster based on your specified configuration. The process may take a few minutes.

10. Access and use your cluster. Once the cluster is successfully created, you can click on the cluster name in the GKE dashboard to view its details and manage the cluster.

### Types of Clusters

Kubernetes clusters are designed for scalability and high availability. Nodes can be added or removed as needed as workloads vary, so applications can scale up or down seamlessly.

The control plane is the brain of the cluster, it consists of several components that manage and monitor the cluster's overall state:

- An API server
- A controller manager
- A scheduler
- An etcd: This is a reliable data storage that can be accessed by the cluster.

#### On-premises cluster

Within the organization's own data center or on private infrastructure.
Involves setting up the control plane and worker nodes on owned hardware and the org. is respsonible for cluster maintenance.

Complete control - suitable for situations with specific compliance or data governance requirements.

One of the primary types of Kubernetes clusters.

#### Public cloud managed cluster

Handle the underlying infrastructure management so it is easier for users to deploy and manage Kubernetes clusters on the cloud.

Focus on deploying and managing applications without dealing with the complexities of cluster maintenance.

They can be spread over zones or even regions.

### Deploying Docker Containers on GCP

Docker containers make it simple to deploy applications across different systems and platforms, allowing them to run the same way no matter what environment they are deployed to. This makes it easy to share, test, manage, and deploy applications quickly and reliably.

There are several platforms that allow you to deploy Docker containers, and each has its own set of advantages. Let’s look at some of these, and some considerations when choosing where to deploy containers.

#### Docker containers on Google Cloud Run

If you don’t need a lot of flexibility in your configuration, you might find Google Cloud Run to be a good option. Cloud Run is a fully-managed platform that allows you to run containerised applications without having to manage the underlying infrastructure. The platform offers easy deployment, and automatically manages scaling and routing traffic based on incoming requests. It can scale down to zero, which means it will not use any unnecessary resources if there are no requests. The platform is based on containers, so you can write your code in any language and then deploy it through Docker images.

Cloud Run may be the best choice of platform for projects that do not need a high level of monitoring or configuration, providing that these applications are stateless. A stateless application is one which does not read or store information about their states from one run to the next. Kubernetes Deployment is most commonly used for stateless applications, so Cloud Run is often a great option .

Cloud Run Deploying Docker containers on Cloud Run

To deploy Docker containers on Cloud Run:

1. Build your Docker image and push it to any supported container registry.

2. Deploy the container to Cloud Run using the `gcloud run deploy` command or through the Cloud Run Console.

#### Docker containers on Google Kubernetes Engine (GKE)

Google Kubernetes Engine (GKE) is a container orchestration platform provided by Google Cloud that allows you to automate the process of deploying, managing, and scaling containerised applications. Its streamlined cluster setup process makes deploying Kubernetes clusters fast and straightforward. Many functions are automated as well, including version upgrades and management of SSL certificates.

Although GKE gives you control of all of your configurations, you can choose GKE Autopilot as a fully-managed option. Autopilot uses the Google Cloud Platform (GCP) to automate cluster configuration and to scale the underlying infrastructure based on your parameters and your application's resource requirements. This eliminates the need for manual intervention on your part, and optimizes resources.

GKE is also particularly resilient, continuously monitoring the cluster and its components. Built-in monitoring and logging features provide real-time insights into your application's performance and health. But you don’t have to watch constantly, because GKE features self-healing clusters which automatically detect and replace unhealthy nodes or containers, maintaining the desired state and application availability.

GKE is also convenient for integration with all of the Google Cloud ecosystem, making it easy to leverage other services like Cloud Storage and Google Cloud Identity and Access Management (IAM) to enhance security and governance. GCP itself ensures regular security updates and follows industry best practices to protect the underlying infrastructure and containers.

You may not be ready for the following consideration, but GKE also supports running “stateful” applications. A stateful application is one for which a server saves status and session information. Kubernetes Deployment is commonly used for stateless applications, but you can make an application stateful by attaching a persistent volume to it. If you find yourself needing to run a stateful application, GKE is a great option.

#### Deploying Docker containers on GKE

Now that you’ve heard about GKE’s features, here's how you can deploy Docker containers on GKE:

1. Build your Docker image and push it to any supported container registry, such as Google Container Registry (GCR).

2. Create a Kubernetes Deployment manifest that specifies your configuration settings, including the container image you want to run and the desired number of replicas.

3. Use the GKE Console, or the Kubernetes command line tool kubectl, to deploy the application to your GKE cluster. GKE will handle the orchestration and scaling of the containers for you.

#### Docker containers on Google Compute Engine

Finally, Google Compute Engine is a virtual machine (VM) service that allows you to run your containerized applications on Google's infrastructure. It has lower access time, which tends to translate to faster performance, and offers easy integration with other GCP services.

Perhaps most attractive to its users, Google Compute Engine lets you run code on Google’s infrastructure, but grants you more control over the underlying infrastructure of your VM instances than GKE, and far more than Cloud Run. It is particularly suitable for custom environments and applications requiring specific configurations. But with more control comes more responsibility: when using Google Compute Engine, you are responsible for managing the VM instances and scaling. The platform itself is not as simplified as GKE or Cloud Run, and you cannot use all programming languages.

#### Deploying Docker containers on Google Compute Engine

To deploy Docker containers on Google Compute Engine:

1. Build your Docker image and push it to any supported container registry.

2. Provision a VM instance on Google Compute Engine.

3. Install Docker on the VM.

4. Build your Docker image and copy it to the virtual machine (or pull the image from a container registry).

5. Run the Docker container on the virtual machine using the docker run command.

### Kubernetes YAML Files

Define and configure Kubernetes resources. Serve as a declarative blueprint for your application infrastructure, describing what resources should be created, what images to use, how many replicas of your service should be running and more.

#### Structure of Kubernetes YAML files

- `apiVersion`: indicates the version of the Kubernetes API you're using to create this particular resource.

- `kind`: specifies the type of resource you want to create, such as a Pod, Deployment, or Service.

- `metadata`: provides data that helps identify the resource, including the name, namespace, and labels.

- `spec`: define the desired state for the resource, including the name, namespace, and labels.

Here's a simple file for creating a Deployment of your Python web application:

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-web-app
  labels:
	app: python-web-app
spec:
  replicas: 3
  selector:
    matchLabels:
	  app: python-web-app
  template:
    metadata:
	  labels:
	    app: python-web-app
	spec:
	  containers:
	  - name: python-web-app
	    image: your-docker-repo/python-web-app:latest
		ports:
		- containerPort: 5000
```

#### Key components and fields in YAML files

##### Pods

A Pod is the smallest and simplest unit in the Kubernetes object model.
It represents a single instance of a running process in a cluster and can contain one or more containers. Because it is the simplest unit, a Pod's YAML file typically contains the basic key components highlighted above:

- `apiVersion`: The version of the API you're using

- `kind`: In this case, it's a Pod.

- `metadata`: Includes data about the Pod, like its name and namespace.

- `spec`: Specify the desired state of the Pod, including the containers that should be running

  - Containers: an array of container specifications, including "name", "image", "ports", and "env"
  - Volumes: array of volume mounts to be attached to containers
  - restartPolicy: Defines the Pod's restart policy (e.g. 'Always', "OnFailure", "Never")

##### Deployments

A higher-level concept that manages Pods and ReplicaSets. Allows you to describe the desired state of your application, and the Deployment controller changes the actual state to the desired state at a controlled rate. In addition to the fields mentioned above:

- `spec.replicas`: the number of Pods you want to run

- `spec.selector`: how the Deployment identifies the Pods it should manage

- `spec.template`: the template for the Pods the Deployment creates

##### Services

An abstraction which defines a logical set of Pods and policy by which to access them.

- `spec.type`: defines the type of Service. Common types include ClusterIp, NodePort, and LoadBalancer

- `spec.ports`: define the ports the Service should expose

- `spec.selector`: how the Service identifies the Pods it should manage

##### ConfigMaps

An API object used to store non-confidential data in key-value pairs. In addition to the common fields, include the data field, which is where you define the key-value pairs.

##### Secrets

Similar to a ConfigMap, but stores sensitive information like passwords or API keys.

- `type`: the type of Secret. Opaque (for arbitrary user-defined data), kubernetes.io/service-account-token (for service account tokens), and others.

- `data`: where you define the key-value pairs. Must be base64-encoded.

```yml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  db_username: dXNlcm5hbWU=
  db_password: cGFzc3dvcmQ=
```

#### Parameterizing YAML files with Python

YAML files are the backbone of defining and managing resources. Static YAML files can be limiting, especially when you need to manage different configuration for different environments or deployment scenarios.

Example, customize your rolling update strategy using Python:

```py
from kubernetes import client, config

def update_deployment_strategy(deployment_name, namespace, max_unavailable):
	config.load_kube_config()
	apps_v1 = client.AppsV1Api()

	deployment = apps_v1.read_namespaced_deployment(deployment_name, namespace)
	deployment.spec.strategy.rolling_update.max_unavailable = max_unavailable
	apps_v1.patch_namespaced_deployment(deployment_name, namespace, deployment)

if __name__ == "__main__":
	update_deployment_strategy('my-deployment', 'my-namespace', '25%')
```

[Objects in Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)

[Get Started with Kubernetes (using Python)](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)

### Scaling Containers on GCP

#### Multidimensional Scaling

A combination of horizontal and vertical scaling. Adding more containers to add to the number of resources and increasing the performance of existing or added resources.

#### Elastic Scaling

Automatically increase or decrease the number of servers or the resources allocated to existing servers or both based on the current demand.

Containers can scale down to a fraction of a computer, or scale up to use all the resources of multiple computers. It's important to decide on the type or types of scaling your application will require in advance so you can make sure to have the right service level agreement.

#### Scaling Containers on GCP

GCP has massive amounts of computers and components at the ready, so the platform lets you avoid a delayed response to scaling needs.

Resources are shared between GCP users, so you pay less during off hours when app requires fewer resources.

Scaling is easy to automate using the dashboards in any of GCP's platforms.
The base price for a Kubernetes cluster may be a lot lower than the price when it operates at scale.

### GCP Networking and Load Balancing

#### Why does knowing GCP infrastructure matter?

Google network infrastructure consists of three main types of networks:

- **A data center network**, which connects all the machines in the network together.

- **A software-based private wide area network (WAN)** that connects all data centers together. The software-based private WAN is particularly beneficial for distributed applications that require fast and secure data transfer between different parts of the system, regardless of where they are located.

- **A software defined public WAN** that is designed for user-facing traffic entering the Google network. This network infrastructure is optimized for high performance and low latency, ensuring that users can access your applications quickly and smoothly, no matter where they are in the world.

#### Pods, clusters, and GCP

A VCP is a global, private network - partitioned from the broader GCP network - that facilitates communication between the Pods in your cluster, allowing them to interact with each other as if they were on the same local network, even thought they might be running on different machines.

The VPC not only provides an isolated network for the Kubernetes cluster, but it also enables secure communication with other GCP resources.
For instance, your Pods might need to interact with a database or a storage service hosted elsewhere on GCP. The VPC ensures that these interactions can occur securely and efficiently over the private network, without exposing the traffic to the public internet.

#### Key components of a GCP VCP network

EAch VPC is divided into subnets, which are regional resources. Each subnet has a specific IP range, and you can have multiple subnets in a single VPC. When you create a Kubernetes cluster in a GCP VPC, you assign each node in the cluster an IP address from the subnet's IP range.

GCP also allows you to define firewall rules at the VPC level. These rules control inbound and outbound traffic to your resources. For example, you might have a rule that allows incoming HTTP traffic to your web servers, or a rule that blocks all outbound traffic to a specific IP range.

A GCP VPC network has several key components:

- **IP ranges:** Each VPC network and its subnets have associated IP ranges. These ranges are used to assign IP addresses to resources within the network and subnets.

- **Routes:** Routes determine the path that network traffic takes to reach an instance. By default, a VPC network has an implied route to the internet default gateway, allowing instances with external IP addresses to reach the internet.

- **Peering:** VPC network peering allows you to connect two VPC networks, potentially across different projects,a s if they were one. This is useful for sharing resources across projects or organizations.

- **Firewall rules:** As mentioned earlier, firewall rules control the traffic to and from instances in your VPC network. They are a crucial part of securing your GCP environment.

#### Other network services

- **Cloud Domain Name System (DNS):** Google cloud DNS is a scalable, reliable, and managed authoritative Domain Name System service that provides high DNS query speeds and low latency for your applications. If your Kubernetes application needs to map domain names to IP addresses (for example, if it's a web application that needs to be accessible via a custom domain), Cloud DNS can be a useful service.

- **Cloud Network Address Translation (NAT):** Cloud NAT allows instances without a public IP address (like your Kubernetes Pods) to access the internet, while not allowing inbound connections from the internet. This can be useful if your application needs to reach external APIs or services but you don't want to expose your application to incoming internet connections.

- **Cloud Load Balancing:** Google Cloud Load Balancing allows you to distribute traffic across your application instances, which can be located in multiple regions. This can help increase the availability and reduce the latency of your application.

#### A closer look: Load Balancing

Distribute incoming traffic among multiple instances of your application, helping to ensure that no single instance bears too much load. This can improve the responsiveness and availability of your application, especially during times of high traffic.

- **Global and regional load balancing**: GCP offers both global and regional load balancing. Global load balancing automatically directs user traffic to the nearest instance of your application, improving latency. Regional load balancing distributes traffic within a specific region.

- **HTTP(S), TCP, and UDP load balancing**: GCP supports load balancing for HTTP(S), TCH, and UDP traffic, allowing you to choose the right option based on your application's needs.

- **Managed Instance Groups**: GCP's managed instance groups work hand-in-hand with its load balancers. They maintain a pool of instances that can automatically scale up or down based on demand, and the load balancer distributes traffic across these instances.

- **Integration with Kubernetes**: GCP's load balancers can be easily integrated with Google Kubernetes Engine (GKE), allowing you to distribute traffic across the Pods in your Kubernetes cluster.

### Protect containers on GCP

#### Security challenges and considerations

You need to secure the container runtime, to protect the underlying host system, and to manage the application dependencies that are packaged within the container.

[Zero Trust model](https://www.nist.gov/publications/zero-trust-architecture) - assuming no trust by default and only granting permissions as necessary.

Using Virtual Private Clouds (VPCs) and properly firewalled subnets mean you can guarantee at the network level that things do not come into contact with other things they shouldn't.

##### Shared Responsibility Model

GCP is responsible for:

- **Infrastructure security:** the physical security of data centers, the security of the hardware and software that underpin the service, and the networking infrastructure of the container orchestration service, GKE.

- **Operational security:** Ensuring GKE is operational and available for customers to use. Protection against attacks like DDoS attacks.

- **Software supply chain security:** Tools such as Binary Authorization for Borg, which can enforce signature verification checks on container images before they are deployed.

You are responsible for:

- **Workload security:** the applications and data you run on GKE. Implementing appropriate access controls, protecting sensitive data, and managing cryptographic keys

- **Network security:** Securing the network connections between workloads. Configuring firewalls, managing network policies, and securing endpoints.

- **Identity and access management:** Access to your GKE resources. Managing user identities, assigning appropriate roles and permissions, strong authentication methods.

- **Software supply chain security:** Use the tools available effectively. Ensuring container images are securely built, stored, and signed.

#### Security Features and Best Practices

Security is usually reactive, zero trust approach lowers the attack surface for your cloud builds, giving less ways for attackers to get in.

- **Use minimal base images:** The fewer components and services running in your container, the fewer potential vulnerabilities.
  Use base images that only contain the essential components needed for your application.
  Closing all IP addresses and ports except those that are necessary, closing data containers off to the outside internet so only parts of the application can reach them, and so on.
  This can mean only opening up containers on VPCs to other VPCs or members of the same subnet.

- **Regularly update and patch:** Regularly update containers and dependencies to ensure you have the latest security patches.
  It can reduce the risk.

- **Implement vulnerability scanning:** Use tools like Googles Container Analysis and Container Threat Detection to regularly scan container for known vulnerabilities.

- **Use runtime security:** Use a tool like gVisor to provide sandboxing for containers at runtime, isolating them from the host kernel and reducing the risk of a container escape vulnerability.

- **Implement access controls:** Use Identity and Access Management to control who can do what with your containers and other resources.

- **Encrypt sensitive date:** Use Google's key Management Service (KMS) to encrypt sensitive data in containers.

- **Monitor and log activity:** Use Google's Cloud Audit Logs to keep track of who did what, when, in you Google Cloud environment. Logs are super important to have on from the start. If you wait for an incident to happen to necessitate turning on logs, it may be too late!

- **Use binary authorization:** A deploy-time security control that ensures only trusted images are deployed in your environment.

#### More information:

- [Exploring Container Security](https://cloud.google.com/blog/products/containers-kubernetes/exploring-container-security-let-google-do-the-patching-with-new-managed-base-images)
- [Google Cloud Security Command Center](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview)
- [Shared Responsibilities and Shared Fate on Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
- [GKE shared responsibility | Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility)

## Glossary of Terms

Artifact: A byproduct of the software development process that can be accessed and used, an item produced during programming

Container registry: A storage location for container images, organized for efficient access

Container repository: A container registry that manages container images

Docker: An open-source tool used to build, deploy, run, update, and manage containers

Pod: A group of one or more containers that are scheduled and run together

Registry: A place where containers or artifacts are stored and organized

Kubernetes: An open-source platform that gives programmers the power to orchestrate containers
