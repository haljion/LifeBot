import requests
from bs4 import BeautifulSoup

def operation_info():
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

    # return値
    return_list = [status, message]
    return return_list
