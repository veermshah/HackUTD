
import requests
import json

#/ Set your API key and ZPID of a property

api_key = "93a177e2-5c9b-439d-b4c6-1681240fbd32"  # CHANGE WITH YOUR API KEY
property_zpid = "2054866553"
query = "3452 Canyon Lake Dr, Little Elm, TX"


querystring = {
  "api_key": api_key,
  "street":"",
  "city":"Little Elm",
  "state":"TX",
  "zipcode":"75068"
}

#/ API endpoint and default headers
api_url = "https://app.scrapeak.com/v1/scrapers/zillow"


paramP = {"api_key": api_key, "zpid": property_zpid}


#/ Make the API request

def get_property_details_by_address(api_key, address, city, state, zipcode):
    api_url = "https://app.scrapeak.com/v1/scrapers/zillow"
    querystring = {
        "api_key": api_key,
        "street": address,
        "city": city,
        "state": state,
        "zipcode": zipcode
    }
    response = requests.get(api_url + "/zpidByAddress", params=querystring)
    return response.text

def get_property_details_by_zpid(api_key, property_zpid):
    api_url = "https://app.scrapeak.com/v1/scrapers/zillow"
    paramP = {"api_key": api_key, "zpid": property_zpid}
    response = requests.get(api_url + "/property", params=paramP)
    return response.text




