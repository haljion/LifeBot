from slacker import Slacker
import slackbot_settings
from plugins.functions import weatehr_info as wi

def main():
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
    
    # botアカウントのトークンを指定
    slack = Slacker(slackbot_settings.API_TOKEN)
    channel = "生活"
    slack.chat.post_message(channel, "おはよう！", as_user=True)
    slack.chat.post_message(channel, weather_message, as_user=True)
    slack.chat.post_message(channel, washing_message, as_user=True)

if __name__ == "__main__":
    main()
