# Git notes

`git log`
`git diff -u earlier-commit-id later...` 
`git checkout commit-id` to checkout an older commit, maybe before a bug was introduced. Commits made on it will make a new tip, ie start off in a new direction
`git add filename` adds to staging area
`git reset filename` unstages a file, or omit filename to remove all
`git diff` w/o args compares unstaged files with staged counterparts
`git diff --staged` compares staged files with most recent commit
`git reset --hard` discards changes in working dir AND staging area - CAUTION!
`git branch` with no args shows current branches
`git checkout` -b new_branch_name - makes a new branch and checks it out at once
`git merge master otherbranch` Actually the checked out branch is assumed so it can be `git merge otherbranch`
`git show commit-id` compares a commit against its parent. Parent isn't obvious after a merge, since commits are sorted by timestamp.
`git merge --abort` aborts merge
`git branch -d branch-name` - delete a branch, usually after merging it into master

Git highlights merge conflicts in the text editor
