from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup


def train_time_info(fromsta="南行徳", tosta="南行徳"):
    driver = webdriver.Chrome()
    driver.get("https://transit.yahoo.co.jp/")
    # sleep(3)
    from_station_box = driver.find_element_by_id("sfrom")
    to_station_box = driver.find_element_by_id("sto")
    from_station_box.send_keys(fromsta)
    to_station_box.send_keys("秋葉原")
    driver.find_element_by_id("searchModuleSubmit").submit()

    sleep(5)

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

    
