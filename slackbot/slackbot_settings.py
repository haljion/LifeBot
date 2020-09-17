# coding: utf-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
print(dotenv_path)
load_dotenv(dotenv_path)

# botアカウントのトークンを指定
API_TOKEN = os.environ.get("API_TOKEN")
print(API_TOKEN)

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "「おしえて」って投稿すると使い方を表示するよ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ["plugins"]