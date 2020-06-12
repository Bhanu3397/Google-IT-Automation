#Data Parsing:- If we know the format of the data, we can separate it into understandable parts.
#Writerow for single, and writerows for multiple rows.
#Dictreader converts csv file in to dictionary
#order does not matter,we can use name of the field.
#dictwriter to generate csv file from the content of list of dictionary

#We're working with a list of flowers and some information about each one. 
#The create_file function writes this information to a CSV file. 
#The contents_of_file function reads this file into records and returns the information in a nicely formatted block. \
#Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.
import os
import csv
# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")
# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as flower_types:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(flower_types)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string
#Call the function
print(contents_of_file("flowers.csv"))

import os
import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

#Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary.
#How do you skip over the header record with the field names?

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""
    # Call the function to create the file 
    create_file(filename)

    # Open the file
    with open(filename) as file:
        # Read the rows of the file
        rows = csv.reader(file)
        rows = list(rows)
        # Process each row
        #print(rows)
        for row in rows:
            name, color, ty = row
            # Format the return string for data rows only
            if row != rows[0]:
                return_string += "a {} {} is {}\n".format(color,name, ty)
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))