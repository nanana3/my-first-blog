import requests
import csv

# APIキーの指定
apikey = "355cd2656197f1f6c6f642913389eab4eb2d529cfc7d65efd83e6a27cda300c6"

# APIのひな型
api = "https://api-tokyochallenge.odpt.org/api/v4/files/mlit/StationMap/Keio_Shinjuku_FacilityInfo.csv?acl:consumerKey={key}"


# 各都市の温度を取得する
    # APIのURLを得る
url = api.format(key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
#r = requests.get(url)
f = open(url,"rb")
s = csv.reader(f)
header = next(s)
print(header)
for row in s:
    #rowはList
    #row[0]で必要な項目を取得することができる
    print(row)
