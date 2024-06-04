import json
import random
import time

# Load people data
with open("jsons/peoplegrowth.json", "r") as json_file:
    people_data = json.load(json_file)

# Load fatal factors
with open("jsons/fatal.json", "r") as json_file:
    fatal_factors = json.load(json_file)

# Function to apply a random fatal scenario to a random person
def apply_fatal_scenario(people):
    # Filter living individuals
    living_people = [person for person in people if person["hp"] > 0]
    
    if living_people:
        # Choose a random person
        person = random.choice(living_people)
        fatal_scenario = random.choice(fatal_factors)
        person["hp"] += fatal_scenario["damage"]
        if person["hp"] < 0:
            person["hp"] = 0
        print(f"{person['name']} experienced {fatal_scenario['factor']}! HP: {person['hp']}")
    else:
        print("All individuals are deceased. Simulation ended.")

# Main loop
try:
    while True:
        # Apply fatal scenario to a random person
        apply_fatal_scenario(people_data)

        # Write updated data to peoplegrowth.json
        with open("jsons/peoplegrowth.json", "w") as json_file:
            json.dump(people_data, json_file, indent=4)

        print("Updated HP written to peoplegrowth.json.")

        # Sleep for 5 minutes
        time.sleep(300)

except KeyboardInterrupt:
    print("\nScript stopped by user.")
