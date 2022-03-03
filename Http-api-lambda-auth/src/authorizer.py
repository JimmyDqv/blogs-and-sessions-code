import hashlib
import hmac
import base64


def lambda_handler(event, context):

    raw_path = event['rawPath']
    if 'rawQueryString' in event:
        raw_query_string = event['rawQueryString']
    domain_name = event['requestContext']['domainName']

    url = f"https://{domain_name}{raw_path}"

    if raw_query_string:
        url = f"{url}?{raw_query_string}"
    print(f"URL: {url}")

    digest = make_digest(url, "SuperSecretKey")
    print(f"Digest: {digest}")

    return {
        "isAuthorized": event['headers']['authorization'] == digest,
        "context": {
            "exampleKey": "exampleValue",
        }
    }


def make_digest(message, key):

    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')

    hmac_digester = hmac.new(key, message, hashlib.sha1)
    digest = hmac_digester.digest()

    return str(base64.urlsafe_b64encode(digest), 'UTF-8')
