# Configuration Management and Monitoring

## Automating with Configuration Management

### What is Scale?

Being able to **scale** what we do means that we can keep achieving larger impacts with the same amount of effort.

For example, if a web application is scalable, it can handle an increase in the number of people using it by adding more servers to serve requests.

A scalable system is a flexible one.

To check the scalability, ask questions like:

- Will adding more servers increase the capacity of the service?
- How are new servers prepared, installed, and configured?
- How quickly can you set up new computers to get them ready to be used?
- Could you deploy a hundred servers with the same IT team that you have today? Or would you need to hire more people to get it done faster?
- Would all the deployed servers be configured exactly the same way?

Automation is an essential tool for keeping up with the infrastructure needs of a growing business.

- Is essential for scale. Allows a small IT team to be in charge of hundreds or even thousands of computers.

### What is Configuration Management?

Configuration includes everything from the current operating system and the applications installed to any necessary configuration files or policies, including anything else that's relevant for the system to do its job.

A managed configuration means using a configuration management system to handle all of the configuration of the devices in your fleet, also known as nodes.

Unmanaged configurations seem inexpensive at a small scale.
Can log into each device and make changes by hand when necessary.

Large deployments become easier to work with because the system will deploy the configuration automatically no matter how many devices you're managing.

When you need to make a change in one or more computers, you don't manually do it. Instead, you edit the configuration management rules and then let the automation apply those rules in the affected machines. This way the changes you make to a system or group of systems are done in a systematic, repaeatable way.

Being repeatable is important because it means that the results will be the same on all the devices.

Configuration management ssystems often also have some form of automatic error correction built in so that they can recover from certain types of errors all by themselves.

You need to pick the configuration management system that best fits your needs and adapt accordingly, if necessary.

### What is Infrastructure as Code?

Model the behavior of infrastructure in files, that can be tracked by version control.

> When all the configuration necessary to deploy and manage a node in the infrastructure is stored in version control.

Can use automation to deploy the configurations. Computers are treated as interchangeable resources. If the machine stops working, can deploy a replacement quickly.

Doesn't depend on a human repeating all the steps. Making it consistent.

Can also run automated tests.
Deploy flexible and scalable system.

### IaC Options

Puppet serves as a robust and well-established solution, several other options bring their unique strengths to the table.

#### Terraform

Specializes in provisioning and managing infrastructure resources across various cloud providers.

Allows you to define your desired infrastructure state, and Terraform takes care of translating this into concrete resources.

This approach enables you to codify youur infrastructure configurations, fostering version control, collaboration, and reproducibility.

Manages a wide spectrum of resources, from virtual machines to databases, across multiple cloud environmentss.

#### Ansible

Unlike Puppet, which revolves around agent-based communication, Ansible adopts an agentless architecture that relies on SSH or other remote APIs for system management.

This simplifies deployment and reduces the overhead of maintaining agents on target nodes. Ansible employs a simple and human-readable YAML syntax to define playbooks, which describe the desired state of systems.

## Introduction to Puppet

### What is puppet?

Puppet is the current industry standard for managing the configuration of computers.

Puppet is typically deployed using a client-server architecture.

- The client is known as the Puppet agent.
- The service is knows as the Puppet master.

The agent connects to the master and sends a bunch oof facts that describe the computer to the master.

The master then processes this information, generates the list of rules to apply to the device, and send the list back to the agent.

The agent is in charge of making necessary changes on the computer.

Available cross-platform.

A simple example of rules:

```
class sudo {
	package { 'sudo':
		ensure => present,
	}
}
```

This says that the package 'sudo' should be present on every computer where the rule gets applied.

On Windows there's an extra attribute that tells where the installer file is located.

Puppet can add, remove, or modify configuration files stored in the system. Can enable, disable, start, or stop services.

### Puppet Resources

Resources - the basic unit for modeling the configuration that we want to manage.

Each resources specifies one configuration we're trying to manage, like a service, package or a file.

```
class sysctl {
	# Make sure the directory exists, some distros don't have it
	file { '/etc/sysctl.d':
		ensure => directory,
	}
}
```

- Makes sure that `etc/systcl.d` exists and is a directory.

When declaring a resource, it goes in a block that starts with the resource time.

title then colon, followed by attributes.

```
class timezone {
	file { '/etc/timezone':
		ensure => file,
		content => "UTC\n",
		replace => true,
	}
}
```

- file, not a directory
- set contents to UTC
- contents will be replaced if the file exists.

Defining a file resource. This resource type is used for managing files and directories.

Can set file owner, modification etc.

The resources are the desired state. Puppet makes that a reality using Providers.

- Depends on the resource defined and the environment.

### Puppet Classes

Classes can collect the resources needed to achieve a goal.

Example - a class that installs a package, sets the contents of a configuration file, and starts the service provided by that package.

```puppet
class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => 'puppet:///modules/ntp/ntp.conf'
    replace => true,
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
  }
}
```

- All are related to the NTP (network time protocol).
- Make sure the ntp package is always upgraded to the latest version
- Set the contents of the config file using the source attribute, which means that the agent will read the required contents from the specified location
- We want the NTP service to be enabled and running.

Grouping all resources together makes it easier to modify and understand.

### Extra Resources

## The Building Blocks of Configuration Management

### What are Domain-specific Languages?

Can do more complex operations using Domain-Specific Language (DSL)

Facts - variables that represents the characteristics of the system.

Used to calculate the rules to be applied.

There are built-in facts, and we can make our own.

```
if $facts['is_virtual'] {
	package { 'smartmontools':
		ensure => purged,
	}
} else {
	package { 'smartmontools':
		ensure => installed,
	}
}
```

This package is used to monitor hard drives...

### The Driving Principles of Configuration Management

Puppet is declarative - we don't write out the steps, but the end goals we wish to achieve. We state what the configuration should be.

idempotent - action that can be performed over and over again without changing the system after the first time the action was performed with no unintended side effects.

```
file { '/etc/issue':
	mode => '0644',
	conte4nt => "internal system \l \n"
}
```

idempotent - can fail halfway through its execution and can be run again with no issues.

The `exec` resource is an exception to the idempotency. It runs commands for us.

Example, moving a file -> if you run the same code twice, an error will occur because the file no longer exists in that space.

Use the `onlyif` to help keep actions idempotent.

```
exec { 'move example file':
  command => 'mv /home/user/example.txt /home/user/Desktop',
  onlyif => 'test -e /home/user/example.txt',
}
```

Checks if the file exists and then moves it.

**Test and repair** - actions are taken only when they are necessary to achieve a goal. First test to see if the resource being managed actaully needs to be modified.

Puppet is stateless - Each puppet run is independent of the previous one.
Just collects the current facts...

### More Information About Configuration Management

[http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html](http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html)

## Deploying Puppet Locally

### Applying Rules Locally

Can be also used as a standalone system. Useful for testing.

Create a Manifest - file where all the rules to be applied are stored. They end with a `.pp` extension.

tools.pp

```pp
package { 'htop':
	ensure => present,

}
```

```bash
sudo apt install puppet-master
#(...)
#Processing triggers for systemd


vim tools.pp
htop
#-bash: /usr/bin/htop: No such file or directory
```

```bash
sudo puppet apply -v tools.pp
```

Catalog - the list of rules that are generated for one specific computer once the server has evaluated all variables, conditionals, and functions.

In this case, the catalog will be the same as the code because there are no conditionals, variables, and functions.

### Managing Resource Relationships

```bash
vim ntp.pp
class ntp {
	package { 'ntp':
	  ensure => latest,
	}
	file { '/etc/ntp.conf':
	  source => '/home/user/ntp.conf',
	  replace => true,
	  require => Package['ntp'],
	  notify => Service['ntp'],
	}
	service {'ntp':
	  enable => true,
	  ensure => running,
	  require => File['/etc/ntp.conf'],
	}
}
include ntp
```

The configuration file requires the `ntp` package and the `ntp` service requires the configuration file.

So Puppet knows before starting the service, the configuration file needs to be correctly set.

`require => Package['ntp']`

And before setting the configuration file, the package needs to be installed.

Also specified that the `ntp` service should be notified if the configuration file changes. - `notify => Service['ntp']`

This means that the service will get restarted if the configuration settings are changed.

The puppet manifests usually use different resources that are related to each other.

> Write resource types in lowercase when declaring them, but capitalize them when referring to them from another resource's attribute.

At the end, we include ntp...

Typically, the class is defined in one file and included in another.

```bash
sudo puppet apply -v ntp.pp
```

### Organizing Puppet Modules

A collection of manifests and related data.

Group things under a sensible topic.

Stored in a directory called manifests, then different stuff goes in different folders.

- Files
  - files that are copied into the client machines without any changes
- Templates
  - files that are preprocessed before they'be been copied into the client machines.
  - can include values that get replaced after calculating the manifests, or sections that are only present if certain conditions are valid.

Start with a simple module - just one manifest in the Manifest directory.

- `init.pp` define a class with the same name as the module that you're creating.

## Deploying Puppet to Clients

### Setting up Puppet Clients and Servers

```
sudo puppet config --section master set autosign true
```

- Configures Puppet to automatically sign the certificate requests of added nodes.

```
ssh webserver
sudo apt install puppet
sudo puppet config set server ubuntu.example.com
```

- `ssh webserver` allows you to ssh into a machine called webserver.
- `sudo apt install puppet` installs the puppet agent
  `sudo puppet config set server ubuntu.example.com` configures Puppet to talk to the server on ubuntu.example.com

```
sudo puppet agent -v --test
```

Tests the connection between the Puppet agent on the machine and the Puppet master.
The `-v` command indicates the output should be verbose.
`--test` indicates it's a test run.

```
vim /etc/puppet/code/environments/production/manifests/site.pp

node webserver {
	class { 'apache': }
}

node default {}
```

- View and create the `site.pp` manifest file. Install Apache on the webserver nodes, define the node with the `node webserver` command, and then include the Apache class without any parameters.
  Then define the default node definition with code `node default{}` - No classes yet

```
sudo systemctl enable puppet
```

- Use the `systemctl` command to enable the puppet service so that Puppet agent is started whenever the machine reboots.

```
sudo systemctl start puppet
sudo systemctl status puppet
```

- starts the puppet service and checks its status.
