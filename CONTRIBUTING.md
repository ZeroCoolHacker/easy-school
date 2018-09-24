# Contributing
Welcome, dear new contributor! In this file you should find everything you need to get started on
helping me out a hand! This document has a very dry style to it, so let me express my insane
gratitude here before we get going. Thank You!

## Git
This repo uses git, hence it is on GitHub. Generally, `master` is the *next-release* branch, which people
~~shouldn't~~ **SHOULD NEVER EVER EVER EVER** clone to run in production, but you still shouldn't hack directly on it.
If you want to add a new feature, make a new branch. 
There is a naming scheme for branches:
`issueID.somename`

If there is no issue in the tracker for what you are doing you should create one and mention in a
comment you are working on a pull request. A maintainer will then set the appropriate tags.
If your branch is ready for production, submit a pull request. A maintainer will review your pull
request and (hopefully) accept it.

## Pull Requests
Every PR should pass the CodeClimate check (unless you provide good arguments for failing a check) 
and the Travis-CI tests (which can be run locally with `python manage.py test`).
If a PR fails the CI, I probably won't even look at it.

## What to do?
Look in the issue tracker. Generally the bugs with nobody assigned to that do not bear the tag
`in-progress` are up for help. Please post a comment stating you are working on that. A maintainer
will add the appropriate tags. New features should also be in the issue tracker, as well as ideas
(albeit with the correct tagging).

## I have an idea!
Great! Make an issue! A maintainer will tag it with `idea`, which means "up for debate" or `task`,
which means "somebody do this, please".

## Style
We use the [Python PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
There is a very practical CodeClimate check that is ran every time you push to a Pull Request.
It will show a nice green checkmark when you're doing good. If it's red, I'll complain.
Our code checker is not all that pedantic, so this should be doable. Thank you!

