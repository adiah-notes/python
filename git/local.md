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

Use `git reset` to unstage changes we don't want to commit. `git reset -p` to get git to ask which specific changes to reset.

### Amending Commits

If you've forgotten to add a file to the same commit change, or you want a more descriptive commit message.

First add the files you may have forgotten.

Use `git commit --amend`, take what's in the current staging area and run `git commit` to overwrite the previous commit.

Git amend is okay for local commits, but don't use it on public commits.

### Rollbacks

If you've pushed to a repo already and there is an issue you can go back to a previous snapshot.

One way is with `git revert`. This isn't just an undo, it creates a commit with the inverse of the changes made in the bad commit.

This keeps the history consistent.

Can revert the latest commit by using the HEAD alias.

`git revert HEAD`

Usually a good idea to add an explanation of why we're doing the rollback.

`git log -p -2` -> last two commits

### Identifying a Commit

What if an error is not the latest commit?
Can target a specific commit by using its commit ID.

The commit ID is made from hashing all the information about a commit.
This helps with data integrity.

Can use `git show <id>` the show a specific commit.

Don't need to copy and paste the whole id. Can just provide the first few characters. Four to eight is usually enough.

Can call the `git revert <id>` with the identifier.

This only reverts that commit, leaving the ones in-between intact.

### Git Revert Cheat Sheet

[`git checkout`](https://git-scm.com/docs/git-checkout) is effectively used to switch branches.

[`git reset`](https://git-scm.com/docs/git-reset#_examples) resets the repo.

[`git commit --amend`](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend) is used to make changes to commits after-the-fact.

[`git revert`](https://git-scm.com/docs/git-revert) makes a new commit which effectively rolls back a previous commit.

[More ways](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) to rollback commits in Git.

## Branching and Merging

### What is a branch

At it's most basic a pointer to a particular commit. It represents an independent line of development in a project.

The commit it points to is the latest link in a chain of developing history.

The default branch in now `main`.
Commonly used to represent the known good state of a project.

To develop a new feature, or try something new, create a separate branch to do your work without worrying about messing up that current state.

You can merge back into the main branch when you've got something you like, or discard changes without negative impact.

### Creating New Branches

`

### Merge Conflicts

### Git Branches and Merging Cheat Sheet
