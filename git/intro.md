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

