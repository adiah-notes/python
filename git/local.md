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

`git branch`
`git branch branch-name`

Switch to a new branch with `git checkout branch_name`
Use `git checkout` to checkout the latest snapshot for both files and for branches.

Create a new branch and switch to it in one with `git checkout -b new_branch`.

Can create new files and commit to the new branch.

The `git log` will show that HEAD points to new branch.

### Working with Branches

`ls -l`

If you switch back to main, the HEAD will point to the latest commit in that branch.
Commits ahead of that in other branches won't even show up.

The working directory and commit history reflects the branch.

Delete branches with `git branch -d branch_name`.

If there are changes that haven't been merged to main, then there will be an error.

### Merging

Combing branched data and history together.

`git merge branch_name` from the branch you want to merge into.

There is

- fast-forward: All the commits in the checked out branch are also in the branch that's being merged.

- three-way: When the history of the merging branches has diverged in some way, there isn't a nice linear path to combine via fast-forwarding. Happens when a commit is made on one branch after the point when both branches split.

If the changes were made in different files or in different places in the same file, git combines the changes to get the result. If the changes are made on the same part, there will be a merge conflict.

### Merge Conflicts

`git merge branch_name`

There will be an error when trying to merge.

Open the files, git shows what needs to be fixed.
You decide which to keep, or if to change the file completely.

Run `git add` on file to update the status.

Call `git commit`

`git log --graph --oneline`

Can use `git merge --abort` to stop the merge and start over.

### Git Branches and Merging Cheat Sheet

| **Command**                 | **Explanation & Link**                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `git branch`                | [Used to manage branches](https://git-scm.com/docs/git-branch)                                                                        |
| `git branch <name>`         | [Creates the branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)                                        |
| `git branch -d <name>`      | [Deletes the branch](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D)                                             |
| `git branch -D <name>`      | [Forcibly deletes the branch](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D)                                    |
| `git checkout <branch>`     | [Switches to a branch](https://git-scm.com/docs/git-checkout)                                                                         |
| `git checkout -b <branch>`  | Creates a new branch and [switches to it](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--bltnewbranchgt)       |
| `git merges <branch>`       | [Merge joins branches together](https://git-scm.com/docs/git-merge)                                                                   |
| `git merge --abort`         | If there are merge conflicts (meaning files are incompatible), `--abort` can be used to abort the merge action.                       |
| `git log --graph --oneline` | [This shows a summarized view of the commit history for a repo](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) |
