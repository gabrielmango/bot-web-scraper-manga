import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(service=service)

driver.get('https://www.brmangas.net/manga/black-clover-online-1/')

def wait_element(value):
    while True:
        if driver.find_element(By.CSS_SELECTOR, value):
            return driver.find_element(By.CSS_SELECTOR, value)

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
folder_manga = manga_title.replace(' ', '_').lower()
if not os.path.exists(folder_manga):
    os.makedirs(folder_manga)


# Getting images from pages
for key, value in manga_chapters.items():
    
    # changing url
    driver.get(value)

    # changing reading mode
    reading_mode = wait_element('#modo_leitura')
    select = Select(reading_mode)
    select.select_by_value('2')

    # Getting all images
    image_all = wait_element('#images_all')
    images = driver.find_elements(By.TAG_NAME, 'img')
    
    # Create folder to store images
    folder_chapter =  folder_manga + '/' + key.replace(' ', '_').lower()
    if not os.path.exists(folder_chapter):
        os.makedirs(folder_chapter)

    images_urls = [image.get_attribute('src') for image in images]

    
    # Save images
    number = 1
    for url in images_urls:
        if url:
            if manga_title.replace('_', '-') in url:
                driver.get(url)
                image_page = wait_element('body > img')

                response = requests.get(image_page.get_attribute('src'))

                if response.status_code == 200:
                    image_name = folder_chapter + '/' + str(number) + '.png'
                    with open(image_name, 'wb') as folder:
                        folder.write(response.content)
                    number += 1

driver.close()