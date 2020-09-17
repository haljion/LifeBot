# coding: utf-8
from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import train_operation as to
from .functions import weatehr_info as wi

@listen_to("おはよう")
def morning(message):
    """
    ・コマンド形式
    おはよう

    東西線の運行情報と天気予報をSlackに投稿するメソッド
    """
    # 運行情報
    status, mes = to.operation_info()
    operation_message = f"*東西線 運行情報*\n{status}\n{mes}"
    
    # 天気予報
    week_info, temp_info = wi.weather_info()
    weather_message = ""
    washing_message = "*洗濯指数*\n"
    count = 0
    
    for dates, weather, washing in week_info:
        if count > 1:
            break
        # 最高気温, 最低気温
        high, low = temp_info[dates]
        weather_message += f"*{dates}の天気*\n{weather}\n最高気温:{high}℃\
        \n最低気温:{low}℃\n"
        washing_message += f"{dates}:{washing}\n"
        count += 1

    message.send(operation_message)
    message.send(weather_message)
    message.send(washing_message)
