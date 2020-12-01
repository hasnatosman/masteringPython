cities = ['Mumbai', 'New york', 'paris']
countries = ['India', 'USA', 'France']
"""
z = zip(cities, countries)
for a in z:
    print(a)
"""
d = {city: country for city, country in zip(cities, countries)}
print(d)