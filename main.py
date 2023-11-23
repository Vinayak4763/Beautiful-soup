import requests
def fetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path,"wb")as f:
     f.write(r.content)

url= "https://timesofindia.indiatimes.com/"

fetchAndSaveToFile(url,"data/times.html")   