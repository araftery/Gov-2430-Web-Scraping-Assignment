from bs4 import BeautifulSoup
import mechanize


def get_precinct(house_num, street_name, zip_code):
    url = "https://www.votercheck.necvr.ne.gov/VoterView/PollingPlaceSearch.do"
    br = mechanize.Browser()

    br.set_handle_robots(False)
    response = br.open(url)

    br.select_form('pollingPlaceSearchForm')

    br.form['houseNumber'] = house_num
    br.form['streetName'] = street_name
    br.form['zipcode'] = zip_code

    br.submit()

    soup = BeautifulSoup(br.response().read())


    return '\n'.join(unicode(i.text) for i in soup.findAll('span', {'class':'precinct'})).strip('\n').strip(' ').strip('\n')


if __name__ == '__main__':
    house_number = 2701
    street_name = 'Hickory'
    zip_code = 68105
    print "Example: {} {}, Zip Code: {}".format(house_number, street_name, zip_code)
    print get_precinct(house_number, street_name, zip_code)
