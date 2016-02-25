from bs4 import BeautifulSoup
import mechanize


def get_precinct(first_name, last_name, dob):
    url = "https://app.mt.gov/cgi-bin/voterinfo/voterinfo.cgi"
    br = mechanize.Browser()
    # spoof user agent
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36')]
    response = br.open(url)

    br.select_form(nr=0)
    br.submit()

    br.select_form(nr=0)

    br.form['first_name'] = first
    br.form['last_name'] = last
    br.form['dob'] = dob

    br.submit()

    soup = BeautifulSoup(br.response().read())

    return '\n'.join(unicode(i.text) for i in soup.findAll('span', {'class':'precinct'})[:-3]).strip('\n').strip(' ').strip('\n')


if __name__ == '__main__':
    first = 'Richard'
    last = 'Hill'
    dob = '12/30/1946'

    print "Example: {} {}, DOB: {}".format(first, last, dob)
    print get_precinct(first, last, dob)
