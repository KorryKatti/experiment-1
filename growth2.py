import json
import time

try:
    while True:
        # Load data from people.json
        with open("jsons/peoplegrowth.json", "r") as json_file:
            people_data = json.load(json_file)

        # Increase age by 0.5 years for every minute
        for person in people_data:
            person["age"] += 0.5
            print(f"{person['name']} aged 0.5 years. New age: {person['age']} years.")

        # Write updated data to peoplegrowth.json
        with open("jsons/peoplegrowth.json", "w") as json_file:
            json.dump(people_data, json_file, indent=4)

        print("Age updated and saved to peoplegrowth.json.")

        # Sleep for 15 seconds 
        time.sleep(15)

except KeyboardInterrupt:
    print("\nScript stopped by user.")
