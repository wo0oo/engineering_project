import requests
from bs4 import BeautifulSoup

def search_signum(url,temp):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    res=requests.get(url,headers=head)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    signum= soup.find_all("tr")[temp+1]
    signum=signum.a["href"]
    
    return signum[-3:-2]