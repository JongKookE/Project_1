from bs4 import BeautifulSoup as BS
from urllib.parse import quote_plus
from selenium import webdriver    
from urllib.request import urlretrieve

name = "박효신"
URL = f"https://www.google.com/search?q={name}&sxsrf=ALiCzsYkP5wvUsHP9P2Iq3R2ItxcysV_xA:1658818837793&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiu28rc_ZX5AhWXqlYBHfn_BJsQ_AUoAXoECAEQAw&biw=1244&bih=1301&dpr=1"

driver=webdriver.Chrome('/home/jongkook/chrome_driver/chromedriver') #크롬 드라이버
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(URL)

html = driver.page_source
soup = BS(html,features="html.parser")

img = soup.select('img')

i_list = []
count = 1

print("Searching...")
for i in img:
   try:
      i_list.append(i.attrs["src"])
   except KeyError:
      i_list.append(i.attrs["data-src"])

print("Downloading...")
for i in i_list:
   urlretrieve(i,"/home/jongkook/박효신/"+name+"_"+str(count)+".jpg")
   count+=1

driver.close()
print("FINISH")
