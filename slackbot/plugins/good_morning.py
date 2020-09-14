# coding: utf-8
from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
import functions
from train_time import train_time_info

@listen_to("おはよう")
def morning(message):
    operations = functions.operation_info()
    weathers = functions.weather_info()

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


@listen_to("おでかけ")
def morning(message):
    message.send("ちょっとまってね")

    operations = functions.operation_info()
    operation_message = f"*東西線 運行情報*\n{operations[0]}\n{operations[1]}"

    res = train_time_info(tosta="秋葉原")
    
    message.send(operation_message)
    message.send(res[0][0] + res[0][1] + res[0][2])
    message.send(res[1][0] + res[1][1][0] + res[1][1][1] + res[1][2])
    message.send(res[2][0] + res[2][1] + res[2][2])
