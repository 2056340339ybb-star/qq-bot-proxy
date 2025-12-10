def handler(event, context):
    # 处理GET请求（QQ平台echostr验证）
    if event['httpMethod'] == 'GET':
        echostr = event['queryStringParameters'].get('echostr', '')
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': echostr
        }
    
    # 处理POST请求（直接返回固定测试内容，验证通路）
    elif event['httpMethod'] == 'POST':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': '{"reply": "测试成功，消息已接收"}'
        }
    
    # 其他请求方法
    else:
        return {'statusCode': 405, 'body': 'Method Not Allowed'}
