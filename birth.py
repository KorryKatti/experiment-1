import json
import random
import time

def load_map():
    with open("locations/map.json", "r") as file:
        map_data = json.load(file)
    return map_data["map"]

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

def generate_gender():
    return random.choice(["male", "female"])

def generate_dob():
    # Start with year 0, 2 years pass every minute
    seconds_passed = time.time()
    years_passed = int(seconds_passed / 60) * 2
    return years_passed

def generate_hp():
    return 100

def generate_traits():
    traits = ["strength", "intelligence", "agility"]
    dominant_trait = random.choice(traits)
    recessive_trait = random.choice(traits)
    while recessive_trait == dominant_trait:
        recessive_trait = random.choice(traits)
    return dominant_trait, recessive_trait

def generate_age():
    return 0

def generate_location_born():
    map_data = load_map()
    land_locations = [data["location"] for data in map_data if data["feature"] in ["land", "mountains"]]
    return random.choice(land_locations)

def generate_player_data():
    gender = generate_gender()
    name = generate_name(gender)
    dob = generate_dob()
    hp = generate_hp()
    dominant_trait, recessive_trait = generate_traits()
    age = generate_age()
    location_born = generate_location_born()

    player_data = {
        "name": name,
        "gender": gender,
        "year_born": dob,
        "hp": hp,
        "dominant_trait": dominant_trait,
        "recessive_trait": recessive_trait,
        "age": age,
        "location_born": location_born
    }
    return player_data

def main():
    num_players = random.randint(2, 10) * 2  # Even number of players
    male_count = num_players // 2
    female_count = num_players // 2

    players_data = []
    while male_count > 0 or female_count > 0:
        player_data = generate_player_data()
        if player_data["gender"] == "male" and male_count > 0:
            players_data.append(player_data)
            male_count -= 1
        elif player_data["gender"] == "female" and female_count > 0:
            players_data.append(player_data)
            female_count -= 1

    with open("data/playersdata.json", "w") as file:
        json.dump(players_data, file, indent=4)
    print("Player data saved to data/playersdata.json")

if __name__ == "__main__":
    main()
