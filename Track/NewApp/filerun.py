import requests
import json
Base_URL='http://127.0.0.1:8000'
endpoint="/api/v1/test/"
def get_resourses(id=None):
    data={}
    if data is not None:
        data={
            'id':id,
        }
    resp=requests.get(Base_URL+endpoint,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resourses(1)