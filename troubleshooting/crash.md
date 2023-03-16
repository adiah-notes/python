# Crashing Programs

## Why Programs Crash

### Systems that Crash

### Understanding Crashing Applications

Look for logs that relate to the problem.

- console
- event viewer

Look for the date and time.

Can search for cryptic error messages online.

Enable debug logging if error messages are unavailable or unhelpful.

Other tools when there are no logs:

Linux:

- strace

Macos:

- dtruss

Windows:

- Process Monitor

Logs can show updates and also configuration changes.
These can be useful for debugging.

### What to do when you can't fix the program?

If you can't change the code, find a way to work around the problem.

Example pre-processing the input to the program to a suitable format.

Wrapper -> A function or program that provides a compatibility layer between two functions or programs, so they can work well together.

If the overall environment is not compatible, try to use the recommended os.
Can use virtual machines or containers.

Watchdog -> A process that checks whether a program is running and, when it's not, starts the program again.
Works well for systems where availability matters more than running continuously.

Always report bugs to the developers. Include as much info as possible.

- Answer questions
- Give the reproduction case

### Internal Server Error

- check that the failure is there for us too.
- look at logs
- `ls -lt | head`

`netstat` -> accesses stats on linux

### Resources for Understanding Crashes

## Code that Crashes

### Accessing Invalid Memory

### Unhandled Errors and Exceptions

### Fixing Someone Else's Code

### Debugging a Segmentation Fault

### Debugging a Python Crash

### Resources for Debugging Crashes

## Handling Bigger Incidents

### Crashes in Complex Systems

### Communication and Documentation During Incidents

### Writing Effective Postmortems
