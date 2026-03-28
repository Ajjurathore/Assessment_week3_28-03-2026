from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get('https://www.vogue.in/')
sleep(2)

driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Shopping']"))).click()

action=ActionChains(driver)

element=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='69845cc157840edfb23334e7']")))
action.scroll_to_element(element)

action.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

all_windows=driver.window_handles

driver.switch_to.window(all_windows[-1])

name=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-flex justify-content-between align-items-center pt-3 pb-2']/h1")))
print(name.text)

price=wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='product-price-final product-price-final-sale']/span[2]")))
print(price.text)

driver.close()