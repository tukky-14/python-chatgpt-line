import os
import json
import openai
import personality
from dynamodb_functions import get_message_history, put_message_history
from linebot import LineBotApi
from linebot.models import TextSendMessage

LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def lambda_handler(event, context):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    try:
        if event['events'][0]['type'] == 'message':
            if event['events'][0]['message']['type'] == 'text':

                user_id = event['events'][0]['source']['userId']
                timestamp = event['events'][0]['timestamp']
                replyToken = event['events'][0]['replyToken']
                message = event['events'][0]['message']['text']

                past_messages = get_message_history(user_id)
                print('past_messages:', past_messages)

                messages = [{'role': 'system', 'content': personality.SONGOKU}]
                messages += past_messages
                messages.append({'role': 'user', 'content': message})

                response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = messages,
                    temperature = 0.5,
                )
                res_content = response['choices'][0]['message']['content']

                put_message_history(user_id, timestamp, message, res_content)

                LINE_BOT_API.reply_message(replyToken, TextSendMessage(text=res_content))

    # エラーが起きた場合
    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': 'Exception occurred.'}

    return {'statusCode': 200, 'body': 'Reply ended normally.'}
