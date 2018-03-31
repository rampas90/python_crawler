from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../chrome/mac/chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.naver.com/')

driver.find_element_by_name('id').send_keys('oceanfog')
driver.find_element_by_name('pw').send_keys('$Rhat1249') # 사용할 패스워드

driver.find_element_by_css_selector('.login .btn_login input').submit()

driver.implicitly_wait(5)
driver.get("https://nid.naver.com/user2/api/route.nhn?m=routePcMyInfo")
driver.implicitly_wait(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(html)
name = soup.find("span", {"class":"gnb_name"})

print(name)

driver.close()