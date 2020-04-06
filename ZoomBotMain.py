from selenium import webdriver
import json
import random
import time

url = ""
password = ""

while True:
	names = json.loads(open('names.json').read())
	name = random.choice(names) + " " + random.choice(names)
	driver = webdriver.Chrome()
	driver.get(url)
	pwd = driver.find_element_by_id('inputpasscode')
	pwd.send_keys(password)
	field = driver.find_element_by_id('inputname')
	field.send_keys(name)
	button = driver.find_element_by_id('joinBtn')
	button.click()
	print("{} has joined the meeting!".format(name))
	time.sleep(10)
	button = driver.find_element_by_class_name('footer-button__chat-icon')
	button.click()
	time.sleep(2)
	field = driver.find_element_by_class_name('chat-box__chat-textarea')
	field.send_keys('Hello There,')
	field.send_keys("\n")
	field.send_keys('General Kenobi')
	field.send_keys("\n")
	driver.close()
