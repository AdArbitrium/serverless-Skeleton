import boto3
import json
from typing import List

s3 = boto3.resource('s3')
bucket_name = "example-s3-database-ahernandez"
bucket = s3.Bucket(bucket_name)

key = "SavedCardsArray.json"


def list_all_buckets() -> List[str]:
    bucket_names = []
    for bucket in s3.buckets.all():
        bucket_names.append(bucket.name)
    return bucket_names


def create_or_open_json():
    try:
        s3_Object = s3.Object(bucket_name, key)
        cards_array = s3_Object.get()["Body"].read()
        result_json = json.loads(cards_array)
    except:
        bucket.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=""
        )
        result_json = {}
    return result_json


def save_card_array_to_Json(card_arr: List[str]):
    the_json = create_or_open_json()
    if ("cardArr" in the_json):
        json_array: List[str] = the_json["cardArr"]
    else:
        json_array = []
    json_array.append(card_arr)

    the_json["cardArr"] = json_array
    body = json.dumps(the_json)
    bucket.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=body)
    return body
