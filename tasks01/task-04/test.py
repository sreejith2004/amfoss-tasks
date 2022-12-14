import requests
import csv
r = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=f2fe03")

data = r.json()
title = data.pop('Title')
year = data.pop('Year')
rating= data.pop('imdbRating')
print(title,year,rating,sep=",")
with open('ctgf.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(title)

    # write the data
    writer.writerow(rating)
