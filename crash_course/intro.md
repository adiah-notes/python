# Python

Python was released almost 30 years ago and has a rich history. You can read more about it on the
[History of Python](https://en.wikipedia.org/wiki/History_of_Python) Wikipedia page or in the
section on the [history of the software](https://docs.python.org/3.0/license.html) from the official
Python documentation.

Python makes it easy to express the fundamental concepts of programming like data structures and
algorithms with easy to read syntax. This makes Python a great language to use to learn programming.

## Hello World

```py
print("Hello, world!")
```

`print` is a Python 'function' that writes whatever you tell it to the screen.
`print` is a part of the basic Python language and is a 'keyword'.

Functions are pieces of code that perform a unit of work.

Keywords are reserved words that are used to construct instructions. Part of the core language and
can only be used in specific ways.

Other examples include `while`, `if`, and `for`.

Wrapping text in `""` indicates that it is a `string`, which means text that is manipulated.
In programming, any text that isn't inside quotation marks is considered part of the code.

> Printing "Hello, world!" is the traditional way to start learning a programming language.
> This practice is from back in the 70s when it was used as the first example in a famous programming
> book: _The C Programming Language_.
>
> ```c
> main() {
> 	printf("hello, world!");
> }
> ```
>
> Hello world gives you an idea of how functions are used and how a program written
> in that language looks.

## Getting Information from the User

For a program to be useful, it needs to get at least some information from the user.
This information can come from different sources, we'll start with the information as just
a separate line in the block of code.

```py
name = 'Brook'
print('Hello' + name)
```

With the name separate from the call to the print function, the line that calls the `print`
function is generic but the greeting is still personalized.

## Mathematical Operations

```py
print(4 + 5)
print(9 * 7)
print(-1 / 4)
```

## Arithmetic operators

Python can operate with numbers using the usual mathematical operators, and some special operators, too. These are all of them (we'll explore the last two in later videos).

- a + b = Adds a and b
- a - b = Subtracts b from a
- a \* b = Multiplies a and b
- a / b = Divides a by b
- a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a)

* a // b = The integer part of the integer division of a by b
* a % b = The remainder part of the integer division of a by b
