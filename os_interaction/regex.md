# Regular Expressions

Allow us to search a text for strings matching a specific pattern.

```py
import re
log = "July 31 07:51:48 mycomputer bad_processes[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
```

### Basic Matching with grep

- Checking if string is present.

```
grep thon /usr/share/dict/words

grep -i python /usr/share/dict/words

grep l.rts /usr/share/dict/words

grep ^fruit /usr/share/dict/words

grep cat$ /usr/share/dict/words
```

## Basic Regular Expressions

### Simple Matching in Python

`re` module.

```py
import re
result = re.search(r"aza", "plaza")
```

`r""` is a raw string. Always use raw strings for regexes in python.

The result is a Match object.

If there is no match, it returns None as a result.

```py
print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "clapping"))
```

Can pass options: `re.ignorecase`

```py
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
```

### Wildcards and Character Classes

Wildcard -> can match any character.

Character classes -> written in square brackets.

```py
print(re.search(r"[Pp]ython", "python"))
```

- [a-z]
- [A-Z]
- [0-9]

```py
print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
```

- [^] -> not in the pattern

```py
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
```

- | -> or

```py
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like dogs and cats."))
```

`findall` function gives all possible matches.

```py
print(re.findall(r"cat|dog", "I like both dogs and cats."))
```

### Repetition Qualifiers

- `*` -> Match any number of times (>= 0).

```py
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))

```

`*` is greedy, takes as many as possible.

```py
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

```

- `+` -> Matches one or more character

```py
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))
```

- `?` -> Either 0 or one occurrence of the character before it

```py
print(re.search(r"p?each", "To each their own"))

print(re.search(r"p?each", "I like peaches"))
```

### Escaping Characters

Use the `\` character to escape a special character.

```py
print(re.search(r"\.com", "welcome"))

print(research(r"\.com", "google.com"))
```

- `\w` matches any alphanumeric character including letters, numbers and underscores.
- `\d` digits
- `\s` spaces and tabs
- `\b` for word boundaries

[Test your regexes](www.regex101.com)

### Regular Expressions in Use

```py
# Countries that start and end with 'A'
print(re.search(r"A.*a", 'Argentina'))

# Need to add beginning and ending
print(re.search(r"^A.*a$", 'Argentina'))
```

A python variable can contain any number of letters, numbers, or underscores, but it can't start with a number

```py
pattern = r"^[\w\W][\w\W\d]*$"
```

### Cheat-sheet

[Regular expression How to](https://docs.python.org/3/howto/regex.html)
[Regular expression operations](https://docs.python.org/3/library/re.html)

## Advanced Regular Expressions

### Capturing Groups

Portions of the pattern that are enclosed in parentheses.

Use parentheses to capture groups.

Eg:
Getting first name and last name from a list.

```py
# Looks for a group of letters, a comma, then a space and another group of letters.
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")

print(result.groups())
# Can access with indexes

print(result[0])
# Lovelace, Ada

print(result[1])
# Lovelace
```

```py
def rearrange_name(name):
	result = re.search(r"^(\w*), (\w*)$", name)

	if result is None:
		return name

	return f"{result[2]} {result[1]}"

rearrange_name("Lovelace, Ada")
rearrange_name("Ritchie, Dennis")
rearrange_name("Hopper, Grace M.")
```

### More on Repetition Qualifiers

`{5}` -> looks for exactly 5 repetition.

`\b` represents word limit -> gives full words.

```py
# Gets all five letter whole words.
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
```

`{5,10}` -> anywhere from 5 - 10 repetitions.  
`{5,}`  
`{,10}`

### Extracting a PID Using Regexes in Python

```py
import re
log = "July 31 07:51:48 mycomputer bad_processes[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])
```

```py
def extract_pid(log_line):
	regex = r"\[(\d+)\]"
	result = re.search(regex, log_line)
	if result is None:
		return ""
	return result[1]

print(extract_pid("99 elephants in a [cage]"))
```

### Splitting and Replacing

`split`

Example split a string into sentences:

```py
re.split(r"[.?!]", "One sentence. Another one? And the last one!")

# To capture the elements using to split the values:
re.split(r"([.?!])", ...)
```

`sub`

Substituting all or part of string fro a different string.

Example removing addresses from logs with email addresses of users:

```py
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@gamil.lcom")

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
# Look up back-referencing
```

Try [Regex Crossword](https://regexcrossword.com/)
