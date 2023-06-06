from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
import time

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox()

# driver.set_page_load_timeout(6)
driver.get('https://www.digikala.com/product/dkp-7919668/%DA%A9%D9%81%D8%B4-%D8%B1%D9%88%D8%B2%D9%85%D8%B1%D9%87-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%DA%86%D8%B1%D9%85-%D8%B9%D8%B7%D8%A7%D8%B1%D8%AF-%D9%85%D8%AF%D9%84-sh05/')
try:
     # click on show more button
     show_more_button = driver.find_element(By.CSS_SELECTOR , 'div.mt-3:nth-child(2) > div:nth-child(2) > div:nth-child(7) > button:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
     # scroll sown to click
     driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", show_more_button)
     time.sleep(2)
     show_more_button.click()
except:
     print('the show more button not found')
     
page_count = 1
try:
     # get the number of opinion pages
     page_count = driver.find_element(By.CSS_SELECTOR , 'div.font-body:nth-child(2)')
     span_elements = page_count.find_elements(By.TAG_NAME,'span')
     last_span_element = span_elements[-1]
     persian_number = last_span_element.text
     page_count = persian_number.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
     print('the number of pages : ' , int(page_count)) 
     page_count = int(page_count)
except:
     print('the product has just one opinion')

opinion_list = []

opinion_tag = driver.find_element(By.CSS_SELECTOR , 'div.mt-3:nth-child(2) > div:nth-child(2)')

for i in range(page_count):
     time.sleep(2)
     p_tags = opinion_tag.find_elements(By.XPATH , ".//p[contains(@class, 'text-body-1 color-900 mb-1 pt-3 break-words')]")
     driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", p_tags[0])
     time.sleep(2)

     for p in p_tags:
          opinion_list.append(p.text)
     try:
          next_button = driver.find_element(By.CSS_SELECTOR , 'div.font-body:nth-child(3) > span:nth-child(2)')
          driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", next_button)
          time.sleep(2)
          next_button.click()
     except:
          print('breaking the loop')
          
print(len(opinion_list))


# driver.quit()