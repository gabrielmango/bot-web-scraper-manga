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

print(manga_title)

driver.close()