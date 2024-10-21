import requests
import json

api_key = "live_gpEYvJSAE4b73OPgaRXw7XOjTtodaMLR1NcFwZNCV0zQ69cz9CYa5vd3TgkquUp1"


def get_dog_breeds():
    url = "https://api.thedogapi.com/v1/breeds"
    headers = {"x-api-key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()

        print("Dog Breeds:")
        print(json.dumps(data, indent=4))  # Pretty-printed JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON data: {e}")
        print("Raw Response Content:")
        # Print the raw response in case of decoding errors
        print(response.text)
    except Exception as e:  # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        print("Raw Response Content:")
        print(response.text)  # Print the raw response for debugging


get_dog_breeds()
