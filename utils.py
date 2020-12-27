import os

from flask import Flask, jsonify, request, abort, send_file
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(usr_id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    image = {
                "original": "https://i.imgur.com/8zbJ5bA.png",
                "preview": "https://i.imgur.com/8zbJ5bA.png"
            }
    line_bot_api.push_message(usr_id, ImageSendMessage(original_content_url=image["original"], preview_image_url=image["preview"]))
#    try:
#        line_bot_api.push_message(usr_id, TextSendMessage(text=text))
#    except LineBotApiError as e:
#        abort(400)
#    return "OK"

"""
def send_button_message(id, text, buttons):
    pass
"""
