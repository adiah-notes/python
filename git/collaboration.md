# Collaboration

## Pull Requests

### A Simple Pull Request on GitHub

Can look at other people's code and collaborate on them.

Example: fixing a typo.

Editing it will create a fork.

A way of creating a copy of the repository so that it belongs to our user. So we can push changes to this copy.

Can eventually merge to the main repository by submitting a pull request.

A commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree.

Only a few people will have commit rights to the repository.

Can make a change proposal on GitHub. And then create pull request.
Allow edits.

### The Typical Pull Request Workflow on GitHub

Instead of doing pull request directly on GitHub.

Use a local copy of the forked repos on our machine.

Create a fork, use `git clone` to get a local copy.

`ls -l` and `git log`

Create a branch to add a README, for example:
`git checkout -b add-readme`

Edit the README.md

save and Commit.
`git add README.md`
`git commit -m "Add README.md"`JKO
`git push -u origiin add-readme`

Can make pull request.

Can include the testing methods and test files for any automatic testing.

### Updating an Existing Pull Request

Make changes, save, commit, and push to repo.

GitHub will automatically edit the pull request.

This is once you've pushed to the same branch.
To create a second pull request, you need to push to a different branch.

### Squashing Changes

`rebase -i`

`git rebase -i main`

Change the first word of each line to choose what to do with each commit:

- `pick` (default) -> takes the commit and rebases it against the branch selected.

- `reword` -> edit the commit messages

- `squash` -> combine the commit messages

- `fixup` ->

`git push -f` to force git to push the commit. This is used because we are replacing the commits in the pull request.

### Git Fork and Pull Request Cheat Sheet

[More info](https://help.github.com/en/articles/about-pull-request-merges)

## Code Reviews

### What are Code Reviews

Going through someone else's code, documentation, or configuration and checking that it all makes sense and follows the expected patterns.

The goal is to improve the project.

Comment on someone else's code. About making our code better.

### The Code Review Workflow

`Nit` ->

Style guide.

### How to Use Code Reviews in GitHub

View changes, to see all the changes requested.

Make the changes.

Use `git commit -a --amend` to amend the commit.

`git push -f`

Forcing pushes is fine for pull requests, because no one else should be using that fork. Don't use for commits already pushed to a public repo though.

Can ignore the outdated requests, and mark as resolved. Then add a comment for the reviewer to know it's been fixed.

### More Information on Code Reviews

- http://google.github.io/styleguide/

- https://help.github.com/en/articles/about-pull-request-reviews

- https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31

- https://smartbear.com/learn/code-review/what-is-code-review/

## Managing Projects

### Managing Collaboration

Try to refactor parts of the project while others are working on some other part.

Good documentation.

Respond to requests quickly.

When maintaining, understand all changes you accept.

Make sure to create a style guide. And use the style guide when contributing.

Slack, Telegram groups to communicate.

### Tracking Issues

Deciding who's going to do what.

Use an issue tracker or a bug tracker. Can add comments to the issue.

Allow users to report bugs later on.

- Bugzilla
- Baked in to GitHub

Use `closes:#4` for example in commit message to automatically close the issue once the pull request is merged.

Assign issue to yourself.

Can use `git commit -a`

end with `Closes #1`

### Continuous Integration

Automated tests to test system and test the code each time there is a change.

Verify that the code will work once it gets merged.

Continuos Deployment/Delivery. Incremental updates with only a few changes at a time.

CI/CD:

- Jenkins
- Travis (with GitHub)

Pipelines - specify the steps that need to run to get the result you want.

Could just be to run the tests.

Or compile, run tests, deploy.

- Make sure authorized entities for test servers are not the same entities authorized to deploy on the production servers.

- Always have a plan to recover your access in case your pipeline gets compromised.

### Additional Tools

- https://arp242.net/diy.html

- https://help.github.com/en/articles/closing-issues-using-keywords

- https://help.github.com/en/articles/setting-guidelines-for-repository-contributors

- https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html

- https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/

- https://docs.travis-ci.com/user/tutorial/

- https://docs.travis-ci.com/user/build-stages/

---

# Steps in real projects

Project steps
Before Version Control: Before diving into code, ensure your team is aligned on the project's scope, goals, and responsibilities.

Version control systems: Choose Github as your version control system to track changes, collaborate effectively, and maintain a history of your project.

Using git: Start by initializing a Github repository, committing your initial code, and using git status and git log to manage and track changes.

Advanced git interaction: Use advanced commands like git diff to visualize changes, git stash to temporarily hide changes, and git tag to mark significant milestones.

Undoing things: Use git reset and git revert to undo changes and address errors in a controlled manner.

Branching and merging: Create branches for feature development using git branch, switch between branches with git checkout, and merge changes using git merge.

Secure shells & API keys: Ensure security by using SSH keys and managing sensitive data like API keys properly.

Solving conflicts: Resolve conflicts that arise from merging branches using git merge or pull requests.

Pull requests: Open pull requests to propose changes, review code, and discuss modifications with your team.

Code reviews: Participate in code reviews to maintain code quality, identify improvements, and ensure best practices.

Managing projects: Organize your project using project boards, milestones, and issues to track progress and prioritize tasks.

Putting it all together
Imagine you're assigned to add a new feature to your project: a user authentication system. Here's how you'd apply your skills:

Before version control: Working with your development team and stakeholders you define the feature's scope and priorities. From the business requirements you develop user stories from which the team can build out tasks. Review the tasks your team created and discuss expected outcomes.

Version control systems: You create a feature branch for the authentication system on the app's existing repository that is already located on github. Your team uses this new branch to begin to work on the tasks associated with the feature request.All progress is tracked in real time and documented with comments in Github.

# Create a new feature branch

git checkout -b feature/user-authentication

Advanced git interaction: You use git diff to view and compare code changes and look back at the history of changes. When needed you can use git diff to compare whole branches as the feature becomes more robust. As you get closer to completing the feature you create tags to mark development milestones. When feature release is approaching, you can use a milestone to share progress with stakeholders.

# View code changes

git diff

# View commit history

git log

# Create a new tag

git tag v1.0.0

# Compare branches

git diff feature/user-authentication main

Undoing things: As you encounter issues, you have stable milestones you know you can restore back. You can stash away pending changes or, safely undo changes using Git's commands.

# Stash changes

git stash

# Restore changes from stash

git stash pop

# Undo changes in working directory

git checkout -- <file>

Branching and merging: Your team makes sure to keep up with branching and merging changes. The team tests their changes in the feature branch to avoid introducing any issues or bugs into the main branch.

# Merge changes from feature branch to main

git checkout main

git merge feature/user-authentication

# Delete feature branch

git branch -d feature/user-authentication

Solving Conflicts: As code conflicts arise during merging, you attempt to automerge. When deeper conflicts arise, you gather your team and address them collaboratively.

# Attempt to automerge

git merge feature/user-authentication

# Resolve conflicts manually

# Edit files to resolve conflicts

git add <resolved-files>

git commit -m "Resolved conflicts"

Pull requests and code reviews: One of your team members opens up a pull request for your feature branch. It is finally time to merge our feature into the main branch. Automated tests run against the code in question and your team schedules a code review. You prepare to gather and track feedback.

# Push changes and open pull request

git push origin feature/user-authentication

# Automated tests run in CI/CD pipeline

# Pull request is reviewed

# Feedback is addressed

Code reviews: All concerned parties participate in code reviews. Team members address the group and review their code additions. Tests and metrics are also reviewed. The team collaborates at addressing feedback and ensuring high-quality code.

Managing projects: Throughout the project, and even after development efforts have concluded, you continue to track the progress of your feature using project boards, milestones, and issues. Development is iterative and your team will continue to work on features as feedback and requests come in from stakeholders.
