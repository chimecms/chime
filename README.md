# What is this?

This is part of the Digital Front Door inititive.  You can read more about it here: https://github.com/codeforamerica/digitalfrontdoor

## Logging issues / ideas 
Make an issue: https://github.com/codeforamerica/ceviche-cms/issues/new

# Install

1. Ceviche CMS is a Python Flask web application. Follow the instructions on
   [Python Virtual Environments](https://github.com/codeforamerica/howto/blob/master/Python-Virtualenv.md)
   to prepare your Python development space.

2. Install the project requirements: `pip install -r requirements.txt`

3. You will need a bare Github repository in the directory `sample-site` with an initial empty commit
   (this will become configurable in the future):

 + `cd sample-site`
 + `git init`
 + `git commit --allow-empty -m "First commit"`

4. copy env.sample to .env

5. Run app using [Honcho and the `Procfile`](https://github.com/codeforamerica/howto/blob/master/Procfile.md):

        $ honcho start

# Who maintains this?

[Mike Migurski](http://github.com/migurski) and [Frances Berriman](http://github.com/phae)

You can read a bit more about what we're up to over here http://digifrodo.tumblr.com

[![Stories in Ready](https://badge.waffle.io/codeforamerica/ceviche-cms.svg?label=ready&title=Ready)](http://waffle.io/codeforamerica/ceviche-cms)
[![Build Status](https://travis-ci.org/codeforamerica/ceviche-cms.svg?branch=master)](https://travis-ci.org/codeforamerica/ceviche-cms)
