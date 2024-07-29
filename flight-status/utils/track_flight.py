from collections import defaultdict
import sys
import os

sys.path.append(os.getcwd())
from dbwrapper import dbutils
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


def analyze_flight_schedule():
    flight_data = dbutils.fetch_documents(
        collection_name="flight_data",
    )
    delayed_flight_list = list()
    for _ in flight_data:
        se_arrival = datetime.strptime(_["scheduled_arrival"], "%Y-%m-%dT%H:%M:%SZ")
        ac_arrival = datetime.strptime(_["actual_arrival"], "%Y-%m-%dT%H:%M:%SZ")
        se_departure = datetime.strptime(_["scheduled_departure"], "%Y-%m-%dT%H:%M:%SZ")
        ac_departure = datetime.strptime(_["actual_departure"], "%Y-%m-%dT%H:%M:%SZ")
        if (se_arrival - ac_arrival).total_seconds() < 0 or (
            se_departure - ac_departure
        ).total_seconds() < 0:
            if (se_arrival - ac_arrival).total_seconds == 0:
                delayed_flight_list.append({'flight_id':_['flight_id'],'delay_by':ac_departure - se_departure, 'cancel':False})
                update_query = {
                        "$set": {
                            "status": "Delay"
                        }
                    }
                dbutils.update_docs(collection_name='flight_data',
                                    condition={"flight_id":_['flight_id']},
                                    update_query=update_query)
            else:
                delayed_flight_list.append({'flight_id':_['flight_id'],'delay_by':ac_arrival - se_arrival,'cancel':False})
                update_query = {
                        "$set": {
                            "status": "Delay"
                        }
                    }
                dbutils.update_docs(collection_name='flight_data',
                                    condition={"flight_id":_['flight_id']},
                                    update_query=update_query)
        elif _['status']=='Cancelled':
            delayed_flight_list.append({'flight_id':_['flight_id'],'cancel':True})

            
    
        

    return delayed_flight_list


def get_user_id_flight(delayed_flight):
    email_ids = list()
    delayed_flight_id  =  [_['flight_id'] for _ in delayed_flight]
    grouped_flight_id = defaultdict(list)
    for item in delayed_flight:
        grouped_flight_id[str(item["flight_id"])].append(item)
    
    condition = {"flight_id": {"$in": delayed_flight_id}}
    users_flight = list(
        dbutils.fetch_documents(collection_name="user_flight", condition=condition)
    )
    grouped_user_flight_data = defaultdict(list)

    for item in users_flight:
        grouped_user_flight_data[str(item["user_id"])].append(item)

    users_id = [_["user_id"] for _ in users_flight]
    users = list(
        dbutils.fetch_documents(
            collection_name="users",
            condition={"_id": {"$in": users_id}},

        )
    )
    user_email_id = [
        {
            "email": _["email_id"],
            "name": _['name'],
            "flight_id": grouped_user_flight_data[str(_["_id"])][0]["flight_id"],
            "delayed_by":grouped_flight_id[grouped_user_flight_data[str(_["_id"])][0]["flight_id"]][0].get('delay_by',''),
            "cancelled":grouped_flight_id[grouped_user_flight_data[str(_["_id"])][0]["flight_id"]][0].get('cancel',''),
        }
        for _ in users
    ]
    return user_email_id


def send_email(
    from_email,
    to_email,
    subject,
    body,
    login,
    password,
    smtp_server="smtp.gmail.com",
    port=587,
):
    # Create the message
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, "plain"))

    try:
        # Setup the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection

        # Login to the email account
        server.login(login, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)

        # Quit the server
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def send_delay_notification():
    user_email_id = get_user_id_flight(analyze_flight_schedule())
    print(user_email_id)
    for _ in user_email_id:
        from_email = "nileshgupta98g@gmail.com"
        to_email = _['email']
        if not _['cancelled']:
            subject = "FLIGHT DELAY - INDIGO"

            body = f"""Dear {_['name']},
                    We hope this message finds you well. We are writing to inform you that your upcoming.flight, {_['flight_id']} , has been delayed by {str(_['delayed_by'])} hour. We apologize for any inconvenience this may cause and appreciate your understanding and patience"""
        else:
            subject = "FLIGHT Cancelled - INDIGO"

            body = f"""Dear {_['name']},
                    We hope this message finds you well. We are writing to inform you that your upcoming.flight, {_['flight_id']} , has been cancelled. We apologize for any inconvenience this may cause and appreciate your understanding and patience"""
        smtp_server = "smtp.gmail.com"
        port = 587  # Typically 587 for TLS, 465 for SSL
        login = "nileshgupta98g@gmail.com"
        password = os.getenv("email_pass")
        send_email(
                    from_email,
                    to_email,
                    subject,
                    body,
                    login,
                    password,
                    
                )
        

send_delay_notification()


