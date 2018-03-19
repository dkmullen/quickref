# Git notes

-`git log`
-`git log --stat` Shows count of additions, deletions, etc.
-`git diff -u earlier-commit-id later...` 
-`git checkout commit-id` to checkout an older commit, maybe before a bug was introduced. Commits made on it will make a new tip, ie start off in a new direction
-`git add filename` adds to staging area
-`git reset filename` unstages a file, or omit filename to remove all
-`git diff` w/o args compares unstaged files with staged counterparts
-`git diff --staged` compares staged files with most recent commit
-`git reset --hard` discards changes in working dir AND staging area - CAUTION!
-`git branch` with no args shows current branches
-`git checkout` -b new_branch_name - makes a new branch and checks it out at once
-`git merge master otherbranch` Actually the checked out branch is assumed so it can be `git merge otherbranch`
-`git show commit-id` compares a commit against its parent. Parent isn't obvious after a merge, since commits are sorted by timestamp.
-`git merge --abort` aborts merge
-`git branch -d branch-name` - delete a branch, usually after merging it into master
-`git remote -v` shows name and path of remote repository
-`git fetch` updates local version of the remote branch (called origin/master). If remote changes were made by a collaborator, fetch pulls them down without messing with my master branch.
-`git log origin/master` shows the changes committed remotely but not on my local origin.
-`git merge origin origin/master` puts them together
-`git diff origin/master master`

-`git pull` is the same as `git fetch` then `git merge`

Git highlights merge conflicts in the text editor
