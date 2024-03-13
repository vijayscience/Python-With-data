# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import csv
import datetime
import json

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
def getsig(x):
    sig = x['properties']['sig']
    return 0 if sig is None else sig


significatevent = sorted(data['features'], key=getsig, reverse=True)
significatevent = significatevent[:40]
significatevent.sort(key=lambda x: x['properties']['time'], reverse=True)

header = ["Magnitude", "Place", "Felt Report", "Date", "Link"]
row = []

for event in significatevent:
    thedate = datetime.date.fromtimestamp(int(event["properties"]["time"] / 1000))
    lat = event['geometry']['coordinates'][1]
    lon = event['geometry']['coordinates'][0]
    gmlink = f"https://maps.googleapis.com/maps/api/staticmap?center={lat}&{lon}&size=400x400"
    # gmlink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{lon}"
    # https://maps.googleapis.com/maps/api/staticmap?center=Berkeley,CA&zoom=14&size=400x400&key=YOUR_API_KEY&signature=YOUR_SIGNATURE
    row.append([event['properties']['mag'], event['properties']['place'],
                0 if event['properties']['felt'] is None else event['properties']['felt'],
                thedate, gmlink])
with open('signnificantevent.csv', 'w') as csvfile:
    write = csv.writer(csvfile, delimiter=',')
    write.writerow(header)
    write.writerows(row)
