import json
import random

def generate_map():
    map_data = []
    features = ["land", "mountains", "sea"]
    
    # Generate features for each location
    for row in range(1, 21):  # rows
        for col in range(ord('a'), ord('a') + 20):  # columns
            location = chr(col) + str(row)
            feature = random.choice(features)
            map_data.append({"location": location, "feature": feature})

    return map_data

def main():
    map_data = generate_map()
    map_json = {"map": map_data}

    with open("locations/map.json", "w") as outfile:
        json.dump(map_json, outfile, indent=2)

if __name__ == "__main__":
    main()
