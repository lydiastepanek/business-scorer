import urllib, json
from datetime import datetime
from dateutil.relativedelta import relativedelta

def run(business_name):
    business_search_response = search_business(business_name)
    total_hits = business_search_response['query']['searchinfo']['totalhits']
    updated_recently = 0
    if total_hits > 0:
        first_result_title_id = business_search_response['query']['search'][0]['title']
        last_updated = get_last_update_date_of(first_result_title_id)
        updated_recently = check_updated_past_year(last_updated) 
    total_rating = (float(total_hits) / 100) + (.5 * updated_recently)
    return min(total_rating, 1)

def search_business(business_name):
    params = {
                'action': 'query',
                'list': 'search',
                'srsearch': business_name,
                'format': 'json'
             }
    URL = 'https://www.wikidata.org/w/api.php?' + urllib.urlencode(params)
    wikiResponse = urllib.urlopen(URL)
    return json.loads(wikiResponse.read())

def get_last_update_date_of(first_result_title_id):
    params = { 'titles': first_result_title_id, 'action': 'query', 'prop': 'revisions', 'format': 'json' }
    URL = 'https://www.wikidata.org/w/api.php?' + urllib.urlencode(params)
    wiki_response = urllib.urlopen(URL)
    json_response = json.loads(wiki_response.read())['query']['pages']
    return parse_date(json_response)

def parse_date(json_response):
    for count, (page_id, info) in enumerate(json_response.iteritems(), 1):
        return json_response[page_id]['revisions'][0]['timestamp']

def check_updated_past_year(date_string):
    parsed_date = datetime.strptime(date_string[:10], '%Y-%m-%d')
    return datetime.now() - relativedelta(years=1) < parsed_date
