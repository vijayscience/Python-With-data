# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json

# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]

# TODO: The min() function finds the minimum value
# print(min(values))
# print(min(strings))

# TODO: The max() function finds the maximum value
# print(max(values))
# print(max(strings))

# TODO: define a custom "key" function to extract a data field
# print(max(strings,key=len))
# print(min(strings,key=len),end='\n\n\n\n')

# TODO: open the data file and load the JSON
with open("/30DayQuakes.json",
          "r") as datafile:
    data = json.load(datafile)

print(data['metadata']['title'])
print(len(data['features']))


def getmagr(dataitem):
    magnitude = dataitem['properties']['mag']
    if magnitude is None:
        magnitude = 0
    return float(magnitude)


print(min(data['features'], key=getmagr))
print(max(data['features'], key=getmagr))
