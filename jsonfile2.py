import urllib.request, urllib.parse, urllib.error
import json
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
api_key = 42
# https://developers.google.com/maps/documentation/geocoding/intro

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

#print(json.dumps(info, indent=4))
print(info['results'][0]['place_id'])

#output
#Enter location: universidad complutense de madrid
#Retrieving http://py4e-data.dr-chuck.net/json?address=universidad+complutense+de+madrid&key=42
#Retrieved 2088 characters
#ChIJgwhILT8oQg0REXLUZnurSe0
