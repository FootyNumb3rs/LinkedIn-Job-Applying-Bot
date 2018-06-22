from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import pprint as pp
import time
from selenium.webdriver.common.keys import Keys


def login(driv): 
	driv.get('https://www.linkedin.com') 
	login_email = driv.find_element_by_class_name('login-email')
	login_password = driv.find_element_by_class_name('login-password')
	login_email.send_keys('EMAIL HERE')
	login_password.send_keys('PASSWORD HERE')
	driv.find_element_by_id('login-submit').click()
	time.sleep(3)
	return (driv)

def apply_to_card(card,temp_driver):
	try:
		temp_driver.switch_to.window(temp_driver.window_handles[1])
		temp_driver.close()
		temp_driver.switch_to.window(temp_driver.window_handles[0])
	except:
		print('No Second Window')

	time.sleep(2)
	card_link = card.find_element_by_class_name('job-card-search__link-wrapper').get_attribute('href')
	temp_driver.get(card_link) 
	apply_part = temp_driver.find_element_by_class_name('jobs-details-top-card__content-container')
	time.sleep(2)

	try:
		apply_part.find_element_by_class_name('jobs-s-apply__button').click()
		time.sleep(2)

		# There's only one 
		easy_apply_pane = temp_driver.find_element_by_id('li-modal-container')

		phone_input = easy_apply_pane.find_element_by_class_name('jobs-apply-form__phone-input ')
		phone_input.send_keys('2016558319')

		edit = easy_apply_pane.find_element_by_class_name('jobs-apply-form__resume-dropdown')
		edit2 = easy_apply_pane.find_element_by_class_name('jobs-apply-form__resume-upload')
		#driver.execute_script("arguments[0].setAttribute('class','jobs-apply-form__resume-upload hidden')",edit2)
		temp_driver.execute_script("arguments[0].setAttribute('class','jobs-apply-form__resume-dropdown  block')",edit)
		time.sleep(3)

		temp_driver.find_element_by_class_name('jobs-apply-form__recent-resume-filename').click()
		temp_driver.find_element_by_class_name('jobs-apply-form__recent-resume-filename').click()
		time.sleep(3)
		easy_apply_pane.find_element_by_class_name('jobs-apply-form__submit-button').click()
	except: 
		print('Non-Standard Easy-Apply')
		pass 


driver = webdriver.Chrome() 
driver = login(driver)
job_name = 'DATA ENGINEER'


# Go to Jobs 
driver.get('https://www.linkedin.com/jobs/search/?keywords={}'.format(job_name.replace(' ','%20')))
time.sleep(3)

# Get Jobs List
jobs_list = driver.find_element_by_class_name('jobs-search-results__list')

# Get Individual Job Cards
job_cards = jobs_list.find_elements_by_class_name('card-list__item')


# Create Driver for Application Process
newDriver = webdriver.Chrome()
newDriver = login(newDriver)

print(len(job_cards))

for card in job_cards:
	apply_to_card(card,newDriver)









