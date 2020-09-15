from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

def train_time_info(fromsta="南行徳", tosta="南行徳", fromtime="9999"):
    # 出発時間
    hour = fromtime[:2]
    minute = fromtime[2:]

    driver = webdriver.Chrome()
    driver.get("https://transit.yahoo.co.jp/")
    sleep(3)
    from_station_box = driver.find_element_by_id("sfrom")
    to_station_box = driver.find_element_by_id("sto")
    from_station_box.send_keys(fromsta)
    to_station_box.send_keys(tosta)

    # 出発時刻に指定があった場合、適用
    # なかった場合は現在時刻
    if hour != "99":
        selectbox_h = Select(driver.find_element_by_id("hh"))
        selectbox_h.select_by_value(hour)
        selectbox_m = Select(driver.find_element_by_id("mm"))
        selectbox_m.select_by_value(minute)
    
    # 検索結果画面へ遷移
    driver.find_element_by_id("searchModuleSubmit").submit()

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

    return_list = list(zip(station_list, timeset_list, route_list))
    return return_list
