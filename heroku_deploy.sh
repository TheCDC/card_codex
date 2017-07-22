# https://brettdewoody.com/deploying-a-heroku-app-from-a-subdirectory/
git push heroku `git subtree split --prefix webapp heroku`:master --force
# ensure card similarity models get built on heroku
heroku run python3 build_all.py
