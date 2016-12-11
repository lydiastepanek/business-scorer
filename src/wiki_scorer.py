import urllib, json
import pprint

def run(business_name):
    business_search_response = search_business(business_name)
    total_hits = business_search_response["query"]["searchinfo"]["totalhits"]
    if total_hits > 0:
        first_result_title_id = business_search_response["query"]["search"][0]["title"]
        last_updated = get_last_update_date_of(first_result_title_id)
    print total_hits
    print last_updated

def search_business(business_name):
    params = {
                "action": "query",
                "list": "search",
                "srsearch": business_name,
                "format": "json"
             }
    URL = "https://www.wikidata.org/w/api.php?" + urllib.urlencode(params)
    wikiResponse = urllib.urlopen(URL)
    return json.loads(wikiResponse.read())

def get_last_update_date_of(first_result_title_id):
    params = { "titles": first_result_title_id, "action": "query", "prop": "revisions", "format": "json" }
    URL = "https://www.wikidata.org/w/api.php?" + urllib.urlencode(params)
    wikiResponse = urllib.urlopen(URL)
    jsonresponse = json.loads(wikiResponse.read())["query"]["pages"]
    for count, (page_id, info) in enumerate(jsonresponse.iteritems(), 1):
        first_result_last_update_date = jsonresponse[page_id]['revisions'][0]['timestamp']
        if count == 1:
            break
    return first_result_last_update_date

#  business_name = 'Asanda Aveda Spa Lounge'
business_name = 'Minneapolis'
run(business_name)
