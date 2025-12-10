import json
import requests

def handler(event, context):
    # 处理GET验证请求
    if event['httpMethod'] == 'GET':
        echostr = event['queryStringParameters'].get('echostr', 'success')
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': echostr
        }
    # 处理POST消息请求
    elif event['httpMethod'] == 'POST':
        try:
            qq_data = json.loads(event['body'])
            # 替换为你的云函数URL
            cf_response = requests.post("https://1391451970-73tz9amjq1.ap-guangzhou.tencentscf.com", json=qq_data)
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps(cf_response.json())
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
