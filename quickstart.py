# coding: UTF-8

# カレンダーを参照して現時点でスケジュールが入っているかを確認する
#
# 2018/11/4 miyamoto

# [START calendar_quickstart]
from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import pytz
import time


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'


#認証のためのwebページ設定

def main():
# 認証処理  this process needs web browser. 
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))


# 現在時点（正確には現在から１秒後の間に）スケジュールがあるかどうかを確認する
    tz = pytz.timezone('Asia/Tokyo')

    the_datetime  = tz.localize(datetime.datetime.now())
    the_datetime2 = tz.localize(datetime.datetime.now()+datetime.timedelta(seconds=+1))
    print(the_datetime)

    # query のボディ　itemsに認証されたアカウントの中の複数・単数のカレンダーIDを指定し、予定の有無を確認
    body = {
      "timeMin": the_datetime.isoformat(),
      "timeMax": the_datetime2.isoformat(),
      "timeZone": 'Asia/Tokyo',
      "items": [{"id": 'INSERT ID OF THE CALENDER YOU INTERESTED'}]
    }

#  the_datetimeからthe_datetime2までの間に予定がなければ busy:[null] のjsonがかえってくる
#  予定があればその予定の開始と終了が入る、複数あれば複数。
#  指定するidは、googleカレンダーのwebから各カレンダーの「設定と共有」から確認可能（結構下の方）

    eventsResult = service.freebusy().query(body=body).execute()
#　戻り値　
#        {u'timeMax': queryの値のUTC, u'kind': u'calendar#freeBusy', u'calendars': {　ID : {u'busy': []}, ID : {u'busy': []}, ID :{}, .... }, u'timeMin': queryの値のUTC}

    cal_dict = eventsResult[u'calendars']

# cal_dict　スケジュールがある場合　{ ID : {u'busy':[{u'start': 時刻, u'end': 時刻}]}}
#          スケジュールがない場合　{ ID : {u'busy':[]}}
# 　時刻はクエリーで問い合わせた時間帯とスケジュールのand をとった開始・終了時刻が帰ってくる
#   スケジュールに設定された始まりと終わりはわからない。

    for cal_name in cal_dict:
#        print(cal_dict)
        if cal_dict[cal_name][u'busy']:
            isBusy=True;
        else:
            isBusy=False;

#        print(cal_dict[cal_name][u'busy'])
        print("Is", cal_name, "busy for now? :", isBusy)
        print("")

if __name__ == '__main__':
#    main()

    while True:
        print('Let us see...')
        time.sleep(10)
        main()


# [END calendar_quickstart]
