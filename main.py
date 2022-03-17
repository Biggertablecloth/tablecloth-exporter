import os
import shutil
import time
from tkinter import *
from tkinter import filedialog, simpledialog

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tqdm.auto import tqdm
import getpass

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://login.tablecloth.io/")

username, password = driver.find_elements_by_tag_name('input')

print('Please write your Tablecloth.io email and password. This information is deleted immediately by the script.')
Tk().withdraw()
username_txt = input('Tablecloth email: ')
password_txt = input('Tablecloth password: ')

username.send_keys(username_txt)
password.send_keys(password_txt)

del username_txt, password_txt

sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/button/span[1]').click()

def wait_for_element(xpath):
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, xpath))
        WebDriverWait(driver, 60).until(element_present)
        element_present = EC.element_to_be_clickable(
            (By.XPATH, xpath))
        WebDriverWait(driver, 60).until(element_present)

    except TimeoutException:
        print('time out occured')

wait_for_element('/html/body/div[1]/div/header/div/div[2]/button[2]')
driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[2]/button[2]').click()

time.sleep(10)



# Select downloads folder
download_folder = filedialog.askdirectory()

# Select gdrive folder
folder_selected = filedialog.askdirectory()

with open('dashboard_ids.txt', 'r') as f:
    dashboard_ids = f.read().split()

for dashboard_id in tqdm(dashboard_ids, desc='Progress'):
    count = 0
    while True:
        try:
            if os.path.exists(os.path.join(folder_selected, dashboard_id + '.pdf')):
                break

            driver.get(f'https://data.tablecloth.io/infographics/{dashboard_id}')
            time.sleep(4)
            driver.find_element_by_class_name("designer-box__more-button").click()
            time.sleep(4)
            driver.find_element_by_xpath("//*[contains(text(), 'Share & export')]").click()
            time.sleep(4)
            driver.find_element_by_xpath("//*[contains(text(), 'Download PDF')]").click()
            time.sleep(15)
            title = driver.title.replace(' - The Data Center', '').replace('/', '_')
            shutil.move(os.path.join(download_folder, title + '.pdf'),
                        os.path.join(folder_selected, dashboard_id + '.pdf'))
            break
        except:
            count += 1
            if count >= 4:
                print('Dashboard skipped too many times. Skipping dashboard permanently.')
                break
            else:
                print('Skipped a dashboard due to an error. Trying again...')
