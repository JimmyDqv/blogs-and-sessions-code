import json


def lambda_handler(event, context):

    unicorns = [
        {
            "name": "Gaia",
            "gift": "Speed"
        },
        {
            "name": "Magestic",
            "gift": "Magic"
        },
        {
            "name": "Sparkles",
            "gift": "Glitter"
        }
    ]

    return {
        'statusCode': 200,
        'body': json.dumps(unicorns)
    }
