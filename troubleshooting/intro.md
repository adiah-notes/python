# Troubleshooting Concepts

## Introduction to Debugging

### What is Debugging?

Troubleshooting -> The process of identifying, analyzing, and solving problems. Any kind of problems.

Debugging -> The process of identifying, analyzing, and removing bugs in a system.

Tools like tcpdump and wireshark.
ps, top, free -> resourses
strace, ltrace

Debuggers.

### Problem Solving Steps

1. Getting information
   Documentation.

   Reproduction case: Clear description of how and when the problem appears.

2. Finding the root cause

   Probably the most difficult.

3. Performing the necessary remediation.

It's important to document what you do throughout the whole process.

### Silently Crashing Application

If a program doesn't even run.

`strace` lets us look more deeply at what a program is doing.
Trace the system calls made by the program and what the result of each of them is.

`strace ./program.py`

Outputs a lot.

System calls are calls that the running program make to the kernel.

`strace -o` store to a file

`strace -o failure.strace ./program.py`

## Understanding the Problem

### "It Doesn't Work"

Need to know what the actual issue is.
User reports usually don't include a lot of information.

Some questions you can ask:

- What were you trying to do?
- What steps did you follow?
- What was the expected result?
- What was the actual result?

Consider simplest explanations first.

Apply a process of elimination with simplest reasons.
First determine whether the problem is user-based.

### Creating a Reproduction Case

A way to verify if the problem is present or not.
Should be as simple as possible.

**Read logs available to you.**

- Linux

  - /var/log/syslog
  - .xsession-errors

- MacOS

  - /Library/Logs

- Windows
  - EventViewer tool

You can find an error message that will let you know what is going on.

**Try to isolate the conditions that trigger the issue.**

The smaller the changes needed, the better.

### Finding the Root Cause

Essential for long-term remediation.

Looking at info, coming up with hypothesis, and testing that hypothesis.

Look at info to come up with the hypotheses.

Whenever possible, check hypothesis in a test environment, instead of the production environment that our users are working with.

Show statistics on input and output operations and virtual memory operations.

- iotop
- iostat
- vmstat

network

current traffic

- iftop

rsync -> used for backing up -> `-bwlimit` for the bandwidth.

trickle also used to limit bandwidth.

Compression -> `nice`

### Dealing with Intermittent Issues

Problem that only occurs occasionally. Hard to reproduce and debug.

Can log more information (if you have access to the source code).

This can give you information when the problem happens again.

- load on computer
- processes running
- network usage

Heisenbug (observer effect). Bug goes away when meddling with them. Usually stem from bad resource management.

Bugs that go away when you turn something off and on again.

Rebooting -> releasing allocated memory, deleting temporary files, resetting running programs, establishing network connections, closing open files, etc.

If the bug can't be found, scheduling restart when system is not in use can also be an option.

### Intermittently Failing Script

## Binary Searching a Problem

### What is Binary Search?

Searching for an element in a list.

Splitting in half. Once the list is sorted
Recursion.

Doesn't make sense to sort a list to search it only for 1 element one time.

### Linear and Binary Search

```py
def linear_search(list, key):
   """If key is in the list returns its position, otherwise returns -1."""
   for i, item in enumerate(list):
      if item == key:
         return i
   return -1
```

```py
def binary_search(list, key):
   """
   Returns the position of key in the list if found, -1 otherwise.

   List must be sorted.
   """
   left = 0
   right = len(list) - 1
   while left <= right:
      middle = (left + right) // 2

      if list[middle] == key:
         return middle
      if list[middle] > key:
         right = middle - 1
      if list[middle] < key:
         left = middle + 1
   return -1
```

> Do this with recursion as exercise.

### Applying Binary Search in Troubleshooting

Going through and testing a long list of hypothesis.

Bisecting.

Example seeing which config file. and then when the file is found, which line.

Try half of them and see if it crashes. If it doesn't try the other half, and then keep cutting in half.

Or which extension crashes a browser, or which commit broke the repo, or which plugin.

`git bisect`

If the check takes time, it might make sense creating a script to check for the issue while doing bisecting.

### Finding Invalid Data

`wc -l` prints the number of lines in a file.

Use `head` and `tail` to print the first and last lines.

`head -50 contacts.csv | ./import.py --server test`
Try the file with just the first half. Using a test database instead of the production.

If this half fails:
`head -50 contacts.csv | head -25 | ./import.py --server test`

Now taking the first half of that first half.

If it succeeds, take the second half:
`head -50 contacts.csv | tail -25 | ./import.py --server test`

Keep splitting.

Once the number of entries is small enough, just display them without piping into the `./import.py`.
