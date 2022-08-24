import random

foodOptions = ["burrito", "burger", "soup", "tendies", "salad :(", "takeout"]

def random_food():
  random.seed()
  decision = random.randint(0, len(foodOptions)-1)
  return foodOptions[decision]