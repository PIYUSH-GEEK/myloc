import requests
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