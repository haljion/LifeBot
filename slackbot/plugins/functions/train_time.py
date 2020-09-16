from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

def train_time_info(mode, time, fromsta="南行徳", tosta="南行徳"):
    """
    乗換情報を取得するメソッド

    引数
    ----------
    fromsta: 出発駅。
    tosta: 到着駅。
    time: 時刻。省略可能。
    mode: 起動モード。fが出発時刻(from)、tが到着時刻(to)。
    return: [ラベル, 駅名, 時刻, 路線情報]
    """

    # 出発時間
    hour = time[:2]
    minute = time[2:]

    # headlessモードで起動
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://transit.yahoo.co.jp/")
    sleep(3)
    # 出発駅、到着駅を入力
    from_station_box = driver.find_element_by_id("sfrom")
    to_station_box = driver.find_element_by_id("sto")
    from_station_box.send_keys(fromsta)
    to_station_box.send_keys(tosta)

    # 出発時刻に指定があった場合、適用
    # なかった場合は現在時刻
    if hour != "99":
        selectbox_h = Select(driver.find_element_by_id("hh"))
        selectbox_h.select_by_value(hour)
        # 分の項目は画面上では指定されるが、
        # 遷移した際に適用されず現在時刻の分になってしまう。
        # name属性が無いのが原因？要調査
        # selectbox_m = Select(driver.find_element_by_id("mm"))
        # selectbox_m.select_by_value(minute)
    
    # 出発時刻 or 到着時刻 を選択
    if mode == "t":
        driver.find_element_by_id("tsArr").click()

    # 検索結果画面へ遷移
    driver.find_element_by_id("searchModuleSubmit").submit()
    sleep(3)

    # 分だけの為に二度画面遷移するパワープレイ
    if hour != "99":
        url = driver.current_url
        url += f"&m1={minute[0]}&m2={minute[1]}"
        driver.get(url)
        sleep(3)

    train_times = driver.find_elements_by_css_selector("#route01 ul.time li")
    time_list = [t_time.text.strip() for t_time in train_times]
    timeset_list = []
    for i in range(len(time_list)):
        if i == 0 or i == len(time_list) - 1:
            timeset_list.append(time_list[i])
        elif i % 2 == 1:
            timeset_list.append([time_list[i], time_list[i+1]])
        else:
            continue
    
    stations = driver.find_elements_by_css_selector("#route01 .station dl dt a")
    station_list = [sta.text.strip() for sta in stations]

    routes = driver.find_elements_by_css_selector("#route01 li.transport div")
    route_list = [route.text.strip().replace("[train]\n", "") for route in routes]
    route_list.append("目的地")

    driver.quit()

    # ラベル(出発、乗換、到着)
    label_list = ["乗換" for i in range(len(station_list))]
    label_list[0] = "出発"
    label_list[-1] = "到着"

    return_list = list(zip(label_list, station_list, timeset_list, route_list))
    return return_list
