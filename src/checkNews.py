# 東京都のコロナのニュースのタイトルとそのリンク先を取得します

from requests_html import HTMLSession
import slackweb
import re

news_url = "https://news.yahoo.co.jp/pages/article/covid19tokyo"
slackweb_url = "https://hooks.slack.com/services/xxxxxxxxxxxxxxxxxxxxx"

# セッション開始
session = HTMLSession()
r = session.get(news_url)

# HTMLを生成
r.html.render()

for num in range(1, 4):
    # スクレイピング
    article_title = r.html.find("#tab_1 > ul.dlpThumbLink > li:nth-child(" + str(num) + ") > a > span.dlpThumbText > span:nth-child(1)", first=True)
    article_title_text = article_title.text
    article_link = r.html.find("#tab_1 > ul.dlpThumbLink > li:nth-child(" + str(num) + ") > a", first=True)
    article_url = article_link.absolute_links

    # slackへ投稿
    slack = slackweb.Slack(url=slackweb_url)
    slack.notify(text=article_title_text + '\n' + re.sub("\{|\}|'", "", str(article_url)), channel="#general", username="covid19-news-bot", icon_emoji=":eyes:", mrkdwn=True)
