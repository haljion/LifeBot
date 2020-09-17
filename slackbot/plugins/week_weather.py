# coding: utf-8
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import weatehr_info as wi

@listen_to("てんき")
def week_weather_info(message):
    """
    ・コマンド形式
    てんき

    東西線の運行情報と天気予報をSlackに投稿するメソッド
    """
    weathers = wi.weather_info()

    week_info = weathers[0]
    week_message = [f"{dates}, 天気:{weather}, 洗濯:{washing}" for dates, weather, washing in week_info]
    week_message = "\n".join(week_message)
    
    message.send(week_message)
