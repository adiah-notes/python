# Strings, Lists, and Dictionaries

## Strings

A string is a data type that represents a piece of text.

**Concatenation** allows adding one string to another.

The `len()` function gives the length of the string.

**Practice**

Modify_the double word function so it returns the same word twice, followed by the length of the new doubled word.

```py
def double_word(word):
    return

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
```

### String Indexing and Slicing

**String indexing**: accessing the character in a given position or index.

**Negative indices**: starts counting from the last

**Slice**: the portion of a string that can contain more than one character; also called a substring.

```py
color = 'Orange'
color[1:4]
# ran
```

The range here works just like the `range()` function.

Leaving out one of the parameters, makes the slice assume it's til the end of the string.

```py
fruit = 'Pineapple'
print(fruit[:4]) # Pine
print(fruit[4:]) # apple
```

### Creating New Strings

```py
message = "A kong string with a silly typo"

message[2] = "l" # Will give an error
```

Strings are immutable -> they can't be modified.

Instead create a new string:

```py
new_message = message[0:2] + "l" + message[3:]
```

Can assign a new value to the variable, but cannot change the underlying string.

```py
pets = "Cats & Dogs"
pets.index("&") # 5
```

Here, we're using a method to find the index of the '&' character.

> A method is a function associate with a specific class

The `index` method gives the index of the first position of the substring.

The keyword `in` can be used to check if a substring is in a string.

```py
pets = "Cats & Dogs"

"Dragons" in pets # False

"Cats" in pets # True
```

Write a program that replaces an old domain in any emails that still have them.

```py
def replace_domain(email, old_domain, new_domain):
	if "@" + old_domain in email:
		index = email.index("@" + old_domain)
		new_email = email[:index] + "@" + new_domain
		return new_email
	return email
```

### More String Methods

- `.uper()`
- `.lower()`
- `.strip()` -> removes surrounding whitespace
- `.lstrip()`
- `.rstrip()`
- `.count()` -> returns how many times a given substring appears within a string
- `.endswith()` -> returns whether the string ends with a certain substring
- `.isnumeric()` -> returns whether it just contains numbers
- `.join()` -> can also be used for concatenation.

```py
" ".join(["this", "is", "a", "phrase", "joined", "by", "spaces"])

"...".join([...])
```

` `.split()` -> returns a list of all the words in the initial string, automatically splits by whitespace, but can use other separators.

### Formatting Strings

```py
name = "Manny"
number = len(name) * 3

print("Hello {}, your lucky number is {}".format(name, number))
```

Can use expressions in `{}` to format strings.

```py
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
```

- Doesn't matter the order since using named parameters.

```py
price = 7.5
with_tax = price * 1.09
print(price, with_tax) # 7.5 8.175

print("Base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax))
```

- the `:.2f` is a formatting expression. Formats a float, with 2 decimal places.

- `:>3` -> numbers aligned to the right for three spaces

- `:>6.2f` -> align to right with 6 spaces and 2 dp

### Cheat Sheet

#### String operations

- `len(string)` -> Returns the length of the string
- `for character in string` -> Iterates over each character in the string
- `if substring in string` -> Checks whether the substring is part of the string
- `string[i]` -> Accesses the character at index i
- `string[i:j]` -> Access the substring starting at index `i`, ending at index `j-1`.

#### String methods

- `string.lower()` -> Returns a copy of the string with all lowercase characters
- `string.upper()` -> returns a copy with all uppercase
- `string.lstrip()` -> returns a copy with all left-side whitespace removed
- `string.rstrip()`
- `string.strip()`
- `string.count(substring)` -> Returns the number of times substring is present in the string
- `string.isnumeric()` -> Returns true if there are only numeric characters in the string.
- `string.isalpha()` -> Returns True if there are only alphabetic characters.
- `string.split()` -> Returns a list of substrings
- `string.replace(old, new)` -> Returns a new string where all occurrences of old have been replaced by new.

#### Formatting expressions

| Expr     | Meaning                                      | Example                            |
| -------- | -------------------------------------------- | ---------------------------------- |
| `{:d}`   | Integer value                                | `'{:d}'.format(10.5)` -> '10'      |
| `{:.2f}` | Floaing point with that many decimals        | `'{:.2f}'.format(0.5)` -> '0.50'   |
| `{:.2s}` | String with that many characters             | `{:.2s}'.format('Python')` -> 'Py' |
| `{:<6s}` | String aligned to the left that many spaces  | `'{:<6s}'.format('Py')` -> 'Py '   |
| `{:>6s}` | String aligned to the right that many spaces | `'{:>6s}'.format('Py')` -> ' Py'   |
| `{:^6s}` | String centered in that many spaces          | `'{:^6s}'.format('Py')` -> ' Py '  |

### F strings

I prefer using f-strings which have the same properties as the format function, but easier to write:

```py
name = "Micha"

print(f'Hello {micah}')
```

Simply add the letter 'f' before the quotes, and used the curly braces to substitute for variables.

### Practice

The is_palindrome function checks if a string is a palindrome. Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

```py
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for ___:
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if ___:
			new_string = ___
			reverse_string = ___
	# Compare the strings
	if ___:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
```

Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".

```py
def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {___} km".___
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
```

The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them

```py
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
	if ___:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the
		# end with the new string
		i = ___
		new_sentence = ___
		return new_sentence

	# Return the original sentence if there is no match
	return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
```

## Lists

Lists in Python are defined using square brackets, with the elements stored in the list separated by commas: list = ["This", "is", "a", "list"].

```py
x = ["now", "we", "are", "cooking"]

len(x) # -> gives the number of elements

"are" in x # True

print(x[0]) # Same as with strings
```

Strings and lists are both sequences:

- `for element in sequence`
- `sequence[x]`
- `len(sequence)`
- `sequence + sequence`
- `element in sequence`

### List Methods

- `list[i]` = x - Replaces the element at index i with x

- `list.append(x)` - Inserts x at the end of the list

- `list.insert(i, x)` - Inserts x at index i

- `list.pop(i)` - Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.

- `list.remove(x)` - Removes the first occurrence of x in the list

- `list.sort()` - Sorts the items in the list

- `list.reverse()` - Reverses the order of items of the list

- `list.clear()` - Removes all the items of the list

- `list.copy()` - Creates a copy of the list

- `list.extend(other_list)` - Appends all the elements of other_list at the end of list

Lists are **mutable**.

Tuple are immutable.
The position of the elements inside the tuple have meaning.

Whenever a function returns more than one value, it returns a tuple.

Can unpack tuples by assigning the correct number of variables.

### Iterating

```py
winners = ["Ashley", "Dylan", "Reese"]

for index, person in enumerate(winners):
	print("{} - {}".format(index + 1, person))
```

`Enumerate` gives you the item and its index in a tuple `(index, element)`.

```py
def full_emails(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name, email))
	return result


print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
```

Using range to loop over indexes in list and then indexing into the list. It's better to loop over items or using enumerate if you need the indices.

It's better to use a copy of the list if you're modifying the list as you iterate over it.

### List Comprehension

Example creating a list with multiples of 7 from 7 to 70:

```py
multiples = []

for x in range(1, 11):
	multiples.append(x * 7)

print(multiples)
```

Using list comprehension:

```py
multiples = [x * 7 for x in range(1, 11)]

print(mutiples)
```

A list of strings and generate a list of lengths of the strings

```py
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
```

```py
z = [x for x in range(0, 101) if x % 3 == 0]
print z
```

### Practice

Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.

```py
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
```

Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

```py
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = ___
  for word in words:
    # Create the pig latin word and add it to the list
    ___
    # Turn the list back into a phrase
  return ___

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
```

The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
For example:
640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
Fill in the blanks to make the code convert a permission in octal format into a string format.

```py
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for ___ in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if ___ >= value:
                result += ___
                ___ -= value
            else:
                ___
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
```

The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

```py
def group_list(group, users):
  members = ___
  return ___

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
```

The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as \_\_." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.

```py
def guest_list(guests):
	for ___:
		___
		print(___.format(___))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
```

---

## Dictionaries

The data inside dictionaries take the form of key-value pairs.

You access the items in a dictionary by using the associated key.

```py
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
```

In this dictionary, the keys are strings and the values are integers. The keys and values are separated by colons.

```py
# Get the number of txt files
file_counts["txt"] # 14

# Check with in
"jpg" in file_counts

file_counts["cfg"] = 8
print(file_counts)

# Setting a value with an existing key just replaces the value.

del file_counts["cfg"]
print(file_counts)
```

### Iterating

```py
file_counts = {
	"jpg": 10,
	"txt": 14,
	"csv": 2,
	"py": 23
}

for extension in file_counts:
	print(extension)
```

Using a for loop by default, iterates over the keys.
Can get the value by indexing in with key or using the `items()` method.

```py
for ext, amount in file_counts.items():
	print("There are {} files with the .{} extension".format(amount, ext))
```

Can access just the values or keys.

```py
file_counts.keys()
file_counts.values()
```

Keys can only occur once, so great for counting and analyzing frequency.

```py
def count_letters(text):
	result = {}
	for letter in text:
		if letter not in result:
			result[letter] = 0
		result[letter] += 1
	return result

count_letters("aaaaa")
count_letters("tenant")
```

### Methods and Operations

**Operations**

- `len(dictionary)` - Returns the number of items in the dictionary.

- `for key in dictionary` - Iterates over each key in the dictionary

- `for key, value in dictionary.items()` - Iterates over each key, value pair in the dictionary.

* `if key in dictionary` - Checks whether the key is in the dictionary.

* `dictionary[key]` - Access the item with key `key` of the dictionary.

* `dictionary[key] = value` - Sets the value associated with key.

* `del dictionary[key]` - Removes the item with key `key` from of the dictionary.

**Methods**

- `dict.get(key, default)` - Returns the element corresponding to key, or default if it's not present.

* `dict.keys()` - Returns a sequence containing the keys in the dictionary.

* `dict.values()` - Returns a sequence containing the values in the dictionary.

* `dict.update(other_dictionary)` - Updates the dictionary with the items coming from the other
  dictionary.

* `dict.clear()` - Removes all the items of the dictionary.

### Practice

The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses.

```py
def email_list(domains):
	emails = []
	for ___:
	  for user in users:
	    emails.___
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
```

The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.

```py
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for ___:
		# Now go through the users in the group
		for ___:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
```

The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.

```py
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for ___:
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += ___
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
```
