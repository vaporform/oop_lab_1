import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
	rows = csv.DictReader(f)
	for r in rows:
		cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
	print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
	temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# NOTE TO SELF:
# 0: CITY
# 1: COUNTRY
# 2: LAT
# 3: LONG
# 4: TEMP
# Well, you can read it as a dict so no problem... :3
print("================================")

print(cities)

print("================================")
print("ALL CITIES IN GERMANY")

germany_list = []
# Print all cities in Germany
for entry in cities:
	if entry['country'] == 'Germany':
		germany_list.append(entry['city'])
print(" ".join(germany_list))

print("================================")
print("ALL CITIES IN SPAIN AND ABOVE 12 DEGREES")
# Print all cities in Spain with a temperature above 12°C

spain_12 = []
for entry in cities:
	if entry['country'] == 'Spain' and float(entry['temperature']) > 12:
		spain_12.append(entry['city'])	

print(" ".join(spain_12))


# Count the number of unique countries
print("================================")
print("UNIQUE COUNTRIES")
c_list = []
for entry in cities:
	if entry['country'] not in c_list:
		c_list.append(entry['country'])
print(len(c_list))

print("================================")
print("AVG TEMPERATURE FOR ALL CITIES IN GERMANY")
# Print the average temperature for all the cities in Germany
a = 0
for entry in cities:
	if entry['country'] == 'Germany':
		a += float(entry['temperature'])
print(a/len(germany_list))

print("================================")
print("MAX TEMP IN ITALY")
# Print the max temperature for all the cities in Italy
italy = []
m_temp = -float('inf')
for entry in cities:
	if entry['country'] == 'Italy':
		if float(entry['temperature']) > m_temp:
			m_temp = float(entry['temperature'])
print(m_temp)
