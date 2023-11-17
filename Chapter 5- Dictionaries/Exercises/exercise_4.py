#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.


#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

#* Use a loop to print the name of each river included in the dictionary.

#* Use a loop to print the name of each country included in the dictionary.


rivers = {'The Amazon river': 'South America', 'The Yangtze river': 'China', 'The Mississippi River': 'North America'}


for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())