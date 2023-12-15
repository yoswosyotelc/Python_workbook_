# # # @#$!@#$@!#$upwork### << ///Oct_2023..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$@
# # # !!!!! don't stay at one part for more than 1 weekds...!!!!
# # # !!!!! proceed as you go through by commenting .. for furhter refirinement..



#1.Write a Python program to read an entire text file.Go to the editor

# def file_read(fname):
        # txt = open(fname)
        # print(txt.read())

# file_read('file.txt')


# #2.Write a Python program to read first n lines of a file.Go to the editor

def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
                        
file_read_from_head('file.txt',2)




# #3.Write a Python program to append text to a file and display the text.Go to the editor

# def file_read(fname):
        # from itertools import islice
        # with open(fname, "w") as myfile:
                # myfile.write("Python Exercises\n")
                # myfile.write("Java Exercises")
        # txt = open(fname)
        # print(txt.read())
# file_read('file.txt')

# #4.Write a Python program to read last n lines of a file.Go to the editor


# import sys
# import os   #https://thomas-cokelaer.info/tutorials/python/module_os.html   #https://docs.python.org/3/library/os.path.html#module-os.path
# def file_read_from_tail(fname,lines):
        # bufsize = 8192
        # fsize = os.stat(fname).st_size
        # iter = 0
        # with open(fname) as f:
                # if bufsize > fsize:
                        # bufsize = fsize-1
                        # print(bufsize)
                        # print(fsize)
                        # data = []
                        # while True:
                                # iter +=1
                                # f.seek(fsize-bufsize*iter)
                                # data.extend(f.readlines())
                                # if len(data) >= lines or f.tell() == 0:
                                        # print(''.join(data[-lines:]))
                                        # break

# file_read_from_tail('file.txt',2)





# #5.Write a Python program to read a file line by line and store it into a list.Go to the editor

# def file_read(fname):
        # with open(fname) as f:
                # #Content_list is the list that contains the read lines.     
                # content_list = f.readlines()
                # print(content_list)

# file_read(\'file.txt\')

# #6.Write a Python program to read a file line by line store it into a variable.Go to the editor

# def file_read(fname):
        # with open (fname, "r") as myfile:
                # data=myfile.readlines()
                # print(data)
# file_read('file.txt')

# #7.Write a Python program to read a file line by line store it into an array.Go to the editor

# def file_read(fname):
        # content_array = []
        # with open(fname) as f:
                # #Content_list is the list that contains the read lines.     
                # for line in f:
                        # content_array.append(line)
                # print(content_array)

# file_read('file.txt')

# #8.Write a python program to find the longest words.Go to the editor

# def longest_word(filename):
    # with open(filename, 'r') as infile:
              # words = infile.read().split()
    # max_len = len(max(words, key=len))
    # return [word for word in words if len(word) == max_len]

# print(longest_word('file.txt'))

# #9.Write a Python program to count the number of lines in a text file.Go to the editor

# def file_lengthy(fname):
        # with open(fname) as f:
                # for i, l in enumerate(f):
                        # pass
        # return i + 1
# print("Number of lines in the file: ",file_lengthy("file.txt"))

# #10.Write a Python program to count the frequency of words in a file.Go to the editor

# from collections import Counter
# def word_count(fname):
        # with open(fname) as f:
                # return Counter(f.read().split())

# print("Number of words in the file :",word_count("file.txt"))

# #11.Write a Python program to get the file size of a plain file.Go to the editor

# def file_size(fname):
        # import os
        # statinfo = os.stat(fname)
        # return statinfo.st_size

# print("File size in bytes of a plain file: ",file_size("file.txt"))

# #12.Write a Python program to write a list to a file.Go to the editor

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# with open('file.txt', "w") as myfile:
        # for c in color:
                # myfile.write("%s\n" % c)

# content = open('file.txt')
# print(content.read())

# #13.Write a Python program to copy the contents of a file to another file .Go to the editor

# from shutil import copyfile
# copyfile('test.py', 'abc.py')

# #14.Write a Python program to combine each line from first file with the corresponding line in second file.Go to the editor

# with open('file.txt') as fh1, open('file2.txt') as fh2:
    # for line1, line2 in zip(fh1, fh2):
        # # line1 from abc.txt, line2 from test.txtg
        # print(line1+line2)
		
# #15.Write a Python program to read a random line from a file.Go to the editor

# import random
# def random_line(fname):
    # lines = open(fname).read().splitlines()
    # return random.choice(lines)
# print(random_line('file.txt'))

# #16.Write a Python program to assess if a file is closed or not.Go to the editor

 # f = open('abc.txt','r')
# print(f.closed)
# f.close()
# print(f.closed)

# #17.Write a Python program to remove newline characters from a file.Go to the editor

# def remove_newlines(fname):
    # flist = open(fname).readlines()
    # return [s.rstrip('\n') for s in flist]

# print(remove_newlines("file.txt"))

# #

# # https://www.geeksforgeeks.org/file-handling-python/

# # Example 1: The open command will open the file in the read mode and the for loop will print each line present in the file.


# # a file named "file", will be opened with the reading mode.
# file = open('file.txt', 'r')

# # This will print every line one by one in the file
# for each in file:
	# print (each)


 
# # # Example 2: In this example, we will extract a string that contains all characters in the file then we can use file.read(). 

# # Python code to illustrate read() mode
# file = open("geeks.txt", "r") 
# print (file.read())


# # #Example 3: In this example, we will see how we can read a file using the with statement.


# # Python code to illustrate with()
# with open("geeks.txt") as file: 
	# data = file.read() 

# print(data)

# # Example 4: Another way to read a file is to call a certain number of characters like in the following code the interpreter will read the first five characters of stored data and return it as a string: 

# # Python code to illustrate read() mode character wise
# file = open("geeks.txt", "r")
# print (file.read(5))

# # #

# # Python code to illustrate split() function
# with open("geeks.txt", "r") as file:
	# data = file.readlines()
	# for line in data:
		# word = line.split()
		# print (word)


# # #
# # Python code to create a file
# file = open('geek.txt','w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()

# # #
# # Python code to illustrate with() alongwith write()
# with open("file.txt", "w") as f: 
	# f.write("Hello World!!!")

# # #
# # Python code to illustrate append() mode
# file = open('geek.txt', 'a')
# file.write("This will add this line")
# file.close()

# # #
# import os

# def create_file(filename):
	# try:
		# with open(filename, 'w') as f:
			# f.write('Hello, world!\n')
		# print("File " + filename + " created successfully.")
	# except IOError:
		# print("Error: could not create file " + filename)

# def read_file(filename):
	# try:
		# with open(filename, 'r') as f:
			# contents = f.read()
			# print(contents)
	# except IOError:
		# print("Error: could not read file " + filename)

# def append_file(filename, text):
	# try:
		# with open(filename, 'a') as f:
			# f.write(text)
		# print("Text appended to file " + filename + " successfully.")
	# except IOError:
		# print("Error: could not append to file " + filename)

# def rename_file(filename, new_filename):
	# try:
		# os.rename(filename, new_filename)
		# print("File " + filename + " renamed to " + new_filename + " successfully.")
	# except IOError:
		# print("Error: could not rename file " + filename)

# def delete_file(filename):
	# try:
		# os.remove(filename)
		# print("File " + filename + " deleted successfully.")
	# except IOError:
		# print("Error: could not delete file " + filename)


# if __name__ == '__main__':
	# filename = "example.txt"
	# new_filename = "new_example.txt"

	# create_file(filename)
	# read_file(filename)
	# append_file(filename, "This is some additional text.\n")
	# read_file(filename)
	# rename_file(filename, new_filename)
	# read_file(new_filename)
	# delete_file(new_filename)

# # #This function adds a new inventory entry into a text file. 
# def add_inventory():
	# item_name = item_name_entry.get()
	# item_qty = int(item_qty_entry.get())
	# with open('inventory.txt', 'a') as file:
		# file.write(f'{item_name},{item_qty}\n')
	# item_name_entry.delete(0, tk.END)
	# item_qty_entry.delete(0, tk.END)

# # #This function update_inventory() updates
# def update_inventory():
	# item_name = item_name_entry.get()
	# item_qty = int(item_qty_entry.get())
	# with open('inventory.txt', 'r') as file:
		# inventory_data = file.readlines()
	# with open('inventory.txt', 'w') as file:
		# for line in inventory_data:
			# name, qty = line.strip().split(',')
			# if name == item_name:
				# file.write(f'{name},{item_qty}\n')
			# else:
				# file.write(line)
	# item_name_entry.delete(0, tk.END)
	# item_qty_entry.delete(0, tk.END)

# # #Search and Display the Current Inventory
# def search_inventory():
	# search_name = item_name_entry.get()
	# with open('inventory.txt', 'r') as file:
		# for line in file:
			# name, qty = line.strip().split(',')
			# if name == search_name:
				# result_label.config(text=f'{name} - {qty}')
				# return
	# result_label.config(text=f'{search_name} not found in inventory.')
	# item_name_entry.delete(0, tk.END)


# # #Removing an Item from the Inventory

# def remove_inventory():
	# remove_name = item_name_entry.get()
	# with open('inventory.txt', 'r') as file:
		# inventory_data = file.readlines()
	# with open('inventory.txt', 'w') as file:
		# for line in inventory_data:
			# name, qty = line.strip().split(',')
			# if name != remove_name:
				# file.write(line)
	# item_name_entry.delete(0, tk.END)
	# item_qty_entry.delete(0, tk.END)

# # #Generate a Full Inventory List

# def generate_inventory():
	# with open('inventory.txt', 'r') as file:
		# inventory_data = file.readlines()
	# inventory_text = '\n'.join(inventory_data)
	# result_label.config(text=inventory_text)

# # #Full reversing: In this type of reversing all the content gets reversed. 
# # Open the file in write mode
# f1 = open("output1.txt", "w")

# # Open the input file and get 
# # the content into a variable data
# with open("file.txt", "r") as myfile:
	# data = myfile.read()

# # For Full Reversing we will store the 
# # value of data into new variable data_1 
# # in a reverse order using [start: end: step],
# # where step when passed -1 will reverse 
# # the string
# data_1 = data[::-1]

# # Now we will write the fully reverse 
# # data in the output1 file using 
# # following command
# f1.write(data_1)

# f1.close()


# # #Example 2: Reversing the order of lines. We will use the above text file as input.

# # Open the file in write mode
# f2 = open("output2.txt", "w")


# # Open the input file again and get 
# # the content as list to a variable data
# with open("file.txt", "r") as myfile:
	# data = myfile.readlines()

# # We will just reverse the 
# # array using following code
# data_2 = data[::-1]

# # Now we will write the fully reverse 
# # list in the output2 file using 
# # following command
# f2.writelines(data_2)

# f2.close()

# # #Python – Copy contents of one file to another file
# # open both files 
# with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile: 
	
	# # read content from first file 
	# for line in firstfile: 
			
			# # write content to second file 
			# secondfile.write(line)


# # #Python – Copy contents of one file to another file
# # import module 
# import shutil 

# # use copyfile() 
# shutil.copyfile('first.txt','second.txt')


# # #Python – Copy contents of one file to another file

# # open both files 
# with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile: 
	
	# # read content from first file 
	# for line in firstfile: 
			
			# # append content to second file 
			# secondfile.write(line)

# # #Read content from one file and write it into another file
# # Taking "gfg input file.txt" as input file 
# # in reading mode 
# with open("gfg input file.txt", "r") as input: 
	
	# # Creating "gfg output file.txt" as output 
	# # file in write mode 
	# with open("gfg output file.txt", "w") as output: 
		
		# # Writing each line from input file to 
		# # output file using loop 
		# for line in input: 
			# output.write(line)
# # #Read content from one file and write it into another file
# # Creating an output file in writing mode 
# output_file = open("gfg output file.txt", "w") 

# # Opening input file and scanning each line 
# # from input file and writing in output file 
# with open("gfg input file.txt", "r") as scan: 
	# output_file.write(scan.read()) 

# # Closing the output file 
# output_file.close()
# # #Read content from one file and write it into another file
# # #Read content from one file and write it into another file


# # #Read CSV File into DataFrame

# from pyspark.sql import SparkSession
# # https://pypi.org/project/pyspark/

# spark = SparkSession.builder.appName(
	# 'Read CSV File into DataFrame').getOrCreate()

# authors = spark.read.csv('/content/authors.csv', sep=',',
						# inferSchema=True, header=True)

# df = authors.toPandas()
# df.head()

# # #Read Multiple CSV Files

# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName('Read Multiple CSV Files').getOrCreate()

# path = ['/content/authors.csv',
		# '/content/book_author.csv']

# files = spark.read.csv(path, sep=',',
					# inferSchema=True, header=True)

# df1 = files.toPandas()
# display(df1.head())
# display(df1.tail())

# # #Read All CSV Files in Directory
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName(
	# 'Read All CSV Files in Directory').getOrCreate()

# file2 = spark.read.csv('/content/*.csv', sep=',', 
					# inferSchema=True, header=True)

# df1 = file2.toPandas()
# display(df1.head())
# display(df1.tail())


# # #How to convert PDF file to Excel file using Python?
# # https://pypi.org/project/pdftables/

# # #Python – Read CSV Columns Into List
# # importing module
# from pandas import *

# # reading CSV file
# data = read_csv("company_sales_data.csv")

# # converting column data to list
# month = data['month_number'].tolist()
# fc = data['facecream'].tolist()
# fw = data['facewash'].tolist()
# tp = data['toothpaste'].tolist()
# sh = data['shampoo'].tolist()

# # printing list data
# print('Facecream:', fc)
# print('Facewash:', fw)
# print('Toothpaste:', tp)
# print('Shampoo:', sh)


# # #Method 2: Using csv module

# # importing the module
# import csv

# # open the file in read mode
# filename = open('company_sales_data.csv', 'r')

# # creating dictreader object
# file = csv.DictReader(filename)

# # creating empty lists
# month = []
# totalprofit = []
# totalunit = []

# # iterating over each row and append
# # values to empty list
# for col in file:
	# month.append(col['month_number'])
	# totalprofit.append(col['moisturizer'])
	# totalunit.append(col['total_units'])

# # printing lists
# print('Month:', month)
# print('Moisturizer:', totalprofit)
# print('Total Units:', totalunit)


# # #How to read numbers in CSV files in Python?

# import csv

# # creating a nested list of roll numbers,
# # subjects and marks scored by each roll number
# marks = [
	# ["RollNo", "Maths", "Python"],
	# [1000, 80, 85],
	# [2000, 85, 89],
	# [3000, 82, 90],
	# [4000, 83, 98],
	# [5000, 82, 90]
# ]

# # using the open method with 'w' mode
# # for creating a new csv file 'my_csv' with .csv extension
# with open('my_csv.csv', 'w', newline = '') as file:
	# writer = csv.writer(file, quoting = csv.QUOTE_NONNUMERIC,
						# delimiter = ' ')
	# writer.writerows(marks)

# # opening the 'my_csv' file to read its contents
# with open('my_csv.csv', newline = '') as file:

	# reader = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC,
						# delimiter = ' ')
	
	# # storing all the rows in an output list
	# output = []
	# for row in reader:
		# output.append(row[:])

# for rows in output:
	# print(rows)

# # #Reading numbers in a CSV file with quotes:
# import csv

# # creating a nested list of roll numbers,
# # subjects and marks scored by each roll number
# marks = [
	# ["RollNo", "Maths", "Python"],
	# [1000, 80, 85],
	# [2000, 85, 89],
	# [3000, 82, 90],
	# [4000, 83, 98],
	# [5000, 82, 90]
# ]

# # using the open method with 'w' mode
# # for creating a new csv file 'my_csv' with .csv extension
# with open('my_csv.csv', 'w', newline = '') as file:
	# writer = csv.writer(file, quoting = csv.QUOTE_ALL,
						# delimiter = ' ')
	# writer.writerows(marks)

# # opening the 'my_csv' file to read its contents
# with open('my_csv.csv', newline = '') as file:
	# reader = csv.reader(file, 
						# quoting = csv.QUOTE_ALL,
						# delimiter = ' ')
	
	# # storing all the rows in an output list
	# output = []
	# for row in reader:
		# output.append(row[:])

# for rows in output:
	# print(rows)



# # #Reading a CSV file
# https://www.geeksforgeeks.org/working-csv-files-python/

# https://pypi.org/project/python-csv/

# # importing csv module
# import csv

# # csv file name
# filename = "aapl.csv"

# # initializing the titles and rows list
# fields = []
# rows = []

# # reading csv file
# with open(filename, 'r') as csvfile:
	# # creating a csv reader object
	# csvreader = csv.reader(csvfile)
	
	# # extracting field names through first row
	# fields = next(csvreader)

	# # extracting each data row one by one
	# for row in csvreader:
		# rows.append(row)

	# # get total number of rows
	# print("Total no. of rows: %d"%(csvreader.line_num))

# # printing the field names
# print('Field names are:' + ', '.join(field for field in fields))

# # printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
	# # parsing each column of a row
	# for col in row:
		# print("%10s"%col,end=" "),
	# print('\n')


# # #Writing to a CSV file

# # importing the csv module
# import csv

# # field names
# fields = ['Name', 'Branch', 'Year', 'CGPA']

# # data rows of csv file
# rows = [ ['Nikhil', 'COE', '2', '9.0'],
		# ['Sanchit', 'COE', '2', '9.1'],
		# ['Aditya', 'IT', '2', '9.3'],
		# ['Sagar', 'SE', '1', '9.5'],
		# ['Prateek', 'MCE', '3', '7.8'],
		# ['Sahil', 'EP', '2', '9.1']]

# # name of csv file
# filename = "university_records.csv"

# # writing to csv file
# with open(filename, 'w') as csvfile:
	# # creating a csv writer object
	# csvwriter = csv.writer(csvfile)
	
	# # writing the fields
	# csvwriter.writerow(fields)
	
	# # writing the data rows
	# csvwriter.writerows(rows)

# # #Writing a dictionary to a CSV file
# # importing the csv module
# import csv

# # my data rows as dictionary objects
# mydict =[{'branch': 'COE', 'cgpa': '9.0', 
		# 'name': 'Nikhil', 'year': '2'},
		# {'branch': 'COE', 'cgpa': '9.1', 
		# 'name': 'Sanchit', 'year': '2'},
		# {'branch': 'IT', 'cgpa': '9.3', 
		# 'name': 'Aditya', 'year': '2'},
		# {'branch': 'SE', 'cgpa': '9.5', 
		# 'name': 'Sagar', 'year': '1'},
		# {'branch': 'MCE', 'cgpa': '7.8', 
		# 'name': 'Prateek', 'year': '3'},
		# {'branch': 'EP', 'cgpa': '9.1', 
		# 'name': 'Sahil', 'year': '2'}]

# # field names
# fields = ['name', 'branch', 'year', 'cgpa']

# # name of csv file
# filename = "university_records.csv"

# # writing to csv file
# with open(filename, 'w') as csvfile:
	# # creating a csv dict writer object
	# writer = csv.DictWriter(csvfile, fieldnames = fields)
	
	# # writing headers (field names)
	# writer.writeheader()
	
	# # writing data rows
	# writer.writerows(mydict)


# # #Storing Emails in CSV files
# # importing the csv module
# import csv

# # field names
# fields = ['Name', 'Email']

# # data rows of csv file
# rows = [ ['Nikhil', 'nikhil.gfg@gmail.com'],
		# ['Sanchit', 'sanchit.gfg@gmail.com'],
		# ['Aditya', 'aditya.gfg@gmail.com'],
		# ['Sagar', 'sagar.gfg@gmail.com'],
		# ['Prateek', 'prateek.gfg@gmail.com'],
		# ['Sahil', 'sahil.gfg@gmail.com']]

# # name of csv file
# filename = "email_records.csv"

# # writing to csv file
# with open(filename, 'w') as csvfile:
	# # creating a csv writer object
	# csvwriter = csv.writer(csvfile)
	
	# # writing the fields
	# csvwriter.writerow(fields)
	
	# # writing the data rows
	# csvwriter.writerows(rows)


# #Using fileinput to Loop Over Multiple Files
# File: fileinput-example.py
import fileinput
import sys

files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()



# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #


# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

