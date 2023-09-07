from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
opt = Options()
opt.add_argument(r"--silent")
opt.add_argument(r"--no-sandbox")
opt.add_argument(r"--disable-dev-shm-usage")
opt.add_argument(r'--ignore-certificate-errors')
opt.add_experimental_option("detach", True)
#opt.add_argument('headless')
opt.add_argument(f'user-agent={user_agent}')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)

url = 'https://www.atptour.com/en/players/carlos-alcaraz/a0e2/overview'
driver.get(url)

search_button = '/html/body/div[1]/div[2]/div/div[2]/div/div/div'
element = (By.XPATH, search_button)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(element)).click()

search_box = '/html/body/div[2]/div/form/input'
element = (By.XPATH, search_box)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(element)).send_keys('Ben Shelton' + '\n')

profile_button = '/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/a[1]'
element = (By.XPATH, profile_button)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(element)).click()
