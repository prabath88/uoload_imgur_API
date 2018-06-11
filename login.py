from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 



from imgurpython import ImgurClient
import configparser

def login():
	config = configparser.ConfigParser()
	config.read('auth.ini')

	client_id = config.get('credentials', 'client_id')
	client_secret = config.get('credentials', 'client_secret')

	imgur_username = config.get('credentials', 'imgur_username')
	imgur_password = config.get('credentials', 'imgur_password')

	client = ImgurClient(client_id, client_secret)

	authorized_url = client.get_auth_url('pin')
	
	
	driver = webdriver.PhantomJS()
	driver.get(authorized_url)
	

	username = driver.find_element_by_xpath('//*[@id="username"]')
	password = driver.find_element_by_xpath('//*[@id="password"]')
	username.clear()
	username.send_keys(imgur_username)
	password.send_keys(imgur_password)

	driver.find_element_by_name("allow").click()

	timeout = 5
	try:
		element_present = EC.presence_of_element_located((By.ID, 'pin'))
		WebDriverWait(driver,timeout)
		pin_element = driver.find_element_by_id('pin')
		pin = pin_element.get_attribute("value")

	except TimeoutException:
		print("timeout")
	driver.close()

	credentials = client.authorize(pin, 'pin')
	client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
	print("success")
	# print(client)

	return client

if __name__ == "__main__":
	login()
