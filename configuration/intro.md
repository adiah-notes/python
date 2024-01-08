# Configuration Management and the Cloud

## Automation in the cloud

Service is running somewhere else that is reachable over the internet.

Software as a Service (SaaS) -> cloud provider manages everything related to the service for you.

Sometimes we need to develop our own service

PaaS - cloud provider offers a preconfigured platform.

If you need a high level of control IaaS - provider supplies only the bare bones. They won't care what you're using the vms for.

- Compute Engine
- Azure Compute

Need to consider regions. Regions contain zones which contain one or more data centres.
Select regions and zones closest to your users.

Latency.
Legal and policy issues.
Close to physical dependencies.

### Scaling in the Cloud

It's easy to scale deployments in the cloud. No need to buy the hardware, and install.

Capacity is how much the service can deliver.

Tied to the number and size of the servers involved.
Depends on what the system is doing:

- storing data - size of memory
- queries per second

#### Scaling.

Upscaling and downscaling.

Changing the capacity of the service.

Can scale horizontally or vertically in the cloud

- Horizontally - add more nodes to the pool of a specific service.
  Add more servers to increase your capacity.

- Vertically - Make the nodes bigger. The resources assigned to the nodes: disk space, cpu, memory.

Can be done automatically or manually:

- Automatic - Use metrics to automatically increase or decrease the capacity of the system.

- Manual - changes are controlled by humans.

Usually easier for smaller companies to use manual for simple systems.

### Evaluating the Cloud

Give up some control to the service provider.

SaaS - gives the provider complete control over how the software runs.

To create our own applications. Platforms as a service -> we are in control of the code.

Know what kind of support is available.

It is great to not worry about maintaining the machines.

You don't know what security measures are in place, however.
REsponsibility to follow reasonable security practices as cloud users.

Use reasonable judgement to protect the machines that we deploy, whether that's on physical servers running on-premise or on virtual machines in the Cloud.

Security might be expensive to implement. Check if it's necessary for your specific needs.

### Migrating to the Cloud

**Lift and Shift**
Lifting server and moving to a new location.
IaaS -
Shifting from on-premise to on cloud.

The core configuration stays the same. The same software is used whether on the premise or on the cloud.
Easy if using version control (ithink) for configs.

PaaS -
Don't need to worry about any tasks about the machine setup.
Managed Web Applications - only worry about the code for the web app, not the framework for running it.

Amazon Elastic Beanstalk, Microsoft App Service, Google App Engine. Requires code changes.

**Containers**
Applications that are packaged together with their configuration and dependencies.
Allows the applications to run the same way, no matter the environment they are in.
Makes migrations super easy.

- Public cloud - the cloud services provided to you by a third party.
  Cloud providers
- Private cloud - when your company owns the services and the rest of your infrastructure, whether that's on-site or in a remote data center
  It's just for your company
- Hybrid cloud - a mixture of both public and private clouds
  Some workloads are run on your own, while others are on hardware provided by providers.
  The important thing is to make sure everything is integrated smoothly.
- Multi-cloud - mix of private and public across different vendors.

## Managing Instances in the Cloud

### Spinning up VMs in the Cloud

Using the Google Cloud platform in this course.

Good idea to familiarize yourself with the console for the specific provider.

Things to set up...

- Name - identify the instance
- Region - close to users for better performance
- Zone
- Machine Type - configure vm to fit your needs. How many processors and how much memory
- Boot disk - contains the os it runs. How much space and which os.

Can use the web interface and the cli.

Web gui doesn't scale well or work with automation.

Reference Images - store the contents of a machine in a reusable format.
Templating - The process of capturing all of the system configuration to let us create VMs in a repeatable way
Disk image - a snapshot of a virtual machine's disk at a given point in time.

### Creating a New VM Using the GCP Web Ui

Go to console.cloud.google.com.

Create a project so that VMs are associated to that project.
`First Cloud Steps`

Compute Engine -> VM instances.

Press the create button.

`linux-instance`

Machine Type ->

Then select the disk OS and size...

Can choose an ubuntu. Can choose standard or ssd

Can copy the command line...

### Customizing VMs in GCP

ssh into virtual machine

```
git clone https://github.com/blue-kale/hello
```

Configure app as service for webapp to run automatically.

Copy the script file to `sudo cp hello_cloud.py /usr/local/bin`
and the service file to `sudo cp hello_cloud.service /etc/systemd/system`
`sudo systemctl enable hello_cloud`

Get a list of running processes : `ps ax | grep hello`

How to update the app:

- Create a different reference image each time there is a new version
- Add a configuration management system

Can use puppet;

`sudo apt install puppet`

### Templating a Customized VM

Stop the instance.
Click on its name and then the boot disk.

Create a snapshot or an image.

Click create image..
Enter name and click create.

Go to instance templates and click create new...

change the boot disk to use the image we created. It's in custom images.
Enable http

Can use it now.

Go the vm instances and create instance.

create from template. Just change the name and leave everything else...

For a batch action, use the cli.

use the gcloud

`gcloud init`
Choose the default project, region and zone.

```
gcloud compute instances create --source-instance-template webserver-template ws1 ws2 ws3 ws4 ws5
```

### Extra REading

[https://cloud.google.com/compute/docs/create-linux-vm-instance](https://cloud.google.com/compute/docs/create-linux-vm-instance)

[https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template)](https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template)

[https://cloud.google.com/sdk/docs)](https://cloud.google.com/sdk/docs)

## Automating Cloud Deployments

Preparation. Set up services so that new nodes can be added.

Load balancer - ensures that each node receives a balanced number of requests

STrategies

- round robin - give each node one request
- always select the same node for requests coming from the same origin
- selecting the node closest to the requestor
- selecting the one with the least current load

Autoscaling allows the service to increase or reduce capacity as needed, while the service owner only pays for the cost of the machines that are in use at any given time.

Since nodes can be shut down, their disks can disappear, so they should be considered as ephemeral.
For data persistance, create separate storage solutions to hold that data.

### What is Orchestration?

The automated configuration and coordination of complex IT systems and services.

Usually use APIs that can be used within scripts.

### Cloud Infrastructure as Code

Lets us create repeatable structures.

Using version control.

Terraform, uses its own domain-specific language lets us specify what our cloud infrsatsurtucre should look like, but it can interact with different cloud provider.

### More Reading

[https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform](https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform)

[https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances)

Official documentation: [https://cloud.google.com/load-balancing/docs/https](https://cloud.google.com/load-balancing/docs/https/)

[https://geekflare.com/gcp-load-balancer/](https://geekflare.com/gcp-load-balancer/)

Hybrid Setups:

[https://blog.inkubate.io/create-a-centos-7-terraform-template-for-vmware-vsphere/](https://blog.inkubate.io/create-a-centos-7-terraform-template-for-vmware-vsphere/)

[https://www.terraform.io/docs/enterprise/before-installing/reference-architecture/gcp.html](https://www.terraform.io/docs/enterprise/before-installing/reference-architecture/gcp.html)

[https://www.hashicorp.com/resources/terraform-on-premises-hybrid-cloud-wayfair](https://www.hashicorp.com/resources/terraform-on-premises-hybrid-cloud-wayfair)

## Software on the Cloud

### Managing Cloud Instances at Scale

- Figure out how applications and components work
- Make sure every tool and application runs reliably
- Troubleshoot problems and compatibility issues
- Account for scaling up or scaling back

### Storing Data in the Cloud

Hw much, the location, how often the data changes and the budget.

The local disks attached to the VMs are examples of `block storage`. It resembles physical machines using physical hard drives.

The os of the VM will create and manage a file system on top of the block storage. The difference is that the disks are virtual so the information is easy to move around.

Persistent storage is used for instances that are long lived and need to keep data across reboots and upgrades.

Ephemeral storage is used for instances that are temporary and only need to keep local data while they're running.

- great for temporary files that the service needs while running.

`Shared file` system solutions - the data can be accessed through network system protocols like NFS or CIFS. Connect many different systems to the same file system

If you need to store application data - `Object storage` or blob storage.

- Lets you place and retrieve objects in a storage bucket.
  Everything in a bucket has a unique name, there is no file system. You just ask for objects by name.
- Need to use API
- SQL
  - standard
- NoSQL
  - can be distributed

It's for a cost.

- throughput
  - the amount of data that you can read and write in a given amount of time
  - can be different for reading and writing
- IOPS (Input/Output Operations Per Second)
  - how many reads or writes you can do in one second, no matter how much data you're accessing
- latency

  - the amount of time it takes to complete a read or write operation

### Load Balancing

More than one machine

- horizontal upscaling
- distribute instances geographically
- create backups

**Round Robin DNS**

**Sticky sessions** - all requests from the same client always go to the same backend server.
Only use it if you really need it, it can make migrating and maintaining service difficult.

**Content Delivery Networks (CDNs)**

- Make up a network of physical hosts that are geographically located as close to the end users as possible

Usually in the same datacentre as the user.
They work by caching content super close to the user.

### Change Management

Most of the time when something stops working, it's because something changed.

We have to make changes to keep things updated and bug-free.
So we make the changes in a controlled and safe way.

This is called change management.

Improving the safety of our changes:

- Step one: Make sure they're well-tested.
  running unit tests and integration tests, and then running these tests whenever there's a change.

  Continuous Integration (CI) - build and test code every time there's a change

  Ideally, should work for changes that are being reviewed, so you can catch problems before they're merged.

  - Jenkins
  - Travis CI

  Continuous Deployment (CD) - automatically deploy the results or build artifacts.

  Lets you control the deployment with rules.
  Eg - configure our CD system to deploy new builds only when all of the tess have passed successfully.

  Can actually push to different environments based on some rules.

  You could have the CD system configured to push new changes to the test environment. Then check that the service is still working correctly there, then manually tell the deployment system to push the same changes to production.

  Might set up different environments if the project is large.

  If there's something to test in production with real customers
  use A/B testing.

  In A/B testing, some requests are served using one set of code and configuration, A, and other requests are served using different set of code and configuration, B.

  So you can start with like 1% of requests going to B, an experimental setup, and slowly ramp up the percentage.

  Check if A or B is working better.

### Understanding Limitations

### More About Cloud Providers

- [https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas](https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas)
- [https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- [https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits)

### Glossary of Terms

Terms and definitions from Course 5, Module 1
A/B testing: A way to compare two versions of something to find out which version performs better

Automatic scaling: This service uses metrics to automatically increase or decrease the capacity of the system

Autoscaling: Allows the service to increase or reduce capacity as needed, while the service owner only pays for the cost of the machines that are in use at any given time

Capacity: How much the service can deliver

Cold data: Accessed infrequently and stored in cold storage

Containers: Applications that are packaged together with their configuration and dependencies

Content Delivery Networks (CDN): A network of physical hosts that are geographically located as close to the end users as possible

Disk image: A snapshot of a virtual machine’s disk at a given point in time

Ephemeral storage: Storage used for instances that are temporary and only need to keep local data while they’re running

Hot data: Accessed frequently and stored in hot storage

Hybrid cloud: A mixture of both public and private clouds

Input/Output Operations Per Second (IOPS): Measures how many reads or writes you can do in one second, no matter how much data you're accessing

Infrastructure as a Service (or IaaS): When a Cloud provider supplies only the bare-bones computing experience

Load balancer: Ensures that each node receives a balanced number of requests

Manual scaling: Changes are controlled by humans instead of software

Multi-cloud: A mixture of public and/or private clouds across vendors

Object storage: Storage where objects are placed and retrieved into a storage bucket

Orchestration: The automated configuration and coordination of complex IT systems and services

Persistent storage: Storage used for instances that are long lived and need to keep data across reboots and upgrades

Platform as a Service (or PaaS): When a Cloud provider offers a preconfigured platform to the customer

Private cloud: When your company owns the services and the rest of your infrastructure

Public cloud: The cloud services provided to you by a third party

Rate limits: Prevent one service from overloading the whole system

Reference images: Store the contents of a machine in a reusable format

Software as a Service (or SaaS): When a Cloud provider delivers an entire application or program to the customer

Sticky sessions: All requests from the same client always go to the same backend server

Templating: The process of capturing all of the system configuration to let us create VMs in a repeatable way

Throughput: The amount of data that you can read and write in a given amount of time

Utilization limits: Cap the total amount of a certain resource that you can provision
