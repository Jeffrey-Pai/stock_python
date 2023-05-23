import requests
 
 
domain_url = 'https://www.twse.com.tw/zh'
response = requests.get(
    f'{domain_url}/exchangeReport/STOCK_DAY?response=csv&date=20210901&stockNo=2330')
	
with open('2330.csv', 'wb') as file:
	file.write(response.content)
	file.close()