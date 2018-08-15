from selenium import webdriver
import random
import time

browser = webdriver.Firefox()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <=10:
	randomPage = random.randint(11,69)
	newUrl = url + str(randomPage)
	browser.get(newUrl)
	
	elements = browser.find_elements_by_css_selector(".content")
	for i in elements:
		entries.append(i.text)
	time.sleep(1)
	pageCount += 1
	
with open("entries.txt","w",encoding="UTF-8") as file:
	
	for i in entries:
		file.write(str(pageCount) + ".\n" + i + "\n")
		file.write(75*("*") +"\n")
		pageCount += 1
		
		
	
browser.close()






