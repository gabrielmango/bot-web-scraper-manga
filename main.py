import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.brmangas.net/manga/black-clover-online-1/')


def wait_element(driver, x_path):
    while True:
        if driver.find_element(By.XPATH, x_path):
            return driver.find_element(By.XPATH, x_path).text
        time.sleep(1)


title_xpath = '//*[@id="posttitle"]/div/h1'

title = wait_element(driver, title_xpath)
manga_title = ''
for letter in title.split():
    if letter not in ['LER', 'ONLINE']:
        manga_title += letter.capitalize()
        manga_title += ' '


driver.close()