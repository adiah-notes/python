# Testing in Python

## Simple Tests

### What is Testing?

With more complex operations, it's harder to be confident that code does what it should.

Software testing is a process of evaluating computer code to determine whether or not it does what you expect it to do.

Need to see where things go wrong.

It's nearly impossible to test for everything that go wrong.

### Manual and Automated Testing

The most basic way to test scripts is to run it with different parameters.

Using, different cla and using the interactive shell first is manual testing.

Automatic testing is when you write code to test code.
Try to test as many test cases as possible. would be very tedious to do by hand.

You'll always get the same results.

## Unit Tests

Used to verify that small isolated parts of a program are correct.

Isolation is important, should only test what that particular function is doing.

Never modify the production environment. Yse a testing environment.

Given a known input, does the output of code match expectations.

rearrange.py

```py
#!/usr/bin/env python3
import re

def rearrange_name(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)
	return f"{result[2]} {result[1]}"
```

Start by first manually checking some inputs and outputs.

`from`

```py
from rearrange import rearrange_name

rearrange_name("Lovelace, Ada")
```

### Writing Unit Tests

Usually write the tests alongside the code itself.
The convention is to call the script with the same name of the module with the `_test` suffix.

`rearrange_test.py`

```py
#!/usr/bin/env python3

import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
```

Use the `unittest` module and the `TestCase` class.
Create a class that inherits from the `TestCase` class.

Any methods in the TestCAse class that start with `test` automatically become tests that can be run by the testing framework.
Use the `unittest.main()` function to run the tests for us.

### Edge Cases

Usually test the code with general cases, but it's useful to give it unusual data.

Example, what would happen if we gave the function an empty string.

```py
class TestRearrange(unittest.TestCase):
	...
	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange_name(testcase), expected)
```

Add a change to rearrange.py:

```py
if result is None:
	return ""
```

It's bad for automation to fail silently.
Check for zeros, negative numbers, and extremely large numbers.

### Additional Test Cases

```py
def test_double_name(self):
	testcase = "Hopper, Grace M."
	expected = "Grace M. Hopper"
	self.assertEqual(rearrange_name(test_case), expected)

def test_one_name(self):
	testcase = "Voltaire"
	expected = "Voltaire"
	self.assertEqual(rearrange_name(test_case), expected)
```

Another change to rearrange.py

```py
if result is None:
	return name
```

### Cheat sheet

- [Basic Example](https://docs.python.org/3/library/unittest.html#basic-example)
- [Running tests in cl](https://docs.python.org/3/library/unittest.html#command-line-interface)
- [Test Design Patterns](https://docs.python.org/3/library/unittest.html#organizing-test-code)

Understand basic assertions:

| Method                    | Checks that          | New in |
| ------------------------- | -------------------- | ------ |
| assertEqual(a, b)         | a == b               |        |
| assertNotEqual(a, b)      | a != b               |        |
| assertTrue(x)             | bool(x) is True      |        |
| assertFalse(x)            | bool(x) is False     |        |
| assertIs(a, b)            | a is b               | 3.1    |
| assertIsNot(a, b)         | a is not b           | 3.1    |
| assertIsNone(x)           | x is None            | 3.1    |
| assertIsNotNone(x)        | x is not None        | 3.1    |
| assertIn(a, b)            | a in b               | 3.1    |
| assertNotIn(a, b)         | a not in b           | 3.1    |
| assertIsInstance(a, b)    | isinstance(a, b)     | 3.2    |
| assertNotIsInstance(a, b) | not isinstance(a, b) | 3.2    |

- (More specific assertions](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)

## Other Test Concepts

## Errors and Exceptions

```

```
