import json
import requests


def lambda_handler(event, context):
    try:
        # Extract Aadhaar number and other required fields from the event
        aadhaar_number = event['aadhaar_number']
        # Additional data such as OTP, customer name, etc., may be required

        # Prepare the payload for the external API
        payload = {
            'aadhaar': aadhaar_number,
            # Add other required fields here
        }

        # Send the POST request to the Aadhaar verification API
        response = requests.post(
            'https://aadhaar-verification-api-url', json=payload)

        # Check if the response is successful
        if response.status_code == 200:
            # Process the response and return success if verified
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Aadhaar verified successfully',
                    'data': response.json()
                })
            }
        else:
            # Handle failure case
            return {
                'statusCode': response.status_code,
                'body': json.dumps({
                    'message': 'Aadhaar verification failed',
                    'error': response.json()
                })
            }

    except Exception as e:
        # Handle any errors that occur
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred during Aadhaar verification',
                'error': str(e)
            })
        }
