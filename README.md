<!-- Lab Overview - What is this lab all about? -->
# Lab Overview

This lab is about processing data from CSV files using an object-oriented Python program. The goal is to read and parse the data. The example dataset contains city-related data which the script parses and presents the data in a simple table class format. 

<!-- Project Structure - How files are organized, e.g,
oop_lab_1/
│
├── README.md                 # This file
├── Cities.csv                      # The dataset
|---- data_processing.py	  # The analysis code -->

# Project Structure

This repository contains three files:
- README.md
    - This file contains documentation and usage instructions.
- data_processing.py
    - The main Python script that implements CSV loading and table operations.
- Cities.csv
    - A sample dataset containing city, country, coordinates and temperature. For usage with the script.
- Countries.csv
    - A sample dataset containing country, population, European Union status and coastline. For joining with cities dataset.

<!-- Design Overview - Detailed explanation of each class, detailing attributes and key methods -->
# Design Overview

In data_processing.py, there are 2 classes: DataLoader and Table.

## DataLoader

This class is responsible for finding and loading the CSV data from the file system.

- `__init__(self, base_path=None)` When a DataLoader object is created, it figures out the correct directory path to look for data files in.

- `load_csv(self, filename)` A method that handles loading CSV files. Passing the filename and it reads the file, parses it, and returns the entire dataset as a list of dictionaries. Each dictionary in the list represents one row from the CSV.

## Table

This class acts as a container for the data and provides methods to interact with it.

- `__init__(self, name, dict_data)` When a Table object is created, it stores the list of dictionaries in an attribute called `self.table`.

- `filter(self, condition)` This method is used to select specific rows. It takes a condition (which can be either a lambda function or a normal function) as an argument. It loops through all rows and applies the condition to each one, then returns a new Table object containing only the rows that matched the condition.

- `aggregate(self, aggregation_function, aggregation_key)`
This method is used to perform calculations on a specific column. It takes an aggregation_function (eg. a lambda for finding an average) and an aggregation_key (the name of the column) to gather all the values from that column and applies the function to them, returning a single result.

- `join(t, key)` Method for joining two tables on `key` and returns a new `Table` object.

- `__str__(self)` Method for printing the object. Returns in a format of `self.name`:`self.table`.
## DB

This class acts as a datbase for storing tables inside it.

- `__init__(self)` When a database is created, it initilizes an empty list of `self.data`.

- `insert(self,Table)` Method for inserting tables into the database. Appends table to `self.data`.

- `search(self,key)` Method for searching tables inside `self.data` returns the table named `key` object if exists.

<!-- How to test and run your code -->
# Running the test

Before testing, make sure that Python is installed in your system. To do so, run the following
```
python3 --version
```

Assuming that Python is already installed, to test the program, you can download the repository or clone it by running
```
git clone https://github.com/vaporform/oop_lab_1.git
```
Open the folder via prefered IDE or in the terminal
```
cd oop_lab_1
```
Then run the command
```
python3 data_processing.py
```
