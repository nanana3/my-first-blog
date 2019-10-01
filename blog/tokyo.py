import requests
import csv
import os
import pandas as pd

# APIキーの指定
apikey = "355cd2656197f1f6c6f642913389eab4eb2d529cfc7d65efd83e6a27cda300c6"

# APIのひな型
api = "https://api-tokyochallenge.odpt.org/api/v4/files/mlit/StationMap/Keio_Shinjuku_FacilityInfo.csv?acl:consumerKey={key}"

#スクリプトのあるディレクトリの絶対パスを取得
name = os.path.dirname(os.path.abspath(__name__))

#絶対パスと相対パスをくっつける csvの場所を入れないといけない
joined_path = os.path.join(name, '../../../Downloads/Keio_Shinjuku_FacilityInfo.csv')

#正規化して絶対パスにする
data_path = os.path.normpath(joined_path)


    # APIのURLを得る
url = api.format(key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
r = requests.get(url)
f = open(data_path,"r")
s = csv.reader(f,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(s)
for row in s:
    #rowはList
    #row[0]で必要な項目を取得することができる
    if row[3]=="2201":
         print(row[3],row[4],row[5])

f.close()
