import os
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

# 環境変数からLINE Botのチャネルアクセストークンを取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
# チャネルアクセストークンを使用して、LineBotApiのインスタンスを作成
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def lambda_handler(event, context):
    try:
        # LINEからメッセージを受信
        if event['events'][0]['type'] == 'message':
        # メッセージタイプがテキストの場合
            if event['events'][0]['message']['type'] == 'text':
            # リプライ用トークン
                replyToken = event['events'][0]['replyToken']
                # 受信メッセージ
                messageText = event['events'][0]['message']['text']
                # メッセージを返信（受信メッセージをそのまま返す）
                LINE_BOT_API.reply_message(replyToken, TextSendMessage(text=messageText))

    # エラーが起きた場合
    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': json.dumps('Exception occurred.')}

    return {'statusCode': 200, 'body': json.dumps('Reply ended normally.')}