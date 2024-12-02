# add and commit all changes
git add .
git commit -m $1

# pull changes from remote repository to local main
git checkout main
git pull origin main

# switch back to your branch and merge main
git checkout $2
git merge main

# push your branch to origin
git push origin $2
