from bs4 import BeautifulSoup
from selenium import webdriver


def get_precinct(house_number, street_name, zip_code):
    url = "https://www.votercheck.necvr.ne.gov/VoterView/PollingPlaceSearch.do"
    driver = webdriver.Firefox()
    driver.get(url)

    driver.find_element_by_name("houseNumber").send_keys(house_number)
    driver.find_element_by_name("streetName").send_keys(street_name)
    driver.find_element_by_name("zipcode").send_keys(zip_code)
    driver.find_element_by_name("zipcode").submit()

    soup = BeautifulSoup(driver.page_source)
    polling_place = soup.find(id="polling-place")
    return '\n'.join([i.text for i in polling_place.findAll(attrs={'class': "data"})[:-2]])


if __name__ == '__main__':
    house_number = 2701
    street_name = 'Hickory'
    zip_code = 68105
    print "Example: {} {}, Zip Code: {}".format(house_number, street_name, zip_code)
    print get_precinct(house_number, street_name, zip_code)
