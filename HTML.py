import requests
from bs4 import BeautifulSoup

# 火山名と活動情報のリンクをリストにまとめる
volcanoes =[]
with open("一覧.txt",encoding="utf-8") as text:
    for i in text.read().split("\n\n"):
        volcanoes.append(tuple(i.split("\n")))

# HTMLテーブルのヘッダー部分を作成
html_table = """
<table>
  <thead>
    <tr>
      <th>火山名</th>
      <th>活動情報</th>
    </tr>
  </thead>
  <tbody>
"""

# リンクから情報を取得してHTMLテーブルの本体部分を作成
for volcano, link in volcanoes:
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # テーブルの活動情報欄には特定の要素がないため、とりあえずリンクを表示する
        activity_info = f'<a href="{link}">リンク</a>'
        html_table += f"<tr><td>{volcano}</td><td>{activity_info}</td></tr>"
    else:
        print(f"Error: Failed to fetch data for {volcano}")

# HTMLテーブルのフッター部分を追加
html_table += """
  </tbody>
</table>
"""

# HTMLファイルに出力
with open("volcanoes_table.html", "w", encoding="utf-8") as file:
    file.write(html_table)

print("HTMLテーブルが作成されました。")
