import os
import requests
import csv
from bs4 import BeautifulSoup
from stock_find import stock_list

def get_stock_price(stock_list):
    for stock_list in stock_list:
        url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=&stockNo={stock_list}"
        
        # 存進的資料夾
        directory = "stock_data"

        # 發送 GET 請求取得網頁內容
        response = requests.get(url)
        
        # 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 找到第一個表格
        table = soup.find("table")
        
        # 找到所有的資料列
        rows = table.find_all("tr")
        
        # 建立一個空的資料清單
        data = []
        
        # 迴圈處理每一列的資料
        for row in rows:
            # 找到每一列中的所有欄位
            columns = row.find_all("td")
            
            # 如果欄位數量不正確，則跳過此列
            if len(columns) != 9:
                continue
            
            # 取得日期、收盤價等資訊
            date = columns[0].text
            closing_price = columns[6].text
            
            # 將資訊加入資料清單
            data.append([date, closing_price])
        
        # 建立檔案名稱
        filename = f"stock_{stock_list}.csv"

        # 建立檔案路徑
        file_path = os.path.join(directory, filename)
        
        # 寫入 CSV 檔案
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["日期", "收盤價"])  # 寫入標題欄位
            writer.writerows(data)  # 寫入資料
        
        print(f"資料已儲存至 {filename} 檔案中。")

# 測試程式碼
get_stock_price(stock_list)
