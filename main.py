import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

service = ChromeService(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.brmangas.net/manga/black-clover-online-1/')


# Getting manga title
manga_title = ''
while True:
    if driver.find_element(By.XPATH, '//*[@id="posttitle"]/div/h1'):
        title = driver.find_element(By.XPATH, '//*[@id="posttitle"]/div/h1').text

        for letter in title.split():
            if letter not in ['LER', 'ONLINE']:
                manga_title += letter.capitalize()
                manga_title += ' '
        break
    time.sleep(0.5)

# Getting manga chapters
manga_chapters = {}
chapters_xpath = '/html/body/div/div[1]/main/div/div[2]/div[2]/div[2]/div[1]/div[4]/ul'
while True:
    if driver.find_element(By.XPATH, chapters_xpath):
        ul_element = driver.find_element(By.XPATH, chapters_xpath)
        a_elements = ul_element.find_elements(By.TAG_NAME, 'a')

        manga_chapters = {
            element.text: element.get_attribute('href')
            for element in a_elements
        }
        break
    time.sleep(1)
driver.close()