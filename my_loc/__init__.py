import requests
from bs4 import BeautifulSoup

def locate(i):
	my_loc = requests.get('https://ipinfo.io').json()
	
	if str(i).isdigit():
		return 'Invalid input. Try a string.'
	else:
		if i == 'ip':
			return my_loc['ip']
		elif i == 'city' or i == 'capital':
			return my_loc['city']
		elif i == 'region' or i == 'state':
			return my_loc['region']
		elif i == 'country':
			return my_loc['country']
		elif i == 'loc':
			return my_loc['loc']
		elif i == 'org':
			return my_loc['org']
		elif i == 'postal' or i == 'pin':
			return my_loc['postal']
		elif i == 'readme':
			return my_loc['readme']

def lat(input):
	
	if input == 'Gomia' or input == 'gomia':
		return 'Try \'gumia\' or \'Gumia\''
	
	try:  	
		page_get = requests.get('https://www.latlong.net/search.php?keyword=%s'%input)
		
		page_content = BeautifulSoup(page_get.content, 'html.parser')
			
		tr1 = page_content.find_all('tr')[1]
		
		td1 = tr1 .find_all('td')[0].text
		td2 = tr1 .find_all('td')[1].text
			
		print('Place: ',td1)
		return td2
		
	except IndexError as Error:
		return 'Search for some other place.'
	
def lng(input):
	
	if input == 'Gomia' or input == 'gomia':
		return 'Try \'gumia\' or \'Gumia\''
	
	try:
			
		page_get = requests.get('https://www.latlong.net/search.php?keyword=%s'%input)
		
		page_content = BeautifulSoup(page_get.content, 'html.parser')
		
		tr1 = page_content.find_all('tr')[1]
		
		td1 = tr1 .find_all('td')[0].text
		td3 = tr1 .find_all('td')[2].text
			
		print('Place: ',td1)
		return td3
		
	except IndexError as Error:
		return 'Search for some other place.'

def ltlng(input):
	
	if input == 'Gomia' or input == 'gomia':
		return 'Try \'gumia\' or \'Gumia\''
	
	try:
			
		page_get = requests.get('https://www.latlong.net/search.php?keyword=%s'%input)
		
		page_content = BeautifulSoup(page_get.content, 'html.parser')
		
		tr1 = page_content.find_all('tr')[1]
		
		td1 = tr1 .find_all('td')[0].text
		td2 = tr1 .find_all('td')[1].text
		td3 = tr1 .find_all('td')[2].text
			
		print('Place: ',td1)
		return td2, td3
		
	except IndexError as Error:
		return 'Search for some other place.'
