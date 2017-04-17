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
    table = soup.find('table')
    
    for row in table.findAll('tr'):
    	list_of_cells = []
    	for cell in row.findAll('td'):
    		if cell.find('a'):
    			link = cell.find('a')['href']
    			list_of_cells.append(link)
    			list_of_cells.append(cell.text)
    		else:
    			list_of_cells.append(cell.text)
    	list_of_rows.append(list_of_cells)

outfile = open("speeches.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["rec", "year", "name", "film", "date", "category", "modified", "transcript"])
writer.writerows(list_of_rows)