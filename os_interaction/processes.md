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

STDIN -> standard in  (like text from the keyboard)  
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

`sys.exit(value)`  can be used to exit.