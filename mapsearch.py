import json

def load_map():
    with open("locations/map.json", "r") as file:
        map_data = json.load(file)
    return map_data["map"]

def get_feature(location):
    map_data = load_map()
    for data in map_data:
        if data["location"] == location:
            return data["feature"]
    return "Unknown"

def main():
    location = input("Enter a location to check its feature (e.g., a1): ").lower()
    feature = get_feature(location)
    print(f"The feature at {location} is: {feature}")

if __name__ == "__main__":
    main()
