import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
	rows = csv.DictReader(f)
	for r in rows:
		cities.append(dict(r))
'''
# Print first 5 cities only
for city in cities[:5]:
	print(city)
'''

def filter(condition, dict_list):
	temps = []
	for item in dict_list:
		if condition(item):
			temps.append(item)
	return temps

def aggregate(aggregation_key, aggregation_function, dict_list):
	# aggregation_key: A way to group things
	# aggregation_function: A way to combine things
	# dict_list: your average dict/dataset.
	info = []
	for i in dict_list:
		try:
			info.append(float(i[aggregation_key]))
		except:
			info.append(i[aggregation_key])
	com_info = aggregation_function(info)
	return com_info

# Print all cities in Germany
filtered_list = filter(lambda x:x['country'] == 'Germany',cities)
print(filtered_list)

# Print all cities in Spain with a temperature above 12°C

'''
Your code here

'''

# Count the number of unique countries

'''
Your code here

'''

# Print the average temperature for all the cities in Germany

'''
Your code here

'''

# Print the max temperature for all the cities in Italy

'''
Your code here

'''
