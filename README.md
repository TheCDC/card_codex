# Card Codex
This repo contains everything powering [cardcodex.com](//cardcodex.com).

The notebook in this root directory shows how to use Gensim and TF/IDF to build the similarity engine.

[webapp/](webapp/) contains a Flask app that powers the website.

# Web App

The web serves an interface for exploring the card similarity engine. [webapp/](webapp/) contains everything required to run it and is also set up for deployment on Heroku. You can see it [here](http://card-codex-clone.herokuapp.com/).

# API

The [webapp](webapp/) also exposes a simple JSON api accessible at `/api` with the desired card name as the parameter. For example, to search for cards similar to the Commander/EDH staple `Lightning Greaves`, navigate to [https://card-codex-clone.herokuapp.com/api/?card=Lightning+Greaves](https://card-codex-clone.herokuapp.com/api/?card=Lightning+Greaves)
