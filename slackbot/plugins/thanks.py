import random
from slackbot.bot import respond_to # メンションで反応
from slackbot.bot import listen_to # チャネル内発言で反応
from slackbot.bot import default_reply # 設定外のワードに対する反応
from .functions import train_operation as to
from .functions import train_time as tt

@listen_to("ありがと")
def thank_you(message):
    # おまけ機能
    message_list = ["ゴンべでした", "ん", "はらへった", "次は貴様の番だ",\
         "ホホホイホ", "オッペケプゥ", "ダブルチーズバーガーパティ倍ピクルス抜きでお願いします",\
              "それちがう思う", "鼻毛でてるよ", "ここから先は有料プランです"]
    random_number = random.randint(0,9)
    
    message.reply(message_list[random_number])
