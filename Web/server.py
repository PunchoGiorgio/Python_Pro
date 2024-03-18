import json
import random
import string
import time
from typing import Callable

import requests
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

variable = 777

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


def f(size):
    return "".join([random.choice(string.ascii_letters) for _ in range(size)])


create_random_string: Callable[[int], str] = f


@app.get("/generate-article")
def get_information():
    """This endpoint returns the random information"""

    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }


@app.get("/fetch-market")
def get_current_market_state():

    API_URL = "https://alphavantage.co/query"

    data = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "USD",
        "to_currency": "UAH",
        "apikey": "UHDZLAS4WZSOC9BW",
    }

    response = requests.post(API_URL, params=data)
    time.sleep(10)

    new_data = (
        {
            "status_code": str(response),
        },
    )

    with open("status.json") as f:
        status_data = json.load(f)

        status_data["results"] += list(new_data)

    with open("status.json", "w") as p:
        json.dump(status_data, p)

    with open("status.json") as k:
        update_data = json.load(k)

        if len(update_data["results"]) == 1:
            rate = response.json()["Realtime Currency Exchange Rate"][
                "5. Exchange Rate"
            ]
            return {"rate": rate}
        else:
            rate = variable
            return {"rate": rate}


if __name__ == "__main__":

    uvicorn.run("server:app", host="127.0.0.1", port=9000)
