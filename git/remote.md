# Working with Remotes

## Introduction to GitHub

### What is GitHub?

Distributed -> Each developer has a copy of the whole repository on their local machine.

Can host one copy on a server and use it as a remote repository for the other copies, allowing synchronization.

### Basic Interaction with GitHub

Create account on github.com.

Create repos.

`git clone` repos to local machine.

Stage and commit changes.

`git push` send to the remote server.

`git pull` to download changes from the remote server.

### Cheat-Sheet

## Using a Remote Repository

### What is a remote?

Lets lots of developers work on shared repositories from their own workstations.

Each individual can make changes and commits to there local copy of the repository, or even on different branches and `push`
to the remote.

If there are changes to the main repository since the last time you updated your local copy, git will let you know.

Modify, stage, and commit local changes.
Then fetch any new changes from the remote repository and manually merge if necessary, then push our changes to the remote repository.

Can access with HTTP, HTTPS, and SSH protocols.

No limits to how many can push to the repo. Good idea to control who can push to the repo.

### Working with Remotes

`git clone` creates a default `origin` name.

`git remote -v`
can see the two urls to fetch and push data.

It is possible to have more than one remote, useful when collaborating with different teams.

`git remote show origin`

`Remote branches` keep copies of data that's stored in the remote repository.
`git branch -r` -> these are read only.
need to merge them with the local branch to make changes.

`git status` can be used to check status with remote as well.

### Fetching New Changes

`git remote show origin`
will show 'out of date' if there were remote changes.

Use `git fetch`, to get data in remote branches.
Use `git checkout` on the branches to see the working tree, and `git log` to see the commit history.

Example `git log origin/master`

If there are changes, the origin will be pointing to the latest commit.

And local main will point to the previous commit.

`git status` will let us know this.
Can merge the remote branch using `git merge origin/main`

`git log` will show the commit reflected.

> `git fetch` fetches remote updates, but doesn't merge; `git pull` fetches remote updates and merges.

Use `git fetch` to review changes. Then merge them if you want to keep.

### Updating the Local Repository

`git pull`, fetches and merges at once.

Remember `git log -p -1`

If there's a new remote branch, can check it out with `git checkout experimental`. Git will set up a new local branch and copy the remote branch.

`git remote update` will let you fetch the contents of remote branches, can checkout or merge as needed.

### Cheat-Sheet

| **Command**              | **Explanation & Links**                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git remote`             | [Lists remote repos](https://git-scm.com/docs/git-remote)                                                                                                           |
| `git remote -v`          | [List remote repos verbosely](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v)                                                                  |
| `git remote show <name>` | [Describes a single remote repo](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem)                                                         |
| `git remote update`      | [Fetches the most up-to-date objects](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem)                                                  |
| `git fetch`              | [Downloads specific objects](https://git-scm.com/docs/git-fetch)                                                                                                    |
| `git branch -r`          | [Lists remote branches](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r); can be combined with other branch argument to manage remote branches. |

## Solving Conflicts

### The Pull-Merge-Push Workflow

`git push`
What if when pushing, there are changes to the remote?

Git will reject the push, since it can't fast forward.

Use `git pull`.

Use `git log --graph --oneline --all`.

May need to do a three way merge if branches split.

`git log -p origin/master`

Shows the conflicts.
Fix them (look for >>>)

Use `git add` and then `git commit` to complete the merge.

Then you can complete the push

### Pushing Remote Branches

Remember to create separate branches for new features.

`git checkout -b refactor`.

`git push -u origin refactor`.
Set the upstream for the branch in origin.

### Rebasing Your Changes

Once branch is reviewed and tested, it can be merged back to main.

Can use `merge` or `git rebase`.

Because of three-way splits, it's difficult to debug etc.
So if there were commits to the main, while you were working on another branch.

Use `git rebase` calling the branch to be the base to keep commits linear.

`git checkout refactor`

`git rebase main`

Then checkout to main and merge refactor.
Afterwards, delete the branches remotely and locally.

`git push --delete origin refactor`

`git branch -d refactor`

Then push changes back to the remote repo.

### Another Rebasing Example

If collaborator makes changes to main and it's not big enough to create a separate branch.
Just happened to commit something at the same time.

To keep history linear instead of creating three way merge.

Use `git fetch`. Can see if there were new changes. If there are, then merging will cause a three way.

Use `git rebase origin/master` to rebase local changes against those made by colleagues.

You might have conflicts -> Just fix them, or abort, or skip.

> Remember when fixing conflicts, to test before committing.

`git add` conflicting files.

`git rebase --continue` to finish the rebase.

Then push to the repo.

### Best Practices for Collaboration

- Always synchronize branches before doing any local work.

- Avoid very large changes that modify a lot of different things. Keep them self-contained.

- When working on a big change, do it on a new branch.

- Regularly merge changes made on the master branch back onto the feature branch.

- Have the latest version on main, and the stable version on a different branch.

- Don't rebase changes that have been pushed to remote repos.

- Good commit messages are important.

With merge conflicts, try removing all your code to see if the code still works before adding piece by piece.

### Conflict Resolution Cheat-Sheet

[`git rebase branchname`](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) changes the base of the current branch to be branchname.

[More information](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) on `git rebase`.
