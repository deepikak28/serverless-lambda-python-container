import decimal
import json

# We will be more strict on headers later, for now we use below.
headers = {"Access-Control-Allow-Headers": "Content-Type", "Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}


# We modify DecimalEncoder to handle decimal() objects, and sets
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            if obj % 1 > 0:
                return float(obj)
            else:
                return int(obj)
        if isinstance(obj, set):
            return list(obj)
        return super(DecimalEncoder, self).default(obj)


# helper function for http return values
def http_response(hcode=200, bcode="Success", message="Done", data=None):
    """Generate proper HTTP response for frontend code"""
    # HTTP Status Code  # Body Return Code - Success, InvalidData, etc.  # Message
    # Data Object if any, otherwise set to null

    return {"statusCode": hcode, "headers": headers, "body": json.dumps({"code": bcode, "message": message, "data": data}, cls=DecimalEncoder)}
