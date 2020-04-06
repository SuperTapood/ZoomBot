from selenium import webdriver
import json
import random
import time

url = "https://us04web.zoom.us/wc/join/455023374?wpk=wcpk41ec98bd4bc26803dd45309a41cb9c3b"
password = "N1hoNFh1SzRkeGJNLzMyU2FEdVdJQT09"

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