# cosmed-store-list-py
使用Python的BeautifulSoup套件，擷取康是美門市列表。

資料來源： [康是美門市查詢](https://www.cosmed.com.tw/Contact/Shop_list.aspx)
![webpage](/screenshots/webpage.png?raw=true "webpage")

輸出結果（csv檔）： 
![webpage](/screenshots/shop_list_csv.png?raw=true "webpage")




## Requirements

須安裝[Python3](https://www.python.org/)以及Python語言的[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)套件

安裝BeautifulSoup4 (for Ubuntu 16.04)
```
sudo apt-get install python3-bs4
```


## Code structure


File/Folder          |	Description
 --------------------| ------------------------------------------------ 
.gitignore           | gitignore
README.md            | README
screenshots          | README.md使用的截圖
store-list-crawler.py| 網頁爬蟲的程式碼（Python）
shop_list.csv        | 網頁爬蟲的結果



## 輸出結果
執行 store-list-crawler.py ，會將結果輸出為CSV檔案：

* shop_list.csv

    除標題欄、標題列之外，共有5欄 * N列。

    欄位名稱  |資料範例
    -------- | ---------------------------------- 
    門市名稱 | 富農門市
    門市網址 | https://www.cosmed.com.tw/Contact/Shop_intro.aspx?ID=519
    門市地址 | 台南市東區裕農路766號
    門市電話 | 036-3317533
    營業時間 | 假日:9-23 平日:9-23

    其中「營業時間」包含換行字元。


## 我的開發環境：
* Ubuntu 16.04.3 LTS
* Python 3.5.2
* PyCharm Community Edition 2017.2.4

尚未在其他環境測試，不確定是否能支援。

