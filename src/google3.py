import urllib, json
import pprint

#  https://maps.googleapis.com/maps/api/place/textsearch/json?query=123+main+street&key=YOUR_API_KEY
#  f = { 'query' : 'coffee 368 Graham Ave, Brooklyn, NY 11211'}
#  place_id': u'ChIJwbb1LlFZwokR43Wu0vdntIY'
#  f = { 'query' : '368 Graham Ave, Brooklyn, NY 11211'}
#  place_id': u'ChIJu921LlFZwokR6qTjDGUEqxs'
#  f = { 'query' : '368 Graham Ave, Brooklyn, NY 11211', 'type' : 'establishment'}
#  nothing
#  f = { 'query' : '598 Broadway, New York, NY'}
f = { 'query' : 'Asanda Aveda Spa Lounge 598 Broadway, New York, NY'}

URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + urllib.urlencode(f) + "&key=AIzaSyDa2cfifSiwMIDSBRWRENhVej5fbuzfweg"
googleResponse = urllib.urlopen(URL)
jsonResponse = json.loads(googleResponse.read())
pprint.pprint(jsonResponse)
#  print jsonResponse
