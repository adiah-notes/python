# Object Oriented Programming

## What is OOP

A flexible paradigm where `classes` represent and define concepts, while objects are `instances` of classes.

### Classes

In Python, `Numbers`, `Strings`, `Lists`, and `Dictionaries` are all classes. When we create one as a variable, that specific one is an instance.

The `attributes` are the characteristics associated to a type.

The `methods` are the functions associated to a type.

Take a file. Attributes include: Date, Name, Permissions, Size, etc.

### Classes and Objects in Python

```py
type(0)
<class 'int'>
```

A string is a class, and has methods such as `upper()`.

User `dir()` to print a list of all methods available for a certain instance.

Try:

```py
dir("")

help("")
```

### Defining New Classes

```py
class Apple:
	pass
```

- The `class` keyword is used to start a new class

- Style guides recommend starting names with a capital letter.

```py
class Apple:
	color = ""
	flavor = ""
```

Here two attributes are defined: color and flavor.
They are defined as strings, since that's what they're expected to be.

```py
jonagold = Apple()
```

To create a new instance of any class, call the name of the class as if it were a function.

```py
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.flavor)
print(jonagold.flavor)
```
