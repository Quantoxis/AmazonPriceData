import requests as r
import bs4 as b
from datetime import datetime as dt
import time as t
import schedule
import smtplib

product_list = ['B08MVBYQFW','B08MVD4YVJ','B08MV9RSPC']
base_url = 'https://www.amazon.co.uk/'
url = 'https://www.amazon.co.uk/dp/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'
}

base_response = r.get(base_url, headers=headers)
cookies = base_response.cookies

def track_prices():
    print(dt.now())
    for product in product_list:

        product_response = r.get(url+product, headers=headers, cookies=cookies)

        soup = b.BeautifulSoup(product_response.text, features='lxml')
        price_lines = soup.find_all(class_="a-price-whole")
        product_name = soup.find_all(class_ = "selection")



        final_price = str(price_lines[0])
        final_price = final_price.replace('<span class="a-price-whole">.', '')
        final_price = final_price.replace('<span class="a-price-decimal">', '')


        print(product_name,url+product, final_price)



track_prices()

schedule.every(30).to(120).minutes.do(track_prices)



while True:
    schedule.run_pending()
    t.sleep(1)








