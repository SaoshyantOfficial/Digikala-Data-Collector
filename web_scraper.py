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
# time.sleep(2)

span_element = driver.find_element(By.CSS_SELECTOR , "span.mx-1:nth-child(1)")
span_element.click()


opinion_tag = driver.find_element(By.CSS_SELECTOR , 'div.mt-3:nth-child(2) > div:nth-child(2)')
p_tags = opinion_tag.find_elements(By.XPATH , ".//p[contains(@class, 'text-body-1 color-900 mb-1 pt-3 break-words')]")
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", p_tags[0])
# time.sleep(2)

for p in p_tags:
    print(p.text)

print('$$$$$$$$$')
print(len(p_tags))

driver.quit()
