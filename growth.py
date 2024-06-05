import json
import random
import time

def load_players_data():
    with open("data/playersdata.json", "r") as file:
        players_data = json.load(file)
    return players_data

def update_age(players_data):
    for player in players_data:
        player["age"] += 2

def save_players_data(players_data):
    with open("data/playersdata.json", "w") as file:
        json.dump(players_data, file, indent=4)

def combine_traits(trait1, trait2):
    if random.choice([True, False]):
        return trait1
    else:
        return trait2

def generate_name(gender):
    vowels = "aeiou" if gender == "female" else "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxyz"
    name = ""
    for _ in range(random.randint(3, 8)):
        if random.choice([True, False]):
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name.capitalize()

def generate_child_hp(parent1_hp, parent2_hp):
    return (parent1_hp + parent2_hp) // 2

def generate_child(parent1, parent2):
    child = {}
    child["name"] = generate_name(random.choice(["male", "female"]))
    child["year_born"] = parent1["year_born"]
    child["hp"] = generate_child_hp(parent1["hp"], parent2["hp"])
    child["dominant_trait"] = combine_traits(parent1["dominant_trait"], parent2["dominant_trait"])
    child["recessive_trait"] = combine_traits(parent1["recessive_trait"], parent2["recessive_trait"])
    child["age"] = 0
    child["location_born"] = parent1["location_born"]
    return child

def main():
    while True:
        players_data = load_players_data()
        update_age(players_data)
        
        potential_parents = [player for player in players_data if player["age"] >= 18 and player["hp"] > 0]
        if len(potential_parents) >= 2:
            parent1, parent2 = random.sample(potential_parents, 2)
            child = generate_child(parent1, parent2)
            players_data.append(child)
            print(f"{parent1['name']} and {parent2['name']} had a child named {child['name']}!")
        
        save_players_data(players_data)
        print("Player data updated.")
        time.sleep(120)  # Wait for 2 minutes

if __name__ == "__main__":
    main()
