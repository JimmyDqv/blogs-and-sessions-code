import json
import boto3
import os


def handler(event, context):
    body = json.loads(event["body"])
    bucket = os.environ["BUCKET"]

    if not body["path"].endswith("/") and len(body["path"]) > 0:
        body["path"] = body["path"] + "/"

    fullpath = body["user"] + "/" + body["path"] + body["name"]

    if check_file_exists(body["user"], fullpath):
        client = boto3.client("s3")
        response = client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket, "Key": fullpath},
            ExpiresIn=600,
        )

        file = {"url": response}

        return file
    else:
        return {"status": 404, "body": "File not found"}


def check_file_exists(user, path):
    table = os.environ["INVENTORY_TABLE"]

    dynamodb_client = boto3.client("dynamodb")
    response = dynamodb_client.query(
        TableName=table,
        KeyConditionExpression="PK = :pk AND SK = :sk",
        ExpressionAttributeValues={":pk": {"S": user}, ":sk": {"S": path}},
    )

    return len(response["Items"]) > 0
