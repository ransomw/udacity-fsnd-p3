# Udacity fullstack nanodegree project 3

[Installing vagrant](https://www.udacity.com/wiki/ud197/install-vagrant), with the included `Vagrantfile`.

To run the project, execute `python run.py` from the `catalog` directory, optionally running `python capp/lotsofitems.py` first to prepopulate the database with some sample data.

For Google login, save the JSON file from the [Google developers console](https://console.developers.google.com/) APIs & auth > Credentials screen as `client_secrets.json` in the `catalog` directory.

For Github login, set the client ID and client secret in `catalog/capp/config.py`.  The Google client ID will be read from `client_secrets.json` and inserted into the appropriate parts of the application.

See the `pip` statements in `pg_config.sh` from non-standard python libraries used in the project.