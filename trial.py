from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://academia.srmuniv.ac.in')
browser.switch_to.frame(browser.find_element_by_class_name('siginiframe'))
email_field = browser.find_element_by_id('Email') 
email_field.send_keys('surya_rajendhran@srmuniv.edu.in')
password_field = browser.find_element_by_id('Password')
password_field.send_keys('Googleismaterial')
password_field.submit()
browser.switch_to.default_content()
#browser.get('https://academia.srmuniv.ac.in/#View:My_Attendance')
#browser.close()