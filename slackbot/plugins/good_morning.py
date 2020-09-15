# coding: utf-8
from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import train_operation as to
from .functions import weatehr_info as wi

@listen_to("おはよう")
def morning(message):
    operations = to.operation_info()
    weathers = wi.weather_info()

    operation_message = f"*東西線 運行情報*\n{operations[0]}\n{operations[1]}"
    
    today_weather_message = f"*今日の天気*\n{weathers[0]}\n最高気温:{weathers[1]}℃\
        \n最低気温:{weathers[2]}℃"
    
    tomorrow_weather_message = f"*明日の天気*\n{weathers[3]}\n最高気温:{weathers[4]}℃\
        \n最低気温:{weathers[5]}℃"
    
    week_info = weathers[6]
    tmp = [washing for dates, weather, washing in week_info]
    today_washing_status = tmp[0]
    tomorrow_washing_status = tmp[1]

    washing_message = f"*洗濯指数*\n今日:{today_washing_status}\
        \n明日:{tomorrow_washing_status}"
    
    message.send(operation_message)
    message.send(today_weather_message)
    message.send(tomorrow_weather_message)
    message.send(washing_message)
