## Python Locally

### How to Run a Python Script

Once Python is installed locally, you can save and run scripts that end in `.py`.

To run a script from the terminal: `python3 hello_world.py`.

```py
#!/usr/bin/env python3
```

The above code is called a shebang. This avoids having to type `python3` each time you want to run your script.
It tells the OS to run the script using Python 3.

Also need to make the file executable using the `chmod` command.
`chmod +x hello_world.py`.

Now run with: `./hello_world.py`.

Since the script is not in the `PATH` variable, use the `./` to indicate that the script is in the current directory.

### Your Own Modules

Put code you want to reuse in a separate file/module.
Then import the modules in the script you wish to use.

Example: 
areas.py
```py
import math

def triangle(base, height):
	return base * height / 2

def rectangle(base, height):
	return base * height

def circle(radius):
	return math.pi * (radius ** 2)
```

To use the module:

```py
import areas

areas.triangle(3, 5)
```

It might become necessary to split modules into multiple files.
In that case, create a directory with the module name and have `.py ` files in it.

Eg. The `requests` module.

`ls -l /usr/lib/python3/dist-packages/requests/`

Lots of `.py` files for different things. There is an `__init__.py` file. Is used to tell the interpreter that the directory is a module.

### Integrated Development Environment (IDE)

* syntax highlighting
* code completion

Common editors for Python:

* [Eclipse](http://www.eclipse.org/)
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Sublime Text](http://www.sublimetext.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

## Automation with Python

### Benefits of Automation

* Scalability
* Centralizing Mistaks

### Pitfalls of Automation

* If the time and effort to automate the task is more than the time it takes to do the task?

	`[time_to_automate < (time_to_perform * amount_of_times_done)]`

* It might be beneficial to automate error prone tasks that aren't performed that often.

* Pareto Priniciple 
	20% of the tasks performed are responsible for 80% of the work.

* If automation fails, will anyone know? Set up notifications.

* What if the automation succeeds, but completes incorrectly.
Schedule checks, can be automated as well.


### Practical Example

Check the health of your computer:
* enough disk space
* processor isn't overloaded
* latest security updates
* running services it's supposed to.

Try out the modules in the interpreter.

```py
import shutil
du = shutil.disk_usage("/")

print(du)

du.free/du.total * 100

import psutil
psutil.cpu_percent(0.1)
psutil.cpu_percent(0.1)

psutil.cpu_percent(0.5)
```

health_checks.py
```py
#!/usr/bin/env python3

import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
	print("ERROR!")
else:
	print("Everything looks ok")
```