
import argparse, os, time
import requests
import urllib.parse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas


def ViewBot(browser):
	while True:
		tweets=[]
		#sleep to make sure everything loads, 
		#time.sleep(random.uniform(3.5,6.9))
		browser.implicitly_wait(100)

		page = BeautifulSoup(browser.page_source,'lxml')
		
		
		all=page.find_all("div",{"class":"js-tweet-text-container"})
		print(len(all))
		
		for a in all:
			tweet = a.find("p")
			tweets.append(tweet.text)
			
		
		d = {'tweet':tweets}
		df = pandas.DataFrame(d)
		df.to_csv('output_file.csv')
		return
		
        

					
def Main():
	parser = argparse.ArgumentParser('lxml')
	parser.add_argument("email",help="twitter email")
	parser.add_argument("password",help="twitter password")
	parser.add_argument("text",help='to search')
	args = parser.parse_args()
	print(args)
	

	chromedriver = r'C:\Users\FFC!\Downloads\chromedriver_win32\chromedriver.exe'
	os.environ["webdriver.chrome.driver"] = chromedriver
	browser = webdriver.Chrome(chromedriver)
	
	browser.get("https://twitter.com/login")
	browser.implicitly_wait(10)

	#login credentials
	emailElement = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
	emailElement.send_keys(args.email)
	passElement  = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
	passElement.send_keys(args.password)
	passElement.submit()
	os.system("cls")
	print("logged in")
	
	#to click on search n send text
	text = browser.find_element_by_id('search-query') 
	text.send_keys(args.text)
	browser.find_element_by_xpath('//*[@id="global-nav-search"]/span/button').click()

	time.sleep(random.uniform(3.5,6.9))
		
	#to click on latest
	browser.find_element_by_link_text('Latest').click() 
	
	
	ViewBot(browser)
	browser.close()

if __name__=="__main__":
	Main()


