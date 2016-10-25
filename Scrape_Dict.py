import bs4
import requests
req =  requests.get("http://www.noslang.com/dictionary/1/")
soup = bs4.BeautifulSoup(req.text, 'html.parser')

let = soup.find_all("dt")
'''
print(let[1].a["name"])
print(let[1].abbr["title"])
'''
count  = 0
f = open("Dict.txt","a")
for elements in let:
    f.write(let[count].a["name"])
    f.write(", ")
    f.write(let[count].abbr["title"])
    f.write("\n")
    count += 1

f.close()
