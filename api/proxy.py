import json
import requests

def handler(event, context):
    # 1. 处理QQ平台的GET验证请求（echostr）
    if event['httpMethod'] == 'GET':
        echostr = event['queryStringParameters'].get('echostr', '')
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': echostr
        }
    
    # 2. 处理QQ平台的POST消息请求（转发到云函数）
    elif event['httpMethod'] == 'POST':
        try:
            # 替换为你的广州云函数URL
            cloud_func_url = 'https://1391451970-73tz9amjq1.ap-guangzhou.tencentscf.com'
            # 转发POST数据到云函数
            resp = requests.post(
                cloud_func_url,
                data=event['body'],
                headers={'Content-Type': 'application/json'}
            )
            # 返回云函数的响应给QQ平台
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': resp.text
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    
    # 3. 其他请求方法
    else:
        return {'statusCode': 405, 'body': 'Method Not Allowed'}
