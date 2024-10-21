import requests
import json


headers = {
    'x-api-key': "live_gpEYvJSAE4b73OPgaRXw7XOjTtodaMLR1NcFwZNCV0zQ69cz9CYa5vd3TgkquUp1"
}


def get_data():
    url = "https://api.thedogapi.com/v1/breeds"

    response = requests.get(url, headers=headers)

    try:
        # Check if the request was successful
        if response.status_code == 200:
            # Check if response content is not empty
            if response.content:
                # Print raw response content for debugging

                # Parse the response content as a dictionary
                data_dict = response.json()

                # Convert the dictionary to a JSON string
                json_string = json.dumps(data_dict, indent=4)

                print("Dictionary:")
                print(data_dict)
                print("\nJSON String:")
                print(json_string)
            else:
                print("Empty response content.")
        else:
            print(
                f"Failed to retrieve data. Status code: {response.status_code}")
            print("Response Headers:")
            print(response.headers)
            print("Response Content:")
            print(response.text)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print("Raw Response Content:")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Raw Response Content:")
        print(response.text)


get_data()
