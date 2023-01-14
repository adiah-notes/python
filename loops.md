# Loops

## While Loops

Instructs computer to continuously execute you code based on the value of a condition.

```py
x = 0
while x < 5:
	print("Not there yet, x=" + str(x))
	x = x + 1
print("x=" + str(x))
```

**Initializing** to give an initial value to a variable.

The program keeps executing until the condition evaluates to `False`.

```py
def attempts(n):
	x = 1
	while x <= n:
		print("Attempt " + str(x))
		x += 1
	print("Done")

attempts(5)
```

```py
username = get_username()
while not valid_username(username):
	print("Invalid username")
	username = get_username()
```

Remember to initialize variables before creating the loop. This makes sure the variable is available and doesn't have any unexpected values in it.

### Infinite loops

A loop that keeps executing and never stops.

```py
while x % 2 == 0:
	x = x / 2
```

This can happen when the condition being evaluated doesn't change. Pay attention to variables and the values they can take. Even unexpected values like zero.

```py
if x != 0:
	while x % 2 ==0:
		x = x / 2
```

Sometimes you actually want to execute continuously until some external condition is met.

```py
while True:
	do_something_cool()
	if user_requested_to_stop():
		break
```

### Practice

1. Fill in the blanks to print all the prime factors of a number.

   ```py
   def print_prime_factors(number):
   	# Start with two
   	factor = ___
   	# Keep going until factor is larger than numbr
   	while factor <= number:
   		# Check if factor is a divisor
   		if number % factor == ___:
   			# If it is, print and divide the original
   			print(factor)
   			number = number / factor
   		else:
   			# If it's not, increment factor by one
   			___
   	return "Done"

   print_prime_factors(100)
   # Should print 2,2,5,5
   ```

2. Fix the infinite loop

```py
def is_power_of_two(n):
	# Check if the number can be divided by two
	while n % 2 == 0:
		n = n / 2
	# If after dividing the number is 1 it's a power
	if n == 1:
		return True
	return False

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
```

3. Return the sum of all divisors of a number without including it.

```py
def sum_divisors(n):
	sum = 0
	return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
```

## For loops

Iterates over a sequence of values.

```py
for x in range(5):
	print(x)
```

The variable (`x`) will take the value of all items `in` the range.

`range`: starts at 0 and ends at 1 before the number indicated.

You can loop over any sequence, not just a range.

```py
values = [23, 52, 59, 37, 48]
sum = 0
length = 0

for value in values:
	sum += value
	lenght += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))
```

> To quickly recap the `range()` function when passing one, two, or three parameters:
>
> - One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
>
> - Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
>
> - Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.

### Nested For loops

Creating domino tiles.

```py
for left in range(7):
	for right in range(left, 7):
		print("[" + str(left) + "|" + str(right) + "]", end=" ")
	print()
```

Team pairings

```py
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
	for away_team in teams:
		if home_team != away_team:
			print(home_team + 'vs' + away_team)
```

### Common Errors

- It will not operate over a single element, it must be a sequence (iterable).

### Practice

1. Make a factorial function return the factorial of n and print the first 10 factorials (0 - 9).

```py
def factorial(n):
	result = 1
	for x in range(1, ___):
		result = ___ * ___
	return ___

for n in range(___, ___):
	print(n, factorial(n+ ___))
```

## Break and Continue

You can interrupt both while and for loops using the `break` keyword. We normally do this to interrupt a cycle due to a separate condition.

You can use the `continue` keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of the elements of the sequence aren’t relevant.

## Recursion

The repeated application of the same procedure to a smaller problem.

Doing a repetitive task by having a function call itself, usually with a modified parameter until it reaches a specific condition called the **base case**.

```py
def factorial(n):
	if n < 2:
		return 1
	return n * factorial(n - 1)
```

### Practice

1. Implement the sum_positive_numbers as a recursive function that returns the sum of all positive numbers between the number n received and 1.

```py
def sum_positive_numbers(n):
	return 0

print(sum_positive_numbers(3)) # should be 6
print(sum_positive_numbers(5)) # should be 15
```
