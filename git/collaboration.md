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
