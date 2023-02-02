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

### Creating a Reproduction Case

### Finding the Root Cause

### Dealing with Intermittent Issues

### Intermittently Failing Script

## Binary Searching a Problem

### What is Binary Search?

### Linear and Binary Search

### Applying Binary Search in Troubleshooting

### Finding Invalid Data
