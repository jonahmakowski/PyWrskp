import requests
from bs4 import BeautifulSoup
url = "https://www.tiobe.com/tiobe-index/"
r = requests.get(url)
soup = BeautifulSoup(r.content, features="lxml")
heading = soup.find(id="top20")
langs = heading.findAll('td')
topLangs = {}
for n in range(0, len(langs), 6):
    topLangs.update({
        langs[n].string: {
            "name": langs[n+3].string,
            "percent": langs[n+4].string,
            "change": langs[n+5].string
            }
                    })
for place in topLangs:
    print("{:5}{:22}{:10}{}".format(place, topLangs[place]["name"], topLangs[place]["percent"], topLangs[place]["change"]))