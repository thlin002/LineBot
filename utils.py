import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import LineBotApiError

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(usr_id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    text = {
                "type": "image",
                "originalContentUrl": "https://imgur.com/gallery/DvRcRcC",
                "previewImageUrl": "https://imgur.com/gallery/DvRcRcC"
            }
    try:
        line_bot_api.push_message(usr_id, TextSendMessage(text=text))
    except LineBotApiError as e:
        abort(400)
    return "OK"

"""
def send_button_message(id, text, buttons):
    pass
"""
