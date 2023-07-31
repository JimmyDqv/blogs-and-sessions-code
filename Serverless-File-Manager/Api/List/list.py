import json
import boto3
import os


def handler(event, context):
    body = json.loads(event["body"])
    table = os.environ["INVENTORY_TABLE"]

    dynamodb_client = boto3.client("dynamodb")
    response = dynamodb_client.query(
        TableName=table,
        KeyConditionExpression="PK = :user AND begins_with ( SK , :filter )",
        ExpressionAttributeValues={
            ":user": {"S": body["user"]},
            ":filter": {"S": f'{body["user"]}/{body["filter"]}'},
        },
    )

    file_list = []

    for item in response["Items"]:
        file = {
            "Path": item["Path"]["S"].replace(f'{body["user"]}/', ""),
            "Size": item["Size"]["N"],
            "Etag": item["Etag"]["S"],
        }
        file_list.append(file)

    return file_list
