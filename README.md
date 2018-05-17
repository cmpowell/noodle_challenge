# Noodle Coding Challenge

## Overview
This coding challenge solution allows a user to manage products and product attributes.
It demonstrates coding techniques, code structure, testing, and other "normal" engineering
activities across both an API application and a front-end application.

## Code Structure
This repository contains two applications:

- noodle-product-manager-server: a Python flask app serving the API and managing persistence
- noodle-product-manager-client: an Ember application providing the usr interface

## Server Application

### Requirements
This Python flask app requires:

- Python 3.6.x
- MySQL 5.7.x+
- pipenv (https://docs.pipenv.org)

### Running It

To run in development mode:
- Install your dependencies
    `pipenv install`
- Create the database and database user using your preferred method
- Update the values in `run.sh` and `run_test.sh` to reflect your db
- Run the server
    `run.sh`

The server will be running on http://0.0.0.0:5000/

### Not Included
This repositpory does not contemplate the following items:

- additional tests; they exist for some endpoint variations but not all due to time constraints
- production build and deployment
- continuous integration (Travis or similar)
- authentication, authorization and other forms of security
- websockets or other push notifications

## Client Application

### Requirements
This Ember app requires:

- Ember 3.1.x

### Running It

Please start the server first.

To run in development mode:
- Install your dependencies
    `pipenv install`
- Run the application pointing at the development server
    `ember serve -proxy http://0.0.0.0:5000/`

The application will be running on http://localhost:4200/ and will send
all API calls to the server running on http://0.0.0.0:5000

### Features
This includes the following features:

- Add product
- Edit product (including adding/removing associated attributes)
- List products
- Show individual product
- Delete product
- Add attribute

There are also component (integration) tests and acceptance tests, and a development environment.

### Not Included
This repository does not contemplate the following items:

- additional tests; they exist mostly as acceptance tests for the basic flows
- production build and deployment
- continuous integration (Travis or similar)
- authentication, authorization, CORS limiting and other forms of security
- error handling and success feedback
- a pylint structured for use with a flask app

The size of the problem was small enough that I didn't split up the API endpoints or other structural changes
that would be appropriate in a much larger application.
