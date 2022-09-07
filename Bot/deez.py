import json
import random

with open("jokes.json", "r") as f:
    data = json.load(f)

not_joke_response = [
    "Wow paranoid much? I can't believe you thought this was a deez nuts joke.",
    "WRONG! Not even close to a deez nuts joke.",
    "You should really be more trusting this definitely wasn't a deez nuts joke.",
    "Please explain to me in what way this could be a deez nuts joke.",
    "Wow, thats embarassing. WRONG.",
    "In all the thousands of galaxies in our universe, there is not a single one where this would be considered a deez nuts joke."
]

was_joke_response = [
    "Get fucked.",
    "Nice try Andrew.",
    "So gullible.",
    "Nice try kid.",
    "*stifled laughter*",
    "Andrew is that you?"
]


def prompt():
    random.seed()
    decision = random.randint(0, len(data) - 1)

    return data[decision]


def prompt_test():
    return data[47]


def nj_response():
    random.seed()
    decision = random.randint(0, len(not_joke_response) - 1)

    return not_joke_response[decision]

def j_response():
    random.seed()
    decision = random.randint(0, len(was_joke_response) - 1)

    return was_joke_response[decision]