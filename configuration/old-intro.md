# Automating With Configuration Management

## Introduction to Automation at Scale

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

Automation is an essential took for keeping up with the infrastructure needs of a growing business.

- Is essential for scale. Allows a small IT team to be in charge of hundreds or even thousands of computers.

### What is Configuration Management?

A managed configuration means using a configuration management system to handle all

### What is Infrastructure as Code?

Model the behavior of infrastructure in files, that can be tracked by version control.

> When all the configuration necessary to deploy and manage a node in the infrastructure is stored in version control.

Can use automation to deploy the configurations. Computers are treated as interchangeable resources. If the machine stops working, can deploy a replacement quickly.

Doesn't depend on a human repeating all the steps. Making it consistent.

Can also run automated tests.
Deploy flexible and scalable system.

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

```
class sysctl {
	# Make sure the directory exists, some distros don't have it
	file { '/etc/sysctl.d':
		ensure => directory,
	}
}
```

```
class timezone {
	file { '/etc/timezone':
		ensure => file,
		content => "UTC\n",
		replace => true,
	}
}
```

Defining a file resource. This resource type is used for managing files and directories.

Ensures that it exists and is a directory.

### Puppet Classes

### Puppet Resources

## The Building Blocks of Configuration Management

### What are Domain-specific Languages?

### The Driving Principles of Configuration Management

### More Information About Configuration Management

```

```
