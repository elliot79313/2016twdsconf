# 2016 資料科學年會 Slideshare 分享量與閱覽量數據


透過 Facebook 資料抓取與 Slideshare 數據提供

讓大家對於本次資料科學年會與會者的喜好有初步認識

-----

抓取方式:

Step1: 從資料科學年會粉絲頁抓資料

```
python fb_post_crawler.py

```

Step2: 訪問各Link 點擊量

```
python fb_link_stats_crawler.py

```

Step3: 將資料轉換成 CSV

```
python jsontocsv.py 0 post_data_insights.json post_data_insights.csv

```


