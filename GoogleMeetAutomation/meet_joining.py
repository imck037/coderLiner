<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt)

mail_address = os.environ['EMAIL_USER']
password = os.environ['EMAIL_PASS']
g_meet_url = "https://meet.google.com/kbi-nixt-ryd"
driver.get(g_meet_url)

driver.find_element(By.CLASS_NAME, "rrdnCc").click()
driver.implicitly_wait(10)

driver.find_element(By.ID, "identifierId").send_keys(mail_address)
driver.find_element(By.ID, "identifierNext").click()
driver.implicitly_wait(10)

# input Password
driver.find_element(By.XPATH,
    '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
driver.implicitly_wait(10)
driver.find_element(By.ID, "passwordNext").click()
driver.implicitly_wait(10)


# turn off mic
time.sleep(2)
driver.find_element(By.CLASS_NAME,'dP0OSd').click()
driver.implicitly_wait(1)

# turn off camera
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'GOH7Zb').click()
driver.implicitly_wait(1)

# Ask to Join meet
time.sleep(5)
driver.implicitly_wait(1)
driver.find_element(By.CSS_SELECTOR, "button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 jEvJdc QJgqC']").click()
    
time.sleep(5)
driver.quit()
=======
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt)

# define your email and password
mail_address = os.environ['EMAIL_USER']      # set your email in the environment_variable
password = os.environ['EMAIL_PASS']          # for security purpose
g_meet_url = "https://meet.google.com/kbi-nixt-ryd"

driver.get(g_meet_url)

driver.find_element(By.CLASS_NAME, "rrdnCc").click()
driver.implicitly_wait(10)

driver.find_element(By.ID, "identifierId").send_keys(mail_address)
driver.find_element(By.ID, "identifierNext").click()
driver.implicitly_wait(10)

# input Password
driver.find_element(By.XPATH,
    '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
driver.implicitly_wait(10)
driver.find_element(By.ID, "passwordNext").click()
driver.implicitly_wait(10)


# turn off mic
time.sleep(2)
driver.find_element(By.CLASS_NAME,'dP0OSd').click()
driver.implicitly_wait(1)

# turn off camera
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'GOH7Zb').click()
driver.implicitly_wait(1)

# Ask to Join meet
time.sleep(5)
driver.implicitly_wait(1)
driver.find_element(By.CSS_SELECTOR, "button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 jEvJdc QJgqC']").click()
    
time.sleep(5)
driver.quit()
>>>>>>> e00d551e6d51a2dc6b0deaab511b0772dfae95c1
