# Introduction to Version Control

## Before Version Control

It's important to have historical information. Provides way to rollback to previous versions.

### Keeping Historical Copies

Occasionally creating copies, so that you could go back. E.g -> version 1, version 2, final version, final final version.

It's manual, and not easy to know who made what changes.

Version control allows us to keep track of when and who did what changes to our files.

### Diffing Files

`diff` shows differences between two files (or even directories).

`diff -u` unified format

`wdiff` shows differences between words

`meld`

`kdiff3`

`vimdiff`

### Applying Changes

`diff -u old_file new_file > change.diff`

`patch` applies changes to original file from diff output.

`patch old_file < change.diff`

The original code could have changed. No matter which version they used.

Might be large files.

### Practical Application of diff and patch


## Version Control Systems

### What is a version control system?

Really just a system that stores files and keeps track of every version of the files.

Can make edits to multiple files and treat that collection of edits as a single change, known as a commit.

Allows author to record why a change was made.

Especially useful when tracking text files.

### Version Control and Automation

Can be invaluable even in one-person IT teams. It's like a time machine.
Can avoid puzzling over code and why it works etc.

## Using Git

### First Steps with Git

use `git config --global user.email "..@gmail.com"`
`git config --global user.name "name"`


Use `git init` -> to initialize a new git repository
creates a `.git` directory which houses all the files about the git repo.

Outside the git directory is the **working tree**, which stores the current version of the code. It's like a workbench. Files already tracked and files not yet tracked.


The git directory acts as a database for all the changes tracked in Git and the working tree acts as a sandbox where we can edit the current version of the files.

To make git track a file use `git add filename`, to the staging area.

**Staging area (index)** - file that contains all of the information about what files and changes are going to go into your next commit.

`git status` gives info on working tree and staging area.

`git commit` tells the computer you want to save.

### Tracking Files

Each time you make a commit, git takes a 'snapshot' of the project at the time.

Tracked files are a part of the snapshot -> can be modified, staged, or committed.
Git won't store changes unless you add files to the staging area.

Files -> modified -> staged > comitted

### The Basic Git Workflow

* All files must be part of a git repository. `git init`.
* `git config -l` -> check user names and emails.
* create file
* `git status`
* Tell git to track: `git add filename`
* Commit changes in the staging area: `git commit` or `git commit -m "message"`
* Add changes to the files
* Add and commit those changes: `git add filename` `git commit -m ""` or `git commit -am "message"`

### Anatomy of a Commit Message

The commit message should have contextual info.

There might be style guidelines for commit messages.

First line  -> short summary of the commit followed by a blank line. (~50chars)

Then full description of the changes, why they're necessary, and anything that might be especially interesting (or difficult to understand).

use `git log` to see history of commits and messages. Or `git log --oneline`


```
Commit message style guide for Git

The first line of a commit message serves as a summary.  When displayed
on the web, it's often styled as a heading, and in emails, it's
typically used as the subject.  As such, you should capitalize it and
omit any trailing punctuation.  Aim for about 50 characters, give or
take, otherwise it may be painfully truncated in some contexts.  Write
it, along with the rest of your message, in the imperative tense: "Fix
bug" and not "Fixed bug" or "Fixes bug".  Consistent wording makes it
easier to mentally process a list of commits.

Oftentimes a subject by itself is sufficient.  When it's not, add a
blank line (this is important) followed by one or more paragraphs hard
wrapped to 72 characters.  Git is strongly opinionated that the author
is responsible for line breaks; if you omit them, command line tooling
will show it as one extremely long unwrapped line.  Fortunately, most
text editors are capable of automating this.

:q
```