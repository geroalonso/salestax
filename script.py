#importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date


url = 'https://ritx-fl-sales.bswa.net' #set the website
driver = webdriver.Chrome(ChromeDriverManager().install()) #set the search engine
driver.implicitly_wait(10) #set implicit wait
driver.get(url) #open tthe browser



#first site
class Corporation:
	manager = 'Tomas Ventura'
	email = 'admin@ibericmalls.com'
	collection_allowance = 30
	pay_date = 15


	def __init__ (self, certificate_number, business_partner_number, routing_number, account_number, gross_sales, exempt_sales, surtax_rate, tax_rate):
		self.certificate_number = certificate_number
		self.business_partner_number = business_partner_number
		self.routing_number = routing_number
		self.account_number = account_number
		self.gross_sales = gross_sales
		self.exempt_sales= exempt_sales
		self.surtax_rate = surtax_rate
		self.tax_rate = tax_rate

#locate login fields and fill out
	def info_fillout_1(self):
		certificate_number_field = driver.find_element_by_id("txtSTCN")
		certificate_number_field.clear()
		certificate_number_field.send_keys(self.certificate_number)

		business_partner_number_field = driver.find_element_by_id('txtBPN')
		business_partner_number_field.clear()
		business_partner_number_field.send_keys(self.business_partner_number)

#accept, continue, next buttons
		login_field = driver.find_element_by_id("btnLogin2")
		login_field.click()
		print('Successful Login')
		login_field = driver.find_element_by_name("btnNext")
		login_field.click()
		print('Next Button Pressed')
		login_field = driver.find_element_by_id("btnSUT")
		login_field.click()
		print('Sales and Use Tax Selected')
		login_field = driver.find_element_by_id('btnfileandpay')
		login_field.click()
		print('File and Pay Selected')
	
# fill out personal info
		contact_name_field = driver.find_element_by_id('zContactName')
		contact_name_field.clear()
		contact_name_field.send_keys(self.manager)

		phone1_field = driver.find_element_by_id('zPhone1')
		phone1_field.clear()
		phone1_field.send_keys(305)
		phone2_field = driver.find_element_by_id('zPhone2')
		phone2_field.clear()
		phone2_field.send_keys(915)
		phone3_field = driver.find_element_by_id('zPhone3')
		phone3_field.clear()
		phone3_field.send_keys(6672)

		email_field = driver.find_element_by_id('zContactEMail')
		email_field.clear()
		email_field.send_keys(self.email)
		print('Personal information Completed')
	


	#date of payment testing
	# @classmethod
	# def pay_date(cls):
	# 	day, month, year = date.today().day, date.today().month, date.today().year
	# 	if date(year, month, 20).isoweekday() == 6:
	# 	    cls.pay_date = 19
	# 	elif date(year, month, 19).isoweekday() == 7:
	# 	    cls.pay_date = 21


	# fill out taxes info
	def taxes_fillout(self):
		gross_sales_field = driver.find_element_by_id('zCColumn1')
		gross_sales_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE,Keys.BACK_SPACE, str(self.gross_sales))

		exempt_field = driver.find_element_by_id('zCColumn2')
		exempt_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE,Keys.BACK_SPACE, str(self.exempt_sales))

		tax_field = driver.find_element_by_id('zCColumn4')
		tax_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, str((self.gross_sales - self.exempt_sales)* self.tax_rate))

		collection_allowance_field = driver.find_element_by_id('zCollectionAllowance')
		collection_allowance_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE,Keys.BACK_SPACE, str(self.collection_allowance))

		surtax_field = driver.find_element_by_id('zTotalSurtaxAmountsCollected')
		surtax_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, str((self.gross_sales - self.exempt_sales)* self.surtax_rate))


	def info_fillout_2 (self):
#accept, continue and next buttons
		login_field = driver.find_element_by_id("Button3")
		login_field.click()
		print('Successful Submital')

		enter_payment_field = driver.find_element_by_id("Button3")
		enter_payment_field.click()
		print('Enter Payment Selected')


#select calendar,date and complete payment info
		calendar_field = driver.find_element_by_id('CheckPayOnly11_BasicDate_Image')
		calendar_field.click()
		date_field = driver.find_element_by_xpath("//a[@class = 'bdpDayItem' and text()= '17']")
		date_field.click()

		routing_field = driver.find_element_by_id('CheckPayOnly11_zBankRoutingNumber')
		routing_field.send_keys(self.routing_number)

		account_field = driver.find_element_by_id('CheckPayOnly11_zBankAccountNumber')
		account_field.send_keys(self.account_number)

		account_field = driver.find_element_by_id('CheckPayOnly11_vBankAccountNumber')
		account_field.send_keys(self.account_number)

		bank_account_type= Select(driver.find_element_by_id('CheckPayOnly11_CheckingSavings'))
		bank_account_type.select_by_visible_text('Checking')
		
		corporate_personal_field = Select(driver.find_element_by_id ('CheckPayOnly11_BankAccountPai'))
		corporate_personal_field.select_by_visible_text('Personal')

		contact_name_field = driver.find_element_by_id('zContactName')
		contact_name_field.send_keys(self.manager)

		phone1_field = driver.find_element_by_id('zPhone1')
		phone1_field.clear()
		phone1_field.send_keys(305)
		phone2_field = driver.find_element_by_id('zPhone2')
		phone2_field.clear()
		phone2_field.send_keys(915)
		phone3_field = driver.find_element_by_id('zPhone3')
		phone3_field.clear()
		phone3_field.send_keys(6672)

		email_field = driver.find_element_by_id('zContactEMail')
		email_field.clear()
		email_field.send_keys(self.email)


		#Next and logout
		submit = driver.find_element_by_id("Button3")
		submit.click()
		print('Successful Submital')
		submit = driver.find_element_by_id("Button3")
		submit.click()
		input('Logout? ')
		logout = driver.find_element_by_xpath("//a[contains(text(), 'Logout')]")
		logout.click()



class Corporation2 (Corporation): 
# fill out taxes info
	def taxes_fillout_2(self):
		gross_sales_field = driver.find_element_by_id('EZzGrossSales')
		gross_sales_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE,Keys.BACK_SPACE, str(self.gross_sales))

		exempt_field = driver.find_element_by_id('EZzExemptSales')
		exempt_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE,Keys.BACK_SPACE, str(self.exempt_sales))

		taxable_field = driver.find_element_by_id('EZzTaxableSales')
		taxable_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, str((self.gross_sales - self.exempt_sales)))

		tax_field = driver.find_element_by_id('EZzTotalAmountTaxCollected')
		tax_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, str((self.gross_sales - self.exempt_sales)* self.tax_rate))

		collection_allowance_field = driver.find_element_by_id('EZzLessCollectionAllowance')
		collection_allowance_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE,Keys.BACK_SPACE, str(self.collection_allowance))

		surtax_field = driver.find_element_by_id('EZzTotalDiscSalesSurtaxCollected')
		surtax_field.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, str((self.gross_sales - self.exempt_sales)* self.surtax_rate))


doral_input_gross_sales = float(input('Doral Gross Sales '))
doral_input_exempt_sales = float(input('Doral Exempt Sales '))
biscayne_input_gross_sales = float(input('Biscayne Gross Sales '))
biscayne_input_exempt_sales = float(input('Biscayne Exempt Sales '))
plantation_input_gross_sales = float(input('Plantation Gross Sales '))
plantation_input_exempt_sales = float(input('Plantation Exempt Sales '))
sample_input_gross_sales = float(input('Sample Gross Sales '))
sample_input_exempt_sales = float(input('Sample Exempt Sales '))
# royal_input_gross_sales = float(input('Royal Gross Sales '))
# royal_input_exempt_sales = float(input('Royal Exempt Sales '))
oaktree_input_gross_sales = float(input('Oaktree Gross Sales '))
oaktree_input_exempt_sales = float(input('Oaktree Exempt Sales '))
hiawassee_input_gross_sales = float(input('Hiawaassee Gross Sales '))
hiawassee_input_exempt_sales = float(input('Hiawaassee Exempt Sales '))
port_richey_input_gross_sales = float(input('Port Richey Gross Sales '))
port_richey_input_exempt_sales = float(input('Port Richey Exempt Sales '))



doral_flex_one_llc = Corporation(2380163071674, 4183044, '066009155', 5111647506, doral_input_gross_sales, doral_input_exempt_sales, 0.01, 0.065 )
total_biscayne_corp = Corporation(2380172137363, 5130704, '267084131', 707570617, biscayne_input_gross_sales, biscayne_input_exempt_sales, 0.01, 0.065)
plantation_one_llc = Corporation(1680162697015, 4108900, '267084131', 708272767, plantation_input_gross_sales, plantation_input_exempt_sales, 0.01, 0.065 )
sample_usa_corp = Corporation2(1680167653324, 4634432, '066004367' , 1954679458, sample_input_gross_sales, sample_input_exempt_sales, 0.01, 0.065 )
yellowbird_international_corp = Corporation(6080184109618, 6328239, '063114030', '0480575265', royal_input_gross_sales, royal_input_exempt_sales, 0.01, 0.065)
iberic_group_corp = Corporation(6080165217174, 4396784, '066009155', 5111767106, oaktree_input_gross_sales, oaktree_input_exempt_sales, 0.01, 0.065)
new_orlando_team_corp = Corporation(5880174253364, 5309753, '063114030', '0480575307', hiawassee_input_gross_sales, hiawassee_input_exempt_sales, 0.005, 0.06)
new_florida_team_corp = Corporation2(6180171856528, 5103229, '066009155', 5111819006, port_richey_input_gross_sales, port_richey_input_exempt_sales, 0.01, 0.065)


doral_flex_one_llc.info_fillout_1()
doral_flex_one_llc.taxes_fillout()
doral_flex_one_llc.info_fillout_2()

total_biscayne_corp.info_fillout_1()
total_biscayne_corp.taxes_fillout()
total_biscayne_corp.info_fillout_2()

plantation_one_llc.info_fillout_1()
plantation_one_llc.taxes_fillout()
plantation_one_llc.info_fillout_2()

sample_usa_corp.info_fillout_1()
sample_usa_corp.taxes_fillout_2()
sample_usa_corp.info_fillout_2()

# yellowbird_international_corp.info_fillout_1()
# yellowbird_international_corp.taxes_fillout()
# yellowbird_international_corp.info_fillout_2()


iberic_group_corp.info_fillout_1()
iberic_group_corp.taxes_fillout()
iberic_group_corp.info_fillout_2()

new_orlando_team_corp.info_fillout_1()
new_orlando_team_corp.taxes_fillout()
new_orlando_team_corp.info_fillout_2()

new_florida_team_corp.info_fillout_1()
new_florida_team_corp.taxes_fillout_2()
new_florida_team_corp.info_fillout_2()














