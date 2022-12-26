import datetime
import json
import requests
import pytz


def get_json_data(file: str):
    if not file.endswith(".json"):
        file = f"{file}.json"
    file = open(file)
    data = json.load(file)
    file.close()
    return data

def get_local_time(timezone: str):
    tz = pytz.timezone(timezone)
    return datetime.datetime.now(tz)

def post_to_factorial(factorial_id: str) -> None:
    url = "https://api.factorialhr.com/api/v2/time/attendance"
    try:
        response = requests.post(url)
    except Exception as e:
        print(f"Error ocurred: {e}")

    if not response.ok:
        print(f"Request error. Status code: {response.status_code}")
        print(f"Error text: {response.text}")
