import json
import random
import time

while True:
    # Load data from peoplegrowth.json
    with open("jsons/peoplegrowth.json", "r") as json_file:
        people_data = json.load(json_file)

    # Select individuals eligible for childbirth
    eligible_females = [person for person in people_data if person["gender"] == "female" and person["age"] >= 18 and person["hp"] > 0]
    eligible_males = [person for person in people_data if person["gender"] == "male" and person["age"] >= 18 and person["hp"] > 0]

    # Check if there are eligible parents
    if eligible_females and eligible_males:
        # Select a random female and male for childbirth
        mother = random.choice(eligible_females)
        father = random.choice(eligible_males)
        
        # Generate a random name for the child
        child_name = "Child_" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))

        # Calculate child's HP as the average of mother's and father's HP
        child_hp = (mother["hp"] + father["hp"]) // 2

        # Create child's data
        child_data = {
            "name": child_name,
            "father": father["name"],
            "mother": mother["name"],
            "hp": child_hp,
            "age": 0
        }

        # Save child's data to children.json
        with open("childjsons/children.json", "a") as json_file:
            json.dump(child_data, json_file, indent=4)
            json_file.write("\n")

        print("Child data saved to children.json.")
    else:
        print("No eligible parents found for childbirth.")

    # Sleep for 119 seconds
    time.sleep(119)
