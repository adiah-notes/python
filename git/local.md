# Using Git Locally

## Advanced Git Interaction

### Skipping the Staging Area

`git commit -a` Shortcut to stage any changes to **tracked** files and commit them in one step.

Git uses the `HEAD` alias to represent the currently checked-out snapshot of your project.

### Getting More Information About Changes

`git log -p` (for patch)

similar to `diff -u`. Shows the changes made in the repository

`git show` takes a commit id as a parameter.

`git log --stat` Shows some stats, such as which files were changed.

`git diff` - Shows what's changed in the staging

`git add -p` - shows the changes before adding

`git diff --staged` -> shows changes that have been staged

### Deleting and Renaming Files

`git rm` removes it from the git directory and stops it from being tracked.
Still needs to be committed.

`git mv` Rename files in the repository.
Still needs to be committed.

`.gitignore` tells git which files to ignore from the repo. For example automatically generated files with programming languages.
Needs to be added and committed.

### Advanced Git Cheat Sheet

| Command             | Explanation & Link                                                                                                           |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `git commit -a`     | [Stages files automatically](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---all)                         |
| `git log -p`        | [Produces patch text](https://git-scm.com/docs/git-log#_generating_patch_text_with_p)                                        |
| `git show`          | [Shows various objects](https://git-scm.com/docs/git-show)                                                                   |
| `git diff`          | [Is similar to the Linux `diff` command, and can show the differences in various commits](https://git-scm.com/docs/git-diff) |
| `git diff --staged` | [An alias to --cached, this will show all staged files compared to the named commit](https://git-scm.com/docs/git-diff)      |
| `git add -p`        | [Allows a user to interactively review patches to add to the current commit](https://git-scm.com/docs/git-add)               |
| `git mv`            | [Similar to the Linux `mv` command, this moves a file](https://git-scm.com/docs/git-mv)                                      |
| `git rm`            | [Similar to the Linux `rm` command, this deletes, or removes a file](https://git-scm.com/docs/git-rm)                        |

[Useful cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

## Undoing Things

### Undoing Changes Before Committing

`git checkout filename` to checkout files not yet staged.

`-p` - asks on a per-file basis.

### Amending Commits

### Rollbacks

### Identifying a Commit

### Git Revert Cheat Sheet

## Branching and Merging

### What is a branch

### Creating New Branches

### Merge Conflicts

### Git Branches and Merging Cheat Sheet
