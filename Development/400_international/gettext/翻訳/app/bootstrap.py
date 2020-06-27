# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:53:26 2019

@author: PC
"""

import gettext
import os

def init_translation():
    # 翻訳ファイルを配置するディレクトリ
    path_to_locale_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../locale'
        )
    )

    # 翻訳用クラスの設定
    translater = gettext.translation(
        'messages',                   # domain: 辞書ファイルの名前
        localedir=path_to_locale_dir, # 辞書ファイル配置ディレクトリ
        languages=['ja_JP'],          # 翻訳に使用する言語
        fallback=True                 # .moファイルが見つからなかった時は未翻訳の文字列を出力
    )

    # Pythonの組み込みグローバル領域に_という関数を束縛する
    translater.install()


# プログラムを実行
if __name__ == "__main__":
    import app
    init_translation()
    app.main()
