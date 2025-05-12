from bs4 import BeautifulSoup
import requests

# get url
url = input('Enter a URL (include http:/): ')
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"html.parser")
print(html)

links = []
for i in soup.find_all("a",href=True):
    links.append(1)
    print("link is found: ", i)
    
# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
emails = re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html)
 
# print the number of links in the list
print("\nFound {} links".format(len(links)))
for email in emails:
    print(email)