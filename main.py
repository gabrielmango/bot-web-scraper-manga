import os
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

def wait_element(value):
    while True:
        if driver.find_element(By.CSS_SELECTOR, value):
            return driver.find_element(By.CSS_SELECTOR, value)
        time.sleep(1)

# Getting manga title
manga_title = ''

title = wait_element('#posttitle > div > h1').text

for letter in title.split():
    if letter not in ['LER', 'ONLINE']:
        manga_title += letter.capitalize()
        manga_title += ' '
manga_title = manga_title.strip()


# Getting manga chapters
manga_chapters = {}
chapters_css_selector = 'body > div > div.wrapper > main > div > div.row.interna > div.col-lg-10.col-md-9.col-sm-9.col-xs-12.col > div.manga > div.container_t > div.lista_manga > ul'

ul_element = wait_element(chapters_css_selector)
a_elements = ul_element.find_elements(By.TAG_NAME, 'a')

manga_chapters = {
    element.text: element.get_attribute('href')
    for element in a_elements
}


# Create folder to store chapters
if not os.path.exists(manga_title):
    os.makedirs(manga_title)

driver.close()