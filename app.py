from flask.wrappers import Request
import clients.s3.client as S3Client
import json
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)

CORS(app)

@app.route("/listBuckets")


@app.route("/save", methods=['POST'])
def save_card_array():
    card_arr = request.json.get("cardArr")
    return S3Client.save_card_array_to_Json(card_arr)

@app.route("/load", methods=['GET'])
def load_card_array():
    result = S3Client.create_or_open_json()
    return result