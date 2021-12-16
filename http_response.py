import decimal
import json

headers = {"Access-Control-Allow-Headers": "Content-Type", "Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}

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


def http_response(hcode=200, bcode="Success", message="Done", data=None):
    """Generate proper HTTP response for frontend code"""
    
    return {"statusCode": hcode, "headers": headers, "body": json.dumps({"code": bcode, "message": message, "data": data}, cls=DecimalEncoder)}
