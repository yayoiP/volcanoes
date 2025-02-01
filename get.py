import requests as req
url = "https://www.data.jma.go.jp/vois/data/tokyo/volcano.html"
from bs4 import BeautifulSoup
res = req.get(url)
res.encoding = res.apparent_encoding
bs = BeautifulSoup(res.text, 'html.parser')
kazan=bs.select("option")
text=""


data=[{"リンク":str(i.get('value')).strip("./"),"名前":i.text}for i in kazan]


for i in data:
    text=text+f"\n\n{i['名前']}\nhttps://www.data.jma.go.jp/vois/data/tokyo/{i['リンク']}"
print(str(text))
