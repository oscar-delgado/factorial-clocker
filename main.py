from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from utils import post_to_factorial, get_json_data, get_local_time


app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=3600)
def clock_to_factorial() -> None:
    users = get_json_data("users")

    for user in users:
        local_time = get_local_time(user["timezone"])

        if local_time.hour == 23:
            post_to_factorial(user["factorial_id"])
