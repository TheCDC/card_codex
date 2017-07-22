# https://brettdewoody.com/deploying-a-heroku-app-from-a-subdirectory/
git push heroku `git subtree split --prefix webapp heroku`:master --force
