# coding: utf-8
import os

# botアカウントのトークンはheroku上で指定
API_TOKEN = os.environ["API_TOKEN"]

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "「おしえて」って投稿すると使い方を表示するよ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ["plugins"]