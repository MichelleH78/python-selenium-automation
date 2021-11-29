from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\miche\\Desktop\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order')

from selenium.webdriver.common.keys import Keys


search.send_keys(Keys.RETURN)

sleep(4)



assert 'Cancel Items or Orders' in driver.page_source, f"Expected query not in {driver.page_source()}"
print('Test Passed')

driver.quit()
