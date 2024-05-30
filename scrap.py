import requests
from bs4 import BeautifulSoup
url = "https://estatelion.com/office-space-rent"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify()) 
# title = soup.title
# GET ALL THE PARAGRPHPS FROM THE WEBPAGE
# markup = "<h2>Career Guidance &amp; Project Support</h2>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))

# navbarSupportedContent = soup.find(id='main-header-bar-navigation')
# print(navbarSupportedContent.contents)