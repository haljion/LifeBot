from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import train_operation as to
from .functions import train_time as tt

@listen_to("かえる.*")
def go_home(message):
    """
    ・コマンド形式
    かえる 出発 (出発時刻)

    出発駅を指定して、
    乗換検索結果と東西線の運行情報をSlackに投稿するメソッド
    """
    message.send("ちょっとまってね")

    status, mes = to.operation_info()
    operation_message = f"*東西線 運行情報*\n{status}\n{mes}"

    # 乗り換え案内
    # Slackに送られたメッセージを取得
    try:
        tmp = message.body["text"].split(" ")
        fromsta = tmp[1]
        time = ""
        if len(tmp) == 3:
            time = tmp[2]
        else:
            time = "9999"
    
        train_time_info = tt.train_time_info(fromsta=fromsta, time=time, mode="f")
    except:
        message.send("エラーが発生したよ\n\
「おしえて」コマンドでもう一度使い方を確認してみてね")
    else:
        train_message = ""

        for label, sta, time, train in train_time_info:
            if type(time) == list:
                time = " ".join(time)
            # 1行単位のメッセージ
            message_line = f"*{label}* {time}\n*:station: {sta}*\n{train}\n\n"
            train_message += message_line
    
        train_message = train_message[:-6]

        message.send(operation_message)
        message.send(train_message)
