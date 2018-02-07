from bs4 import BeautifulSoup
import urllib3
import certifi
import datetime
import random
import tweepy
import tw

def main():
    title = []
    description = []
    resp = getUrl()
    getDescription(resp, title, description)
    rm = random.randint(0, len(title))
    
    text = title[rm] + "\n" + description[rm]
    api = tw.getKey()
    api.update_status(status=text)


def getUrl():
    today = datetime.datetime.today()
    url = "https://fushinsha-joho.co.jp/serif.cgi?ym="
    year_month= str(today.year) + "{0:02d}".format(today.month)
    print(year_month)
    
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    
    return http.request('GET', url+year_month)

def getDescription(resp, title, description):
    soup = BeautifulSoup(resp.data, "lxml")
    for res in soup.findAll('div', attrs={'style':'font-size: 14px; line-height: 18px;'}):
        title.append(res.text)
    for  a in soup.findAll(class_ = 'headline'):
        description.append(a.text)

if __name__ == '__main__':
    main()
