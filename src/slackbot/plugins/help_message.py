from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import train_operation as to
from .functions import train_time as tt

@listen_to("おしえて")
def morning(message):
    help_message = """
    【コマンド一覧】\n
    :cat: おはよう :cat:\n
    天気予報・東西線の運行情報を教えるよ\n\n

    :cat: てんき :cat:\n
    一週間の天気予報を教えるよ\n\n

    :cat: しゅっぱつ 到着駅 (出発時刻) :cat:\n
    東西線の運行情報・南行徳~到着駅の乗換案内を教えるよ\n
    時間は省略すると現在時刻になるよ\n\n

    :cat: とうちゃく 到着駅 (到着時刻) :cat:\n
    東西線の運行情報・南行徳~到着駅の乗換案内を教えるよ\n
    時間は省略すると現在時刻になるよ\n\n
    
    :cat: かえる 出発駅 (出発時刻) :cat:\n
    東西線の運行情報・出発駅~南行徳の乗換案内を教えるよ\n
    時間は省略すると現在時刻になるよ\n\n

    :cat: おでかけ 出発駅 到着駅 (出発時刻) :cat:\n
    東西線の運行情報と出発駅~到着駅の乗換案内を教えるよ\n
    時間は省略すると現在時刻になるよ\n

    :cat: ありがと :cat:\n
    しゃべるよ\n
    """
    
    message.send(help_message)
    
