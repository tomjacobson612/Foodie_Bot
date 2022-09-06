import json
import random

with open("jokes.json", "r") as f:
    data = json.load(f)


def prompt():
    random.seed()
    decision = random.randint(0, len(data) - 1)

    return data[decision]
