# Gmail Ruler

This application provides two core functionalities.
1. REST API Server
2. A Command line tool to synchronize

## Pre Installation
This application is designed to run on Python 3. 
1. Install Python 3
2. Install virtualenv [Link](https://virtualenv.pypa.io/en/stable/installation/)
3. Extract the submission.
4. cd into the `gmail_ruler` folder and `pip install -r requirements.txt` will install all the dependent libraries.

## Instructions
### Run the initialization.
1. Run `python cli.py --help` for more detailed info. This package is developed using Click library.
2. Run `python cli.py initialize` to sync the recent emails only. To sync all the emails from your account, try it with the `--all` flag.

Now, take some nap while the emails synchronize with your current database.

### Run the server.
1. Run `python cli.py server` to start the flask server. 
2. There is only one endpoint that serves the core functionality.
3. You can find few examples in the example folder that has detailed comments and a working functions using the requests library.

## Few changes.
There are few changes in the names given to the Email model's attributes. 
The attributes are:
1. from_email
2. to_email
3. subject
4. content
5. received_at

