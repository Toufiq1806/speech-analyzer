from bs4 import BeautifulSoup
import requests
import re 
url="https://trumpwhitehouse.archives.gov/farewell-address/"
speech=requests.get(url).text
scrap=BeautifulSoup(speech,"lxml")
content=scrap.find("div",class_="page-content__content editor")
para=content.find_all("p")
cleaned_li=[]
for i in para:
    remove_tag=i.get_text()
    cleaned_li.append(remove_tag)
final_version=" ".join(cleaned_li)
remove_unwanted_char=re.sub(r'[^a-zA-Z\s]',"",final_version).lower()
final_version_li=remove_unwanted_char.split()
