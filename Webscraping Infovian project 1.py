import requests ,string
import pandas as pd
from bs4 import BeautifulSoup

data={'title':[],'price':[]}

url= "https://www.amazon.in/s?k=iphone&crid=3B20VBEEWRHGQ&sprefix=iphone%2Caps%2C236&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
 
  
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
spans=soup.select(".a-size-medium.a-color-base.a-text-normal")

for span in spans:
    print(span.string)
    data["title"].append(span.string)
    
prices=soup.select(".a-price")
for price in prices:
    if not("a-text-price" in price.get("class")):
     print(price.find("span").get_text())
     data["price"].append(price.find("span").get_text())
     if len(data["price"])==len(data["title"]):
        break
df=pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)