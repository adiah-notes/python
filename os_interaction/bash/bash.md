# Bash Scripting Tutorial

## Variables

The most common ways to set values are directly and for its value to be set as the result of processing by a command or program.

To read the variables place its name preceded by a `$` sign.

- Place `$` sign before variable name when referring to or reading a variable.
- When setting a variable, leave out the `$` sign

Command line arguments are commonly used. use the variables `$1` to represent the first command line argument.

### Special variables

- `$0` - The name of the Bash script
- `$1 - $9` - The first 9 arguments to the Bash script
- `$#` - How many arguments were passed to the Bash script
- `$@` - All the arguments supplied to the Bash script
- `$?` - The exit status of the most recently run process
- `$$` - The process ID of the current script
- `$USER` - The username of the user running the script
- `$HOSTNAME` - The hostname of the machine the script is running on
- `$SECONDS` - The number of seconds since the script was started
- `$RANDOM` - Returns a different random number each time it is referred to
- `$LINENO` - Returns the current line number in the Bash script

### Setting our own variables

```bash
variable=value
```

- No space on either side of the equals sign.

simplevariables.sh

```sh
#!/bin/bash
# A simple variable example

myvariable=Hello

anothervar=Fred

echo $myvariable $anothervar
echo

sampledir=/etc

ls $sampledir
```

### Quotes

To store more complex values, make use of quotes. In normal circumstances Bash uses a space to determine separate items.

```
user@bash: myvar=Hello World
-bash: World: command not found
```

### Command Substitution

Allows taking the output of a command or program and save it as the value of a variable. Place in brackets, preceded by a $ sign.

```
user@bash: myvar=$( ls /etc | wc -l )
user@bash: echo There are $myvar entries in the directory /etc
```

It's nice and simple if the output of the command is a single word or line.

Test output. Use `echo` to show the variable and see what has happened.

### Exporting Variables

Variables are limited to the process they were created in.
Sometimes a script may run another script as one of its commands.
To make it available to the second script, export the variable.

scrip1.sh

```sh
#!/bin/bash
# demonstrate variable scope 1

var1=blah
var2=foo

# Let's verify their current value

echo $0 :: var1 : $var1, var2: $var2

export var1
./script2.sh

# Let's see what they are now

echo $0 :: var1 : $var1, var2 : $var2
```

script2.sh

```sh
#!/bin/bash
# demonstrate variable scope 2

# Let's verify their current value

echo $0 :: var1 : $var1, var2 : $var2

# Let's change their values

var1=flop
var2=bleh
```

Results:

```
user@bash: ./script1.sh
script1.sh :: var1 : blah, var2: foo
script2.sh :: var1 : blah, var2:
script1.sh :: var1 : blah, var2: foo
user@bash:
```

## User Input

### Ask the User for Input

Use a command called `read`.

```sh
read var1
```

introduction.sh

```sh
#!/bin/bash
# Ask the user for their name

echo Hello, who am I talking to?

read varname

echo It\'s nice to meet you $varname
```

You are able to alter the behaviour of `read` with a variety of command line options.
Two commonly used options:

- `-p` - allows you to specify a prompt
- `-s` - makes the input silent

login.sh

```sh
#!/bin/bash
# Ask the user for login details

read -p 'Username: ' uservar
read -sp 'Password: ' passvar
echo
echo Thank you $uservar we now have your login details
```

More variables

cars.sh

```sh
#!/bin/bash
# Demonstrate how read actually works

echo What cars do you like?

read car1 car2 car3

echo Your first car was $car1
echo Your second car was $car2
echo Your third car was $car3
```

### Reading from STDin

Piping.

Each process gets its own set of files (one for STDIN, STDOUT and STDERR)

To allow our script to process data that is piped to it all we need to do is read the relevant file.

- STDIN - /dev/stdin or /proc/self/fd/0
- STDOUT - /dev/stdout or /proc/self/fd/1
- STDERR - /dev/stderr or /proc/self/fd/2

summary.sh

```sh
#!/bin/bash
# A basic summary of my sales report

echo Here is a summary of the sales data:
echo ====================================
echo

cat /dev/stdin | cut -d' ' -f 2,3 | sort
```

### Which to use?

Favor command line arguments wherever possible.
They are the most convenient for users.

If all the script is doing is processing data in a certain way, it's probably best to work with STDIN.

## Arithmetic

The recommended approach is arithmetic expansion.

### Let

`let` is a builtin function of Bash that allows us to do simple arithmetic.

```sh
let<arithmetic expression>
```

let_example.sh

```sh
#!/bin/bash
# Basic arithmetic using let

let a=5+4
echo $a

let "a = 5 + 4"
echo $a

let a++
echo $a # 10

let "a = 4 * 5"
echo $a # 20

let "a = $1 + 30"
echo $a # 30 + first command line argument
```

### Expr

`expr` is similar to `let` except it instead prints the answer.
No need to enclose the expression in quotes.

```sh
expr item1 operator item2
```

expr_example.sh

```sh
#!/bin/bash
# Basic arithmetic using expr

expr 5 + 4

expr "5 + 4"

expr 5+4

expr 5 /* $1

expr 11 % 2

a=$( expr 10 -3 )
echo $a # 7
```

### Double Parentheses

```sh
$(( expression ))
```

expansion_example.sh

```sh
#!/bin/bash
# Basic arithmetic using double parentheses

a=$(( 4 + 5 ))
echo $a # 9

a=$((3+5))
echo $a #8
```

## If Statements

### Basic If Statements

```
if[ <some test> ]
then
	<commands>
fi
```

Anything between `then` and `fi` will be executed only if the test is true.

if_example.sh

```sh
#!/bin/bash
# Basic if statement

if [ $1 -gt 100 ]
then
  echo Hey that\'s a large number.
  pwd
fi

date
```

### Test

The square brackets (`[]`) are actually a reference to the command `test`.

Some of the common operators:

| Operator                | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| `!Exprssion`            | The EXPRESSION is false.                                              |
| `-n STRING`             | The length of STRING is greater than zero                             |
| `-z STRING`             | The length of STRING is zero                                          |
| `STRING1 = STRING2`     | STRING1 is equal to STRING2                                           |
| `STRING1 != STRING2`    | STRING1 is not equal to STRING2                                       |
| `INTEGER1 -eq INTEGER2` | INTEGER1 is numerically equal to INTEGER2                             |
| `INTEGER1 -gt INTEGER2` | INTEGER1 is numerically greater than INTEGER2                         |
| `INTEGER1 -lt INTEGER2` | INTEGER1 is numerically less than INTEGER2                            |
| `-d FILE`               | FILE exists and is a directory.                                       |
| `-e FILE`               | FILE exists.                                                          |
| `-r FILE`               | FILE exists and the read permission is granted.                       |
| `-s FILE`               | FILE exists and it's size is greater than zero (ie. it is not empty). |
| `-w FILE`               | FILE exists and the write permission is granted.                      |
| `-x FILE`               | FILE exists and the execute permission is granted.                    |

```
user@bash: test 001 = 1
user@bash: echo $?
1
user@bash: test 001 -eq 1
user@bash: echo $?
0
user@bash: touch myfile
user@bash: test -s myfile
user@bash: echo $?
1
user@bash: ls /etc > myfile
user@bash: test -s myfile
user@bash: echo $?
0
user@bash:
```

### Indenting

No rules regarding indenting in Bash.

### Nested if Statements

nested_if.sh

```sh
#!/bin/bash
# Nested if statements

if [ $1 -gt 100 ]
then
	echo Hey that\'s a large number.

	if (( $1 % 2 == 0 ))
	then
		echo And is also an even number.
	fi
fi
```

### If Else

```
if [<some test>]
then
	<commands>
else
	<other commands>
fi
```

else.sh

```sh
#!/bin/bash
# else example

if [ $# -eq 1 ]
then
	nl $1
else
	nl /dev/stdin
fi
```

### If Elif Else

```
if [<some test>]
then
	<commands>
elif [<some test>]
then
	<different commands>
else
	<other commands>
fi
```

### Case Statements

```sh
case <variable> in
<pattern1>)
	<commands>
	;;
<pattern2>)
	<other commands>
	;;
esac
```

case.sh

```sh
#!/bin/bash
# case example

case $1 in
	start)
		echo starting
		;;
	stop)
		echo stopping
		;;
	restart)
		echo restarting
		;;
	*)
		echo don\'t know
		;;
esac
```

disk_usage.sh

```sh
#!/bin/bash
# Print a message about disk useage.
space_free=$( df -h | awk '{ print $5 }' | sort -n | tail -n 1 | sed 's/%//' )
case $space_free in
[1-5]*)
echo Plenty of disk space available
;;
[6-7]*)
echo There could be a problem in the near future
;;
8*)
echo Maybe we should look at clearing out old files
;;
9*)
echo We could have a serious problem on our hands soon
;;
*)
echo Something is not quite right here
;;
esac
```

## Loops

### While Loops

```
while [ <some test>]
do
	<commands>
done
```

while_loop.sh

```sh
#!/bin/bash
# Basic while loop

counter=1
while [ $counter -le 10 ]
do
	echo $counter
	(( counter++ ))
done

echo All done
```

### Until Loops

The `until` loop is fairly similar to the while loop.

```
until [<some test>]
do
	<commands>
done
```

until_loop.sh

```sh
#!/bin/bash
# Basic until loop

counter=1
until [ $counter -gt 10 ]
do
  echo $counter
  (( counter++ ))
done

echo All done
```

### For Loops

```
for var in <list>
do
	<commands>
done
```

for_loop.sh

```sh
#!/bin/bash
# Basic for loop

names='Stan Kyle Cartman'

for name in $names
do
	echo $name
done

echo All done
```

Ranges

for_loop_series.sh

```sh
#!/bin/bash
# Basic range in for loop

for value in {1..5}
do
	echo $value
done

echo All done
```

for_loop_stepping.sh

```sh
#!/bin/bash
# Basic range with steps for loop

for value in {10..0..2}
do
	echo $value
done

echo All done
```

### Controlling Loops: Break and Continue

#### Break

Leave the loop straight away.

copy_files.sh

```sh
#!/bin/bash
# Make a backup set of files

for value in $1/*
do
	used=$( df $1 | tail -1 | awk '{ print $5 }' | sed 's/%\\' )
	if [ $used -gt 90 ]
	then
		echo Low disk space 1>&2
		break
	fi
	cp $value $1/backup/
	done
```

#### Continue

Stop running through this iteration and begin the next iteration.

copy_check.sh

```sh
#!/bin/bash
# Make a backup set of files

for value in $1/*
do
	if [ ! -r $value ]
	then
		echo $value not readable 1>&2
		continue
	fi
	cp $value $1/backup/
done
```

### Select

Allows the creation of a simple menu system.

```
select var in <list>
do
	<command>
done
```

select_example.sh

```sh
#!/bin/bash
# A simple menu system

names='Kyle Cartman Stan Quit'

PS3='Select character: '

select name in $names
do
	if [ $name == 'Quit' ]
	then
		break
	fi
	echo Hello $name
done

echo Bye
```

## Functions

Two different formats:

```
function_name() {
	<commands>
}
```

```
function function_name{
	<commands>
}
```

function_example.sh

```sh
#!/bin/bash
# Basic function

print_something () {
	echo Hello I am a function
}

print_something
print_something
```

### Passing Arguments

Supply the arguments directly after the function name. Within the function they are accessible as `$1`, `$2`, etc.

arguments_example.sh

```sh
#!/bin/bash
# Passing arguments to a function

print_something  () {
	echo Hello $1
}

print_something Mars
print_something Jupiter
```

### Return Values

Don't have return values, but can set a return status.

return_status_example.sh

```sh
#!/bin/bash
# Setting a return status for a function

print_something () {
	echo Hello $1
	return 5
}

print_something Mars
print_something Jupiter
echo The previous function has a return value of $?
```

return_hack.sh

```sh
#!/bin/bash
# Setting a return value to a function

lines_in_file () {
	cat $1 | wc -l
}

num_lines=$( lines_in_file $1 )

echo The file $1 has $num_lines in it.
```
