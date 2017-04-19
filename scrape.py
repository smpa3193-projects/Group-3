import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "http://aaspeechesdb.oscars.org/results.aspx?AC=NEXT_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2Findex.aspx&TN=aatrans&SN=AUTO"
list_of_rows = []
speeches = ['32354&SE=1901&RN=0&', '32354&SE=1901&RN=1&', '32354&SE=1901&RN=2&']

for speech in speeches:
    response = requests.get(url+speech)
    html = response.content
    soup = BeautifulSoup(html)
    mydivs = soup.findAll("div", { "p class" : "MInormal" })
    for div in mydivs:
    	print mydivs

outfile = open("speeches.csv", "wb")



