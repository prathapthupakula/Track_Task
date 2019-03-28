import json
def is_json(data):
    try:
        jsonData=json.loads(data)
        valid=True
    except ValueError:
        # print("inside")
        valid =False
    return valid