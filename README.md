# Devsite

This will be a small blog application to learn how to make a site w/ Flask. I will be following the [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by **Miguel Grinberg**.

## First time setup

If this is your first time running the site, please go through the following initialization steps:

- First clone the repository to your local machine using `git clone` and navigate into the repository.
- Setup a virtual environment for this project using `python -m venv <your_env_name>`.
    - I've used `pyenv` for my project, but `venv` is also good and is used by the tutorial linked above.
- Start the virtual environment with `source <your_env_name>/bin/activate`.
    - The virtual environment will stay active for the duration of the terminal session. This means everytime you opena  terminal, you will need to re-activate the virtual environment before developing.
- Install the list of packages outlined in the **Python modules** section below.
- After having installed `flask-sqlalchemy` and `flask-migrate` you should be able to run the command `flask db upgrade` to create a local SQLite DB with the required DB schema for the site to function.

## Running the site

Once the site is setup, here's how to run it from your terminal:

- Navigate to the repository.
- Before we can run the site, we need to let Flask know *where* the application is located. To do this, from the base directory simply do `export FLASK_APP=devsite.py` (On Windows it would be `set FLASK_APP=devsite.py`).
- Flask also supports `development` and `production` modes. You can change the mode by doing `export FLASK_ENV=<mode>` (On Windows it would be `set FLASK_ENV=<mode>`).
    - In `production` mode, the app will try to send emails for internal server errors, and will display the built in error pages if found. If the application is running, any changes to the source files will not be reflected until the site is restarted.
    - In `development` mode, the app will not display the built in error page for internal server errors, but instead show some debugging information. Addtionally, in this mode, hot-reloading is enabled, meaning any changes to the source files will take effect immediately.
- Now you should now be able to run the site using `flask run`.

### A note about SMTP configuration

The application should support sending emails to a list of admins whenever there is an ERROR level event/log.

The SMTP configuration, along with the list of admins, can be found in `config.py`.

**Miguel Grinberg** has provided two ways to setup and test the SMTP server functionality in the 7th installment of his tutorial: [The Flask Mega-Tutorial Part VII: Error Handling](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling). I would recommend checking it out for the full details.

## Python modules

Modules installed for this project are:
- `flask`
- `flask-wtf`
- `flask-sqlalchemy`
- `flask-migrate`
- `flask-login`
- `email-validator` (Note: I only needed to install this because I had an error. It should have been installed w/ `flask-wtf` above.)