from bs4 import BeautifulSoup
import requests

#movie = raw_input("Name of movie on Box Office Mojo: ")
movie = "Fast7"
url = "http://www.boxofficemojo.com/movies/?page=weekly&id=" + movie + ".htm"

req = requests.get(url)
soup = BeautifulSoup(req.text)

results_table = soup.find_all("table", class_="chart-wide")[0]

rows = results_table.find_all("tr")
results = []

for row in rows[1:]:
	results.append(list(td.string for td in row.find_all("td")))


print "Results:", results