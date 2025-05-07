
import json

def lambda_handler(event, context):
    """
    Lambda関数のエントリーポイント
    """
    print("イベントを受信しました:", event)
    print("he2")

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda!',
            'input': event
        })
    }

    return response
