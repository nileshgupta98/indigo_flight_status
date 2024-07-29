
# Indigo Flight Status System

This system allows customers to check the status of their flights. After logging in, users can access a page to check flight status, where they can enter the flight number. The system will then display all relevant details about the flight. Additionally, users will receive notifications if their flight is delayed and cancelled. This repository contains both the front-end and back-end code.


## Tech Stack

**Frontend:** Reactjs, HTML, CSS

**Backend:** Python, Flask

**Database:** MongoDB


## Run Locally
## Frontend

Clone the project

```bash
  git clone https://github.com/nileshgupta98/indigo_flight_status.git
```

Go to the project directory

```bash
  cd my-project/airline-login
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```
## Backend

```bash
  git clone https://github.com/nileshgupta98/indigo_flight_status.git
```

Go to the project directory

```bash
  cd my-project/flight-status
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```

## Notification Script

```bash
    cd my-project/flight-status/utils
```
For push Notification you have to schedule the script track_flight.py at every 5 minute


## Setup Database

First you have to create database with the name **flight** and create Three collections.

* **Users:** It contain the user detail.

* **flight_data:** It contain the details of the flight.

* **user_flight:** It contain the user data and the flight data mapping.

**Note:** There is a dump of these three collections in the flight_status directory.
