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

Remember in linux logs are stored in `/var/log`.

- `ls -lt | head`
- `tail syslog`

`netstat` -> accesses stats on linux
Gives info on the sockets etc.
Restricted to root, the administrator user on Linux.

use `sudo`.

```
sudo netstat -nlp | grep :80
```

Configuration files are stored in `/etc/`.

Check `/etc/nginx` for configs for `nginx` a popular web serving software.

```
ls -l /etc/nginx/
```

### Resources for Understanding Crashes

[Scientific American article](https://www.scientificamerican.com/article/why-do-computers-crash/) discusses possible reasons for crashes.

- Kernel Panic on Linux/MacOS
- Blue Screen of Death on Windows

* [How to find logs on Windows 10](https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/)

* [How to view the System Log on a Mac](https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/)

* [How to check systems logs on Linux](https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm)

Tools for diagnosing problems:

- [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) (Microsoft)
- [Linux strace command](https://www.howtoforge.com/linux-strace-command/)
- [How to trace your system calls on Mac OS](https://etcnotes.com/posts/system-call/)

## Code that Crashes

### Accessing Invalid Memory

If the code can be fixed, that's even better than working around the problem.

One reason for crashes is accessing invalid memory.

#### How does memory access work on modern operating systems?

Each process on the running on the computer gets a chunk of memory from the OS. This is used to store values and do operations on them during the program's execution.

The OS keeps a mapping table to which process is assigned which potion of the memory. Processes can't read or write outside the portions they were assigned.

> Accessing invalid memory means that the process tried to access a portion of the system's memory that wasn't assigned to it.

Programming errors might lead to a process trying to write to areas outside. This leads to an error message such as segmentation fault.

This type of error usually occurs with low level languages where the programmer has to control the program requesting memory and giving back when it's not needed anymore.

Pointers - the variables that store memory addresses.

- Forgetting to initialize a variable
- accessing a list element outside a valid range
- trying to use a portion of memory after having given it back
- trying to write more data than the requested portion of memory can hold.

The best way to deal with this is to attach a debugger to the faulty program. So you can get info when the program crashes.

You can get the parameters that the function received and find out the address that was invalid.

You can also get more information about what the application is doing and why the memories are invalid.

Debugging symbols - extra information that are usually stripped away from the binaries. Either by recompiling or downloading the debugging symbols.

Linux ships with theirs. Windows can generate in a PDB file.

Memory problems are usually Undefined behavior.

- The code is doing something that's not valid in the programming language.

Can be caused by different operating systems, and libraries.

For memory can use Valgrind.  
A powerful took that can tell us if the code is doing any invalid operations, no matter if it crashes or not.

Available on linux and Mac OS. Dr. Memory is similar and can be used on Windows and Linux.

### Unhandled Errors and Exceptions

If code encounters and exception or error that isn't handled properly, the application will stop suddenly.

Happens when the program makes incorrect assumptions.

An exception or error in one function doesn't mean the problem is in that function. A bad value could have been set in an earlier function.

Can use the debuggers for the specific languages:

- Python - pdb

Can also print data related to the code's execution.
Can show the contents of variables, return values of functions, or metadata like the length of a list or size of a file.

This is called print f debugging.

Add print lines in a way that is easy to enable or disable depending on whether you want to debug.

Can use the logging module in Python.
Can use it to set whether to include all debug messages or only info warning or error messaging.

Need to specify what type of message is being printed.
And can change the debug level with a flag or configuration setting.

Instead of crashing unexpectedly, it should inform the user of the problem and tell them what they need to do.

Sometimes it makes sense for a program to not even run if certain conditions are not met.

### Fixing Someone Else's Code

- Comments and well-documented functions are helpful and a great place to start.
  - If there aren't enough. Add them as you figure out what the code does.
- Reading the tests are also helpful. Tells what each function is expected to do. And which use cases weren't accounted for.

For really long codes, start with the function that has the error and then check the ones that call it and so on until you grasp the contexts that lead to the error.

### Debugging a Segmentation Fault

Core files store all the information related to the crash so that the programmer can debug what's going on.

Like taking a snapshot of the crash.

Tell the OS to store them:

```
ulimit -c unlimited

ls -l core
```

Pass the core file to the debugger.

```
gdb -c core [location]

(gdb) backtrace - shows a summary of the function calls that were  used to the point where the failure occurs.
```

Can assume some library functions such as `strlen` to be correct.

```
(gdb) up - moves calling function into backtrace

(gdb) list  - gives more information

(gdb) print  - prints a variable
```

### Debugging a Python Crash

```
pdb3 update_products.py new_products.csv

next - step through lines one by one
continue - let program run until it fails
```

### Resources for Debugging Crashes

- [https://realpython.com/python-concurrency/](https://realpython.com/python-concurrency/)
- [https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)
- [https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults](https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults)
- [https://sites.google.com/a/case.edu/hpcc/hpc-cluster/software/programming-computing-languages/cc/debugging-segmentation-faults](https://sites.google.com/a/case.edu/hpcc/hpc-cluster/software/programming-computing-languages/cc/debugging-segmentation-faults)

Readable Python code on GitHub:

- [https://github.com/fogleman/Minecraft](https://github.com/fogleman/Minecraft)
- [https://github.com/cherrypy/cherrypy](https://github.com/cherrypy/cherrypy)
- [https://github.com/pallets/flask](https://github.com/pallets/flask)
- [https://github.com/tornadoweb/tornado](https://github.com/tornadoweb/tornado)
- [https://github.com/gleitz/howdoi](https://github.com/gleitz/howdoi)
- [https://github.com/bottlepy/bottle/blob/master/bottle.py](https://github.com/bottlepy/bottle/blob/master/bottle.py)
- [https://github.com/sqlalchemy/sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)

## Handling Bigger Incidents

### Crashes in Complex Systems

Look for logs in a service that is failing.

- Any changes?
- Other services?
- Changes in database?

Rollback changes you suspect might cause the problem.

- Can restore the system to a functional state
- Or at least eliminate the change as a possible cause

Change the error message from something vague to something more informative.
Such as including what the request and response were and why the response was invalid.

Always look at logs first to see what the cause is.

Generating good logs is important as well as good monitoring of what the service is doing and use version control for all changes so that they can be rolled back.

Ability to quickly deploy new machines

- have machines on standby
- having a tested pipeline that allows deployment of new servers on demand

### Communication and Documentation During Incidents

Always document what you're doing while fixing a bug or problem.
Lets you keep track of what you tried and what were the outcomes.

Lets you share the data with other team members.

Helps you remember to roll forward the stuff you rolled back.

Communicate:

- Expected time of fix
- Regular communication of what is happening
- Regular updates of clear steps that users can do

If it's a large problem:

- Agree on who is working on what task
  - possible workarounds
  - root cause and solution
  - communicate with those affected
    - know what's going on and provide timely updates on the current state and how long until the problem's resolved.
  - delegating tasks (incident commander/controller)
    - ensure no duplication of work between team members

Once the issue is solved:

Sum up the information that was helpful.

- the root cause
- how you diagnosed the problem and found the root cause
- what you did to fix the issue
- what needs to be done to prevent the problem from happening again

Can be the last update to the ticket.

### Writing Effective Postmortems

Documents that describe details of incidents to help us learn from our mistakes.

Not to blame whoever caused the incident.

Document what happened, why it happened, how it was diagnosed, how it was fixed, and what we can do to avoid it happening in the future.

Can practice writing them for any event, no matter how small.

- What caused the issue
- What the impact of the issue was
- How it got diagnosed
- The short-term remediation you applied
- The long-term remediation you recommend

If it's long:

Summary:

- impact
- root cause
- action items

Document what went well as well.

Most important thing is what we can learn for the future.
