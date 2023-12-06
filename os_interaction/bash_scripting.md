# Bash Scripting

## Interacting with the Command Line Shell

### Basic Linux Commands

- echo - display to the screen
- cat - display contents of a file
- ls - display items in a directory
- chmod - change file permissions
- mkdir - make new directory
- cd - change into directory
- pwd - print curent directory
- cp - copy
- touch - create empty file

Most don't give any output once they've suceeded.

- ls -l - command line argument (extra information permissions, nodes,)
- ls -la - (-a shows hidden files)
- mv - rename or move a file
- rm - delete files (one at a time, or with \*)
- rmdir - only works on empty directories

### Redirecting Streams

Input, output, and error.

The process of sending a stream to a different location.

Use `>`.

stdout_example.py

```py
#!/usr/bin/env python3

print("Don't mind me, just a bit of text here...")
```

use `>` :

```bash
./stdout_example.py > new_file.txt
```

The output of the program is stored into what's after the `>` symbol.
This writes over the file or creates a new one.

Use `>>` to append to the file.

---

Use `<` to read the input from a file

streams_err.py

```py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
```

```bash
./streams_err.py < new_file.txt
```

`2>` is used to redirect errors to a file. Useful for logging errors.

`.streams_err.py < new_file.txt 2> error_file.txt`

`2` is the file descriptor for errors.

### Pipes and Pipelines

Connect multiple scripts...

Connect the output of one program to the input of another in order to pass data between programs.

`|`

`ls -l | less`

`cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head`

- `cat` gets the contents from the spider.txt file
- the output is passed to `tr`, translate, takes the first character and transforms it to the second character
- pass the results to a `sort` command, which sorts alphabetically
- passed to the `uniq` command which displays each match once, with the `-c` flag it prefixes each line with a number of times it occured.
- passed to the `sort` with `-nr` flags (numerically and in reverse order)
- passed to the `head` which prints the first 10 lines to the std out

Can pipe to python scripts as well. Python can read from stdin using `stdin` file object provided by the `sys` module, already open for input.

capitalize.py

```py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
	print(line.strip().capitalize())
```

haiku.txt

```
advance your career,
automating with Python,
it's so fun to learn.
```

Pipeline to capitalize haiku:

```
cat haiku.txt | ./capitalize.py
```

Better to just redirect to get contents into the script:

```
./capitalize.py < haiku.txt
```

But to connect multiple in a pipeline, use the pipes.

### Signalling Processes

Tokens delivered to running processes to indicate a desired action.

Can tell a program if to pause or terminate for example.

example:

`ping www.example.com`

Keeps running forever

can use `ctrl-C` to end. Tells the process to finish cleanly.

`SIGINT`

`ctrl-Z` - Stopped abruptly.
`SIGSTOP`
`fg` to continue running

`kill` -> `SIGTERM`
Needs the pid (process id) and to be run in a separate terminal.
Use `ps` to list current processes.

`ps ax` -> all running processes on computer:

```
ps ax | grep ping
kill 4619
```

### Basic Linux Commands Cheat-Sheet

#### Managing files and directories

- `cd directory`: changes the current working directory to the specified one
- pwd: prints the current working directory
- `ls`: lists the contents of the current directory
- `ls directory`: lists the contents of the received directory
- `ls -l`: lists the additional information for the contents of the directory
- `ls -a:` lists all files, including those hidden
- `ls -la`: applies both the -l and the -a flags
- `mkdir directory`: creates the directory with the received name
- `rmdir directory`: deletes the directory with the received name (if empty)
- `cp old_name new_name`: copies old_name into new_name
- `mv old_name new_name`: moves old_name into new_name
- `touch file_name`: creates an empty file or updates the modified time if it exists
- `chmod modifiers files`: changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable
- `chown user files`: changes the owner of the files to the given user
- `chgrp group files`: changes the group of the files to the given group

#### Operating with the content of files

- `cat file`: shows the content of the file through standard output
- `wc file`: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin
- `file file`: prints the type of the given file, as recognized by the operating system
- `head file`: shows the first 10 lines of the given file
- `tail file`: shows the last 10 lines of the given file
- `less file`: scrolls through the contents of the given file (press "q" to quit)
- `sort file`: sorts the lines of the file alphabetically
- `cut -dseparator -ffields file`: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

#### Additional commands

- `echo "message"`: prints the message to standard output
- `date`: prints the current date
- `who`: prints the list of users currently logged into the computer
- `man command`: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)
- `uptime`: shows how long the computer has been running
- `free`: shows the amount of unused memory on the current system

### Redirections, Pipes, and Signals

#### Managing streams

These are the redirectors that we can use to take control of the streams of our programs

- `command > file`: redirects standard output, overwrites file
- `command >> file`: redirects standard output, appends to file
- `command < file`: redirects standard input from file
- `command 2> file`: redirects standard error to file
- `command1 | command2`: connects the output of command1 to the input of command2

#### Operating with processes

These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

- `ps`: lists the processes executing in the current terminal for the current user
- `ps ax`: lists all processes currently executing for all users
- `ps e`: shows the environment for the processes listed
- `kill PID`: sends the SIGTERM signal to the process identified by PID
- `fg`: causes a job that was stopped or in the background to return to the foreground
- `bg`: causes a job that was stopped to go to the background
- `jobs`: lists the jobs currently running or stopped
- `top`: shows the processes currently using the most CPU time (press "q" to quit)

## Bash Scripting

### Creating Bash Scripts

Bash is the interpreter and scripting language.

gather-information.sh

```bash
#!/bin/bash
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"
```

Can write commands on same line with semicolons as well:

```sh
echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"
```

### Using Variables and Globs

Environment variables. prefix variables with `$`

example=hello
echo $example

`export` variable to be used

```sh
#!/bin/bash
line="----------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"
```

globs are characters that allow you to create lists of files. `?` and `*`.

Can create sequences of filenames that can be used as parameters to the commands.

- `echo *.py`
- `echo c*`
- `echo *`
- `echo ?????.py`

Available in `glob` module in Python.

### Conditional Execution in Bash

Based on the exit status of commands

`$?`

```sh
if grep "127.0.0.1" /etc/hosts/; then
	echo "Everything ok"
else
	echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi
```

`test` - evaluates the conditions received and exits with zero when they're true and with one when they're false.

```sh
if test -n "$PATH"; then echo "Your path is not empty"; fi
```

`-n` checks if string variable is empty or notl

```sh
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
```

`[]` are aliases for the test command, must have space before the closing bracket.

### Bash Scripting Resources

- [https://ryanstutorials.net/bash-scripting-tutorial/](https://ryanstutorials.net/bash-scripting-tutorial/)
- [https://linuxconfig.org/bash-scripting-tutorial-for-beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
- [https://www.shellscript.sh/](https://www.shellscript.sh/)

## Advanced Bash Concepts

### While Loops in Bash Scripts

while.sh

```sh
#!/bin/bash

n=1
while [ $n -le 5 ]; do
	echo "Iteration number $n"
	((n+=1))
done
```

`-le` -> less than or equal

`(())` -> allows arithmethic expressions

random_exit.py

```py
#!/usr/bin/env python

import sys
import random

value=random.randint(0, 3)
print(f"Returning: {value}")
sys.exit(value)
```

retry.sh

```sh
#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
	sleep $n
	((n=n+1))
	echo "Retry #$n"
done;
```

`./retry.sh ./random_exit.py`

`$1` === `sys.argv[1]`

### For Loops in Bash Scripts

fruits.sh

```sh
#!/bin/bash
for fruit in peach orange apple; do
	echo "I like $fruit!"
done
```

```sh
#!/bin/bash

for file in *.HTM; do
	name=$(basename "$file" .HTM)
	mv "$file" "$name.html"
done
```

`basename` -> returns filename without extension

Surround variable name with `""`, in case there are spaces, so that it can work.

Good idea to run it without actually modifying the files

Use echo to see what it will do

```sh
...
 echo mv "$file" "$name.html"
```

### Advanced Command Interaction

`/var/log/syslog`

`tail /var/log/syslog`

`cut` -> takes bit of each line

`tail /var/log/syslog | cut -d' ' -f5-`

`-d' '` -> uses space as delimter
`-f5-` only keeps the field 5

`cut -d' ' -f5- /var/log/syslog | sort |uniq -c | sort -nr | head`

toploglines.sh

```sh
#!/bin/bash

for logfile in /var/log/*log; do
	echo "Processing: $logfile"
	cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
```

### Choosing Between Bash and Python

Remember bash is os specific.
Mightn't be good to use with some complicated tasks.

---

```sh
#!/bin/bash

> oldFiles.txt

files=$(grep ' jane ' ~/data/list.txt | cut -d ' ' -f 3)

for file in $files
do
  if [ -e ~/$file ]
  then
    echo /home/student$file >> oldFiles.txt
  fi
done
```

changeJane.py

```py
import sys
import subprocess

filename = sys.argv[1]


with open(filename, 'r') as file:
	lines = file.readlines()
	for line in lines:
		old_name = line.strip()
		new_name = old_name.replace('jane', 'jdoe')

		subprocess.run(['mv', old_name, new_name])
```
