from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import train_operation as to
from .functions import train_time as tt

@listen_to("おでかけ .*")
def morning(message):
    message.send("ちょっとまってね")

    operations = to.operation_info()
    operation_message = f"```*東西線 運行情報*\n{operations[0]}\n{operations[1]}```"

    # 乗り換え案内
    tmp = message.body["text"].split(" ") # Slackに送られたメッセージを取得
    tostation = tmp[1]
    fromtime = tmp[2]
    train_time_info = tt.train_time_info(tosta=tostation, fromtime=fromtime)
    
    
    train_message = ""

    for sta, time, train in train_time_info:
        if a or train == "目的地":



    message.send(res[0][0] + res[0][1] + res[0][2])
    message.send(res[1][0] + res[1][1][0] + res[1][1][1] + res[1][2])
    message.send(res[2][0] + res[2][1] + res[2][2])

    message.send(operation_message)
    