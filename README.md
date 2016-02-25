# Description of Files
* **montana.py** - Script to scrape precinct location for voters in Montana. Uses [Mechanize](http://wwwsearch.sourceforge.net/mechanize/) to submit the form and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the result.
* **nebraska.py** - Script to scrape precinct location for voters in Nebraska. Uses [Mechanize](http://wwwsearch.sourceforge.net/mechanize/) to submit the form and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the result. Unfortunately, since the HTML on the page seems to be broken, Mechanize has trouble parsing it and throws an exception. As an alternative, I wrote two additional scripts for Nebraska using Requests and Selenium respectively.
* **nebraska_requests.py** - Script to scrape precinct location for voters in Nebraska. Uses [Requests](http://docs.python-requests.org/en/master/) to submit the form by directly posting the relevant data to the page, and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the result. Luckily, this one works.
* **nebraska_selenium.py** - Script to scrape precinct location for voters in Nebraska. Uses [Selenium](http://selenium-python.readthedocs.org/) to submit the form and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the result. This one works too, despite the broken HTML.

# Requirements
To install the required libraries for this repo, execute:
```
pip install beautifulsoup4==4.4.1 requests==2.8.1 selenium==2.52.0 mechanize==0.2.5
```
