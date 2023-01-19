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

You can access the attributes and methods on an instance using the dot notation.

```py
golden = Apple()
golden.color = "yellow"
golden.flavor = "soft"
```

### Practice

The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote.

```py
# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results.
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables,
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK.
    	___
    	return you.apples, me.apples

def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to
    #each idea attribute? Do you need a temporary variable to store
    #the sum of ideas, or can you find another way?
    #Use as many lines of code as you need here.
    you.ideas ___
    me.ideas ___
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

```

The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population.

```py
# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold
# the information of the city with
# the highest elevation
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___

	#Format the return string
	if return_city.name:
		return ___
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""
```

## Classes and Methods

### Instance Methods

Methods are functions that operate on the attributes of a specific instance of a class.

For instance the `append` method on a list adds an element to the end of that specific list.

```py
class Piglet:
	def speak(self):
		print("oink oink")
```

`self` represents the instance that the method is executed on.

```py
hamlet = Piglet()
hamlet.speak()
```

Can make the methods do specific things based on the specific attributes on that instance.

```py
class Piglet:
	name = "piglet"
	def speak(self):
		print(f"Oink! I'm {self.name}! Oink!")
```

The value for `name` inside the class definition is the default value which can be changed.

```py
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
```

Variables that have different values for different instances of the same class are called **instance variables**.

### Constructors and Other Special Methods

#### Constructors

**Constructor** lets you define all the initial values for an instance. It's called when you call the name of the class.

```py
class Apple:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor

jonagold = Apple("red", "sweet")

print(jonagold.color)
```

Special methods begin and end with `__`, double underscores (or dunders).

#### Str

```py
print jonagold

# <__main__.Apple object at ------>
```

Need to specify how to represent the object with a string.

```py
class Apple:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor

	def __str__(self):
		return f"THis apple is {self.color} and its flavor is {self.flavor}"

jonagold = Apple("red", "sweet")
```

### Documenting Functions, Classes, and Methods

```py
def to _seconds(hours, minutes, seconds):
	"""Returns the amount of seconds in the given hours, minutes, and seconds."""
	return hours * 3600 + minutes * 60 + seconds

help(to_seconds)


class Piglet:
	"""Represents a piglet that can say their name."""
	years = 0
	name = ""
	def speak(self):
		"""Outputs a message including the name of the piglet."""
		print(f"Oink! I'm {name}! Oink!")

	def pig_years(self):
		"""Converts the current age to equivalent pig years."""
		return self.years * 18

pig = Piglet()
pig.name = "gg"
```

## Code Reuse

### Inheritance

```py
class Fruit:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor

class Apple(Fruit):
	pass

class Grape(Fruit):
	pass
```

Both `Apple` and `Grape` inherit from the `Fruit` class. So they have the same constructor which sets the flavor and color attributes.

The `Fruit` class is the parent class, while `Apple` and `Grape` are siblings.

```py
granny_smith = Apple("green" "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)
```

There can also be changes for the specific child classes that are different from the parent.

```py
class Animal:
	sound = ""
	def __init__(self, name):
		self.name = name
	def speak(self):
		print(f"{self.sound} I'm {self.name}! {self.sound}")

class Piglet(Animal):
	sound = "Oink!"


hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
	sound = "Mooooo"
```

### Composition

Can use the `is a` to check the inheritance.

When two different classes are related, but there is no inheritance is **composition**.

E.g.
A `Package` class which represents a software package: which contains attributes about the software package, like name, version, and size.

There is also a `Repository` class which represents all the products available for installation.

There's no inheritance relationship, but they are related. The `Repository` class will have a dictionary, or list, of `Packages` in that repository

```py
class Repository:
	def __init__(self):
		self.packages = {}

	def add_package(self, package):
		self.packages[package.name] = package

	def total_size(self):
		result = 0
		for package in self.packages.values():
			result += package.size
		return result
```

Initialize the packages dictionary in the constructor method, to ensure that every instance of the `Repository` has its own dictionary.

Composition allows us to use objects as attributes, as well as access all their attributes and methods.

**NB** Always initialize mutable attributes in the constructor. If you initialize in teh class level, then all instances of the class will have the same things.

### Python Modules

Used to organize functions, classes, and other data together in a structured way. MOdules are set up through separate files containing the necessary classes and functions.

Use the `import` keyword. There are a lot in the Python standard libraries.

```py
import random

random.randint(1, 10)
```

Uses the dot notation like methods in classes.

```py
import datetime

now = datetime.datetime.now()
type(now)
<class 'datetime.datetime'>

print(now + datetime.timedelta(days=28))
```

The official documentation lists all the modules in the standard library.

[Pypi](https://pypi.org/) is the Python repository and index of a number of modules developed by Python programmers around the world.
