# Basic Python Syntax

## Expressions and Variables

### Data Types

Most programs need to manipulate some kind of data
which can come in a lot of different forms (data types).

- `string`
- `int`: whole numbers without a fraction
- `float`: real numbers or numbers with fractional part

Generally, the computer is unable to mix different data types.

For example, adding two integers makes perfect sense:

```py
print(7 + 8)
```

Adding two strings also makes sense:

```py
print("hello" + "world")
```

But cannot add an integer to a string:

```py
print(7 + "8")
```

### Variables

When a computer performs an operation for us, we need to store values and give them names so that we can refer to them later.

**Variables** are names that we give to certain values in our programs. Think of variables as containers for data.

The computer stores a chunk of memory for that data so that it can be accessed and modified later.

```py
length = 10
width = 2
area = length  * width
print(area)
# 20
```

The process of storing a value inside a variable is called **assignment**. In Python we used the `=` operator.

An **expression** is a combination of numbers, symbols, or other variables that produce a result when evaluated.

Variables let you perform operations on data that may change.

Can't use keywords, must start with a letter or underscore. Can only contain letters, numbers, or underscores. No spaces. Capitalization matters.

### Expressions, Numbers, and Type Conversions

Integer \* float is possible with Python.

```py
7 + 8.5
> 15.5
```

This is due to **Implicit conversion** where the interpreter automatically converts one data type into another.

**Explicit conversion** to convert between one data type and another, call a function with the name of the type we're converting to.

```py
base = 6
height = 3
area = (base * height) / 2
print ("The area of the triangle is: " + str(area))
```

### Practice

1. Two friends are eating dinner. The bill comes in the amount of $47.28. Split the bill evenly between
   them after adding 15% tip. Calculate the tip, total amount to pay, and each friend's share.
   Output a message saying "Each person needs to pay: " followed by the resulting number.

   ```py
   bill = ___
   tip = bill * ___
   total = bill + ___
   share = ___
   print("")
   ```

## Functions

The print() and type() and str() functions come as a part of the Python language.

```py
def greeting(name):
	print("Welcome, " + name)
```

In this example, the function `greeting()` is defined, and takes a parameter `name`, and prints
a greeting for that name.

Use the `def` keyword, and the name comes after the keyword. **Parameters** are written in parentheses.

The body is indented and contain many lines of code.

```py
greeting('Kay')
```

That's how you call the function.

### Returning Values

The work that functions do can produce new results.

```python
def area_triangle(base, height):
	return base * height / 2

area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b

print("The sum of both triangles is " + str(sum))
```

You can return more than one value.
Assume you have a duration of time in seconds and you want to convert that to hours, minutes, and seconds:

```py
def convert_seconds(seconds):
	hours = seconds // 3600
	minutes = (seconds - hours * 3600) // 60
	remaining_seconds = seconds - hours * 3600 - minutes * 60
	return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
```

> The `//` operator is called **floor division** and divides a number and takes the integer part of the quotient.

Assign the result of the function to separate variables.

### Code Reuse

```py
name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number)
```

This script reuses the same codes. When there is code duplication, see if you can use a function.

```py
def lucky_number(name):
	number = len(name) * 9
	print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")
```

The code is now easier to read and reusable.

## Conditionals

Comparing smaller, lesser, or equal
**Comparison operators**:

- `==`
- `!=`
- `<` and `>`

```py
print(10 > 3)
# True

print("cat" == "dog")
# False

print(1 != 2)
# True
```

`True` is a **Boolean**, one of two possible states: either true or false.

**Logical operators** `and`, `or` and `not`.

To evaluate as True, the `and` operator needs both expressions to be true at the same time.

### Branching with `if` statements

`Branching` is the ability of a program to alter its execution sequence.

```py
def hint_username(username):
	if len(username) < 3:
		print("Invalid username. Must be at least 3 characters long")
```

The body of the `if` block will only execute if the condition evaluates to true.

### `else` statements

Program can go in one of two directions now:

```py
def hint_username(username):
	if len(username) < 3:
		print("Invalid username. Must be at least 3 characters long")
	else:
		print("Valid username")
```

Don't always need to use it.

```py
def is_even(number):
	if number % 2 == 0:
		return True
	return False
```

> The `%` operator (modulo) gives the remainder after integer division.

The trick is that when a return statement is executed, the function exits so that the code that follows doesn't get executed.

> I would actually just return the expression:
>
> ```py
> def is_even(number):
>    return number % 2 == 0
>
> ```
>
> In this case the return value of the function would be the result of the evaluation of the conditional either `True` of `False`

### `elif` Statements

Short for `else if`

```py
def hint_username(username):
	if len(username) < 3:
		print("Invalid username. Must be at least 3 characters long")
	elif (len(username) > 15):
		print("Invalid username. Must be at most 15 characters long")
	else:
		print("Valid username")
```

The `elif` condition will only be checked if the the `if` condition is false.

### Summary

**Comparison operators**

- a == b: a is equal to b
- a != b: a is different than b
- a < b: a is smaller than b
- a <= b: a is smaller or equal to b
- a > b: a is bigger than b
- a >= b: a is bigger or equal to b

**Logical operators**

- a and b: True if both a and b are True. False otherwise.
- a or b: True if either a or b or both are True. False if both are False.
- not a: True if a is False, False if a is True.

**Branching blocks**

In Python, we branch our code using if, else and elif. This is the branching syntax:

```py
if condition1:
	if-block
elif condition2:
	elif-block
else:
	else-block
```

### Practice

1. If a filesystem has a block size of 4096 bytes, a file comprised of only one byte will still use 4096 bytes of storage. Fill in the function below to calculate the total number of bytes needed to store a file of a given size.

```py
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = ___
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = ___
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return ___
    return ___

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
```
