import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.brmangas.net/manga/black-clover-online-1/')


# Geting the title of the manga
manga_title = ''
while True:
    if driver.find_element(By.XPATH, '//*[@id="posttitle"]/div/h1'):
        title = driver.find_element(By.XPATH, '//*[@id="posttitle"]/div/h1').text

        for letter in title.split():
            if letter not in ['LER', 'ONLINE']:
                manga_title += letter.capitalize()
                manga_title += ' '
        break

print(manga_title)

driver.close()