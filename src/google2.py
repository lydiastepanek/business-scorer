import urllib, json
import pprint

#  one of the place ids from URL2 was 'ChIJOwg_06VPwokRYv534QaPC8g'
#  DETAILS
#  https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJOwg_06VPwokRYv534QaPC8g&key=my_key
#  https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=my_key
#  DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJOwg_06VPwokRYv534QaPC8g&key=AIzaSyDa2cfifSiwMIDSBRWRENhVej5fbuzfweg"
#  URL2 = "http://maps.googleapis.com/maps/api/geocode/json?address=New+York&sensor=false"
#  f = { 'address' : 'Oxford University, uk', 'sensor' : "false"}
#  pprint.pprint(jsonResponse['results'][0]['place_id'])

f = { 'address' : '368 Graham Ave, Brooklyn, NY 11211', 'sensor' : "false"}
URL = "https://maps.googleapis.com/maps/api/geocode/json?" + urllib.urlencode(f)

googleResponse = urllib.urlopen(URL)
jsonResponse = json.loads(googleResponse.read())
place_id = jsonResponse['results'][0]['place_id']

DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + place_id + "&key=AIzaSyDa2cfifSiwMIDSBRWRENhVej5fbuzfweg"
googleResponse = urllib.urlopen(DETAILS_URL)
jsonResponse = json.loads(googleResponse.read())
print pprint.pprint(jsonResponse)
