import requests
import json

#/ Set your API key 

api_key = "93a177e2-5c9b-439d-b4c6-1681240fbd32"

#/ Make the API request
def get_property_details_by_address(city, state, zipcode):
    api_url = "https://app.scrapeak.com/v1/scrapers/zillow/zpidByAddress"
    querystring = {
        "api_key": api_key,
        "street": "",
        "city": city,
        "state": state,
        "zipcode": zipcode
    }
    response = requests.get(api_url, params=querystring)
    return response.text

def get_property_details_by_zpid(api_key, property_zpid):
    api_url = "https://app.scrapeak.com/v1/scrapers/zillow/property"
    paramP = {"api_key": api_key, "zpid": property_zpid}
    response = requests.get(api_url, params=property_zpid)
    return response.text


# print(get_property_details_by_zpid(api_key, 26914709))

