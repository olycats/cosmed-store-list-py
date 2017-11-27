import requests
import csv
from bs4 import BeautifulSoup

base_url = "https://www.cosmed.com.tw/Contact"

# get total page count
# find the last element of <div class="btn-digit">
response = requests.get(base_url + "/Shop_list.aspx?pg=9999")
page = BeautifulSoup(response.text, "lxml")
last_pages = page.find_all("div",class_="btn-digit")
page_count = int(last_pages[len(last_pages)-1].find("a").string)

store_name = []  # 門市名稱
store_url = []  # 門市網址
store_address = []  # 門市地址
store_tel = []  # 門市電話
store_hours = []  # 營業時間

# for each page
for i in range(1, page_count + 1):
    response = requests.get(base_url + "/Shop_list.aspx/Shop_list.aspx?pg=" + str(i))
    page = BeautifulSoup(response.text, "lxml")

    # for each store (6 stores in a page)
    for outletsList in page.find_all("div", class_="outletsList"):
        # 門市名稱
        for td in outletsList.find_all("td", class_="TableTitile_OrangeredNo", string="門市名稱"):
            store_name.append(td.parent.find("td", class_="TableItem_OrangeredNo").find("a").string)
        # 門市網址
        for td in outletsList.find_all("td", class_="TableTitile_OrangeredNo", string="門市名稱"):
            store_url.append(td.parent.find("td", class_="TableItem_OrangeredNo").find("a").attrs['href'])
        # 門市地址
        for td in outletsList.find_all("td", class_="TableTitile_OrangeredNo", string="門市地址"):
            store_address.append(td.parent.find("td", class_="TableItem_OrangeredNo").string)
        # 門市電話
        for td in outletsList.find_all("td", class_="TableTitile_OrangeredNo", string="門市電話"):
            store_tel.append(td.parent.find("td", class_="TableItem_OrangeredNo").string)
        # 營業時間
        for td in outletsList.find_all("td", class_="TableTitile_OrangeredNo", string="營業時間"):
            # replace <br> to "\n"
            for br in td.parent.find_all("br"):
                br.replace_with("\n")
            store_hours.append(td.parent.find("td", class_="TableItem_OrangeredNo").contents)

# write data to csv file
with open('shop_list.csv', 'w',) as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市網址', '門市地址', '門市電話', '營業時間']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(base_url + '/' + store_url[n])
        newrow.append(store_address[n])
        newrow.append(store_tel[n])
        newrow.append(''.join(store_hours[n]))
        csvwriter.writerow(newrow)