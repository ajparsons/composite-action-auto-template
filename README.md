# Base project template

This is a base version of the github/cookiecutter template.

All it does it create an empty folder with readme, changelog, licence, and an empty version of testing and publishing workflows.

This is based on the general approach of [simonw/python-lib](https://github.com/simonw/python-lib), but with a different default structure. 

# Creating a new template

A new repository based on this template can be created in Github or through cookiecutter.

## Templating in GitHub

The templating process can be run entirely in GitHub to create a new repository. 

Start here: https://github.com/ajparsons/base-auto-template/generate

Add a one-line description of your repository, then click "Create repository from template".

# Templating with cookiecutter

This repo can also be used to set up a template offline using [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/). To start the processs:

```
python -m cookiecutter https://github.com/ajparsons/base-auto-template/
```

# Development and forking

If you want to modify or extend this approach - the self-bootstrapping behaviour will only happen when a repo does *not* end in '-auto-template'. If you clone this repo, into a different user or org space, it will not self-bootstrap because the name is the same.

If you wanted to extend this into a basic django template - you might fork or clone the repo and call it 'django-auto-template'. This will not self-bootstrap, but new projects created from that template would. 

## Meta tests

This project defines several meta tests in `tests/` that will:

* Attempt to provision a template with basic variables.

This requires the packages listed in `requirements.dev.txt` to be installed.
