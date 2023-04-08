import os
import json
import openai
import personality
from linebot import LineBotApi
from linebot.models import TextSendMessage

LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def lambda_handler(event, context):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    try:
        if event['events'][0]['type'] == 'message':
            if event['events'][0]['message']['type'] == 'text':
            # リプライ用トークン
                replyToken = event['events'][0]['replyToken']
                # 受信メッセージ
                messageText = event['events'][0]['message']['text']
                # ChatGPT-3.5-turboで返信
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {'role': 'system', 'content': personality.SONGOKU},
                        {'role': 'user', 'content': messageText }
                    ],
                    temperature=0.0,
                )
                res_content = response['choices'][0]['message']['content']
                LINE_BOT_API.reply_message(replyToken, TextSendMessage(text=res_content))

    # エラーが起きた場合
    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': json.dumps('Exception occurred.')}

    return {'statusCode': 200, 'body': json.dumps('Reply ended normally.')}