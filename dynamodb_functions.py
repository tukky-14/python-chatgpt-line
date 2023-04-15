import boto3
import datetime

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
table = dynamodb.Table('goku_chat_history')

def put_message_history(user_id, timestamp, message, reply_message):
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    current_time = now.strftime('%Y%m%d%H%M%S')
    item = {
        'user_id': user_id,
        'timestamp': timestamp,
        'message': message,
        'reply_message': reply_message,
        'created_at': current_time
    }
    print('item:', item)

    try:
        response = table.put_item(Item=item)
        print('PutItem succeeded:', response)
    except Exception as e:
        print('Unable to put item. Error:', e)

def get_message_history(user_id):
    response = table.query(
        KeyConditionExpression='user_id = :uid',
        ExpressionAttributeValues={
            ':uid': user_id
        },
        ScanIndexForward=False,
        Limit=5
    )
    print('response:', response)
    past_messages = response['Items']
    past_messages.sort(key=lambda x: x['timestamp'])
    past_message_array = []

    for past_message in past_messages:
        past_message_array.append({'role': 'user', 'content': past_message['message']})
        past_message_array.append({'role': 'assistant', 'content': past_message['reply_message']})

    return past_message_array