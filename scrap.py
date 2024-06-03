# import requests
# from bs4 import BeautifulSoup
# url = "https://rainbow-enterprise.in/"
# r = requests.get(url)
# htmlContent = r.content
# #print(htmlContent)
# soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify()) 
# # title = soup.title
# # GET ALL THE PARAGRPHPS FROM THE WEBPAGE
# # markup = "<h2>Career Guidance &amp; Project Support</h2>"
# # soup2 = BeautifulSoup(markup)
# # print(type(soup2.p.string))

# # navbarSupportedContent = soup.find(id='main-header-bar-navigation')
# # print(navbarSupportedContent.contents)

import bs4
import requests
url = "https://rainbow-enterprise.in/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
# # print(soup.prettify())
# for para in soup.find_all('p'):
#     print(para.text)
for links in soup.find_all('a'):
    link = links.get('href')
    print(link)
    