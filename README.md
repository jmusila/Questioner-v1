## Questioner-v1  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  [![Build Status](https://travis-ci.com/jonathanmusila/Questioner-v1.svg?branch=develop)](https://travis-ci.com/jonathanmusila/Questioner-v1)  [![Coverage Status](https://coveralls.io/repos/github/jonathanmusila/Questioner-v1/badge.svg?branch=master)](https://coveralls.io/github/jonathanmusila/Questioner-v1?branch=master)


## Summary

- Questioner is a platform where people can see meetups, ask questions and attend meetups. 

## NOTE
* The project is managed using PivotalTracker board [click here](https://www.pivotaltracker.com/n/projects/2235195)


## Getting Started 

* Clone the repository: 

    ```https://github.com/jonathanmusila/Questioner-v1.git```

* Navigate to the cloned repo.

### Prerequisites

```
1. Python3
2. Flask
3. Postman
```

## Installation 
After navigating to the cloned repo;

Create a virtualenv and activate it ::

    create a directory 
    cd into the directory
    virtualenv -p python3 venv
    source venv/bin activate

Install the dependencies::

    pip install -r requirements.txt 

## Configuration

After activativating the virtualenv, run:

    ```
    export FLASK_APP="run.py"
    export FLASK_DEBUG=1
    export FLASK_ENV="development"

    ```
## Running Tests
Run:
```
pytest --cov-report term-missing --cov=app
```

### Testing on Postman
Fire up postman and start the development server by:
  ```
  $ flask run
  ```

Test the following endpoints:

### Meetups endpoints

| EndPoint                       | Functionality                           |
| -------------------------------|:---------------------------------------:|
| POST     /meetups/upcoming     | Posts new meetup                        |
| GET     /meetups/upcoming      | Gets all meetups as a list              |
| GET     /meetups/upcoming      | Gets a single meetup by id              |
|                                                                          |

### Questions endpoints

| EndPoint                            | Functionality                           |
| ------------------------------------|:---------------------------------------:|
| POST     /meetups/id/questions      | Posts new question                      |
| PATCH     /meetups/id/upvote        | Patches a upvote to a question          |
| PATCH     /meetups/id/upvote        | Patches a upvote to a question          |
|                                                                               |

### Rsvp endpoints

| EndPoint                            | Functionality                           |
| ------------------------------------|:---------------------------------------:|
| POST     /meetups/id/rsvp           | Posts a response to a meetup tag        |
|                                                                               |
