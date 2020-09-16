from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import train_operation as to
from .functions import train_time as tt

@listen_to("help")
def morning(message):
    message.send("使い方だよ")
    
