# Slowness

## Understanding Slowness

### Why is My Computer Slow?

Identify the bottleneck.

Getting rid of other resources.
Only helps if too many processes trying to use the resources.

Hardware?

Ensure that you're addressing the bottleneck.

Check which resources are being exhausted (fully used).

`top` -> see which processes are using the most cpu time/memory.

`iotop` and `iftop` -> which processes are using the most IO usage or network bandwidth.

Activity Monitor (Mac)

Window (Resource Monitor and Performance Monitor)

First step is to open one of these tools and figure out which resource is the bottleneck and why.

Sometimes the software could be the issue.

### How Computers Use Resources

When an application is accessing some data, time to access will depend on location. Internal memory is really fast (variable currently being used in a function).

Running program, but not currently executed it'll be in RAM, which is still pretty fast.

In a file, it will be read from Disk, which is much slower. Over network is even worse.

So if a process needs to continuously access data over network, maybe it would be better to read once and store to disk.
Maybe read data from disk and store to cpu.

This is cache. Store data in a location that's much faster to use.

What happens when RAM runs out, swap. First closes anything cached not currently in use. Then swaps stuff not in use right now to the disk.

Might spend a lot of time reading and writing to disk to release RAM.

Too many open applications, close them. Add more RAM.

One of the programs may have a memory leak. Memory which is no longer needed is not getting released.

### Possible Causes of Slowness

Use the process of elimination, starting with the simplest.

When is the computer slow?

- at startup - too many applications configured to launch on boot. Disable any not really needed.

- slows after days of running fine, gets better with reboot. Some program that saves state while running. Almost certainly a bug. Schedule restart if no access to code.

- not solved with reboot. Files that application is handling is too large. Bug in design. Try to reduce size of files. rotate logs

All users or some?

- indexing. Can be slower.

- File system mounted over network. Use local directory.

- Hardware errors. Ensure hard drives are in good health.

- Malicious software. e.g scripts in webpages that mine crypto.

### Slow Web Server

`ab` to determine speed. `ab -n 500 site.example.com/`

`ssh webserver` ->

- look at output of `top`

load number -> how much time the processor is busy at a given minute, with one meaning it was busy for the whole minute.
So any number above the number of processors means it's overloaded.

change the process priorities. 0 - 19.

`nice` -> start process with priority
`renice` -> change priority of running processes

`pidof`

```bash
for pid in $(pidof ffmpeg); do renice 19 $pid; done
```

Run cpu intensive tasks one after the other instead of parallel.

`ps ax` shows all running processes on the computer

`ps ax | less`

`locate` -> gives the directory

`grep` -> check if any of the files contain call
`grep ffmpeg`

`killall -STOP` -> doesn't kill processes completely.

itereate over list of processes with `pidof`

```sh
for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done;
```

### Monitoring Tools

https://docs.microsoft.com/en-us/sysinternals/downloads/procmon

http://www.brendangregg.com/linuxperf.html

http://brendangregg.com/usemethod.html

Activity Monitor in Mac:

Performance Monitor on Windows

https://www.digitalcitizen.life/how-use-resource-monitor-windows-7

https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer

https://en.wikipedia.org/wiki/Cache_(computing)

https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/

## Slow Code

### Writing Efficient Code

Always start by writing clear code that does what it should, and only try to make it faster if we realize that it's not fast enough.

- Make computer do less work.
  - store data so not to calculate again
  - right data structures
  - reorganizing code

Where is the program spending most of its time.

profiler -> measures the resources that our code is using.
How memory is allocated.

`cProfile` for python.

How many times a program calls a function. And how much time for each function.

Expensive actions are those that take a long time to complete..

### Using the Right Data Structures

Avoid unnecessary expensive actions.

List -> fast to add/remove elements at ends, but slow in middle. Need to reposition all other elements.

Dictionary -> Key value pairs.
Super fast for looking up keys

> If you need to access elements by position, or will always iterate through all the elements, use a list to store them.

> If you need to look up the elements using a key, use a dictionary.

Double check if copies are necessary in memory. If the structures are large, it can become expensive.

### Expensive Loops

If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop.

For instance parsing a file outside of a loop, then store that in a dictionary and then only access the dictionary in the loop.

Make sure the list of elements you're iterating through is only as long as you really need it to be.

Break out of loops as soon as you find what you're looking for.

### Keeping Local Results

Can avoid accessing the data from a slow source over and over.

If it's stable information, won't get outdated quickly.

Depending on the use, the cache will need to be short-lived.

- How often the data changes
- How critical it is to have the latest data
- How frequently the program will be executed

A cache can be as simple as a variable that contains a value instead of calculating it over and over.

Storing intermediate results can be a way to cut down on how much of the expensive operation needs to be done.

### Slow Script with Expensive Loop

Use `time ./program` -> runs the script and calculates the time.

- Real -> The amount of actual time that it takes took to execute the command. Wall-clock time.
- User -> Time spent doing operations in the user space
- Sys -> Time spent doing system-level operations

`pprofile3` to get info on the program.  
`pprofile3 -f callgrind -o profile.out ./program`

Using the callgrind format?

Open with `kcachegrind` -> gui for callgrind.

`kcachegrind profile.out`

### More About Improving Our Code

[Profiling](https://en.wikipedia.org/wiki/Profiling_(computer_programming)

## When Slowness Problems Get Complex

### Parallelizing Operations

Reading from disk is slow, and the program will not usually be doing anything while that is happening.

Do operations in parallel.

`Concurrency`.

OS handles the processes. Decides which proceses occurs on which core.
What fraction of cpu time.

Split into different processes and let the os handle the concurrency.

Eg. if script collects stats for a list of computers, instead of the script being called for all the computers and going through one at a time, call the script on a smaller subset of computers and call it many times at once.

Have a good balance of processes that use different resources.

What about shared data?
**Threads** allow running parallel tasks inside a process.

Not handled by os.

In python -> `threading` or `async io`.

I/O bound may not need multiple processes.

### Slowly Growing in Complexity

### Dealing with Complex Slow Systems

Find the bottleneck.

Have a good monitoring system.

Eg having indexes for items queried often.

Modify code to be able to run on a distributed system.

Make sure that you're only doing what you really need to.

### Using Threads to Make Things Go Faster

import `futures` from `cuncurrent`

Executor -> process in charge of distributing teh work among the different workes.

Futures module -> provides different executors; one for threads and one for processes.

`executor = futures.ThreadPoolExecutor()`

instead of calling function directly, submit a new task to the executor.
`executor.submit(process_file, root, basename)`

The executor runs the functions in parallel.
the loop is finished as soon as all are assigned.

`executor.shutdown()`

Can try with `ProcessPoolExecutor()` instead. Makes more use of cpu.

Threads have a lot of safety features in python. May make them wait their turn.

### More About Complex Slow Systems

- https://realpython.com/python-concurrency/

- https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
