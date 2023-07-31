import json
import boto3
import os


def handler(event, context):
    headers = event["headers"]
    table = os.environ["INVENTORY_TABLE"]

    dynamodb_client = boto3.client("dynamodb")
    response = dynamodb_client.query(
        TableName=table,
        KeyConditionExpression="PK = :user AND SK = :sk",
        ExpressionAttributeValues={
            ":user": {"S": headers["user"]},
            ":sk": {"S": "Quota"},
        },
    )

    quota = {"Size": response["Items"][0]["TotalSize"]["N"]}

    return quota
