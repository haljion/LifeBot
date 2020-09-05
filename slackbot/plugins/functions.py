import requests
from bs4 import BeautifulSoup

def operation_info():

    # return値
    return_list = []

    # 東西線の運行情報(Yahoo)
    url = "https://transit.yahoo.co.jp/traininfo/detail/135/0/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")

    # 運行ステータス
    div_status = bs.select_one("#mdServiceStatus")

    # ステータス
    status = div_status.select_one("dt")
    status = status.text.strip()
    status = status.split("]")[1]

    # メッセージ
    message = div_status.select_one("dd")
    message = message.select_one("p")
    message = message.text.strip()

    return_list += [status, message]
    return return_list


def weather_info():
    # return値
    return_list = []

    # 市川市の天気予報
    url = "https://tenki.jp/forecast/3/15/4510/12203/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")

    # 今日の天気予報
    today_weather = bs.select_one(".today-weather")
    temperatures = today_weather.select(".temp")
    
    # 最高気温(きょう)
    high_temp = temperatures[0].select_one(".value")
    high_temp = high_temp.text.strip()

    # 最低気温(きょう)
    low_temp = temperatures[1].select_one(".value")
    low_temp = low_temp.text.strip()

    # 天気(きょう)
    today_weather = today_weather.select_one(".weather-telop")
    today_weather = today_weather.text.strip()

    # 明日の天気予報
    tomorrow_weather = bs.select_one(".tomorrow-weather")

    # 最高気温(あした)
    t_temperatures = tomorrow_weather.select(".temp")
    t_high_temp = t_temperatures[0].select_one(".value")
    t_high_temp = t_high_temp.text.strip()

    # 最低気温(あした)
    t_low_temp = t_temperatures[1].select_one(".value")
    t_low_temp = t_low_temp.text.strip()
    
    # 天気(あした)
    tomorrow_weather = tomorrow_weather.select_one(".weather-telop")
    tomorrow_weather = tomorrow_weather.text.strip()

    # 週間天気
    week_weather_table = bs.select_one("table.forecast-point-week")
    date_list = ["きょう", "あした"] # 日付
    weather_list = ["pass", "pass"] # 天気

    for tr in week_weather_table.select("tr"):
        th = tr.select_one("th")
        th = th.text.strip()
        
        if th == "日付":
            for dates in tr.select(".date-box"):
                dates = dates.text.strip()
                date_list.append(dates)
        elif th == "天気":
            for weathers in tr.select("p"):
                weathers = weathers.text.strip()
                weather_list.append(weathers)
        else:
            continue

    # 洗濯
    washing_data = bs.select_one("ul.indexes-pickup-another")
    washing_data = washing_data.select("li")
    washing_data = washing_data[1].select_one("a")
    washing_url = washing_data.get("href")
    washing_url = "https://tenki.jp" + washing_url.strip()

    # 洗濯指数のページに移動
    w_response = requests.get(washing_url)
    w_bs = BeautifulSoup(w_response.text, "html.parser")

    week_washing = w_bs.select(".indexes-telop-0")
    washing_list = [] # 洗濯指数

    for w_status in week_washing:
        washing_list.append(w_status.text.strip())
    
    # 1週間の日付、天気、洗濯指数
    week_weather_info = zip(date_list[:7], weather_list[:7], washing_list[:7])

    return_list += [today_weather, high_temp, low_temp, \
        tomorrow_weather, t_high_temp, t_low_temp, week_weather_info]
    return return_list