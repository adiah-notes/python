# Managing Data and Processes

## Data Streams

### Reading Data Interactively

`input` function

hello.py

```py
#!/usr/bin/env python3

name = input("Please enter your name: ")
print(f"Hello, {name}")
```

Always gives a string.

seconds.py

```py
def to_seconds(hours, minutes, seconds):
	return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"

while(cont.lower() == 'y'):
	hours = int(input("Enter the number of hours: "))
	minutes = int(input("Enter the number of minutes: "))
	seconds = int(input("Enter the number of seconds: "))

	print(f"That's {to_seconds(hours, minutes, seconds)} seconds.")
	print()
	cont = input("Do you want to do another conversion? [y to continue] ")

print("Good bye!")
```

### Standard Streams

I/O streams are the basic mechanism for performing input and output operations in your programs.

STDIN -> standard in (like text from the keyboard)  
STDOUT -> standard out (like printing to the screen)  
STDERR -> standard error

### Environment Variables

Shell -> Command line interface used to interact with the os.

use the `env` command to see a list of variables.

`echo $PATH` -> where to look for executable files to call programs.

variables.py

```py
#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
```

`os.environ` to access evironment variables.

The `get` dictionary method allows you to access dictionary variables, but doesn't give an error if they don't exist, can specify what value to return if a key isn't present.

Set a variable with `export`.

`export FRUIT=Pineapple`

### Command-Line Arguments and Exit Status

Parameters that are passed to a program when it's started.

Use the `argv` list in the `sys` module.

parameters.py

```py
#!/usr/bin/env python3

import sys
print(sys.argv)
```

```
./parameters.py # []
```

Value returned by a program to shell.

0 = success  
anything else means an error.

`$?` gives the exit code of the last command.

create_file.py

```py
import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
	with open(filename, 'w') as f:
		f.write("New file created \n")
else:
	print(f"Error, the file {filename} already exists!")
	sys.exit(1)
```

`sys.exit(value)` can be used to exit.

## Python Subprocesses

### Running System Commands in Python

`ICMP` packets to a host. Can run the `ping` command. Sometimes it's easier to use a system command.

`subprocess` module.

```py
import subprocess
subprocess.run(["date"])

subprocess.run(["sleep", "2"])
```

The parent process is blocked until the child process is done. any elements after the command are the arguments.

```py
import subprocess

result = subprocess.run(["ls", "this_file_does_not_exist"])

print(result.returncode)
```

The output of `run` command is printed to the screen. So if you only want to know if the command was successful, eg changing permissions for a bunch of files.

If you want to capture the result and then operate with the results, need something else.

### Obtaining the Output of a System Command

Tell the `run` function to capture it for us.

Eg stats on which users are logging on for a day.

`who` -> prints the users currently logged into a computer.

Set `capture_output`to true when calling the `run` function.

`host` command -> converts a host name to an IP address and vice versa.

```py
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)

print(result.stdout)

```

the `b` tells that the string is an array of bytes, not a proper string.
`decode` method -> transform bytes to string.

```py
print(result.stdout.decode().split())
```

```py
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
```

### Advanced Subprocess Management

myapp.py

The usual strategy for modifying the environment of a child process is to first copy the environment seen by our process, do any necessary changes, and then pass that as the environment the child process will see.

```py
import os
import subprocess

my_env = os.environ.copy()
# Adding a directory to the path
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

# Call the myapp command with the updated value of path
result = subprocess.run(["myapp"], env=my_env)
```

can also use the `cwd`. To change the working directory.

set the `timeout` parameter.

Set `shell` to true, run an instance of the shell and then run the command inside of it. Can be a security risk.

Using the system-level commands builds assumptions into the scripts about the infrastructure the automation will run on.

- switching operating systems
- old flags instead of new flags

Automating a one-off, well-defined task where developing a solution quickly is the biggest requirement, then system commands and subprocesses helps a lot.

More complex or long-running, use something baked in or external modules.

Try not to reinvent the wheel.

### Subprocesses Cheat Sheet

[Subprocess](https://docs.python.org/3/library/subprocess.html)

## Processing Log Files

### Filtering Log Files with Regexes

First step is usually to open, with `open` and iterate through each line.

```py
import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
	for line in f:
		if 'CRON' not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)
		print(result[1])
```

### Making Sense out of the Data

```py
usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
```

```py
import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
	for line in f:
		if 'CRON' not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)
		if result is None:
			continue
		name = result[1]
		usernames[name] = usernames.get(name, 0) + 1

print(usernames)
```
