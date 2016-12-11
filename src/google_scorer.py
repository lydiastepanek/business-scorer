import urllib, json

def run(business_name, business_address):
    params = { "query" : business_name + " " + business_address }
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + urllib.urlencode(params) + "&key=AIzaSyDa2cfifSiwMIDSBRWRENhVej5fbuzfweg"
    googleResponse = urllib.urlopen(URL)
    jsonResponse = json.loads(googleResponse.read())['results'][0]
    rating = jsonResponse['rating'] if jsonResponse['rating'] else 0
    business_categories = len(jsonResponse['types']) if jsonResponse['types'] else 0
    total_rating = (float(rating) / 5) + (.05 * business_categories)
    return min(total_rating, 1)