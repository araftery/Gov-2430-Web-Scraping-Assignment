from bs4 import BeautifulSoup
import requests


def get_precinct(house_number, street_name, zip_code):
    url = "https://www.votercheck.necvr.ne.gov/VoterView/PollingPlaceSearch.do"
    payload = {
        "action": "Search",
        "fullElectionListLong": "48377_200000,05/10/2016 Primary Election 2016;48371_200000,11/08/2016 General Election 2016;",
        "countyRequired": "false",
        "electionCombo": "0",
        "houseNumber": house_number,
        "streetDirection": "",
        "streetName": street_name,
        "streetType": "",
        "streetSuffix": "",
        "zipcode": zip_code,
        "search": "Search",
    }

    r = requests.post(url, data=payload)
    soup = BeautifulSoup(r.content)
    polling_place = soup.find(id="polling-place")
    return '\n'.join([i.text for i in polling_place.findAll(attrs={'class': "data"})[:-2]])


if __name__ == '__main__':
    house_number = 2701
    street_name = 'Hickory'
    zip_code = 68105
    print "Example: {} {}, Zip Code: {}".format(house_number, street_name, zip_code)
    print get_precinct(house_number, street_name, zip_code)
