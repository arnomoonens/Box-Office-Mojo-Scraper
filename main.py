from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import urlparse

def get_box_office(movie):
	url = "http://www.boxofficemojo.com/movies/?page=weekly&id=" + movie + ".htm"

	req = requests.get(url)
	soup = BeautifulSoup(req.text)
	results = []

	for table in soup.find_all("table", class_="chart-wide"):
		rows = table.find_all("tr")
		for row in rows[1:]: #First "td" has column names
			result = []
			link = row.td.nobr.font.a['href']
			parsed = urlparse.urlparse(link)
			week_of_year = int(urlparse.parse_qs(parsed.query)['wk'][0])

			year = int(table.find_previous_sibling().font.string)
			begin_day = datetime(year, 1, 1) + timedelta(days=(7*(week_of_year-1))+1)
			end_day = begin_day + timedelta(days=7)
			result.append([begin_day, end_day])

			#Add box office
			result.append(int(row.find_all("td")[2].string.replace(",","").replace("$", "")))
			results.append(result)

	return results


if __name__ == "__main__":
	movie = raw_input("Name of movie on Box Office Mojo: ")
	print "Results:", get_box_office(movie)