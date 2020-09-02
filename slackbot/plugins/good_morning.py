# coding: utf-8
from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
import functions

@listen_to("おはよう")
def morning(message):
    result = functions.operation_info()
    bot_message = f"*東西線 運行情報*\n{result[0]}\n{result[1]}"
    message.send(bot_message)
