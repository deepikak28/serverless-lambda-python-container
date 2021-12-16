import json
from http_response import http_response

print('Loading function')

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    return http_response(200, "Success", "Hello From Lambda", None)
