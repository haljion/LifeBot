# coding: utf-8

import sys
sys.path.append("C:\\workspace_app\\LifeBot\\slackbot\\plugins")
from slackbot.bot import Bot
import functions

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()