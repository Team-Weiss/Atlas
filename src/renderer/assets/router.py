from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import sys

config = {
	'env': 'prod',
	'routerPageURL': 'http://admin:password@routerlogin.net',
	'portal': 'https://selfcare.actcorp.in/web/hyd/home',
	'userID': '101872545250',
	'password': 'XvSY32dt'
}

class RouterAutomate:
	def __init__(self, mode):
		# Mode: Resets router connection
		if mode == '1':
			print('Mode 1: Reseting the router connection')
			self.resetRouterConnection()
		elif mode == '2':
			print('Mode 2: Signing in')
			self.tryToSignin()
		elif mode == '3':
			print('Mode 3: Total reset')
			self.resetRouterConnection()
			self.tryToSignin()

	def setURL(self, url):
		self.driver = webdriver.Firefox()
		self.driver.get(url)
		self.driver.implicitly_wait(300)

	def resetRouterConnection(self):
		self.setURL(config['routerPageURL'])
		self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
		self.advancedLabel = self.driver.find_element_by_id('advanced_label')
		self.advancedLabel.click()

		print('Action:: Click:Advanced Label')
		print('Waiting for page to load')
		time.sleep(3)
		print('Continuing')

		self.driver.switch_to.default_content()
		self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@name='formframe']"))

		main_window_handle = None
		while not main_window_handle:
			main_window_handle = self.driver.current_window_handle

		print('Action:: Click: Connection Status')
		connectionStatus = self.driver.find_element_by_id('conn_status')
		connectionStatus.click()

		signin_window_handle = None
		while not signin_window_handle:
				for handle in self.driver.window_handles:
						if handle != main_window_handle:
								signin_window_handle = handle
								break

		self.driver.switch_to.window(signin_window_handle)

		if (config['env'] == 'prod'):
			self.driver.find_element_by_xpath(u'//input[@name="disconnect"]').click()

			print('Waiting for release')
			time.sleep(5)
			print('Continuing')

			self.driver.find_element_by_xpath(u'//input[@name="connect"]').click()

			print('Waiting for renew')
			time.sleep(5)
			print('Continuing')
			# driver.find_element_by_xpath(u'//input[@name="close"]').click()
		
		self.driver.close()
		self.driver.switch_to.window(main_window_handle)
		self.driver.close()

	def verifyIfSignedIn(self):
	# variables
		isLoggedIn = False
		userId = None
		ipAddress = None
		try:
			logout2 = self.driver.find_element_by_xpath('//div[@class="logout2"]')
			ps = logout2.find_elements(By.XPATH, '//p')
			iterator = 0
			for p in ps:
				if iterator == 4:
					break
				message = p.get_attribute('innerHTML').strip()
				
				if iterator == 1:
					isLoggedIn = message == 'You are logged in as'
				elif iterator == 2:
					userId = message
				elif iterator == 3:
					ipAddress = message.split()[2]
				iterator += 1
		finally:
			if isLoggedIn:
				print('Logged in as ' + userId )
				print('Your IP Address: ' + ipAddress)
			else:
				print('Not Logged in')
			return isLoggedIn

	def tryToSignin(self):
		self.setURL(config['portal'])
		# Checki if logged in
		isLoggedIn = False
		if isLoggedIn == False:
			self.driver.find_element_by_id('_login_WAR_BeamPromotionalNDownloadsportlet_uname').send_keys(config['userID'])
			self.driver.find_element_by_id('pword').send_keys(config['password'])
			self.driver.find_element_by_xpath('//input[@value="LOGIN"]').click()
			# Make sure if logged in
			isLoggedIn = self.verifyIfSignedIn()
			if isLoggedIn:
				print('Login successfull')
				self.driver.close()
			else:
				print('Couldn\'t login. Please proceed manually')

if __name__ == "__main__":
	RouterAutomate(sys.argv[1])