import json
import boto3
import os


def handler(event, context):
    body = json.loads(event["body"])
    bucket = os.environ["BUCKET"]

    if not body["path"].endswith("/") and len(body["path"]) > 0:
        body["path"] = body["path"] + "/"

    fullpath = body["user"] + "/" + body["path"] + body["name"]

    client = boto3.client("s3")
    response = client.generate_presigned_url(
        "put_object",
        Params={"Bucket": bucket, "Key": fullpath},
        ExpiresIn=600,
    )

    file = {"url": response}

    return file
