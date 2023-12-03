# Managing Resources

## Managing Computer Resources

Make sure that applications make the best use of the resources available.

### Memory Leaks and How to Prevent Them

A chunk of memory that is no longer needed is not released.

Can become larger and larger over time and cause the whole system to give trouble.
Reduces the memory other processes can access, causing other unrelated processes to crash.

Garbage collector - checks what memory is not in use anymore.

If the code keeps variables pointing to data in memory, the garbage collector won't release that memory.

Example returning a whole dictionary instead of just a single value.

Less of an issue for programs that are short-lived.

If a program starts with a small amount of memory but requires more and more as it runs, then it's pretty likely that the program has a memory leak.

Can use a `memory profiler` to figure out how the memory is being used:

- valgrind (c)
-

Only keep data that you actually need.

### Managing Disk Space

As available space gets smaller, system slows down.
Data gets fragmented across the disk and operations become slower.

A full hard drive can cause crashes as programs try to write.
Can also lead to data loss as some programs may truncate a file before writing an updated version of it, then fail to write the new content.

User machine - uninstall unused applications or delete unneeded files

Server - check if an application is misbehaving or needs more space.

See if large chunks of space are taken up by valid information or if it needs to be purged.

A program that keeps logging error messages can take up a lot of space.

Maybe valid logs that are just too much.

Temporary files that are not being cleaned up.

Deleted files taking up space.

### Network Saturation

- latency - delay between sending a byte of data from one point and creceiving it on the other

  - affected by physical distance and objects between them.

- bandwidth - how much data can be sent or received in a second.

For smaller data -> want server to be as close to client to reduce latency

For larger data -> want server to have as high a bandwidth as possible

`iftop` shows how much data each application is sending

Traffic shaping - marking packets with different priorities so huge chunks don't monopolize all the data.

There are limits to how many connections a single server can have, which can prevent new connections.

### Dealing with Memory Leaks

`uxterm`

scroll buffer

### More About Managing Resources

- [https://realpython.com/python-concurrency/](https://realpython.com/python-concurrency/)
- [https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)
- [https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python](https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python)
- [https://www.linuxjournal.com/content/troubleshooting-network-problems](https://www.linuxjournal.com/content/troubleshooting-network-problems)

## Managing Our Time

### Getting to the Important Tasks

Eisenhower Decision -> urgent and important tasks

Technical debt - the pending work that accumulates when we choose a quick and easy solution instead of applying a sustainable long-term one.

### Prioritizing Tasks

1. Make a list of all the tasks that need to get done.
   Could keep it in an issue tracker.

2. Check the real urgency of the tasks.
   Complete the most urgent tasks.

3. Assess the importance of each issue.

   - a task that benefits more people is more important than one that just benefits.

4. How much effort they'll take.
   Can use small, medium, and large.

Try to start with larger and more important tasks first.

Can also save most complex tasks for times when you're less likely to get interrupted.

The key is to always work on important tasks. Then select the urgency.

Shouldn't stop you from taking breaks and working on personal interesting projects.

Working extra hours is not sustainable:

- get extra help
- decide some tasks weren't as important and won't get done

This needs to be communicated with managers.

Some tasks are small and self-contained. Others are more involved.

### Estimating the Time Tasks Will Take

Most of us are too optimistic about how long it takes.

We son't take into account things that aren't optimum in terms of focus and things going wrong.

One way is to compare similar tasks completed prior. And assuming the time would be similar.

If there aren't previous tasks similar enough, break the task up into smaller steps and compare each step to a similar task and assign time based on that.

Even that is going to be optimistic since it'll take time combining all the steps.
So add in some extra time for integration. This comes from prior experience.

This number is gonna be close for the best case scenario.
Things can go wrong. So use a factor for example multiplying the time by three.
This gives you a buffer.

After can adjust future estimations based on how the actual time compared with the assumed time.

### Communicating Expectations

It's important to know that users have expectations that might not line up with reality.

Communicate with users and let them know the timeframe they can expect. Then figure out how critical it is to solve the problem.

Make sure to tell user if you're dealing with a crisis.
Be upfront with the time it would take to solve the problem.
Or when they can expect updates.

A ticket tracking system can be valuable.
All the work is in one place and can organize by priority.

Practical shortcuts

- asking a user to bring a broken mouse to you instead of going to check.
- have spare hardware if something breaks down

### More About Making the Best Use of Our Time

[https://blog.rescuetime.com/how-to-prioritize/](https://blog.rescuetime.com/how-to-prioritize/)

## Making Our Future Lives Easier

### Dealing with Hard Problems

> Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?

Don't write complicated programs, make everything clear.

This applies to engineering systems.
When something goes wrong we can fix it easier.

- Develop code in small digestible steps.
- Keep your goal clear
  - write tests first so you know what the code should do

Remember you can do short-term remediation to get things up and running.

Ask for help if you need it.

### Proactive Practices

Good unit tests and integration tests.

Test changes before they get to end user.

continuous integration and a test environment.

Test the software how it will be used by end users.

Deploy in phases or canaries. Eg. updating some computers and then seeing how they go before updating more.

Set up architecture that allows for quick rollbacks.

Good debug logging.

Centralized logs collection - a special server that gathers all the logs from all the servers, or even all the computers in the network.

don't need to connect to each machine to check logs.

Good Monitoring system.

- can catch issues early

Ticketing services

ask users to provide needed information upfront.
Or have a script to collect all necessary data and let users attach that to ticket.

Documentation of troubleshooting steps. A checklist.

### Planning Future Resource Usage

A service that is expected to grow with popularity.

figure out a plan to allow resources to grow.

This is better to do when not under pressure to change.

Mix and match processes that use different resources on the same machine.

Cloud services make this process easier.

### Preventing Future Problems

Good monitoring.

Send data to a centralized location where you can look at all the logs for the systems you care about.

- cpu
- disk
- memory
- network usage
- info on the specific service running
  - no of queries in a databae

Remember to report bugs to relevant developers.
Workarounds for this version might not be applicable in future versions.

If it's software ou own write tests to catch the case.
Perform the tests whenever there's a new version.

### More About Preventing Future Breakage

#### Problem Domains

The complexity of a given problem that one is trying to solve

- [https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/](https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/)
- [https://deploy.equinix.com/blog/explaining-failure-domains-sre-lifeblood/](https://deploy.equinix.com/blog/explaining-failure-domains-sre-lifeblood/)
- [https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/](https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/)
