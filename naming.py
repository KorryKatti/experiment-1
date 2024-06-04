import json
import random

# Randomly generated names
female_names = ["ek", "do", "teen", "chaar"]
male_names = ["alpha", "beta", "gamma", "delta"]

# Selecting random names
female_people = []
male_people = []

# Generate starting HP
starting_hp = 100.0

for _ in range(3):
    female_name = random.choice(female_names)
    male_name = random.choice(male_names)
    female_people.append({"name": female_name, "gender": "female", "age": 0.0, "hp": starting_hp})
    male_people.append({"name": male_name, "gender": "male", "age": 0.0, "hp": starting_hp})

# Combine female and male people
people = female_people + male_people

# Writing the list of people to a JSON file
with open("jsons/people.json", "w") as json_file:
    json.dump(people, json_file, indent=4)

print("Names written to people.json file successfully.")
