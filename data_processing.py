import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data

class DB:
	def __init__(self):
		self.data = []

	def insert(self,Table):
		self.data.append(Table)
	
	def search(self,key):
		for i in self.data:
			if i.name == key: #Found it!
				return i
		

class Table:
	def __init__(self,name,dict_data):
		self.name = name
		self.table = dict_data
		pass
	
	def filter(self,condition):
		temps = []
		for item in self.table:
			if condition(item):
				temps.append(item)
		return Table(f"{self.name}_filtered",temps)

	def aggregate(self, aggregation_function,aggregation_key):
		# aggregation_key: A way to group things
		# aggregation_function: A way to combine things
		# dict_list: your average dict/dataset.
		info = []
		for i in self.table:
			try:
				info.append(float(i[aggregation_key]))
			except:
				info.append(i[aggregation_key])
		com_info = aggregation_function(info)
		return com_info
	
	def join(self,t,key):
		info = self.table.copy()

		new_data = t.table
		for index,original_data in enumerate(info):
			# Check original data
			for j in new_data: # line of new_data
				if original_data[key] == j[key]: # SAME THING!
					info[index] = original_data | j
				
		return Table(f"{self.name}_joined",info)
			
	def __str__(self):
		return f"{self.name}:{self.table}"

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()