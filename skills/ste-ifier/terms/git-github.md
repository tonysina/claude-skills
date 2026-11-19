# Git and GitHub terms

Technical nouns (TN, rule 1.5 category 19: computer science and ICT) and
technical verbs (TV, rule 1.12 category 2: computer processes) for Git and GitHub.

- A TN is only a noun (rule 1.7). A TV is only a verb (rule 1.13). A term that
  is both is marked (TN, TV).
- Use a term only with its Git or GitHub meaning. In other contexts, the
  dictionary applies. For example, PUSH (v) is "to apply a force".
- If an approved verb gives the same instruction, use the approved verb.
  For example, "examine the pull request", not "review the pull request".
- Write commands, button names, and UI labels as quoted text or code
  (`git rebase`, "Approve"). Each counts as one word (rule 8.6).
- Write an abbreviation in full the first time (pull request (PR)).
- "Not:" at the end of an entry lists words to replace with that term (rule 1.11).

## Technical verbs
- commit (TN, TV): save changes to the local repository
- push (TV): send commits to a remote repository
- pull (TV): get commits from a remote repository and merge them
- fetch (TV): get commits from a remote repository without a merge
- merge (TN, TV): join the changes of two branches
- rebase (TN, TV): move commits onto a different base commit
- clone (TN, TV): make a local copy of a repository
- fork (TN, TV): make a copy of a repository in a different account
- stash (TN, TV): keep changes temporarily without a commit
- revert (TV): add a commit that cancels an earlier commit
- squash (TV): combine commits into one commit
- cherry-pick (TV): apply one commit from a different branch
- sign (TV): add a cryptographic signature to a commit or tag
- resolve (TV): only in "resolve a merge conflict" or "resolve a conversation"
- comment (TN, TV): write a comment on an issue or pull request
- edit (TV): change the text of a file, comment, issue, or pull request
- deploy (TV): approved in the dictionary, listed here for the Git meaning
- tag (TN, TV): add a named reference to a commit

## Technical nouns
- Git (TN)
- GitHub (TN)
- repository (TN): a Git repository. Not: repo
- project (TN): a software project or a GitHub Project
- file (TN): a computer file
- dropdown menu (TN)
- browser (TN)
- branch (TN)
- default branch (TN)
- main branch (TN)
- feature branch (TN)
- remote-tracking branch (TN)
- base branch (TN): the branch that a pull request merges into
- head branch (TN): the branch that contains the changes of a pull request
- compare branch (TN): the head branch, as GitHub shows it
- topic branch (TN)
- commit message (TN)
- commit hash (TN)
- SHA (TN)
- merge commit (TN)
- merge conflict (TN)
- pull request (TN): Not: merge request
- PR (TN)
- draft pull request (TN)
- review (TN): only as "pull request review" or "code review"
- code review (TN)
- reviewer (TN)
- review comment (TN)
- issue (TN)
- label (TN)
- milestone (TN)
- assignee (TN)
- mention (TN)
- remote (TN)
- origin (TN): the default remote name
- HEAD (TN)
- release (TN)
- release notes (TN)
- changelog (TN)
- diff (TN)
- staging area (TN)
- working tree (TN)
- checkout (TN): only as the command name "git checkout"
- hook (TN)
- pre-commit hook (TN)
- gitignore (TN)
- README (TN)
- workflow (TN)
- workflow run (TN)
- workflow file (TN)
- GitHub Actions (TN)
- action (TN): only a GitHub Actions action
- job (TN)
- runner (TN)
- pipeline (TN)
- build (TN)
- artifact (TN)
- CI (TN)
- status check (TN)
- branch protection rule (TN)
- environment (TN)
- secret (TN)
- access token (TN)
- personal access token (TN)
- SSH key (TN)
- GPG key (TN)
- webhook (TN)
- organization (TN)
- team (TN)
- owner (TN)
- collaborator (TN)
- maintainer (TN)
- contributor (TN)
- gist (TN)
- wiki (TN)
- CLI (TN)

## STE wording for Git actions with no approved verb

| Do not write | Write |
|---|---|
| Branch from main. | Make a branch from the main branch. |
| Create a pull request. | Open a pull request. / Make a pull request. |
| Review the pull request. | Examine the pull request. |
| Approve the pull request. | Give approval to the pull request. / Click "Approve". |
| Run the workflow. | Start the workflow. |
| Build the project. | Do a build of the project. / Start the build. |
| Stage the file. | Add the file to the staging area. |
| Assign the issue to Sam. | Make Sam the assignee of the issue. |
| Label the issue. | Add a label to the issue. |
| Reopen the issue. | Open the issue again. |
| Check out the branch. | Use `git switch` to go to the branch. |
