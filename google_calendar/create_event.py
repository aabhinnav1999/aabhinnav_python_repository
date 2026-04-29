import os.path
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_user_datetime():
    while True:
        try:
            start_date_input = input("Enter start date (DD-MM-YYYY): ")
            start_time = input("Enter start time (HH:MM): ")

            # Ask user if end date is same
            same_day = input("Is end date same as start date? (yes/no): ").strip().lower()

            if same_day == "yes":
                end_date_input = start_date_input
            else:
                end_date_input = input("Enter end date (DD-MM-YYYY): ")

            end_time = input("Enter end time (HH:MM): ")

            # Convert dates
            start_date_obj = datetime.strptime(start_date_input, "%d-%m-%Y")
            end_date_obj = datetime.strptime(end_date_input, "%d-%m-%Y")

            # Validate time format
            datetime.strptime(start_time, "%H:%M")
            datetime.strptime(end_time, "%H:%M")

            # Convert to ISO format
            start_date = start_date_obj.strftime("%Y-%m-%d")
            end_date = end_date_obj.strftime("%Y-%m-%d")

            start_datetime = f"{start_date}T{start_time}:00"
            end_datetime = f"{end_date}T{end_time}:00"

            return start_datetime, end_datetime

        except ValueError:
            print("Invalid input. Please use correct formats.")


def get_calendar_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service


def create_calendar_event():
    service = get_calendar_service()

    start_dt, end_dt = get_user_datetime()

    event = {
    "summary": "Domino's",
    "start": {
        "dateTime": start_dt,
        "timeZone": "Europe/Dublin",
    },
    "end": {
        "dateTime": end_dt,
        "timeZone": "Europe/Dublin",
    },
    "reminders": {
        "useDefault": False,
        "overrides": [
            {"method": "popup", "minutes": 75},
        ],
    },
    "colorId": "5"
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event,
        sendUpdates="none"
    ).execute()

    print("Event created successfully!")
    print("Event link:", created_event.get("htmlLink"))


if __name__ == "__main__":
    create_calendar_event()