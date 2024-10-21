import json

def lambda_handler(event, context):
    try:
        # Extract PAN and other required fields from the event
        provided_pan_last4 = event['pan_last4']
        # Assuming you have stored the correct last 4 digits in your system
        correct_pan_last4 = '1234'  # This should come from your database

        # Compare the provided last 4 digits with the correct value
        if provided_pan_last4 == correct_pan_last4:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'PAN verified successfully'
                })
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'PAN verification failed'
                })
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred during PAN verification',
                'error': str(e)
            })
        }
