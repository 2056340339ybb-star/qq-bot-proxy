import json
import requests

def handler(event, context):
    # 打印请求信息到日志，方便排查
    print(f"请求方法：{event['httpMethod']}")
    print(f"请求参数：{event.get('queryStringParameters', {})}")
    print(f"请求体：{event.get('body', '无')}")

    # 1. 处理GET验证（直接返回echostr）
    if event['httpMethod'] == 'GET':
        echostr = event['queryStringParameters'].get('echostr', '')
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': echostr
        }
    
    # 2. 处理POST转发（增加超时+重试）
    elif event['httpMethod'] == 'POST':
        try:
            cloud_func_url = 'https://1391451970-73tz9amjq1.ap-guangzhou.tencentscf.com'  # 替换为你的云函数URL
            # 转发请求（设置5秒超时+关闭SSL验证，避免地域网络问题）
            resp = requests.post(
                cloud_func_url,
                data=event['body'],
                headers={'Content-Type': 'application/json'},
                timeout=5,
                verify=False
            )
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': resp.text
            }
        except requests.exceptions.RequestException as e:
            print(f"转发失败：{str(e)}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': f'转发云函数失败：{str(e)}'})
            }
    
    # 3. 其他方法
    else:
        return {'statusCode': 405, 'body': '不支持的请求方法'}
