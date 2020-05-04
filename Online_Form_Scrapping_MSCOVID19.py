# This code scrapes the price from an Amazon product webpage

import bs4                                                                                #beautiful soup is used to parse html pages. requests module only downloads the webpage as a text file
import requests                                                                           #to handle the actual downloading

def getCompanyEmail(contactURL):
    res = requests.get(contactURL)
    res.raise_for_status()                                                                # raises exception if teres a problem or returns nothing
    soup = bs4.BeautifulSoup(res.text, 'html.parser')                                     #returns a beautiful soup object from the HTML text stored in the res.text variable. Need to specify HTML as BS also parses other formats
    elems = soup.findAll('label')
    #elems = soup.select(cssSelect)                                                        #Can find HTML elements in the webpage using the select() method for selecting css. Specify the path of the css selector by using inspect element on the browser
    #print(elems)
    #return elems[0].text.strip()                                                          # returns the  first element elen[0] in text format and strips all whitespace charachters
    return elems

def printElems (elems):
    file = open('MicrosoftCOVIDForm.docx', 'a')
    for i in elems:
        print(i.text.strip())
        file.write(i.text.strip())
        file.write('\n\n')
    file.close()

print('Enter the URL of the page you want to scrape')
URL = input()
#print('Enter the CSS selector you want to find on the page')
#cssSelect = input()
                                                                                          #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
elems = getCompanyEmail(URL)
printElems(elems)

