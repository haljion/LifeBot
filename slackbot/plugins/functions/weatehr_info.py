import requests
from bs4 import BeautifulSoup

def weather_info():
    """
    市川市の天気予報、洗濯指数等を取得するメソッド
    return: [週間天気予報, 最高・最低気温]
    """

    # 市川市の天気予報
    url = "https://tenki.jp/forecast/3/15/4510/12203/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")

    # 今日の天気予報
    today_weather = bs.select_one(".today-weather")
    temperatures = today_weather.select(".temp")
    
    # 最高気温(今日)
    high_temp = temperatures[0].select_one(".value")
    high_temp = high_temp.text.strip()

    # 最低気温(今日)
    low_temp = temperatures[1].select_one(".value")
    low_temp = low_temp.text.strip()

    high_low = {"今日": [high_temp, low_temp]}

    # 天気(今日)
    today_weather = today_weather.select_one(".weather-telop")
    today_weather = today_weather.text.strip()
    today_weather = today_weather.replace("晴", ":sunny:")\
.replace("雨", ":umbrella:").replace("曇", ":cloud:")\
.replace("のち", "→").replace("時々", "or")

    # 明日の天気予報
    tomorrow_weather = bs.select_one(".tomorrow-weather")

    # 最高気温(明日)
    t_temperatures = tomorrow_weather.select(".temp")
    t_high_temp = t_temperatures[0].select_one(".value")
    t_high_temp = t_high_temp.text.strip()

    # 最低気温(明日)
    t_low_temp = t_temperatures[1].select_one(".value")
    t_low_temp = t_low_temp.text.strip()

    high_low.setdefault("明日", [t_high_temp, t_low_temp])
    
    # 天気(明日)
    tomorrow_weather = tomorrow_weather.select_one(".weather-telop")
    tomorrow_weather = tomorrow_weather.text.strip()
    tomorrow_weather = tomorrow_weather.replace("晴", ":sunny:")\
.replace("雨", ":umbrella:").replace("曇", ":cloud:")\
.replace("のち", "→").replace("時々", "or")

    # 週間天気
    week_weather_table = bs.select_one("table.forecast-point-week")
    date_list = ["今日", "明日"] # 日付
    weather_list = [today_weather, tomorrow_weather] # 天気

    for tr in week_weather_table.select("tr"):
        th = tr.select_one("th")
        th = th.text.strip()
        
        if th == "日付":
            for dates in tr.select(".date-box"):
                dates = dates.text.strip()
                dates = dates.replace("月", "/").replace("日", "")
                date_list.append(dates)
        elif th == "天気":
            for weathers in tr.select("p"):
                weathers = weathers.text.strip()
                weathers = weathers.replace("晴", ":sunny:")\
.replace("雨", ":umbrella:").replace("曇", ":cloud:")\
.replace("のち", "→").replace("時々", "or")
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
    
    conv_list = {"部屋干し推奨": "★☆☆☆☆", "やや乾く": "★★☆☆☆",\
         "乾く": "★★★☆☆", "よく乾く": "★★★★☆", "大変よく乾く": "★★★★★"}
    for i in range(len(washing_list)):
        washing_list[i] = conv_list[washing_list[i]]
    
    # 1週間の日付、天気、洗濯指数
    week_weather_info = zip(date_list[:7], weather_list[:7], washing_list[:7])

    # return値
    return_list = [week_weather_info, high_low]
    return return_list
