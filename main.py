from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import urlparse

movie = raw_input("Name of movie on Box Office Mojo: ")
url = "http://www.boxofficemojo.com/movies/?page=weekly&id=" + movie + ".htm"

req = requests.get(url)
soup = BeautifulSoup(req.text)

results_table = soup.find_all("table", class_="chart-wide")[0]

rows = results_table.find_all("tr")
results = []

for row in rows[1:]: #First "td" has column names
	result = []
	link = row.td.nobr.font.a['href']
	parsed = urlparse.urlparse(link)
	week_of_year = int(urlparse.parse_qs(parsed.query)['wk'][0])

	begin_day = datetime(datetime.now().year, 1, 1) + timedelta(days=(7*(week_of_year-1))+1)
	end_day = begin_day + timedelta(days=7)
	result.append([begin_day, end_day])

	#Add box office
	result.append(int(row.find_all("td")[2].string.replace(",","").replace("$", "")))
	results.append(result)


print "Results:", results