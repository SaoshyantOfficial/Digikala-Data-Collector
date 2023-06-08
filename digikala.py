#import statements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import csv
     
class data_collector:
     
     # list of opinions
     opinion_list = []
     
     def driver_options(self):

          # Selenium options
          options = webdriver.FirefoxOptions()
          options.add_argument('--headless')
          driver = webdriver.Firefox()
          return driver
     
     def save_to_csv(self , opinion_list):
          #save the opinions
          with open('opinions.csv', 'w') as csvfile:
               writer = csv.writer(csvfile)
               
               for element in self.opinion_list:
                    writer.writerow([element])


     def __init__(self , product_url):
          
          self.product_url = product_url
          
           # driver oprion
          driver = self.driver_options()
          

         
          driver.get(self.product_url)

          try:
               
               # click on show more button
               show_more_button = driver.find_element(By.CSS_SELECTOR , 'div.mt-3:nth-child(2) > div:nth-child(2) > div:nth-child(7) > button:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
               # scroll sown to click
               driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", show_more_button)
               time.sleep(1)
               show_more_button.click()
               
          except:
               
               print('the show more button not found')

          opinion_tag = driver.find_element(By.CSS_SELECTOR , 'div.mt-3:nth-child(2) > div:nth-child(2)')

          while True:
               
               try:
                    p_tags = opinion_tag.find_elements(By.XPATH , ".//p[contains(@class, 'text-body-1 color-900 mb-1 pt-3 break-words')]")
                    # driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", p_tags[0])
                    time.sleep(1)
               except:
                    print('error')

               for p in p_tags:
                    self.opinion_list.append(p.text )
                         
               try:
                    
                    #click on next button
                    next_button = driver.find_element(By.CSS_SELECTOR , 'div.font-body:nth-child(3) > span:nth-child(2)')
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", next_button)
                    time.sleep(2)
                    next_button.click()
                    
               except:
                    
                    print('breaking the loop')
                    #break the loop
                    break

          print(len(self.opinion_list))
 
          self.save_to_csv(self.opinion_list)
          
          driver.quit()
          


product_url_list = ['https://www.digikala.com/product/dkp-592455/%D9%81%D8%B1%DA%A9%D9%86%D9%86%D8%AF%D9%87-%D9%85%D9%88-%D9%85%D8%AE%D8%B1%D9%88%D8%B7%DB%8C-%D9%85%D8%AE%D9%85%D9%84%DB%8C-%D9%BE%D8%B1%D9%88%D9%85%D8%A7%D8%B1%D9%88%D9%86-rl-9905/','https://www.digikala.com/product/dkp-7919668/%DA%A9%D9%81%D8%B4-%D8%B1%D9%88%D8%B2%D9%85%D8%B1%D9%87-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%DA%86%D8%B1%D9%85-%D8%B9%D8%B7%D8%A7%D8%B1%D8%AF-%D9%85%D8%AF%D9%84-sh05/',
                    'https://www.digikala.com/product/dkp-5476010/%D9%85%D8%A7%D9%86%DB%8C%D8%AA%D9%88%D8%B1-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vg328h1b-%D8%B3%D8%A7%DB%8C%D8%B2-315-%D8%A7%DB%8C%D9%86%DA%86/']

# for i in product_url_list:
#      data = data_collector(i)
# temp = data_collector('https://www.digikala.com/product/dkp-7919668/%DA%A9%D9%81%D8%B4-%D8%B1%D9%88%D8%B2%D9%85%D8%B1%D9%87-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%DA%86%D8%B1%D9%85-%D8%B9%D8%B7%D8%A7%D8%B1%D8%AF-%D9%85%D8%AF%D9%84-sh05/')
