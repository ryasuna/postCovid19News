# postCovid19News
東京都のコロナのニュースのタイトルとそのリンク先を取得しslackに投稿します。

## 取得元ページ

<img width="500" alt="yahoonews" src="https://user-images.githubusercontent.com/71859553/121776917-6a2b7f80-cbca-11eb-843a-3a7adee54f33.png">

## 投稿結果

<img width="500" alt="slack" src="https://user-images.githubusercontent.com/71859553/121776953-9e06a500-cbca-11eb-9b8f-aa1b7da6d25c.png">

## 使用手順

incoming webhookのリクエスト先は適宜変更する。
https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-%E3%81%A7%E3%81%AE-Incoming-Webhook-%E3%81%AE%E5%88%A9%E7%94%A8

```
docker-compose up -d
docker-compose exec python bash
# python getNews.py
```

