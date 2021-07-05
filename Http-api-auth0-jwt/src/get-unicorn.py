import json


def lambda_handler(event, context):

    if 'queryStringParameters' in event and 'name' in event['queryStringParameters']:
        unicorn = {
            "name": event['queryStringParameters']['name'],
            "gift": "Flight"
        }

        return {
            'statusCode': 200,
            'body': json.dumps(unicorn)
        }

    return {
        'statusCode': 400,
        'body': json.dumps('Missing Unicorn Name')
    }
