
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
![Login_page](https://github.com/user-attachments/assets/e408e044-d52d-47f0-a3a6-061fda15860c)
![Check_Status_page](https://github.com/user-attachments/assets/99fbc1a9-9e96-4cf5-ae13-a46397a8350a)
![Flight_status](https://github.com/user-attachments/assets/b58860d2-5a11-4165-b9b8-f6c59d07b61c)
![Check_Status_page1](https://github.com/user-attachments/assets/d20defdf-05eb-4b5c-916a-15a324f37a50)
![Flight_status1](https://github.com/user-attachments/assets/72982851-cecd-4799-ac42-b283f3eada46)
