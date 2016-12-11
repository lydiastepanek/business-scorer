import urllib, json

def run(business_name, business_address):
    json_response = get_business_details(business_name, business_address)
    rating = json_response['rating'] if 'rating' in json_response else 0
    business_categories = len(json_response['types']) if 'types' in json_response else 0
    total_rating = (float(rating) / 5) + (.05 * business_categories)
    return min(total_rating, 1)

def get_business_details(business_name, business_address):
    params = { "query" : business_name + " " + business_address }
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + urllib.urlencode(params) + "&key=AIzaSyDa2cfifSiwMIDSBRWRENhVej5fbuzfweg"
    google_response = urllib.urlopen(URL)
    return json.loads(google_response.read())['results'][0]
