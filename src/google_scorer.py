import urllib, json

def run(business_name, business_address, google_api_key):
    json_response = get_business_details(business_name, business_address, google_api_key)
    if not json_response['results']:
        return 0
    first_result = json_response['results'][0]
    rating = first_result['rating'] if 'rating' in first_result else 0
    business_categories = len(first_result['types']) if 'types' in first_result else 0
    total_rating = (float(rating) / 5) + (.05 * business_categories)
    return min(total_rating, 1)

def get_business_details(business_name, business_address, google_api_key):
    params = { 'query' : business_name + ' ' + business_address }
    URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' + urllib.urlencode(params) + '&key=' + google_api_key
    google_response = urllib.urlopen(URL)
    return json.loads(google_response.read())
