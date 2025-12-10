from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 替换为你的云函数完整URL（例如：https://1391451970-8294b0lly.ap-shanghai.tencentscf.com）
CF_URL = "你的云函数URL"

@app.route('/', methods=['GET'])
def handle_verify():
    echostr = request.args.get('echostr', '验证失败')
    return echostr

@app.route('/', methods=['POST'])
def handle_message():
    try:
        qq_data = request.get_json()
        cloud_response = requests.post(CF_URL, json=qq_data)
        return jsonify(cloud_response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handler(event, context):
    from flask import request
    with app.test_request_context(
        path=event['path'],
        method=event['httpMethod'],
        headers=event['headers'],
        data=event['body']
    ):
        response = app.full_dispatch_request()
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }
