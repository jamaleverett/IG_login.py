from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from time import sleep 

browser = webdriver.Chrome()
sleep(2) #inp sleep function but you can change this to your preferred delay for testing 
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = browser.find_element_by_name('username')
username.send.keys('#yourusername)#browser will enter username

password = browser.find_element_by_name('password')
password.send.keys('#yourpassword) #browser will enter password 

submit = browser.find_element_by_tag_name('form')
submit.submit() #browser will submit/login/enter
