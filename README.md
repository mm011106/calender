# calender
Google Calender watch script 


## Function：

指定のカレンダーをしらべて現在イベントが進行中であればTure
イベントがなければFalseを返す。

## 手順

参照：https://developers.google.com/calendar/quickstart/python

### APIを使うための手順

- google APIのアカウントを開く
- Calenderを使うためのプロジェクトを作る
- 認証のための設定をする(OAuth)
- credentials.jsonとして認証設定時の設定ファイルをダウンロードしておく。アプリケーション実行時参照されるので、同じディレクトリにいれておく。

### クライアントの設定

- ツールキット（今回はpython）を導入
- プログラミング
- API：freebusyを使用

## 動作確認

- 最初のスクリプト起動時に認証作業（webブラウザが必要）
- token.json will be generated.
- API経由でのやり取り

## 問題点：

- 認証作業が必要なので、UIが必要。IoTでは他の認証方法が必要。
