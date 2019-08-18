import requests
def locate(i):
	loc = requests.get('https://ipinfo.io').json()
	
	if str(i).isdigit():
		return 'Invalid input. Try a string.'
	else:
		if i == 'ip':
			return loc['ip']
		elif i == 'city' or i == 'capital':
			return loc['city']
		elif i == 'region' or i == 'state':
			return loc['region']
		elif i == 'country':
			return loc['country']
		elif i == 'loc':
			return loc['loc']
		elif i == 'org':
			return loc['org']
		elif i == 'postal' or i == 'pin':
			return loc['postal']
		elif i == 'readme':
			return loc['readme']
