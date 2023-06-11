import logging
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename='errors.log', filemode="w", format='occurred date & time: %(asctime)s %(levelname)-8s \nfile name: %(filename)s\nline number: %(lineno)d \nerror: %(message)s',
level=logging.ERROR, datefmt='%Y-%m-%d %H:%M:%S')

class Digikala:
    """
    A class to scrape reviews from the Digikala website.

    Attributes:
    reviews: A list of review texts.
    reviews_url: A list of URLs to the review pages.
    error: A boolean indicating if an error has occurred during the scraping process.
    """
    def __init__(self, reviews_url):
        self.reviews = []
        self.reviews_url = reviews_url
        self.error = False

    def driver_options(self):
        """
        Set up the Firefox webdriver with headless option.

        Returns:
        A webdriver instance with headless option.
        """
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        return webdriver.Firefox(options=options)

    def save_to_csv(self, reviews):
        """
        Save reviews as a CSV file.

        Args:
        reviews: A list of review texts.
        """
        try:
            with open('reviews.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                for review_text in self.reviews:
                    writer.writerow([review_text])
        except Exception as e:
            logging.exception("Error saving reviews to CSV file: %s", e)

    def collector(self):
        """
        Scrape reviews from the review pages.
        """
        with self.driver_options() as driver:
          #   driver.set_page_load_timeout(20)
            wait = WebDriverWait(driver, 10)

            for url in self.reviews_url:
                try:
                    # Get target page
                    driver.get(url)

                    try:
                        # Click on show more button if available
                        time.sleep(2)
                        show_more_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.color-secondary-500:nth-child(1)')))
                        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", show_more_button)
                        time.sleep(1)
                        show_more_button.click()

                    except Exception as e:
                         print("nooo", e)
                        

                    while True:
                        comments = wait.until(EC.presence_of_element_located((By.ID, "commentSection")))
                        wait_1 = WebDriverWait(comments, 10)
                        p_tags = wait_1.until(EC.presence_of_all_elements_located((By.XPATH, ".//p[contains(@class, 'text-body-1 color-900 mb-1 pt-3 break-words')]")))
                        for p in p_tags:
                            self.reviews.append(p.text)

                        try:
                            # Click on next page button
                            time.sleep(1)
                            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.font-body:nth-child(3) > span:nth-child(2)')))
                            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", next_button)
                            time.sleep(1.5)
                            next_button.click()

                        except:
                            # Break the loop when there is no other page
                            print('breaking the loop')
                            break

                except Exception as e:
                    print("An error has occurred")
                    self.error = True
                    logging.exception("Error scraping reviews: %s", e)
                    break

            # Save reviews as csv
            self.save_to_csv(self.reviews)

# product_url_list = ['https://www.digikala.com/product/dkp-5476010/%D9%85%D8%A7%D9%86%DB%8C%D8%AA%D9%88%D8%B1-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-%D9%85%D8%AF%D9%84-vg328h1b-%D8%B3%D8%A7%DB%8C%D8%B2-315-%D8%A7%DB%8C%D9%86%DA%86/',
# 'https://www.digikala.com/product/dkp-7919668/%DA%A9%D9%81%D8%B4-%D8%B1%D9%88%D8%B2%D9%85%D8%B1%D9%87-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%DA%86%D8%B1%D9%85-%D8%B9%D8%B7%D8%A7%D8%B1%D8%AF-%D9%85%D8%AF%D9%84-sh05/']

# temp = Digikala(product_url_list)
# temp.collector()