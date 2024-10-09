import requests
import json

# URL of the ACE system or the HTTP API endpoint that accepts robot commands
url = "http://0.0.0.0:48987"  # Replace with the actual API URL

# Define the coordinates you want to send (Pick and Place)
coordinates = {
    "pick_position": {"x": 100.0, "y": 200.0, "z": 300.0},
    "place_position": {"x": 400.0, "y": 500.0, "z": 600.0}
}

# Convert the coordinates to JSON format
json_payload = json.dumps(coordinates)

try:
    # Send the coordinates via an HTTP POST request
    response = requests.post(url, data=json_payload, headers={'Content-Type': 'application/json'})

    # Check if the request was successful
    if response.status_code == 200:
        print("Coordinates successfully sent to ACE robot.")
        print("Response:", response.json())
    else:
        print(f"Failed to send coordinates. Status code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
