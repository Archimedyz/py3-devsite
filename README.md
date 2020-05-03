# Devsite

This will be a small blog application to learn how to makea site w/ Flask. I will be following the [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by **Miguel Grinberg**.

## First time setup

If this is your first time running the site, please go through the following initialization steps:

- First clone the repository to your local machine using `git clone` and navigate into the repository.
- Setup a virtual environment for this project using `python -m venv <your_env_name>`.
    - I've used `pyenv` for my project, but `venv` is also good.
- Start the virtual environment with `source <your_env_name>/bin/activate`.
    - The virtual environment will stay active for the duration of the terminal session. This means everytime you opena  terminal, you will need to re-activate the virtual environment before developing.
- Install the list of packages outlined in the **Python modules** section below.
- After having installed `flask-sqlalchemy` and `flask-migrate` you should be able to run the command `flask db upgrade` to create a local SQLite DB with the required DB schema for the site to function.

## Running the site

Once the site is setup, here's how to run it from your terminal:

- Navigate to the repository.
- Before we can run the site, we need to let Flask know *where* the application is located. To do this, from the base directory simply do `export FLASK_APP=app.py`.
- Now you should nw be able to run the site using `flask run`.

## Python modules

Modules installed for this project are:
- `flask`
- `flask-wtf`
- `flask-sqlalchemy`
- `flask-migrate`
- `flask-login`
