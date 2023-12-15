# @#$!@#$@!#$Progress### << ///Dec_2023..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$
# !!!!! don't stay at one part for more than 1 weekds...!!!!
# !!!!! proceed as you go through by commenting .. for furhter refirinement..
# //..//...//..//...//..//..//..//...//
# C:\Users\User\AppData\Local\Programs\Python\Python311
# //..//...//..//...//..//..//..//...//

#rewind using sololearn basic... to proceed.. to >>>14

#your sample dir... C:\Users\User\AppData\Local\Programs\Python\Python311

print("problem 1  Write a Python program to print the following string in a specific format (see the output). ")
print("Spain","madrid",sep = "_") # adds separator.. 

abc='A\nB\tC'

print(len(abc)) # notice tab and new line gets counted..
    
print("Twingle, twingle, littel star,\n \t How I wonder what you are!\n\t\tUp above the world so high,\n\t\tlike a diamondin the sky.\n Twinkle twinkle, little star,\n\t\t How I wonder what you are")
print()


print("problem 2. Write a Python program to get the Python version you are using. ")

import sys #https://docs.python.org/3/library/sys.html

print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
print()


print("problem 3. Write a Python program to display the current date and time.")

import datetime #https://docs.python.org/3/library/datetime.html
now = datetime.datetime.now()
#now = datetime.datetime.today()    # more on date and time python excerciese packages...
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S")) #time.strftime(format[, t])
            #https://docs.python.org/3/library/time.html

print()


print("problem 4. Write a Python program which accepts the radius of a circle from the user and compute the area. ")

from math import pi #https://docs.python.org/3/library/math.html
r = float(input ("Input the radius of the circle : ")) # more on math excerciese.. 

print ("The area of the circle with radius "   +str(r) + " is: " + str(pi * r**2))
print()

print("problem 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.")

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
print()

print("problem 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.")

values = input("Input some comma seprated numbers : ")
# converting to list
list =values.split(",") # this will covert to list
list =[word for word in  values.split(",")]

# converting to tuple
tuple = tuple(list) #so you need to convert to list to get it in tuple...

print('List : ',list)
print('Tuple : ',tuple)

print()

print("problem 7. Write a Python program to accept a filename from the user and print the extension of that.")
 # [coment] for string not containing "dots" . has a problem
filename = input("Input the Filename: ")
f_extns = filename.split(".") # .. just like (Alt +A +E) txt to column Excel
print(f_extns)
# exit()
print ("The extension of the file is : " + repr(f_extns[-1])) # from list access teh laast item.. out put using ..repr()
 # Python repr() Function returns a printable representation of an object in Python.
print(repr.__doc__)
s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))
print(repr(['a', 'b', 'c']))
strObj = 'geeksforgeeks'
print(repr(strObj))
print()

print("problem 8. Write a Python program to display the first and last colors from the following list. ")

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1])) 
print( color_list[0],color_list[-1])
print()

print("problem 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date")

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date) # str formatting table see ??
        #https://docs.python.org/3/library/string.html
print()

print("problem 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. ")

a = int(input("Input an integer : "))
n1 = int( "%s" % a ) # int((str(a) +str(a)))


print(n1)
n2 = int( "%s%s" % (a,a) ) # int((str(a) +str(a)))
# print(n2)


n3 = int( "%s%s%s" % (a,a,a) ) # int((str(a) +str(a)+str(a)))
print(n3)
# exit()

print (n1+n2+n3)

print()

print("problem # 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s)")


print(abs.__doc__) 

print()



print("problem 12. Write a Python program to print the calendar of a given month and year.")
# more on dates_and_time exercise..
import calendar   #https://docs.python.org/3/library/calendar.html
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
print()


print("problem 13. Write a Python program to print the following here document. ")

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
print()



print("problem 14. Write a Python program to calculate number of days between two dates.")

from datetime import date   #date module
f_date = date(2014, 7, 2) # how to get the date of user input..???
l_date = date(2014, 7, 11) # '' just like Excel '=Date(Serial_number)"

delta = l_date - f_date
print(delta.days)
print()


print("problem 15. Write a Python program to get the volume of a sphere with radius 6.")

# from math import pi # 
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)
print()



print("problem 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. ")

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))

print()


# print("problem  17. Write a Python program to test whether a number is within 100 of 1000 or 2000. ")

# # def near_thousand(n):
      # # return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# # print(near_thousand(1000))
# # print(near_thousand(900))
# # print(near_thousand(800))   
# # print(near_thousand(2200))
# print()



# print("problem 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. ")

# # def new_string(str):
  # # if len(str) >= 2 and str[:2] == "Is":
    # # return str
  # # return "Is" + str

# # print(new_string("Array"))
# # print(new_string("IsEmpty"))

# print()


# print("problem 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. ")


# # def new_string(str):
  # # if len(str) >= 2 and str[:2] == "Is":
    # # return str
  # # return "Is" + str

# # print(new_string("Array"))
# # print(new_string("IsEmpty"))
# print()


# print("problem 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. ")


# # def larger_string(str, n):
   # # result = ""
   # # for i in range(n):
      # # result = result + str
   # # return result

# # print(larger_string('abc', 2))
# # print(larger_string('.py', 3))

# print()


# print("problem 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. ")

# # num = int(input("Enter a number: "))
# # mod = num % 2
# # if mod > 0:
    # # print("This is an odd number.")
# # else:
    # # print("This is an even number.")

# print()



# print("problem 22. Write a Python program to count the number 4 in a given list. ")


# # def list_count_4(nums):
  # # count = 0  
  # # for num in nums:
    # # if num == 4:
      # # count = count + 1

  # # return count

# # print(list_count_4([1, 4, 6, 7, 4]))
# # print(list_count_4([1, 4, 6, 4, 7, 4]))
# print()


# print("problem 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. ")

# # def substring_copy(str, n):
  # # flen = 2
  # # if flen > len(str):
    # # flen = len(str)
  # # substr = str[:flen]
  
  # # result = ""
  # # for i in range(n):
    # # result = result + substr
  # # return result
# # print(substring_copy('abcdef', 2))
# # print(substring_copy('p', 3));
# print()



# print("problem 24. Write a Python program to test whether a passed letter is a vowel or not. ")

# # def is_vowel(char):
    # # all_vowels = 'aeiou'
    # # return char in all_vowels
# # print(is_vowel('c'))
# # print(is_vowel('e'))
# print()



# print("problem 25. Write a Python program to check whether a specified value is contained in a group of values. ")

# # def is_group_member(group_data, n):
    # # for value in group_data:
        # # if n == value:
            # # return True
    # # return False
# # print(is_group_member([1, 5, 8, 3], 3))
# # print(is_group_member([5, 8, 3], -1))
# print()



# print("problem 26. Write a Python program to create a histogram from a given list of integers. ")


# # def histogram( items ):
    # # for n in items:
        # # output = ''
        # # times = n
        # # while( times > 0 ):
          # # output += '*'
          # # times = times - 1
        # # print(output)

# # histogram([2, 3, 6, 5])

# print()


# print("problem 27. Write a Python program to concatenate all elements in a list into a string and return it. ")

# # def concatenate_list_data(list):
    # # result= ''
    # # for element in list:
        # # result += str(element)
    # # return result

# # print(concatenate_list_data([1, 5, 12, 2]))

# print()


# print("problem 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. ")

# # numbers = [    
    # # 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    # # 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    # # 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    # # 958,743, 527
    # # ]

# # for x in numbers:
    # # if x == 237:
        # # print(x)
        # # break;
    # # elif x % 2 == 0:
        # # print(x)
		
# print()


# print("problem 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. ")

# # color_list_1 = set(["White", "Black", "Red"])
# # color_list_2 = set(["Red", "Green"])

# # print(color_list_1.difference(color_list_2))
# print()



# print("problem 30. Write a Python program that will accept the base and height of a triangle and compute the area. ")

# # b = int(input("Input the base : "))
# # h = int(input("Input the height : "))

# # area = b*h/2

# # print("area = ", area)

# print()


# print("problem 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. ")


# # def gcd(x, y):
    # # gcd = 1
    
    # # if x % y == 0:
        # # return y
    
    # # for k in range(int(y / 2), 0, -1):
        # # if x % k == 0 and y % k == 0:
            # # gcd = k
            # # break  
    # # return gcd

# # print(gcd(12, 17))
# # print(gcd(4, 6))
# print()


# print("problem 32. Write a Python program to get the least common multiple (LCM) of two positive integers. ")

# # def lcm(x, y):
   # # if x > y:
       # # z = x
   # # else:
       # # z = y

   # # while(True):
       # # if((z % x == 0) and (z % y == 0)):
           # # lcm = z
           # # break
       # # z += 1

   # # return lcm
# # print(lcm(4, 6))
# # print(lcm(15, 17))

# print()


# print("problem 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. ")

# # def sum(x, y, z):
    # # if x == y or y == z or x==z:
        # # sum = 0
    # # else:
        # # sum = x + y + z
    # # return sum

# # print(sum(2, 1, 2))
# # print(sum(3, 2, 2))
# # print(sum(2, 2, 2))
# # print(sum(1, 2, 3))

# print()

# print("problem 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.")
# # def sum(x, y):
    # # sum = x + y
    # # if sum in range(15, 20):
        # # return 20
    # # else:
        # # return sum

# # print(sum(10, 6))
# # print(sum(10, 2))
# # print(sum(10, 12))

# print()


# print("problem 35.Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.")

# # def test_number5(x, y):
    # # if x == y or abs(x-y) == 5 or (x+y) == 5:
        # # return True
    # # else:
        # # return False

# # print(test_number5(7, 2))
# # print(test_number5(3, 2))
# # print(test_number5(2, 2))
# print()



# print("problem 36. Write a Python program to add two objects if both objects are an integer type. ")

# # def add_numbers(a, b):
    # # if not (isinstance(a, int) and isinstance(b, int)):
         # # raise TypeError("Inputs must be integers")
    # # return a + b

# # print(add_numbers(10, 20))

# print()


# print("problem 37. Write a Python program to display your details like name, age, address in three different lines. ")

# # def personal_details():
    # # name, age = "Simon", 19
    # # address = "Bangalore, Karnataka, India"
    # # print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# # personal_details()
# print()



# print("problem 38. Write a Python program to solve (x + y) * (x + y). ")

# # x, y = 4, 3
# # result = x * x + 2 * x * y + y * y
# # print("({} + {}) ^ 2) = {}".format(x, y, result))

# print()


# print("problem 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. ")

# # amt = 10000
# # int = 3.5
# # years = 7

# # future_value  = amt*((1+(0.01*int)) ** years)
# # print(round(future_value,2))

# print()


# print("problem 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). ")

# # import math
# # p1 = [4, 0]
# # p2 = [6, 6]
# # distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

# # print(distance)

# print()


# print("problem 41. Write a Python program to check whether a file exists. ")

# # import os.path
# # open('abc.txt', 'w')
# # print(os.path.isfile('abc.txt'))

# print()


# print("problem 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. ")


# # # For 32 bit it will return 32 and for 64 bit it will return 64
# # import struct
# # print(struct.calcsize("P") * 8)

# print()


# print("problem 43. Write a Python program to get OS name, platform and release information. ")

# # import platform
# # import os
# # print(os.name)
# # print(platform.system())
# # print(platform.release())

# print()


# print("problem 44. Write a Python program to locate Python site-packages. ")

# # import site; 
# # print(site.getsitepackages())

# print()


# print("problem 45. Write a python program to call an external command in Python. ")

# # from subprocess import call
# # call(["ls", "-l"])
# print()


# print("problem 46. Write a python program to get the path and name of the file that is currently executing. ")

# # import os
# # print("Current File Name : ",os.path.realpath(__file__))
# print()



# print("problem 47. Write a Python program to find out the number of CPUs using. ")

# # import multiprocessing
# # print(multiprocessing.cpu_count())
# print()



# print("problem 48. Write a Python program to parse a string to Float or Integer. ")

# # n = "246.2458"
# # print(float(n))
# # print(int(float(n)))
# print()



# print("problem 49. Write a Python program to list all files in a directory in Python. ")

# # from os import listdir
# # from os.path import isfile, join
# # files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# # print(files_list);

# print()


# print("problem 50. Write a Python program to print without newline or space. ")

# # for i in range(0, 10):
    # # print('*', end="")
# # print("\n")
	
# print()


# print("problem 51. Write a Python program to determine profiling of Python programs. ")

# # import cProfile
# # def sum():
    # # print(1+2)
# # cProfile.run('sum()')



# print("problem 52. Write a Python program to print to stderr. ")


# # from __future__ import print_function
# # import sys

# # def eprint(*args, **kwargs):
    # # print(*args, file=sys.stderr, **kwargs)

# # eprint("abc", "efg", "xyz", sep="--")


# print("problem 53. Write a python program to access environment variables. ")

# # import os
# # # Access all environment variables 
# # print('*----------------------------------*')
# # print(os.environ)
# # print('*----------------------------------*')
# # # Access a particular environment variable 
# # print(os.environ['HOME'])
# # print('*----------------------------------*')
# # print(os.environ['PATH'])
# # print('*----------------------------------*')



# print("problem 54. Write a Python program to get the current username ")

# # import getpass
# # print(getpass.getuser())



# print("problem 55. Write a Python to find local IP addresses using Python's stdlib ")

# # import socket
# # print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
# # if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
# # s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
# # socket.SOCK_DGRAM)]][0][1]]) if l][0][0])



# print("problem 56. Write a Python program to get height and width of the console window. ")

# # def terminal_size():
    # # import fcntl, termios, struct
    # # th, tw, hp, wp = struct.unpack('HHHH',
        # # fcntl.ioctl(0, termios.TIOCGWINSZ,
        # # struct.pack('HHHH', 0, 0, 0, 0)))
    # # return tw, th

# # print('Number of columns and Rows: ',terminal_size())



# print("problem 57. Write a program to get execution time for a Python method. ")

# # import time
# # def sum_of_n_numbers(n):
    # # start_time = time.time()
    # # s = 0
    # # for i in range(1,n+1):
        # # s = s + i
    # # end_time = time.time()
    # # return s,end_time-start_time

# # n = 5
# # print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))



# print("problem 58. Write a python program to sum of the first n positive integers. ")

# # n = int(input("Input a number: "))
# # sum_num = (n * (n + 1)) / 2
# # print(sum_num)



# print("problem 59. Write a Python program to convert height (in feet and inches) to centimeters. ")

# # print("Input your height: ")
# # h_ft = int(input("Feet: "))
# # h_inch = int(input("Inches: "))

# # h_inch += h_ft * 12
# # h_cm = round(h_inch * 2.54, 1)

# # print("Your height is : %d cm." % h_cm)



# print("problem 60. Write a Python program to calculate the hypotenuse of a right angled triangle. ")

# # from math import sqrt
# # print("Input lengths of shorter triangle sides:")
# # a = float(input("a: "))
# # b = float(input("b: "))

# # c = sqrt(a**2 + b**2)
# # print("The length of the hypotenuse is", c )



# print("problem 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. ")

# # d_ft = int(input("Input distance in feet: "))
# # d_inches = d_ft * 12
# # d_yards = d_ft / 3.0
# # d_miles = d_ft / 5280.0

# # print("The distance in inches is %i inches." % d_inches)
# # print("The distance in yards is %.2f yards." % d_yards)
# # print("The distance in miles is %.2f miles." % d_miles)



# print("problem 62. Write a Python program to convert all units of time into seconds. ")

# # days = int(input("Input days: ")) * 3600 * 24
# # hours = int(input("Input hours: ")) * 3600
# # minutes = int(input("Input minutes: ")) * 60
# # seconds = int(input("Input seconds: "))

# # time = days + hours + minutes + seconds

# # print("The  amounts of seconds", time)



# print("problem 63. Write a Python program to get an absolute file path. ")

# # def absolute_file_path(path_fname):
        # # import os
        # # return os.path.abspath('path_fname')        
# # print("Absolute file path: ",absolute_file_path("test.txt"))



# print("problem 64. Write a Python program to get file creation and modification date/times. ")

# # import os.path, time
# # print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
# # print("Created: %s" % time.ctime(os.path.getctime("test.txt")))



# print("problem 65. Write a Python program to convert seconds to day, hour, minutes and seconds. ")

# # time = float(input("Input time in seconds: "))
# # day = time // (24 * 3600)
# # time = time % (24 * 3600)
# # hour = time // 3600
# # time %= 3600
# # minutes = time // 60
# # time %= 60
# # seconds = time
# # print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))



# print("problem 66. Write a Python program to calculate body mass index. ")

# # height = float(input("Input your height in meters: "))
# # weight = float(input("Input your weight in kilogram: "))
# # print("Your body mass index is: ", round(weight / (height * height), 2))



# print("problem 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. ")

# # kpa = float(input("Input pressure in in kilopascals> "))
# # psi = kpa / 6.89475729
# # mmhg = kpa * 760 / 101.325
# # atm = kpa / 101.325
# # print("The pressure in pounds per square inch: %.2f psi"  % (psi))
# # print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
# # print("Atmosphere pressure: %.2f atm." % (atm))



# print("problem 68. Write a Python program to calculate the sum of the digits in an integer. ")

# # num = int(input("Input a four digit numbers: "))
# # x  = num //1000
# # x1 = (num - x*1000)//100
# # x2 = (num - x*1000 - x1*100)//10
# # x3 = num - x*1000 - x1*100 - x2*10
# # print("The sum of digits in the number is", x+x1+x2+x3)



# print("problem 69. Write a Python program to sort three integers without using conditional statements and loops. ")

# # x = int(input("Input first number: "))
# # y = int(input("Input second number: "))
# # z = int(input("Input third number: "))

# # a1 = min(x, y, z)
# # a3 = max(x, y, z)
# # a2 = (x + y + z) - a1 - a3
# # print("Numbers in sorted order: ", a1, a2, a3)



# print("problem 70. Write a Python program to sort files by date. ")

# # import glob
# # import os

# # files = glob.glob("*.txt")
# # files.sort(key=os.path.getmtime)
# # print("\n".join(files))



# print("problem 71. Write a Python program to get a directory listing, sorted by creation date. ")

# # from stat import S_ISREG, ST_CTIME, ST_MODE
# # import os, sys, time

# # #Relative or absolute path to the directory
# # dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

# # #all entries in the directory w/ stats
# # data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
# # data = ((os.stat(path), path) for path in data)

# # # regular files, insert creation date
# # data = ((stat[ST_CTIME], path)
           # # for stat, path in data if S_ISREG(stat[ST_MODE]))

# # for cdate, path in sorted(data):
    # # print(time.ctime(cdate), os.path.basename(path))
	


# print("problem 72. Write a Python program to get the details of math module. ")

# # # Imports the math module
# # import math            
# # #Sets everything to a list of math module
# # math_ls = dir(math) # 
# # print(math_ls)



# print("problem 73. Write a Python program to calculate midpoints of a line. ")

# # print('\nCalculate the midpoint of a line :')

# # x1 = float(input('The value of x (the first endpoint) '))
# # y1 = float(input('The value of y (the first endpoint) '))

# # x2 = float(input('The value of x (the first endpoint) '))
# # y2 = float(input('The value of y (the first endpoint) '))

# # x_m_point = (x1 + x2)/2
# # y_m_point = (y1 + y2)/2
# # print();
# # print("The midpoint of line is :")
# # print( "The midpoint's x value is: ",x_m_point)
# # print( "The midpoint's y value is: ",y_m_point)
# # print();




# print("problem 74. Write a Python program to hash a word. ")

# # soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
# # word=input("Input the word be hashed: ")
 
# # word=word.upper()
 
# # coded=word[0]
 
# # for a in word[1:len(word)]:
    # # i=65-ord(a)
    # # coded=coded+str(soundex[i])
# # print() 
# # print("The coded word is: "+coded)
# # print()



# print("problem 75. Write a Python program to get the copyright information. ")

# # import sys
# # print("\nPython Copyright Information")
# # print(sys.copyright)
# # print()



# print("problem 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. ")

# # import sys
# # print("This is the name/path of the script:"),sys.argv[0]
# # print("Number of arguments:",len(sys.argv))
# # print("Argument List:",str(sys.argv))



# print("problem 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. ")

# # import sys
# # print()
# # if sys.byteorder == "little":
    # # #intel, alpha
    # # print("Little-endian platform.")
# # else:
    # # #motorola, sparc
    # # print("Big-endian platform.")
# # print()



# print("problem 78. Write a Python program to find the available built-in modules. ")

# # import sys
# # import textwrap
# # module_name = ', '.join(sorted(sys.builtin_module_names))
# # print(textwrap.fill(module_name, width=70))



# print("problem 79. Write a Python program to get the size of an object in bytes. ")

# # import sys
# # str1 = "one"
# # str2 = "four"
# # str3 = "three"
# # print()
# # print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
# # print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
# # print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
# # print()



# print("problem 80. Write a Python program to get the current value of the recursion limit. ")


# # import sys
# # print()
# # print("Current value of the recursion limit:")
# # print(sys.getrecursionlimit())
# # print()


# print("problem 81. Write a Python program to concatenate N strings. ")


# # list_of_colors = ['Red', 'White', 'Black']  
# # colors = '-'.join(list_of_colors)
# # print()
# # print("All Colors: "+colors)
# # print()


# print("problem 82. Write a Python program to calculate the sum over a container. ")


# # s = sum([10,20,30])
# # print("\nSum of the container: ", s)
# # print()


# print("problem 83. Write a Python program to test whether all numbers of a list is greater than a certain number. ")

# # num = [2,3,4]
# # print()
# # print(all(x > 1 for x in num))
# # print(all(x > 4 for x in num))
# # print()



# print("problem 84. Write a Python program to count the number occurrence of a specific character in a string. ")

# # s = "The quick brown fox jumps over the lazy dog."
# # print()
# # print(s.count("q"))
# # print()



# print("problem 85. Write a Python program to check if a file path is a file or a directory. ")


# # import os  
# # path="abc.txt"  
# # if os.path.isdir(path):  
    # # print("\nIt is a directory")  
# # elif os.path.isfile(path):  
    # # print("\nIt is a normal file")  
# # else:  
    # # print("It is a special file (socket, FIFO, device file)" )
# # print()


# print("problem 86. Write a Python program to get the ASCII value of a character. ")

# # print()
# # print(ord('a'))
# # print(ord('A'))
# # print(ord('1'))
# # print(ord('@'))
# # print()



# print("problem 87. Write a Python program to get the size of a file. ")

# # import os
# # file_size = os.path.getsize("abc.txt")
# # print("\nThe size of abc.txt is :",file_size,"Bytes")
# # print()



# print("problem 88. Given variables x=30 and y=20, write a Python program to print t "30+20=50". ")

# # x = 30
# # y = 20
# # print("\n%d+%d=%d" % (x, y, x+y))
# # print()



# print("problem 89. Write a Python program to perform an action if a condition is true. ")


# # n=1
# # if n == 1:
    # # print("\nFirst day of a month")
# # print()


# print("problem 90. Write a Python program to create a copy of its own source code. ")

# # print()
# # print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
# # print()



# print("problem 91. Write a Python program to swap two variables. ")

# # a = 30
# # b = 20
# # print("\nBefore swap a = %d and b = %d" %(a, b))
# # a, b = b, a
# # print("\nAfter swaping a = %d and b = %d" %(a, b))
# # print()



# print("problem 92. Write a Python program to define a string containing special characters in various forms. ")

# # print()
# # print("\#{'}${\"}@/")
# # print("\#{'}${"'"'"}@/")
# # print(r"""\#{'}${"}@/""")
# # print('\#{\'}${"}@/')
# # print('\#{'"'"'}${"}@/')
# # print(r'''\#{'}${"}@/''')
# # print()



# print("problem 93. Write a Python program to get the identity of an object. ")

# # obj1 = object()
# # obj1_address = id(obj1)
# # print()
# # print(obj1_address)
# # print()



# print("problem 94. Write a Python program to convert a byte string to a list of integers. ")

# # x = b'Abc'
# # print()
# # print(list(x))
# # print()



# print("problem 95. Write a Python program to check if a string is numeric. ")

# # str = 'a123'
# # #str = '123'
# # try:
    # # i = float(str)
# # except (ValueError, TypeError):
    # # print('\nNot numeric')
# # print()
# print("problem 14")



# print("problem 96. Write a Python program to print the current call stack. ")

# # import traceback
# # print()
# # def f1():return abc()
# # def abc():traceback.print_stack()
# # f1()
# # print()



# print("problem 97. Write a Python program to list the special variables used within the language. ")

# # s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# # print()
# # print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
# # print()



# print("problem 98. Write a Python program to get the system time. ")

# # import time
# # print()
# # print(time.ctime())
# # print()



# print("problem 99. Write a Python program to clear the screen or terminal. ")

# # import os
# # import time
# # # for windows
# # # os.system('cls')
# # os.system("ls")
# # time.sleep(2)
# # # Ubuntu version 10.10
# # os.system('clear')



# print("problem 100. Write a Python program to get the name of the host on which the routine is running. ")

# # import socket
# # host_name = socket.gethostname()
# # print()
# # print("Host name:", host_name)
# # print()



# print("problem 101. Write a Python program to access and print a URL's content to the console. ")

# # from http.client import HTTPConnection
# # conn = HTTPConnection("example.com")
# # conn.request("GET", "/")  
# # result = conn.getresponse()
# # # retrieves the entire contents.  
# # contents = result.read() 
# # print(contents)



# print("problem 102. Write a Python program to get system command output. ")

# # import subprocess
# # # file and directory listing
# # returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
# # print("dir command to list file and directory")
# # print(returned_text)



# print("problem 103. Write a Python program to extract the filename from a given path. ")

# # import os
# # print()
# # print(os.path.basename('/users/system1/student1/homework-1.py'))
# # print()



# print("problem 104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. ")

# # import os
# # print("\nEffective group id: ",os.getegid())
# # print("Effective user id: ",os.geteuid())
# # print("Real group id: ",os.getgid())
# # print("List of supplemental group ids: ",os.getgroups())
# # print()



# print("problem 105. Write a Python program to get the users environment. ")

# # import os
# # print()
# # print(os.environ)
# # print()



# print("problem 106. Write a Python program to divide a path on the extension separator. ")

# # import os.path
# # for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    # # print('"%s" :' % path, os.path.splitext(path))
	


# print("problem 107. Write a Python program to retrieve file properties. ")

# # import os.path
# # import time

# # print('File         :', __file__)
# # print('Access time  :', time.ctime(os.path.getatime(__file__)))
# # print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# # print('Change time  :', time.ctime(os.path.getctime(__file__)))
# # print('Size         :', os.path.getsize(__file__))



# print("problem 108. Write a Python program to find path refers to a file or directory when you encounter a path name. ")

# # import os.path

# # for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    # # print('File        :', file)
    # # print('Absolute    :', os.path.isabs(file))
    # # print('Is File?    :', os.path.isfile(file))
    # # print('Is Dir?     :', os.path.isdir(file))
    # # print('Is Link?    :', os.path.islink(file))
    # # print('Exists?     :', os.path.exists(file))
    # # print('Link Exists?:', os.path.lexists(file))
	


# print("problem 109. Write a Python program to check if a number is positive, negative or zero. ")

# # num = float(input("Input a number: "))
# # if num > 0:
   # # print("It is positive number")
# # elif num == 0:
   # # print("It is Zero")
# # else:
   # # print("It is a negative number")
   


# print("problem 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. ")

# # num_list = [45, 55, 60, 37, 100, 105, 220]
# # # use anonymous function to filter
# # result = list(filter(lambda x: (x % 15 == 0), num_list))
# # print("Numbers divisible by 15 are",result)



# print("problem 111. Write a Python program to make file lists from current directory using a wildcard. ")

# # import glob
# # file_list = glob.glob('*.*')
# # print(file_list)



# print("problem 112. Write a Python program to remove the first item from a specified list. ")

# # color = ["Red", "Black", "Green", "White", "Orange"]
# # print("\nOriginal Color: ",color)
# # del color[0]
# # print("After removing the first color: ",color)
# # print()



# print("problem 113. Write a Python program to input a number, if it is not a number generate an error message. ")

# # while True:
    # # try:
        # # a = int(input("Input a number: "))
        # # break
    # # except ValueError:
        # # print("\nThis is not a number. Try again...")
        # # print()
		


# print("problem 114. Write a Python program to filter the positive numbers from a list. ")

# # nums = [34, 1, 0, -23]
# # print("Original numbers in the list: ",nums)
# # new_nums = list(filter(lambda x: x >0, nums))
# # print("Positive numbers in the list: ",new_nums)



# print("problem 115. Write a Python program to compute the product of a list of integers (without using for loop). ")

# # from functools import reduce
# # nums = [10, 20, 30,]
# # nums_product = reduce( (lambda x, y: x * y), nums)
# # print("Product of the numbers : ",nums_product)




# print("problem 116. Write a Python program to print Unicode characters. ")

# # str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
# # print()
# # print(str)
# # print()


# print("problem 117. Write a Python program to prove that two string variables of same value point same memory location. ")

# # str1 = "Python"
# # str2 = "Python"
 
# # print("\nMemory location of str1 =", hex(id(str1)))
# # print("Memory location of str2 =", hex(id(str2)))
# # print()



# print("problem 118. Write a Python program to create a bytearray from a list. ")

# # print()
# # nums = [10, 20, 56, 35, 17, 99]
# # # Create bytearray from list of integers.
# # values = bytearray(nums)
# # for x in values: print(x)
# # print()




# print("problem 119. Write a Python program to display a floating number in specified numbers. ")

# # order_amt = 212.374
# # print('\nThe total order amount comes to %f' % order_amt)
# # print('The total order amount comes to %.2f' % order_amt)
# # print()



# print("problem 120. Write a Python program to format a specified string to limit the number of characters to 6. ")

# # str_num = "1234567890"
# # print()
# # print('%.6s' % str_num)
# # print()



# print("problem 121. Write a Python program to determine if variable is defined or not. ")

# # try:
  # # x = 1
# # except NameError:
  # # print("Variable is not defined....!")
# # else:
  # # print("Variable is defined.")
# # try:
  # # y
# # except NameError:
  # # print("Variable is not defined....!")
# # else:
  # # print("Variable is defined.")
  


# print("problem 122. Write a Python program to empty a variable without destroying it. ")

# # n = 20
# # d = {"x":200}
# # l = [1,3,5]
# # t= (5,7,8)
# # print(type(n)())
# # print(type(d)())
# # print(type(l)())
# # print(type(t)()) 



# print("problem 123. Write a Python program to determine the largest and smallest integers, longs, floats. ")

# # import sys
# # print("Float value information: ",sys.float_info)
# # print("\nInteger value information: ",sys.int_info)
# # print("\nMaximum size of an integer: ",sys.maxsize) 



# print("problem 124. Write a Python program to check if multiple variables have the same value. ")

# # x = 20
# # y = 20
# # z = 20
# # if x == y == z == 20:
    # # print("All variables have same value!")  
	
# # # #125. Write a Python program to sum of all counts in a collections? 
# print("problem 14")

# # import collections
# # num = [2,2,4,6,6,8,6,10,4]
# # print(sum(collections.Counter(num).values()))



# print("problem 126. Write a Python program to get the actual module object for a given object. ")

# # from inspect import getmodule
# # from math import sqrt
# # print(getmodule(sqrt))



# print("problem 127. Write a Python program to check if an integer fits in 64 bits. ")

# # int_val = 30
# # if int_val.bit_length() <= 63:
    # # print((-2 ** 63).bit_length())
    # # print((2 ** 63).bit_length())
	


# print("problem 128. Write a Python program to check if lowercase letters exist in a string. ")

# # str1 = 'A8238i823acdeOUEI'
# # print(any(c.islower() for c in str1))



# print("problem 129. Write a Python program to add leading zeroes to a string. ")

# # str1='122.22'
# # print("Original String: ",str1)
# # str1 = str1.ljust(8, '0')
# # print(str1)
# # str1 = str1.ljust(10, '0')
# # print(str1)



# print("problem 130. Write a Python program to use double quotes to display strings. ")

# # import json
# # print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))



# print("problem 131. Write a Python program to split a variable length string into variables. ")

# # var_list = ['a', 'b', 'c']
# # x, y, z = (var_list + [None] * 3)[:3]
# # print(x, y, z)
# # var_list = [100, 20.25]
# # x, y = (var_list + [None] * 2)[:2]
# # print(x, y)



# print("problem 132. Write a Python program to list home directory without absolute path. ")

# # import os.path
# # print(os.path.expanduser('~'))



# print("problem 133. Write a Python program to calculate the time runs (difference between start and current time) of a program. ")

# # from timeit import default_timer
# # def timer(n):
    # # start = default_timer()
    # # # some code here
    # # for row in range(0,n):
        # # print(row)
    # # print(default_timer() - start)

# # timer(5)
# # timer(15)



# print("problem 134. Write a Python program to input two integers in a single line. ")

# # print("Input the value of x & y")
# # x, y = map(int, input().split())
# # print("The value of x & y are: ",x,y)



# print("problem 135. Write a Python program to print a variable without spaces between values. ")

# # x = 30
# # print('Value of x is "{}"'.format(x))



# print("problem 136. Write a Python program to find files and skip directories of a given directory. ")

# # import os
# # print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])



# print("problem 137. Write a Python program to extract single key-value pair of a dictionary in variables. ")

# # d = {'Red': 'Green'}
# # (c1, c2), = d.items()
# # print(c1)
# # print(c2)



# print("problem 138. Write a Python program to convert true to 1 and false to 0. ")

# # x = 'true'
# # x = int(x == 'true')
# # print(x)
# # x = 'abcd'
# # x = int(x == 'true')
# # print(x)



# print("problem 139. Write a Python program to valid a IP address. ")

# # import socket
# # addr = '127.0.0.2561'
# # try:
    # # socket.inet_aton(addr)
    # # print("Valid IP")
# # except socket.error:
    # # print("Invalid IP")
	


# print("problem 140. Write a Python program to convert an integer to binary keep leading zeros. ")

# # x = 12
# # print(format(x, '08b'))
# # print(format(x, '010b'))



# print("problem 141. Write a python program to convert decimal to hexadecimal. ")

# # x = 30
# # print(format(x, '02x'))
# # x = 4
# # print(format(x, '02x'))



# print("problem 142. Write a Python program to find the operating system name, platform and platform release date. ")

# # import os, platform
# # print("Operating system name:")
# # print(os.name)
# # print("Platform name:")
# # print(platform.system())
# # print("Platform release:")
# # print(platform.release())



# print("problem 143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system. ")

# # import struct
# # print(struct.calcsize("P") * 8)



# print("problem 144. Write a Python program to check if variable is of integer or string. ")

# # print(isinstance(25,int) or isinstance(25,str))
# # print(isinstance([25],int) or isinstance([25],str))
# # print(isinstance("25",int) or isinstance("25",str))



# print("problem 145. Write a Python program to test if a variable is a list or tuple or a set. ")

# # #x = ['a', 'b', 'c', 'd']
# # #x = {'a', 'b', 'c', 'd'}
# # x = ('tuple', False, 3.2, 1)
# # if type(x) is list:
    # # print('x is a list')
# # elif type(x) is set:
    # # print('x is a set')
# # elif type(x) is tuple:
    # # print('x is a tuple')    
# # else:
    # # print('Neither a list or a set or a tuple.')



# print("problem 146. Write a Python program to find the location of Python module sources. ")

# # import sys
# # print("\nList of directories in sys module:")
# # print(sys.path)
# # print("\nList of directories in os module:")
# # import os
# # print(os.path)



# print("problem 147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. ")

# # def multiple(m, n):
	# # return True if m % n == 0 else False

# # print(multiple(20, 5))
# # print(multiple(7, 2))



# print("problem 148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. ")

# # def max_min(data):
  # # l = data[0]
  # # s = data[0]
  # # for num in data:
    # # if num> l:
      # # l = num
    # # elif num< s:
        # # s = num
  # # return l, s

# # print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))



# print("problem 149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. ")


# # def sum_of_cubes(n):
  # # n -= 1
  # # total = 0
  # # while n > 0:
    # # total += n * n * n
    # # n -= 1
  # # return total
# # print("Sum of cubes: ",sum_of_cubes(3))


# print("problem 150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values. ")

# # def odd_product(nums):
  # # for i in range(len(nums)):
    # # for j in range(len(nums)):
      # # if  i != j:
        # # product = nums[i] * nums[j]
        # # if product & 1:
          # # return True
          # # return False
          
# # dt1 = [2, 4, 6, 8]
# # dt2 = [1, 6, 4, 7, 8]
# # print(dt1, odd_product(dt1));
# # print(dt2, odd_product(dt2));



#print(problem 151 open URL from chrome")

# # import webbrowser
# # url = 'https://www.w3resource.com/python-exercises/python-basic-exercises.php'
# # webbrowser.register('chrome',
		# # None,
		# # webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
# # webbrowser.get('chrome').open(url)







# # #1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other. 
# print("problem 1")

# # def test_distinct(data):
  # # if len(data) == len(set(data)):
    # # return True
  # # else:
    # # return False;
# # print(test_distinct([1,5,7,9]))
# # print(test_distinct([2,4,5,5,7,9]))

# # #2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once. 
# print("problem 1")

# # import random
# # char_list = ['a','e','i','o','u']
# # random.shuffle(char_list)
# # print(''.join(char_list))

# # #3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
# print("problem 1")

# # def remove_nums(int_list):
  # # #list starts with 0 index
  # # position = 3 - 1 
  # # idx = 0
  # # len_list = (len(int_list))
  # # while len_list>0:
    # # idx = (position+idx)%len_list
    # # print(int_list.pop(idx))
    # # len_list -= 1
# # nums = [10,20,30,40,50,60,70,80,90]
# # remove_nums(nums)

# # #4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers. 
# print("problem 1")

# # def three_sum(nums):
  # # result = []
  # # nums.sort()
  # # for i in range(len(nums)-2):
    # # if i> 0 and nums[i] == nums[i-1]:
      # # continue
    # # l, r = i+1, len(nums)-1
    # # while l < r:
      # # s = nums[i] + nums[l] + nums[r]
      # # if s > 0:
        # # r -= 1
      # # elif s < 0:
          # # l += 1
      # # else:
        # # # found three sum
        # # result.append((nums[i], nums[l], nums[r]))
        # # # remove duplicates
        # # while l < r and nums[l] == nums[l+1]:
          # # l+=1
          # # while l < r and nums[r] == nums[r-1]:
            # # r -= 1
            # # l += 1
            # # r -= 1
          # # return result

# # x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
# # print(three_sum(x))

# # #5. Write a Python program to create the combinations of 3 digit combo. 
# print("problem 1")

# # numbers = []
# # for num in range(1000):
  # # num=str(num).zfill(3)
# # print(num)
# # numbers.append(num)


# # #6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies. 
# print("problem 1")

# # string_words = '''United States Declaration of Independence
# # From Wikipedia, the free encyclopedia
# # The United States Declaration of Independence is the statement
# # adopted by the Second Continental Congress meeting at the Pennsylvania State
# # House (Independence Hall) in Philadelphia on July 4, 1776, which announced
# # that the thirteen American colonies, then at war with the Kingdom of Great
# # Britain, regarded themselves as thirteen independent sovereign states, no longer
# # under British rule. These states would found a new nation – the United States of
# # America. John Adams was a leader in pushing for independence, which was passed
# # on July 2 with no opposing vote cast. A committee of five had already drafted the
# # formal declaration, to be ready when Congress voted on independence.

# # John Adams persuaded the committee to select Thomas Jefferson to compose the original
# # draft of the document, which Congress would edit to produce the final version.
# # The Declaration was ultimately a formal explanation of why Congress had voted on July
# # 2 to declare independence from Great Britain, more than a year after the outbreak of
# # the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
# # Second Day of July 1776, will be the most memorable Epocha, in the History of America."
# # But Independence Day is actually celebrated on July 4, the date that the Declaration of
# # Independence was approved.

# # After ratifying the text on July 4, Congress issued the Declaration of Independence in
# # several forms. It was initially published as the printed Dunlap broadside that was widely
# # distributed and read to the public. The source copy used for this printing has been lost,
# # and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
# # with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
# # by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
# # is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
# # popularly regarded as the official document. This engrossed copy was ordered by Congress on
# # July 19 and signed primarily on August 2.

# # The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
# # The Declaration justified the independence of the United States by listing colonial grievances against
# # King George III, and by asserting certain natural and legal rights, including a right of revolution.
# # Having served its original purpose in announcing independence, references to the text of the
# # Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
# # (as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
# # on human rights, particularly its second sentence:

# # We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
# # Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

# # This has been called "one of the best-known sentences in the English language", containing "the most potent
# # and consequential words in American history". The passage came to represent a moral standard to which
# # the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
# # Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
# # through which the United States Constitution should be interpreted.

# # The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
# # being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
# # (modern-day Belgium). It also served as the primary model for numerous declarations of independence across
# # Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
# # 19th century.'''

# # word_list = string_words.split()

# # word_freq = [word_list.count(n) for n in word_list]

# # print("String:\n {} \n".format(string_words))
# # print("List:\n {} \n".format(str(word_list)))
# # print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))



# # #7. Write a Python program to count the number of each character of a given text of a text file. 
# print("problem 1")


# # import collections
# # import pprint
# # file_input = input('File Name: ')
# # with open(file_input, 'r') as info:
  # # count = collections.Counter(info.read().upper())
  # # value = pprint.pformat(count)
# # print(value)


# # #8. Write a Python program to get the top stories from Google news. 
# print("problem 1")

# # import bs4
# # from bs4 import BeautifulSoup as soup
# # from urllib.request import urlopen

# # news_url="https://news.google.com/news/rss"
# # Client=urlopen(news_url)
# # xml_page=Client.read()
# # Client.close()

# # soup_page=soup(xml_page,"xml")
# # news_list=soup_page.findAll("item")
# # # Print news title, url and publish date
# # for news in news_list:
  # # print(news.title.text)
  # # print(news.link.text)
  # # print(news.pubDate.text)
  # # print("-"*60)

# # #9. Write a Python program to get a list of locally installed Python modules. 
# print("problem 1")

# # import pkg_resources
# # installed_packages = pkg_resources.working_set
# # installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     # # for i in installed_packages])
# # for m in installed_packages_list:
    # # print(m)


# # #10. Write a Python program to display some information about the OS where the script is running. 
# print("problem 1")

# # import platform as pl

# # os_profile = [
        # # 'architecture',
        # # 'linux_distribution',
        # # 'mac_ver',
        # # 'machine',
        # # 'node',
        # # 'platform',
        # # 'processor',
        # # 'python_build',
        # # 'python_compiler',
        # # 'python_version',
        # # 'release',
        # # 'system',
        # # 'uname',
        # # 'version',
    # # ]
# # for key in os_profile:
  # # if hasattr(pl, key):
    # # print(key +  ": " + str(getattr(pl, key)()))

# # #11. Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations. 
# print("problem 1")

# # import itertools
# # from functools import partial
# # X = [10, 20, 20, 20]
# # Y = [10, 20, 30, 40]
# # Z = [10, 30, 40, 20]
# # T = 70

# # def check_sum_array(N, *nums):
  # # if sum(x for x in nums) == N:
    # # return (True, nums)
  # # else:
      # # return (False, nums)
# # pro = itertools.product(X,Y,Z)
# # func = partial(check_sum_array, T)
# # sums = list(itertools.starmap(func, pro))

# # result = set()
# # for s in sums:
    # # if s[0] == True and s[1] not in result:
      # # result.add(s[1])
      # # print(result)

# # #12. Write a Python program to create all possible permutations from a given collection of distinct numbers.
# print("problem 1")

# # def permute(nums):
  # # result_perms = [[]]
  # # for n in nums:
    # # new_perms = []
    # # for perm in result_perms:
      # # for i in range(len(perm)+1):
        # # new_perms.append(perm[:i] + [n] + perm[i:])
        # # result_perms = new_perms
  # # return result_perms

# # my_nums = [1,2,3]
# # print("Original Cofllection: ",my_nums)
# # print("Collection of distinct numbers:\n",permute(my_nums))

# # #13. Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string. 
# print("problem 1")

# # def letter_combinations(digits):
    # # if digits == "":
        # # return []
    # # string_maps = {
        # # "1": "abc",
        # # "2": "def",
        # # "3": "ghi",
        # # "4": "jkl",
        # # "5": "mno",
        # # "6": "pqrs",
        # # "7": "tuv",
        # # "8": "wxy",
        # # "9": "z"
    # # }
    # # result = [""]
    # # for num in digits:
        # # temp = []
        # # for an in result:
            # # for char in string_maps[num]:
                # # temp.append(an + char)
        # # result = temp
    # # return result

# # digit_string = "47"
# # print(letter_combinations(digit_string))
# # digit_string = "29"
# # print(letter_combinations(digit_string))

# # #14. Write a Python program to add two positive integers without using the '+' operator. 
# print("problem 1")

# # def add_without_plus_operator(a, b):
    # # while b != 0:
        # # data = a & b
        # # a = a ^ b
        # # b = data << 1
    # # return a
# # print(add_without_plus_operator(2, 10))
# # print(add_without_plus_operator(-20, 10))
# # print(add_without_plus_operator(-10, -20))

# # #15. Write a Python program to check the priority of the four operators (+, -, *, /). 
# print("problem 1")

# # from collections import deque
# # import re

# # __operators__ = "+-/*"
# # __parenthesis__ = "()"
# # __priority__ = {
    # # '+': 0,
    # # '-': 0,
    # # '*': 1,
    # # '/': 1,
# # }

# # def test_higher_priority(operator1, operator2):
    # # return __priority__[operator1] >= __priority__[operator2]

# # print(test_higher_priority('*','-'))
# # print(test_higher_priority('+','-'))
# # print(test_higher_priority('+','*'))
# # print(test_higher_priority('+','/'))
# # print(test_higher_priority('*','/'))

# # #16. Write a Python program to get the third side of right angled triangle from two given sides. 
# print("problem 1")

# # def pythagoras(opposite_side,adjacent_side,hypotenuse):
        # # if opposite_side == str("x"):
            # # return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        # # elif adjacent_side == str("x"):
            # # return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        # # elif hypotenuse == str("x"):
            # # return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        # # else:
            # # return "You know the answer!"
    
# # print(pythagoras(3,4,'x'))
# # print(pythagoras(3,'x',5))
# # print(pythagoras('x',4,5))
# # print(pythagoras(3,4,5))

# # #17. Write a Python program to get all strobogrammatic numbers that are of length n. 
# print("problem 1")

# # #https://github.com/keon/algorithms/blob/master/math/generate_strobogrammtic.py
# # def gen_strobogrammatic(n):
    # # """
    # # :type n: int
    # # :rtype: List[str]
    # # """
    # # result = helper(n, n)
    # # return result


# # def helper(n, length):
    # # if n == 0:
        # # return [""]
    # # if n == 1:
        # # return ["1", "0", "8"]
    # # middles = helper(n-2, length)
    # # result = []
    # # for middle in middles:
        # # if n != length:
            # # result.append("0" + middle + "0")
        # # result.append("8" + middle + "8")
        # # result.append("1" + middle + "1")
        # # result.append("9" + middle + "6")
        # # result.append("6" + middle + "9")
    # # return result

# # print("n = 2: \n",gen_strobogrammatic(2))
# # print("n = 3: \n",gen_strobogrammatic(3))
# # print("n = 4: \n",gen_strobogrammatic(4))

# # #18. Write a Python program to find the median among three given numbers. 
# print("problem 1")

# # x = input("Input the first number")
# # y = input("Input the second number")
# # z = input("Input the third number")
# # print("Median of the above three numbers -")

# # if y < x and x < z:
    # # print(x)
# # elif z < x and x < y:
    # # print(x)
    
# # elif z < y and y < x:
    # # print(y)
# # elif x < y and y < z:
    # # print(y)
    
# # elif y < z and z < x:
    # # print(z)    
# # elif x < z and z < y:
    # # print(z)

# # #19. Write a Python program to find the value of n where n degrees of number 2 are written sequentially in a line without spaces. 
# print("problem 1")

# # def ndegrees(num):
  # # ans = True
  # # n, tempn, i = 2, 2, 2
  # # while ans:
    # # if str(tempn) in num:
      # # i += 1
      # # tempn = pow(n, i)
    # # else:
      # # ans = False
  # # return i-1;
# # print(ndegrees("2481632"))
# # print(ndegrees("248163264"))

# # #20. Write a Python program to find the number of zeros at the end of a factorial of a given positive number. 
# print("problem 1")

# # def factendzero(n):
  # # x = n // 5
  # # y = x 
  # # while x > 0:
    # # x /= 5
    # # y += int(x)
  # # return y
       
# # print(factendzero(5))
# # print(factendzero(12))
# # print(factendzero(100))

# # #21. Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against an given amount. 
# print("problem 1")

# # def no_notes(a):
  # # Q = [500, 200, 100, 50, 20, 10]
  # # x = 0
  # # for i in range(6):
    # # q = Q[i]
    # # x += int(a / q)
    # # a = int(a % q)
  # # if a > 0:
    # # x = -1
  # # return x
# # print(no_notes(880))
# # print(no_notes(1000))


# # #22. Write a Python program to create a sequence where the first four members of the sequence are equal to one, and each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence. 
# print("problem 1")

# # def new_seq(n):
    # # if n==1 or n==2 or n==3 or n==4:
        # # return 1
    # # return new_seq(n-1) + new_seq(n-2) + new_seq(n-3) + new_seq(n-4)
# # print(new_seq(5))
# # print(new_seq(6))
# # print(new_seq(7))


# # #23. Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive. 
# print("problem 1")

# # def repeat_times(n):
  # # s = 0
  # # n_str = str(n)
  # # while (n > 0):
    # # n -= sum([int(i) for i in list(n_str)])
    # # n_str = list(str(n))
    # # s += 1
  # # return s
# # print(repeat_times(9))
# # print(repeat_times(21))


# # #24. Write a Python program to find the number of divisors of a given integer is even or odd. 
# print("problem 1")

# # def divisor(n):
  # # for i in range(n):
    # # x = len([i for i in range(1,n+1) if not n % i])
  # # return x
# # print(divisor(15))
# # print(divisor(12))
# # print(divisor(9))
# # print(divisor(6))
# # print(divisor(3))


# # #25. Write a Python program to find the digits which are absent in a given mobile number. 
# print("problem 1")

# # def absent_digits(n):
  # # all_nums = set([0,1,2,3,4,5,6,7,8,9])
  # # n = set([int(i) for i in n])
  # # n = n.symmetric_difference(all_nums)
  # # n = sorted(n)
  # # return n
# # print(absent_digits([9,8,3,2,2,0,9,7,6,3]))



# # #26. Write a Python program to compute the summation of the absolute difference of all distinct pairs in an given array (non-decreasing order). 
# print("problem 1")

# # def sum_distinct_pairs(arr):
    # # result = 0
    # # i = 0
    # # while i<len(arr):
        # # result+=i*arr[i]-(len(arr)-i-1)*arr[i]
        # # i+=1
    # # return result
# # print(sum_distinct_pairs([1,2,3]))
# # print(sum_distinct_pairs([1,4,5]))



# # #27. Write a Python program to find the type of the progression (arithmetic progression/geometric progression) and the next successive member of a given three successive members of a sequence. 
# print("problem 1")

# # def ap_gp_sequence(arr):
  # # if arr[0]==arr[1]==arr[2]==0:
    # # return "Wrong Numbers"
  # # else:
    # # if arr[1]-arr[0]==arr[2]-arr[1]:
      # # n=2*arr[2]-arr[1]
      # # return "AP sequence, "+'Next number of the sequence: '+str(n)
    # # else:
      # # n=arr[2]**2/arr[1]
      # # return "GP sequence, " + 'Next number of the sequence:  '+str(n)

# # print(ap_gp_sequence([1,2,3]))
# # print(ap_gp_sequence([2,6,18]))
# # print(ap_gp_sequence([0,0,0]))



# # #28. Write a Python program to print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series. 
# print("problem 1")

# # tn = int(input("Input third term of the series:"))
# # tltn = int(input("Input 3rd last term:"))
# # s_sum = int(input("Sum of the series:"))
# # n = int(2*s_sum/(tn+tltn))
# # print("Length of the series: ",n)


# # if n-5==0:
  # # d = (s_sum-3*tn)//6
# # else:
  # # d = (tltn-tn)/(n-5)

# # a = tn-2*d
# # j = 0
# # print("Series:")
# # for j in range(n-1):
  # # print(int(a),end=" ")
  # # a+=d
# # print(int(a),end=" ")



# # #29. Write a Python program to find common divisors between two numbers in a given pair. 
# print("problem 1")


# # def ngcd(x, y):
    # # i=1
    # # while(i<=x and i<=y):
        # # if(x%i==0 and y%i == 0):
            # # gcd=i;
        # # i+=1
    # # return gcd;
# # def num_comm_div(x, y):
  # # n = ngcd(x, y)
  # # result = 0
  # # z = int(n**0.5)
  # # i = 1
  # # while( i <= z ):
    # # if(n % i == 0):
      # # result += 2 
      # # if(i == n/i):
        # # result-=1
    # # i+=1
  # # return result

# # print("Number of common divisors: ",num_comm_div(2, 4))
# # print("Number of common divisors: ",num_comm_div(2, 8))
# # print("Number of common divisors: ",num_comm_div(12, 24))


# # #30. Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure. 
# print("problem 1")


# # def rev_number(n):
  # # s = 0
  # # while True:
    # # k = str(n)
    # # if k == k[::-1]:
      # # break
    # # else:
      # # m = int(k[::-1])
      # # n += m
      # # s += 1
  # # return n 

# # print(rev_number(1234))
# # print(rev_number(1473))


# # #31. Write a Python program to count the number of carry operations for each of a set of addition problems. 
# print("problem 1")

# # def carry_number(x, y):
  # # ctr = 0
  # # if(x == 0 and y == 0):
    # # return 0
  # # z = 0  
  # # for i in reversed(range(10)):
      # # z = x%10 + y%10 + z
      # # if z > 9:
        # # z = 1
      # # else:
        # # z = 0
      # # ctr += z
      # # x //= 10
      # # y //= 10
      
  # # if ctr == 0:
    # # return "No carry operation."
  # # elif ctr == 1:
    # # return ctr
  # # else:
    # # return ctr
# # print(carry_number(786, 457))
# # print(carry_number(5, 6))



# # #32. Write a python program to find heights of the top three building in descending order from eight given buildings. 
# print("problem 1")

# # print("Input the heights of eight buildings:")
# # l = [int(input()) for i in range(8)]
# # print("Heights of the top three buildings:")
# # l = sorted(l)
# # print(*l[:4:-1], sep='\n')



# # #33. Write a Python program to compute the digit number of sum of two given integers. 
# print("problem 1")

# # print("Input two integers(a b): ")
# # a,b = map(int,input().split(" "))
# # print("Number of digit of a and b.:")
# # print(len(str(a+b)))



# # #34. Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No". 
# print("problem 1")

# # print("Input three integers(sides of a triangle)")
# # int_num = list(map(int,input().split()))
# # x,y,z = sorted(int_num)
# # if x**2+y**2==z**2:
    # # print('Yes')
# # else:
    # # print('No')



# # #35. Write a Python program which solve the equation: 
# print("problem 1")

# # print("Input the value of a, b, c, d, e, f:")
# # a, b, c, d, e, f = map(float, input().split())
# # n = a*e - b*d
# # print("Values of x and y:")
# # if n != 0:
    # # x = (c*e - b*f) / n
    # # y = (a*f - c*d) / n
    # # print('{:.3f} {:.3f}'.format(x+0, y+0))



# # #36. Write a Python program to compute the amount of the debt in n months. The borrowing amount is $100,000 and the loan adds 5% interest of the debt and rounds it to the nearest 1,000 above month by month. 
# print("problem 1")

# # def round_n(n):
    # # if n%1000:
        # # return (1+n//1000)*1000
    # # else:
        # # return n
     
# # def compute_debt(n):
    # # if n==0: return 100000
    # # return int(round_n(compute_debt(n-1)*1.05))

# # print("Input number of months:")
# # result = compute_debt(int(input()))
# # print("Amount of debt: ","$"+str(result).strip())



# # #37. Write a Python program which reads an integer n and find the number of combinations of a,b,c and d (0 = a,b,c,d = 9) where (a + b + c + d) will be equal to n. 
# print("problem 1")

# # import itertools
# # print("Input the number(n):")
# # n=int(input())
# # result=0
# # for (i,j,k) in itertools.product(range(10),range(10),range(10)):
    # # result+=(0<=n-(i+j+k)<=9)
# # print("Number of combinations:",result)



# # #38. Write a Python program to print the number of prime numbers which are less than or equal to an given integer. 
# print("problem 1")


# # primes = [1] * 500000
# # primes[0] = 0
 
# # for i in range(3, 1000, 2):
    # # if primes[i // 2]:
        # # primes[(i * i) // 2::i] = [0] * len(primes[(i * i) // 2::i])
 
# # print("Input the number(n):")
# # n=int(input())
# # if n < 4:
    # # print("Number of prime numbers which are less than or equal to n.:",n - 1)
# # else:
    # # print("Number of prime numbers which are less than or equal to n.:",sum(primes[:(n + 1) // 2]) + 1)


# # #39. Write a program to compute the radius and the central coordinate (x, y) of a circle which is constructed by three given points on the plane surface. 
# print("problem 1")


# # print("Input three coordinate of the circle:")
# # x1, y1, x2, y2, x3, y3 = map(float, input().split())
# # c = (x1-x2)**2 + (y1-y2)**2
# # a = (x2-x3)**2 + (y2-y3)**2
# # b = (x3-x1)**2 + (y3-y1)**2
# # s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) 
# # px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
# # py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 
# # ar = a**0.5
# # br = b**0.5
# # cr = c**0.5 
# # r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5
# # print("Radius of the said circle:")
# # print("{:>.3f}".format(r))
# # print("Central coordinate (x, y) of the circle:")
# # print("{:>.3f}".format(px),"{:>.3f}".format(py))


# # #40. Write a Python program to check if a point (x,y) is in a triangle or not. There is a triangle formed by three points. 
# print("problem 1")


# # print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
# # x1,y1,x2,y2,x3,y3,xp,yp = map(float, input().split())
# # c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
# # c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
# # c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
# # if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0):
    # # print("The point is in the triangle.")
# # else:
    # # print("The point is outside the triangle.")


# # #41. Write a Python program to compute and print sum of two given integers (more than or equal to zero). If given integers or the sum have more than 80 digits, print "overflow". 
# print("problem 1")

# # print("Input first integer:")
# # x = int(input())
# # print("Input second integer:")
# # y = int(input())
# # if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
    # # print("Overflow!")
# # else:
    # # print("Sum of the two integers: ",x + y)



# # #42. Write a Python program that accepts six numbers as input and sorts them in descending order. 
# print("problem 1")


# # print("Input six integers:")
# # nums = list(map(int, input().split()))
# # nums.sort()
# # nums.reverse()
# # print("After sorting the said ntegers:")
# # print(*nums)


# # #43. Write a Python program to test whether two lines PQ and RS are parallel. The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4). 
# print("problem 1")

# # print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
# # x1, y1,x2, y2, x3, y3, x4, y4 = map(float, input().split())
# # print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')



# # #44. Write a Python program to find the maximum sum of a contiguous subsequence from a given sequence of numbers a1, a2, a3, ... an. A subsequence of one element is also a continuous subsequence. 
# print("problem 1")

# # while True:
    # # print("Input number of sequence of numbers you want to input (0 to exit):")
    # # n = int(input())
    # # if n == 0:
        # # break
    # # else:
        # # A = []
        # # Sum = []
        # # print("Input numbers:") 
        # # for i in range(n):
            # # A.append(int(input()))
        # # Wa = 0
        # # for i in range(0,n):
            # # Wa += A[i]
            # # Sum.append(Wa)
        # # for i in range(0 , n):
            # # for j in range(0 , i):
                # # Num = Sum[i] - Sum[j]
                # # Sum.append(Num)
        # # print("Maximum sum of the said contiguous subsequence:")
        # # print(max(Sum))



# # #45. There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2). 
# print("problem 1")

# # import math
# # print("Input x1, y1, r1, x2, y2, r2:")
# # x1,y1,r1,x2,y2,r2 = [float(i) for i in input().split()]
# # d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
# # if d < r1-r2:
    # # print("C2  is in C1")
# # elif d < r2-r1:
    # # print("C1  is in C2")
# # elif d > r1+r2:
    # # print("Circumference of C1  and C2  intersect")
# # else:
    # # print("C1 and C2  do not overlap")



# # #46. Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year. 
# print("problem 1")


# # from datetime import date
# # print("Input month and date (separated by a single space):")
# # m, d = map(int, input().split())
# # weeks = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
# # w = date.isoweekday(date(2016, m, d))
# # print("Name of the date: ",weeks[w])


# # #47. Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters. 
# print("problem 1")

# # import collections
# # print("Input a text in a line.")
# # text_list = list(map(str, input().split()))
# # sc = collections.Counter(text_list)
# # common_word = sc.most_common()[0][0]
# # max_char = ""
# # for s in text_list:
    # # if len(max_char) < len(s):
        # # max_char = s
# # print("\nMost frequent text and the word which has the maximum number of letters.")
# # print(common_word, max_char)



# # #48. Write a Python program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations where the sum of the digits equals to another given number (s). Do not use the same digits in a combination. 
# print("problem 1")



# # import itertools
# # print("Input number of combinations and sum, input 0 0 to exit:")
# # while True:
  # # x, y = map(int, input(). split())
  # # if x == 0 and y == 0:
    # # break
  # # s = list(itertools.combinations(range(10), x))
  # # ctr = 0
  # # for i in s:
    # # if sum(i) == y:
            # # ctr += 1
 
# # print(ctr)


# # #49. Write a Python program which reads the two adjoined sides and the diagonal of a parallelogram and check whether the parallelogram is a rectangle or a rhombus. 
# print("problem 1")


# # print("Input two adjoined sides and the diagonal of a parallelogram (comma separated):")
# # a,b,c = map(int, input().split(","))
# # if c**2 == a**2+b**2 :
    # # print("This is a rectangle.")
# # if a == b:
    # # print("This is a rhombus.")



# # #50. Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string. 
# print("problem 1")


# # print("Input a text with two words 'Python' and 'Java'")
# # text = input().split()
# # for i in range(len(text)):
    # # if "Python" in text[i]:n = text[i].index("Python");text[i] = text[i][:n] + "Java" + text[i][n + 6:]
    # # elif "Java" in text[i]:n = text[i].index("Java");text[i] = text[i][:n] + "Python" + text[i][n + 4:]
# # print(*text)


# # #51. Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668. 
# print("problem 1")


# # print("Input an integer created by 8 numbers from 0 to 9.:")
# # num = list(input())
# # print("Difference between the largest and the smallest integer from the given integer:")
# # print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))


# # #52. Write a Python program to compute the sum of first n given prime numbers. 
# print("problem 1")


# # MAX = 105000
# # print("Input a number (n≤10000) to compute the sum:(0 to exit)") 
# # is_prime = [True for _ in range(MAX)]
# # is_prime[0] = is_prime[1] = False
# # for i in range(2, int(MAX ** (1 / 2)) + 1):
  # # if is_prime[i]:
    # # for j in range(i ** 2, MAX, i):
      # # is_prime[j] = False 
# # primes = [i for i in range(MAX) if is_prime[i]] 
# # while True:
  # # n = int(input())
  # # if not n:
    # # break
  # # print("Sum of first",n,"prime numbers:")
  # # print(sum(primes[:n]))


# # #53. Write a Python program that accept a even number (>=4, Goldbach number) from the user and create a combinations that express the given number as a sum of two prime numbers. Print the number of combinations. 
# print("problem 1")


# # import sys
# # from bisect import bisect_right
# # from itertools import chain, compress
# # print("Input an even number (0 to exit):") 
# # ub = 50000
# # is_prime = [0, 0, 1, 1] + [0]*(ub-3)
# # is_prime[5::6] = is_prime[7::6] = [1]*int(ub/6)
# # primes = [2, 3]
# # append = primes.append
 
# # for n in chain(range(5, ub, 6), range(7, ub, 6)):
    # # if is_prime[n]:
        # # append(n)
        # # is_prime[n*3::n*2] = [0]*((ub-n)//(n*2))
# # primes.sort()

# # for n in map(int, sys.stdin):
    # # if not n:
        # # break
    # # if n%2:
        # # print("Number of combinations:")  
        # # print(is_prime[n-2])
    # # else:
        # # print("Number of combinations:")  
        # # print(len([1 for p in primes[:bisect_right(primes, n/2)] if is_prime[n-p]]))


# # #54. if you draw a straight line on a plane, the plane is divided into two regions. For example, if you pull two straight lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas.
# print("problem 1")



# # while True:
    # # print("Input number of straight lines (o to exit): ")
    # # n=int(input())
    # # if n<=0:
        # # break
    # # print("Number of regions:") 
    # # print((n*n+n+2)//2)

# # #55. There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys). Write a Python program to test AB and CD are orthogonal or not. 
# print("problem 1")


# # while True:
    # # try:
        # # print("Input xp, yp, xq, yq, xr, yr, xs, ys:")
        # # x_p, y_p, x_q, y_q, x_r, y_r, x_s, y_s = map(float, input().split())
        # # pq_x, pq_y = x_q - x_p, y_q - y_p
        # # rs_x, rs_y = x_s - x_r, y_s - y_r
        # # rs = pq_x*rs_x + pq_y*rs_y
        # # if abs(rs) > 1e-10:
            # # print("AB and CD are not orthogonal!")
        # # else:
            # # print("AB and CD are orthogonal!")
    # # except:
        # # break


# # #56. Write a Python program to sum of all numerical values (positive integers) embedded in a sentence.
# print("problem 1")


# # import sys,re
# # def test(stri):
  # # print("Input some text and numeric values (<ctrl-d> to exit):")
  # # print("Sum of the numeric values: ",sum([sum(map(int,re.findall(r"[0-9]{1,5}",stri)))]))

# # print(test("sd1fdsfs23 dssd56"))
# # print(test("15apple2banana"))
# # print(test("flowers5fruit5"))



# # #57. There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and left, they are said to be ground. The area created by only one green square is called "island". For example, there are five islands in the figure below.
# print("problem 1")


# # c=0
# # def f(x,y,z):
    # # if 0<=y<10 and 0<=z<10 and x[z][y]=='1':
        # # x[z][y]='0'
        # # for dy,dz in [[-1,0],[1,0],[0,-1],[0,1]]:f(x,y+dy,z+dz)
# # print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros") 
# # while 1:
    # # try:
        # # if c:input()
    # # except:break
    # # x = [list(input()) for _ in [0]*10]
    # # c=1;b=0
    # # for i in range(10):
        # # for j in range(10):
            # # if x[j][i]=='1':
                # # b+=1;f(x,i,j)
    # # print("Number of islands:")     
    # # print(b)



# # #58. When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character.
# print("problem 1")


# # def restore_original_str(a1):
  # # result = ""
  # # ind = 0
  # # end = len(a1)
  # # while ind < end:
    # # if a1[ind] == "#":
      # # result += a1[ind + 2] * int(a1[ind + 1])
      # # ind += 3
    # # else:
      # # result += a1[ind]
      # # ind += 1
  # # return result
# # print("Original text:","XY#6Z1#4023")
# # print(restore_original_str("XY#6Z1#4023"))
# # print("Original text:","#39+1=1#30")
# # print(restore_original_str("#39+1=1#30"))



# # #59. A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees.
# print("problem 1")


# # def poly_area(c):
  # # add = []
  # # for i in range(0, (len(c) - 2), 2):
    # # add.append(c[i] * c[i + 3] - c[i + 1] * c[i + 2])
    # # add.append(c[len(c) - 2] * c[1] - c[len(c) - 1] * c[0])
    # # return abs(sum(add) / 2)

# # print(poly_area([1, 0, 0, 0, 1, 1, 2, 0, -1, 1]))



# # #60. Internet search engine giant, such as Google accepts web pages around the world and classify them, creating a huge database. The search engines also analyze the search keywords entered by the user and create inquiries for database search. In both cases, complicated processing is carried out in order to realize efficient retrieval, but basics are all cutting out words from sentences.
# print("problem 1")


# # print("Input a sentence (1024 characters. max.)")
# # yy = input()
# # yy = yy.replace(",", " ")
# # yy = yy.replace(".", " ")
# # print("3 to 6 characters length of words:")
# # print(*[y for y in yy.split() if 3 <= len(y) <= 6])


# # #61. Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge, when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that compute the maximum value of the sum of the passing integers. 
# print("problem 1")


# # import sys
# # print("Input the numbers (ctrl+d to exit):")
# # x = [list(map(int, l.split(","))) for l in sys.stdin]
# # dp = x[0]
 
# # for i in range(1, (len(x)+1)//2):
    # # _dp = [0]*(i+1)
    # # for j in range(i):
        # # _dp[j] = max(_dp[j], dp[j]+x[i][j])
        # # _dp[j+1] = max(_dp[j+1], dp[j]+x[i][j+1])
    # # dp = _dp
 
# # for i in range((len(x)+1)//2, len(x)):
    # # _dp = [0]*(len(dp)-1)
    # # for j in range(len(_dp)):
        # # _dp[j] = max(dp[j], dp[j+1]) + x[i][j]
    # # dp = _dp
# # print("Maximum value of the sum of integers passing according to the rule on one line.") 
# # print(dp[0])



# # #62. Write a Python program to find the number of combinations that satisfy p + q + r + s = n where n is a given number <= 4000 and p, q, r, s in the range of 0 to 1000. 
# print("problem 1")

# # from collections import Counter
# # print("Input a positive integer: (ctrl+d to exit)") 
# # pair_dict = Counter()
# # for i in range(2001):
  # # pair_dict[i] = min(i, 2000 - i) + 1 
 
# # while True:
  # # try:
    # # n = int(input())
    # # ans = 0
    # # for i in range(n + 1):
      # # ans += pair_dict[i] * pair_dict[n - i]
    # # print("Number of combinations of a,b,c,d:",ans) 
  # # except EOFError:
    # # break



# # #63. Write a Python program which adds up columns and rows of given table as shown in the specified figure. 
# print("problem 1")


# # while True:
    # # print("Input number of rows/columns (0 to exit)")
    # # n = int(input())
    # # if n == 0:
        # # break
    # # print("Input cell value:")
    # # x = []
    # # for i in range(n):
        # # x.append([int(num) for num in input().split()])

    # # for i in range(n):
        # # sum = 0
        # # for j in range(n):
            # # sum += x[i][j]
        # # x[i].append(sum)

    # # x.append([])
    # # for i in range(n + 1):
        # # sum = 0
        # # for j in range(n):
            # # sum += x[j][i]
        # # x[n].append(sum)
    # # print("Result:")
    # # for i in range(n + 1):
        # # for j in range(n + 1):
            # # print('{0:>5}'.format(x[i][j]), end="")
        # # print()


# # #_____________________________ Conditional _______________________________



# # #1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 
# # nl=[]
# # for x in range(1500, 2701):
    # # if (x%7==0) and (x%5==0):
        # # nl.append(str(x))
# # print (','.join(nl))

# # #2. Write a Python program to convert temperatures to and from celsius, fahrenheit. 

# # temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# # degree = int(temp[:-1])
# # i_convention = temp[-1]

# # if i_convention.upper() == "C":
  # # result = int(round((9 * degree) / 5 + 32))
  # # o_convention = "Fahrenheit"
# # elif i_convention.upper() == "F":
  # # result = int(round((degree - 32) * 5 / 9))
  # # o_convention = "Celsius"
# # else:
  # # print("Input proper convention.")
  # # quit()
# # print("The temperature in", o_convention, "is", result, "degrees.")

# # #3. Write a Python program to guess a number between 1 to 9. 

# # import random
# # target_num, guess_num = random.randint(1, 10), 0
# # while target_num != guess_num:
    # # guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# # print('Well guessed!')

# # #4. Write a Python program to construct the following pattern, using a nested for loop.

# # n=5;
# # for i in range(n):
    # # for j in range(i):
        # # print ('* ', end="")
    # # print('')

# # for i in range(n,0,-1):
    # # for j in range(i):
        # # print('* ', end="")
    # # print('')
	
# # #5. Write a Python program that accepts a word from the user and reverse it. 

# # word = input("Input a word to reverse: ")

# # for char in range(len(word) - 1, -1, -1):
  # # print(word[char], end="")
# # print("\n")

# # #6. Write a Python program to count the number of even and odd numbers from a series of numbers. 

# # numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# # count_odd = 0
# # count_even = 0
# # for x in numbers:
        # # if not x % 2:
    	     # # count_even+=1
        # # else:
    	     # # count_odd+=1
# # print("Number of even numbers :",count_even)
# # print("Number of odd numbers :",count_odd)

# # #7. Write a Python program that prints each item and its corresponding type from the following list.

# # datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
# # {"class":'V', "section":'A'}]
# # for item in datalist:
   # # print ("Type of ",item, " is ", type(item))
   
# # #8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# # for x in range(6):
    # # if (x == 3 or x==6):
        # # continue
    # # print(x,end=' ')
# # print("\n")
	
# # #9. Write a Python program to get the Fibonacci series between 0 to 50. 

# # x,y=0,1

# # while y<50:
    # # print(y)
    # # x,y = y,x+y
	
# # #10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# # for fizzbuzz in range(50):
    # # if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        # # print("fizzbuzz")
        # # continue
    # # elif fizzbuzz % 3 == 0:
        # # print("fizz")
        # # continue
    # # elif fizzbuzz % 5 == 0:
        # # print("buzz")
        # # continue
    # # print(fizzbuzz)
	
# # #11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 

# # row_num = int(input("Input number of rows: "))
# # col_num = int(input("Input number of columns: "))
# # multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# # for row in range(row_num):
    # # for col in range(col_num):
        # # multi_list[row][col]= row*col

# # print(multi_list)

# # #12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case). 

# # lines = []
# # while True:
    # # l = input()
    # # if l:
        # # lines.append(l.upper())
    # # else:
        # # break;

# # for l in lines:
    # # print(l)
	
# # #13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. 

# # items = []
# # num = [x for x in input().split(',')]
# # for p in num:
    # # x = int(p, 2)
    # # if not x%5:
        # # items.append(p)
# # print(','.join(items))

# # #14. Write a Python program that accepts a string and calculate the number of digits and letters. 

# # s = input("Input a string")
# # d=l=0
# # for c in s:
    # # if c.isdigit():
        # # d=d+1
    # # elif c.isalpha():
        # # l=l+1
    # # else:
        # # pass
# # print("Letters", l)
# # print("Digits", d)

# # #15. Write a Python program to check the validity of password input by users. 

# # import re
# # p= input("Input your password")
# # x = True
# # while x:  
    # # if (len(p)<6 or len(p)>12):
        # # break
    # # elif not re.search("[a-z]",p):
        # # break
    # # elif not re.search("[0-9]",p):
        # # break
    # # elif not re.search("[A-Z]",p):
        # # break
    # # elif not re.search("[$#@]",p):
        # # break
    # # elif re.search("\s",p):
        # # break
    # # else:
        # # print("Valid Password")
        # # x=False
        # # break

# # if x:
    # # print("Not a Valid Password")

# # #16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence. 

# # items = []
# # for i in range(100, 401):
    # # s = str(i)
    # # if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        # # items.append(s)
# # print( ",".join(items))

# # #17. Write a Python program to print alphabet pattern 'A'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #18. Write a Python program to print alphabet pattern 'D'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #19. Write a Python program to print alphabet pattern 'E'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #20. Write a Python program to print alphabet pattern 'G'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #21. Write a Python program to print alphabet pattern 'L'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (column == 1 or (row == 6 and column != 0 and column < 6)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #22. Write a Python program to print alphabet pattern 'M'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            # # result_str=result_str+"* "    
        # # else:      
            # # result_str=result_str+"  "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #23. Write a Python program to print alphabet pattern 'O'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #24. Write a Python program to print alphabet pattern 'P'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #25. Write a Python program to print alphabet pattern 'R'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #26. Write a Python program to print the following patterns. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # row=15    
# # col=18   
# # result_str=""    
# # for i in range(1,row+1):    
    # # if((i<=3)or(i>=7 and i<=9)or(i>=13 and i<=15)):    
        # # for j in range(1,col):    
            # # result_str=result_str+"o"    
        # # result_str=result_str+"\n"    
    # # elif(i>=4 and i<=6):    
        # # for j in range(1,5):    
            # # result_str=result_str+"o"    
        # # result_str=result_str+"\n"    
    # # else:    
        # # for j in range(1,14):    
            # # result_str=result_str+" "    
        # # for j in range(1,5):    
            # # result_str=result_str+"o"    
        # # result_str=result_str+"\n"    
# # print(result_str);

# # #27. Write a Python program to print alphabet pattern 'T'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (column == 3 or (row == 0 and column > 0 and column <6)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #28. Write a Python program to print alphabet pattern 'U'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #29. Write a Python program to print alphabet pattern 'X'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (((column == 1 or column == 5) and (row > 4 or row < 2)) or row == column and column > 0 and column < 6 or (column == 2 and row == 4) or (column == 4 and row == 2)):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #30. Write a Python program to print alphabet pattern 'Z'. 

# # result_str="";    
# # for row in range(0,7):    
    # # for column in range(0,7):     
        # # if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):  
            # # result_str=result_str+"*"    
        # # else:      
            # # result_str=result_str+" "    
    # # result_str=result_str+"\n"    
# # print(result_str);

# # #31. Write a Python program to calculate a dog's age in dog's years. 

# # h_age = int(input("Input a dog's age in human years: "))

# # if h_age < 0:
	# # print("Age must be positive number.")
	# # exit()
# # elif h_age <= 2:
	# # d_age = h_age * 10.5
# # else:
	# # d_age = 21 + (h_age - 2)*4

# # print("The dog's age in dog's years is", d_age)

# # #32. Write a Python program to check whether an alphabet is a vowel or consonant. 

# # l = input("Input a letter of the alphabet: ")

# # if l in ('a', 'e', 'i', 'o', 'u'):
	# # print("%s is a vowel." % l)
# # elif l == 'y':
	# # print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
# # else:
	# # print("%s is a consonant." % l) 
	
# # #33. Write a Python program to convert month name to a number of days. 

# # print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
# # month_name = input("Input the name of Month: ")

# # if month_name == "February":
	# # print("No. of days: 28/29 days")
# # elif month_name in ("April", "June", "September", "November"):
	# # print("No. of days: 30 days")
# # elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	# # print("No. of days: 31 day")
# # else:
	# # print("Wrong month name") 
	
# # #34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 

# # def sum(x, y):
    # # sum = x + y
    # # if sum in range(15, 20):
        # # return 20
    # # else:
        # # return sum

# # print(sum(10, 6))
# # print(sum(10, 2))
# # print(sum(10, 12))

# # #35. Write a Python program to check a string represent an integer or not. 

# # text = input("Input a string: ")
# # text = text.strip()
# # if len(text) < 1:
    # # print("Input a valid text")
# # else:
    # # if all(text[i] in "0123456789" for i in range(len(text))):
        # # print("The string is an integer.")
    # # elif (text[0] in "+-") and \
         # # all(text[i] in "0123456789" for i in range(1,len(text))):
         # # print("The string is an integer.")
    # # else:
        # # print("The string is not an integer.") 
		
# # #36. Write a Python program to check a triangle is equilateral, isosceles or scalene. 

# # print("Input lengths of the triangle sides: ")
# # x = int(input("x: "))
# # y = int(input("y: "))
# # z = int(input("z: "))

# # if x == y == z:
	# # print("Equilateral triangle")
# # elif x==y or y==z or z==x:
	# # print("isosceles triangle")
# # else:
	# # print("Scalene triangle")

# # #37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day. 

# # month = input("Input the month (e.g. January, February etc.): ")
# # day = int(input("Input the day: "))

# # if month in ('January', 'February', 'March'):
	# # season = 'winter'
# # elif month in ('April', 'May', 'June'):
	# # season = 'spring'
# # elif month in ('July', 'August', 'September'):
	# # season = 'summer'
# # else:
	# # season = 'autumn'

# # if (month == 'March') and (day > 19):
	# # season = 'spring'
# # elif (month == 'June') and (day > 20):
	# # season = 'summer'
# # elif (month == 'September') and (day > 21):
	# # season = 'autumn'
# # elif (month == 'December') and (day > 20):
	# # season = 'winter'

# # print("Season is",season)

# # #38. Write a Python program to display astrological sign for given date of birth. 

# # day = int(input("Input birthday: "))
# # month = input("Input month of birth (e.g. march, july etc): ")
# # if month == 'december':
	# # astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
# # elif month == 'january':
	# # astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
# # elif month == 'february':
	# # astro_sign = 'Aquarius' if (day < 19) else 'pisces'
# # elif month == 'march':
	# # astro_sign = 'Pisces' if (day < 21) else 'aries'
# # elif month == 'april':
	# # astro_sign = 'Aries' if (day < 20) else 'taurus'
# # elif month == 'may':
	# # astro_sign = 'Taurus' if (day < 21) else 'gemini'
# # elif month == 'june':
	# # astro_sign = 'Gemini' if (day < 21) else 'cancer'
# # elif month == 'july':
	# # astro_sign = 'Cancer' if (day < 23) else 'leo'
# # elif month == 'august':
	# # astro_sign = 'Leo' if (day < 23) else 'virgo'
# # elif month == 'september':
	# # astro_sign = 'Virgo' if (day < 23) else 'libra'
# # elif month == 'october':
	# # astro_sign = 'Libra' if (day < 23) else 'scorpio'
# # elif month == 'november':
	# # astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
# # print("Your Astrological sign is :",astro_sign)

# # #39. Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born. 

# # year = int(input("Input your birth year: "))
# # if (year - 2000) % 12 == 0:
    # # sign = 'Dragon'
# # elif (year - 2000) % 12 == 1:
    # # sign = 'Snake'
# # elif (year - 2000) % 12 == 2:
    # # sign = 'Horse'
# # elif (year - 2000) % 12 == 3:
    # # sign = 'sheep'
# # elif (year - 2000) % 12 == 4:
    # # sign = 'Monkey'
# # elif (year - 2000) % 12 == 5:
    # # sign = 'Rooster'
# # elif (year - 2000) % 12 == 6:
    # # sign = 'Dog'
# # elif (year - 2000) % 12 == 7:
    # # sign = 'Pig'
# # elif (year - 2000) % 12 == 8:
    # # sign = 'Rat'
# # elif (year - 2000) % 12 == 9:
    # # sign = 'Ox'
# # elif (year - 2000) % 12 == 10:
    # # sign = 'Tiger'
# # else:
    # # sign = 'Hare'

# # print("Your Zodiac sign :",sign)

# # #40. Write a Python program to find the median of three values. 

# # a = float(input("Input first number: "))
# # b = float(input("Input second number: "))
# # c = float(input("Input third number: "))
# # if a > b:
    # # if a < c:
        # # median = a
    # # elif b > c:
        # # median = b
    # # else:
        # # median = c
# # else:
    # # if a > c:
        # # median = a
    # # elif b < c:
        # # median = b
    # # else:
        # # median = c

# # print("The median is", median)

# # #41. Write a Python program to get next day of a given date. 

# # year = int(input("Input a year: "))

# # if (year % 400 == 0):
    # # leap_year = True
# # elif (year % 100 == 0):
    # # leap_year = False
# # elif (year % 4 == 0):
    # # leap_year = True
# # else:
    # # leap_year = False

# # month = int(input("Input a month [1-12]: "))

# # if month in (1, 3, 5, 7, 8, 10, 12):
    # # month_length = 31
# # elif month == 2:
    # # if leap_year:
        # # month_length = 29
    # # else:
        # # month_length = 28
# # else:
    # # month_length = 30


# # day = int(input("Input a day [1-31]: "))

# # if day < month_length:
    # # day += 1
# # else:
    # # day = 1
    # # if month == 12:
        # # month = 1
        # # year += 1
    # # else:
        # # month += 1
# # print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

# # #42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish. 

# # print("Input some integers to calculate their sum and average. Input 0 to exit.")

# # count = 0
# # sum = 0.0
# # number = 1

# # while number != 0:
	# # number = int(input(""))
	# # sum = sum + number
	# # count += 1

# # if count == 0:
	# # print("Input some numbers")
# # else:
	# # print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
	
# # #43. Write a Python program to create the multiplication table (from 1 to 10) of a number. 

# # n = int(input("Input a number: "))

# # # use for loop to iterate 10 times
# # for i in range(1,11):
   # # print(n,'x',i,'=',n*i)
   
# # #44. Write a Python program to construct the following pattern, using a nested loop number. 

# # for i in range(10):
    # # print(str(i) * i)
	
# # #___________________________________ Array ___________________________________


# # #1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes. 

# # from array import *
# # array_num = array('i', [1,3,5,7,9])
# # for i in array_num:
    # # print(i)
# # print("Access first three items individually")
# # print(array_num[0])
# # print(array_num[1])
# # print(array_num[2])

# # #2. Write a Python program to append a new item to the end of the array. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 7, 9])
# # print("Original array: "+str(array_num))
# # print("Append 11 at the end of the array:")
# # array_num.append(11)
# # print("New array: "+str(array_num))

# # #3. Write a Python program to reverse the order of the items in the array. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# # print("Original array: "+str(array_num))
# # array_num.reverse()
# # print("Reverse the order of the items:")
# # print(str(array_num))

# # #4. Write a Python program to get the length in bytes of one array item in the internal representation. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 7, 9])
# # print("Original array: "+str(array_num))
# # print("Length in bytes of one array item: "+str(array_num.itemsize))

# # #5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 7, 9])
# # print("Original array: "+str(array_num))
# # print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
# # print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))

# # #6. Write a Python program to get the number of occurrences of a specified element in an array. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
# # print("Original array: "+str(array_num))
# # print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))

# # #7. Write a Python program to append items from inerrable to the end of the array. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 7, 9])
# # print("Original array: "+str(array_num))
# # array_num.extend(array_num)
# # print("Extended array: "+str(array_num))

# # #8. Write a Python program to convert an array to an array of machine values and return the bytes representation. 

# # from array import *
# # print("Bytes to String: ")
# # x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
# # s = x.tobytes()
# # print(s)

# # #9. Write a Python program to append items from a specified list. 

# # from array import *
# # num_list = [1, 2, 6, -8]
# # array_num = array('i', [])
# # print("Items in the list: " + str(num_list))
# # print("Append items from the list: ")
# # array_num.fromlist(num_list)
# # print("Items in the array: "+str(array_num))

# # #10. Write a Python program to insert a new item before the second element in an existing array. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 7, 9])
# # print("Original array: "+str(array_num))
# # print("Insert new value 4 before 3:")
# # array_num.insert(1, 4)
# # print("New array: "+str(array_num))

# # #11. Write a Python program to remove a specified item using the index from an array. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 7, 9])
# # print("Original array: "+str(array_num))
# # print("Remove the third item form the array:")
# # array_num.pop(2)
# # print("New array: "+str(array_num))

# # #12. Write a Python program to remove the first occurrence of a specified element from an array. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# # print("Original array: "+str(array_num))
# # print("Remove the first occurrence of 3 from the said array:")
# # array_num.remove(3)
# # print("New array: "+str(array_num))

# # #13. Write a Python program to convert an array to an ordinary list with the same items. 

# # from array import *
# # array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# # print("Original array: "+str(array_num))
# # num_list = array_num.tolist()
# # print("Convert the said array to an ordinary list with the same items:")
# # print(num_list)


# # #___________________________ String ___________________________________



# # #1. Write a Python program to calculate the length of a string. 

# # def string_length(str1):
    # # count = 0
    # # for char in str1:
        # # count += 1
    # # return count
# # print(string_length('w3resource.com'))

# # #2. Write a Python program to count the number of characters (character frequency) in a string. 

# # def char_frequency(str1):
    # # dict = {}
    # # for n in str1:
        # # keys = dict.keys()
        # # if n in keys:
            # # dict[n] += 1
        # # else:
            # # dict[n] = 1
    # # return dict
# # print(char_frequency('google.com'))

# # #3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 

# # def string_both_ends(str):
  # # if len(str) < 2:
    # # return ''

  # # return str[0:2] + str[-2:]

# # print(string_both_ends('w3resource'))
# # print(string_both_ends('w3'))
# # print(string_both_ends('w'))


# # #4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 

# # def change_char(str1):
  # # char = str1[0]
  # # str1 = str1.replace(char, '$')
  # # str1 = char + str1[1:]

  # # return str1

# # print(change_char('restart'))

# # #5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

# # def chars_mix_up(a, b):
  # # new_a = b[:2] + a[2:]
  # # new_b = a[:2] + b[2:]

  # # return new_a + ' ' + new_b
# # print(chars_mix_up('abc', 'xyz'))

# # #6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 

# # def add_string(str1):
  # # length = len(str1)

  # # if length > 2:
    # # if str1[-3:] == 'ing':
      # # str1 += 'ly'
    # # else:
      # # str1 += 'ing'

  # # return str1
# # print(add_string('ab'))
# # print(add_string('abc'))
# # print(add_string('string'))

# # #7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 

# # def not_poor(str1):
  # # snot = str1.find('not')
  # # spoor = str1.find('poor')
  

  # # if spoor > snot and snot>0 and spoor>0:
    # # str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    # # return str1
  # # else:
    # # return str1
# # print(not_poor('The lyrics is not that poor!'))
# # print(not_poor('The lyrics is poor!'))

# # #8. Write a Python function that takes a list of words and returns the length of the longest one. 

# # def find_longest_word(words_list):
    # # word_len = []
    # # for n in words_list:
        # # word_len.append((len(n), n))
    # # word_len.sort()
    # # return word_len[-1][1]

# # print(find_longest_word(["PHP", "Exercises", "Backend"]))

# # #9. Write a Python program to remove the nth index character from a nonempty string. 

# # def remove_char(str, n):
      # # first_part = str[:n] 
      # # last_part = str[n+1:]
      # # return first_part + last_part
# # print(remove_char('Python', 0))
# # print(remove_char('Python', 3))
# # print(remove_char('Python', 5))

# # #10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 

# # def change_sring(str1):
      # # return str1[-1:] + str1[1:-1] + str1[:1]
	  
# # print(change_sring('abcd'))
# # print(change_sring('12345'))

# # #11. Write a Python program to remove the characters which have odd index values of a given string. 

# # def odd_values_string(str):
  # # result = "" 
  # # for i in range(len(str)):
    # # if i % 2 == 0:
      # # result = result + str[i]
  # # return result

# # print(odd_values_string('abcdef'))
# # print(odd_values_string('python'))

# # #12. Write a Python program to count the occurrences of each word in a given sentence. 

# # def word_count(str):
    # # counts = dict()
    # # words = str.split()

    # # for word in words:
        # # if word in counts:
            # # counts[word] += 1
        # # else:
            # # counts[word] = 1

    # # return counts

# # print( word_count('the quick brown fox jumps over the lazy dog.'))

# # #13. Write a Python script that takes input from the user and displays that input back in upper and lower cases. 

# # user_input = input("What's your favourite language? ")
# # print("My favourite language is ", user_input.upper())
# # print("My favourite language is ", user_input.lower())

# # #14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 

# # items = input("Input comma separated sequence of words")
# # words = [word for word in items.split(",")]
# # print(",".join(sorted(list(set(words)))))

# # #15. Write a Python function to create the HTML string with tags around the word(s). 

# # def add_tags(tag, word):
	# # return "<%s>%s</%s>" % (tag, word, tag)
# # print(add_tags('i', 'Python'))
# # print(add_tags('b', 'Python Tutorial'))

# # #16. Write a Python function to insert a string in the middle of a string. 

# # def insert_sting_middle(str, word):
	# # return str[:2] + word + str[2:]

# # print(insert_sting_middle('[[]]', 'Python'))
# # print(insert_sting_middle('{{}}', 'PHP'))
# # print(insert_sting_middle('<<>>', 'HTML'))

# # #17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 

# # def insert_end(str):
	# # sub_str = str[-2:]
	# # return sub_str * 4

# # print(insert_end('Python'))
# # print(insert_end('Exercises'))

# # #18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 

# # def first_three(str):
	# # return str[:3] if len(str) > 3 else str

# # print(first_three('ipy'))
# # print(first_three('python'))
# # print(first_three('py'))

# # #19. Write a Python program to get the last part of a string before a specified character. 

# # str1 = 'https://www.w3resource.com/python-exercises/string'
# # print(str1.rsplit('/', 1)[0])
# # print(str1.rsplit('-', 1)[0])

# # #20. Write a Python function to reverses a string if it's length is a multiple of 4. 

# # def reverse_string(str1):
    # # if len(str1) % 4 == 0:
       # # return ''.join(reversed(str1))
    # # return str1

# # print(reverse_string('abcd'))
# # print(reverse_string('python'))

# # #21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 

# # def to_uppercase(str1):
    # # num_upper = 0
    # # for letter in str1[:4]: 
        # # if letter.upper() == letter:
            # # num_upper += 1
    # # if num_upper >= 2:
        # # return str1.upper()
    # # return str1

# # print(to_uppercase('Python'))
# # print(to_uppercase('PyThon'))

# # #22.Write a Python program to sort a string lexicographically. 

# # def lexicographi_sort(s):
    # # return sorted(sorted(s), key=str.upper)

# # print(lexicographi_sort('w3resource'))
# # print(lexicographi_sort('quickbrown'))

# # #23. Write a Python program to remove a newline in Python. 

# # str1='Python Exercises\n'
# # print(str1)
# # print(str1.rstrip())

# # #24. Write a Python program to check whether a string starts with specified characters. 

# # string = "w3resource.com"
# # print(string.startswith("w3r"))

# # #25. Write a Python program to create a Caesar encryption. 

# # #https://gist.github.com/nchitalov/2f2b03e5cf1e19da1525
# # def caesar_encrypt(realText, step):
	# # outText = []
	# # cryptText = []
	
	# # uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	# # lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	# # for eachLetter in realText:
		# # if eachLetter in uppercase:
			# # index = uppercase.index(eachLetter)
			# # crypting = (index + step) % 26
			# # cryptText.append(crypting)
			# # newLetter = uppercase[crypting]
			# # outText.append(newLetter)
		# # elif eachLetter in lowercase:
			# # index = lowercase.index(eachLetter)
			# # crypting = (index + step) % 26
			# # cryptText.append(crypting)
			# # newLetter = lowercase[crypting]
			# # outText.append(newLetter)
	# # return outText

# # code = caesar_encrypt('abc', 2)
# # print()
# # print(code)
# # print()

# # #26. Write a Python program to display formatted text (width=50) as output. 

# # import textwrap
# # sample_text = '''
  # # Python is a widely used high-level, general-purpose, interpreted,
  # # dynamic programming language. Its design philosophy emphasizes
  # # code readability, and its syntax allows programmers to express
  # # concepts in fewer lines of code than possible in languages such
  # # as C++ or Java.
  # # '''
# # print()
# # print(textwrap.fill(sample_text, width=50))
# # print()

# # #27. Write a Python program to remove existing indentation from all of the lines in a given text. 

# # import textwrap
# # sample_text = '''
    # # Python is a widely used high-level, general-purpose, interpreted,
    # # dynamic programming language. Its design philosophy emphasizes
    # # code readability, and its syntax allows programmers to express
    # # concepts in fewer lines of code than possible in languages such
    # # as C++ or Java.
    # # '''
# # text_without_Indentation = textwrap.dedent(sample_text)
# # print()
# # print(text_without_Indentation )
# # print()

# # #28. Write a Python program to add a prefix text to all of the lines in a string. 

# # import textwrap
# # sample_text ='''
    # # Python is a widely used high-level, general-purpose, interpreted,
    # # dynamic programming language. Its design philosophy emphasizes
    # # code readability, and its syntax allows programmers to express
    # # concepts in fewer lines of code than possible in languages such
    # # as C++ or Java.
    # # '''
# # text_without_Indentation = textwrap.dedent(sample_text)
# # wrapped = textwrap.fill(text_without_Indentation, width=50)
# # #wrapped += '\n\nSecond paragraph after a blank line.'
# # final_result = textwrap.indent(wrapped, '> ')
# # print()
# # print(final_result)
# # print()

# # #29. Write a Python program to set the indentation of the first line. 

# # import textwrap
# # sample_text ='''
# # Python is a widely used high-level, general-purpose, interpreted, dynamic
# # programming language. Its design philosophy emphasizes code readability,
# # and its syntax allows programmers to express concepts in fewer lines of
# # code than possible in languages such as C++ or Java.
    # # '''

# # text1 =  textwrap.dedent(sample_text).strip()
# # print()
# # print(textwrap.fill(text1,
                    # # initial_indent='',
                    # # subsequent_indent=' ' * 4,
                    # # width=80,
                    # # ))
# # print()

# # #30. Write a Python program to print the following floating numbers upto 2 decimal places. 

# # x = 3.1415926
# # y = 12.9999
# # print("\nOriginal Number: ", x)
# # print("Formatted Number: "+"{:.2f}".format(x));
# # print("Original Number: ", y)
# # print("Formatted Number: "+"{:.2f}".format(y));
# # print() 

# # #31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign. 

# # x = 3.1415926
# # y = -12.9999
# # print("\nOriginal Number: ", x)
# # print("Formatted Number with sign: "+"{:+.2f}".format(x));
# # print("Original Number: ", y)
# # print("Formatted Number with sign: "+"{:+.2f}".format(y));
# # print()

# # #32. Write a Python program to print the following floating numbers with no decimal places. 

# # x = 3.1415926
# # y = -12.9999
# # print("\nOriginal Number: ", x)
# # print("Formatted Number with no decimal places: "+"{:.0f}".format(x));
# # print("Original Number: ", y)
# # print("Formatted Number with no decimal places: "+"{:.0f}".format(y));
# # print()

# # #33. Write a Python program to print the following integers with zeros on the left of specified width. 

# # x = 3
# # y = 123
# # print("\nOriginal Number: ", x)
# # print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
# # print("Original Number: ", y)
# # print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
# # print()

# # #34. Write a Python program to print the following integers with '*' on the right of specified width. 

# # x = 3
# # y = 123
# # print("\nOriginal Number: ", x)
# # print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x));
# # print("Original Number: ", y)
# # print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y));
# # print()

# # #35. Write a Python program to display a number with a comma separator. 

# # x = 3000000
# # y = 30000000
# # print("\nOriginal Number: ", x)
# # print("Formatted Number with comma separator: "+"{:,}".format(x));
# # print("Original Number: ", y)
# # print("Formatted Number with comma separator: "+"{:,}".format(y));
# # print()

# # #36. Write a Python program to format a number with a percentage. 

# # x = 0.25
# # y = -0.25
# # print("\nOriginal Number: ", x)
# # print("Formatted Number with percentage: "+"{:.2%}".format(x));
# # print("Original Number: ", y)
# # print("Formatted Number with percentage: "+"{:.2%}".format(y));
# # print()

# # #37. Write a Python program to display a number in left, right and center aligned of width 10. 

# # x = 22
# # print("\nOriginal Number: ", x)
# # print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
# # print("Right aligned (width 10)  :"+"{:10d}".format(x));
# # print("Center aligned (width 10) :"+"{:^10d}".format(x));
# # print()

# # #38. Write a Python program to count occurrences of a substring in a string. 

# # str1 = 'The quick brown fox jumps over the lazy dog.'
# # print()
# # print(str1.count("fox"))
# # print()

# # #39. Write a Python program to reverse a string. 

# # def reverse_string(str1):
    # # return ''.join(reversed(str1))
# # print()
# # print(reverse_string("abcdef"))
# # print(reverse_string("Python Exercises."))
# # print()

# # #40. Write a Python program to reverse words in a string. 

# # def reverse_string_words(text):
    # # for line in text.split('\n'):
        # # return(' '.join(line.split()[::-1]))
# # print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
# # print(reverse_string_words("Python Exercises."))

# # #41. Write a Python program to strip a set of characters from a string. 

# # def strip_chars(str, chars):
    # # return "".join(c for c in str if c not in chars)

# # print("\nOriginal String: ")
# # print("The quick brown fox jumps over the lazy dog.")
# # print("After stripping a,e,i,o,u")      
# # print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
# # print()

# # #42. Write a Python program to count repeated characters in a string. 

# # import collections
# # str1 = 'thequickbrownfoxjumpsoverthelazydog'
# # d = collections.defaultdict(int)
# # for c in str1:
    # # d[c] += 1

# # for c in sorted(d, key=d.get, reverse=True):
  # # if d[c] > 1:
      # # print('%s %d' % (c, d[c]))

# # #43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder. 

# # area = 1256.66
# # volume = 1254.725
# # decimals = 2
# # print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
# # decimals = 3
# # print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))

# # #44. Write a Python program to print the index of the character in a string. 

# # str1 = "w3resource"
# # for index, char in enumerate(str1):
    # # print("Current character", char, "position at", index )

# # #45. Write a Python program to check if a string contains all letters of the alphabet. 

# # import string
# # alphabet = set(string.ascii_lowercase)
# # input_string = 'The quick brown fox jumps over the lazy dog'
# # print(set(input_string.lower()) >= alphabet)
# # input_string = 'The quick brown fox jumps over the lazy cat'
# # print(set(input_string.lower()) >= alphabet)

# # #46. Write a Python program to convert a string in a list. 

# # str1 = "The quick brown fox jumps over the lazy dog."
# # print(str1.split(' '))
# # str1 = "The-quick-brown-fox-jumps-over-the-lazy-dog."
# # print(str1.split('-'))

# # #47. Write a Python program to lowercase first n characters in a string. 

# # str1 = 'W3RESOURCE.COM'
# # print(str1[:4].lower() + str1[4:])

# # #48. Write a Python program to swap comma and dot in a string. 

# # amount = "32.054,23"
# # maketrans = amount.maketrans
# # amount = amount.translate(maketrans(',.', '.,'))
# # print(amount)

# # #49. Write a Python program to count and display the vowels of a given text. 

# # def vowel(text):
    # # vowels = "aeiuoAEIOU"
    # # print(len([letter for letter in text if letter in vowels]))
    # # print([letter for letter in text if letter in vowels])
# # vowel('w3resource');

# # #50. Write a Python program to split a string on the last occurrence of the delimiter. 

# # str1 = "w,3,r,e,s,o,u,r,c,e"
# # print(str1.rsplit(',', 1))
# # print(str1.rsplit(',', 2))
# # print(str1.rsplit(',', 5))

# # #51. Write a Python program to find the first non-repeating character in given string. 

# # def first_non_repeating_character(str1):
  # # char_order = []
  # # ctr = {}
  # # for c in str1:
    # # if c in ctr:
      # # ctr[c] += 1
    # # else:
      # # ctr[c] = 1 
      # # char_order.append(c)
  # # for c in char_order:
    # # if ctr[c] == 1:
      # # return c
  # # return None

# # print(first_non_repeating_character('abcdef'))
# # print(first_non_repeating_character('abcabcdef'))
# # print(first_non_repeating_character('aabbcc'))

# # #52. Write a Python program to print all permutations with given repetition number of characters of a given string. 

# # from itertools import product
# # def all_repeat(str1, rno):
  # # chars = list(str1)
  # # results = []
  # # for c in product(chars, repeat = rno):
    # # results.append(c)
  # # return results
# # print(all_repeat('xyz', 3))
# # print(all_repeat('xyz', 2))
# # print(all_repeat('abcd', 4))

# # #53. Write a Python program to find the first repeated character in a given string. 

# # def first_repeated_char(str1):
  # # for index,c in enumerate(str1):
    # # if str1[:index+1].count(c) > 1:
      # # return c 
  # # return "None"

# # print(first_repeated_char("abcdabcd"))
# # print(first_repeated_char("abcd"))

# # #54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest. 

# # def first_repeated_char_smallest_distance(str1):
  # # temp = {}
  # # for ch in str1:
    # # if ch in temp:
      # # return ch;
    # # else:
      # # temp[ch] = 0
  # # return 'None'
# # print(first_repeated_char_smallest_distance("abcabc"))
# # print(first_repeated_char_smallest_distance("abbcabc"))
# # print(first_repeated_char_smallest_distance("abcbabc"))
# # print(first_repeated_char_smallest_distance("abcxxy"))
# # print(first_repeated_char_smallest_distance("abc"))

# # #55.Write a Python program to find the first repeated word in a given string. 

# # def first_repeated_word(str1):
  # # temp = set()
  # # for word in str1.split():
    # # if word in temp:
      # # return word;
    # # else:
      # # temp.add(word)
  # # return 'None'
# # print(first_repeated_word("ab ca bc ab"))
# # print(first_repeated_word("ab ca bc ab ca ab bc"))
# # print(first_repeated_word("ab ca bc ca ab bc"))
# # print(first_repeated_word("ab ca bc"))

# # #56. Write a Python program to find the second most repeated word in a given string. 

# # def word_count(str):
    # # counts = dict()
    # # words = str.split()

    # # for word in words:
        # # if word in counts:
            # # counts[word] += 1
        # # else:
            # # counts[word] = 1

    # # counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    # # #print(counts_x)
    # # return counts_x[-2]
 
# # print(word_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))

# # #57.Write a Python program to remove spaces from a given string. 

# # def remove_spaces(str1):
  # # str1 = str1.replace(' ','')
  # # return str1
    
# # print(remove_spaces("w 3 res ou r ce"))
# # print(remove_spaces("a b c"))

# # #58. Write a Python program to move spaces to the front of a given string. 

# # def move_Spaces_front(str1):
  # # noSpaces_char = [ch for ch in str1 if ch!=' ']
  # # spaces_char = len(str1) - len(noSpaces_char)
  # # result = ' '*spaces_char
  # # result = '"'+result + ''.join(noSpaces_char)+'"'
  # # return(result)

# # print(move_Spaces_front("w3resource .  com  "))
# # print(move_Spaces_front("   w3resource.com  "))

# # #59. Write a Python program to find the maximum occurring character in a given string. 

# # def get_max_occuring_char(str1):
  # # ASCII_SIZE = 256
  # # ctr = [0] * ASCII_SIZE
  # # max = -1
  # # ch = ''
  # # for i in str1:
    # # ctr[ord(i)]+=1;
 
  # # for i in str1:
    # # if max < ctr[ord(i)]:
      # # max = ctr[ord(i)]
      # # ch = i
  # # return ch

# # print(get_max_occuring_char("Python: Get file creation and modification date/times"))
# # print(get_max_occuring_char("abcdefghijkb"))

# # #60. Write a Python program to capitalize first and last letters of each word of a given string. 

# # def capitalize_first_last_letters(str1):
     # # str1 = result = str1.title()
     # # result =  ""
     # # for word in str1.split():
        # # result += word[:-1] + word[-1].upper() + " "
     # # return result[:-1]  
     
# # print(capitalize_first_last_letters("python exercises practice solution"))
# # print(capitalize_first_last_letters("w3resource"))

# # #61. Write a Python program to remove duplicate characters of a given string. 

# # from collections import OrderedDict
# # def remove_duplicate(str1):
  # # return "".join(OrderedDict.fromkeys(str1))
     
# # print(remove_duplicate("python exercises practice solution"))
# # print(remove_duplicate("w3resource"))

# # #62. Write a Python program to compute sum of digits of a given string. 

# # def sum_digits_string(str1):
    # # sum_digit = 0
    # # for x in str1:
        # # if x.isdigit() == True:
            # # z = int(x)
            # # sum_digit = sum_digit + z

    # # return sum_digit
     
# # print(sum_digits_string("123abcd45"))
# # print(sum_digits_string("abcd1234"))

# # #63. Write a Python program to remove leading zeros from an IP address. 

# # def remove_zeros_from_ip(ip_add):
  # # new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])  
  # # return new_ip_add ;

# # print(remove_zeros_from_ip("255.024.01.01"))
# # print(remove_zeros_from_ip("127.0.0.01 "))

# # #64. Write a Python program to find maximum length of consecutive 0's in a given binary string. 

# # def max_consecutive_0(input_str): 
     # # return  max(map(len,input_str.split('1')))
# # str1 = '111000010000110'
# # print("Original string:" + str1)
# # print("Maximum length of consecutive 0’s:")
# # print(max_consecutive_0(str1))
# # str1 = '111000111'
# # print("Original string:" + str1)
# # print("Maximum length of consecutive 0’s:")
# # print(max_consecutive_0(str1))

# # #65. Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters". 

# # from collections import Counter 
# # def common_chars(str1,str2): 	
	# # d1 = Counter(str1) 
	# # d2 = Counter(str2) 
	# # common_dict = d1 & d2 
	# # if len(common_dict) == 0: 
		# # return "No common characters."
# # def make_map(s):
    # # temp_map = {}
    # # for char in s:
        # # if char not in temp_map:
            # # temp_map[char] = 1
        # # else:
            # # temp_map[char] +=1 
    # # return temp_map        
# # def make_anagram(str1, str2):
    # # str1_map1 = make_map(str1)
    # # str2_map2 = make_map(str2)
 
    # # ctr = 0
    # # for key in str2_map2.keys():
        # # if key not in str1_map1:
            # # ctr += str2_map2[key]
        # # else:
            # # ctr += max(0, str2_map2[key]-str1_map1[key])
 
    # # for key in str1_map1.keys():
        # # if key not in str2_map2:
            # # ctr += str1_map1[key]
        # # else:
            # # ctr += max(0, str1_map1[key]-str2_map2[key]) 
    # # return ctr 
# # str1 = input("Input string1: ")
# # str2 = input("Input string2: ")
# # print(make_anagram(str1, str2))

	# # # list of common elements 
# # common_chars = list(common_dict.elements()) 
# # common_chars = sorted(common_chars) 

# # return ''.join(common_chars) 

# # str1 = 'Python'
# # str2 = 'PHP'
# # print("Two strings: "+str1+' : '+str2)
# # print(common_chars(str1, str2))
# # str1 = 'Java'
# # str2 = 'PHP'
# # print("Two strings: "+str1+' : '+str2)
# # print(common_chars(str1, str2))

# # #66. Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings. 

# # def make_map(s):
    # # temp_map = {}
    # # for char in s:
        # # if char not in temp_map:
            # # temp_map[char] = 1
        # # else:
            # # temp_map[char] +=1 
    # # return temp_map        
# # def make_anagram(str1, str2):
    # # str1_map1 = make_map(str1)
    # # str2_map2 = make_map(str2)
 
    # # ctr = 0
    # # for key in str2_map2.keys():
        # # if key not in str1_map1:
            # # ctr += str2_map2[key]
        # # else:
            # # ctr += max(0, str2_map2[key]-str1_map1[key])
 
    # # for key in str1_map1.keys():
        # # if key not in str2_map2:
            # # ctr += str1_map1[key]
        # # else:
            # # ctr += max(0, str1_map1[key]-str2_map2[key]) 
    # # return ctr 
# # str1 = input("Input string1: ")
# # str2 = input("Input string2: ")
# # print(make_anagram(str1, str2))

# # #67. Write a Python program to remove all consecutive duplicates of a given string. 

# # from itertools import groupby 
# # def remove_all_consecutive(str1): 
	# # result_str = [] 
	# # for (key,group) in groupby(str1): 
		# # result_str.append(key) 

	# # return ''.join(result_str)
	
# # str1 = 'xxxxxyyyyy'
# # print("Original string:" + str1)
# # print("After removing consecutive duplicates: " + str1)
# # print(remove_all_consecutive(str1))

# # #68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string. 

# # from collections import Counter  
# # def generateStrings(input): 
     # # str_char_ctr = Counter(input) 
     # # part1 = [ key for (key,count) in str_char_ctr.items() if count==1] 
     # # part2 = [ key for (key,count) in str_char_ctr.items() if count>1] 
     # # part1.sort() 
     # # part2.sort()
     # # return part1,part2
# # input = "aabbcceffgh"
# # s1, s2 = generateStrings(input)
# # print(''.join(s1))   
# # print(''.join(s2))

# # #69. Write a Python program to find the longest common sub-string from two given strings. 

# # from difflib import SequenceMatcher 
  
# # def longest_Substring(s1,s2): 
  
     # # seq_match = SequenceMatcher(None,s1,s2) 
  
     # # match = seq_match.find_longest_match(0, len(s1), 0, len(s2)) 
  
     # # # return the longest substring 
     # # if (match.size!=0): 
          # # return (s1[match.a: match.a + match.size])  
     # # else: 
          # # return ('Longest common sub-string not present')  

# # s1 = 'abcdefgh'
# # s2 = 'xswerabcdwd'
# # print("Original Substrings:\n",s1+"\n",s2)
# # print("\nCommon longest sub_string:")
# # print(longest_Substring(s1,s2))

# # #70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings. 

# # def uncommon_chars_concat(s1, s2):   
     
     # # set1 = set(s1) 
     # # set2 = set(s2) 
  
     # # common_chars = list(set1 & set2) 
     # # result = [ch for ch in s1 if ch not in common_chars] + [ch for ch in s2 if ch not in common_chars] 
     # # return(''.join(result))

# # s1 = 'abcdpqr'
# # s2 = 'xyzabcd'
# # print("Original Substrings:\n",s1+"\n",s2)
# # print("\nAfter concatenating uncommon characters:")
# # print(uncommon_chars_concat(s1, s2))

# # #71. Write a Python program to move all spaces to the front of a given string in single traversal. 

# # def moveSpaces(str1): 
    # # no_spaces = [char for char in str1 if char!=' ']   
    # # space= len(str1) - len(no_spaces)
    # # # Create string with spaces
    # # result = ' '*space    
    # # return result + ''.join(no_spaces)
  
# # s1 = "Python Exercises"
# # print("Original String:\n",s1)

# # print("\nAfter moving all spaces to the front:")
# # print(moveSpaces(s1))

# # #72. Write a Python program to remove all consecutive duplicates from a given string. 

# # import itertools
# # def remove_consecutive_duplicates(s1):
     # # return (''.join(i for i, _ in itertools.groupby(s1)))

# # s1= "aabcdaee"
# # print("Original String: ",s1)
# # print("\nRemoving all consecutive duplicates:")
# # print(remove_consecutive_duplicates(s1))

# # #73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string. 

# # def count_chars(str):
     # # upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
     # # for i in range(len(str)):
          # # if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          # # elif str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1
          # # elif str[i] >= '0' and str[i] <= '9': number_ctr += 1
          # # else: special_ctr += 1
     # # return upper_ctr, lower_ctr, number_ctr, special_ctr
           
# # str = "@W3Resource.Com"
# # print("Original Substrings:",str)
# # u, l, n, s = count_chars(str)
# # print('\nUpper case characters: ',u)
# # print('Lower case characters: ',l)
# # print('Number case: ',n)
# # print('Special case characters: ',s)

# # #74. Write a Python program to find the minimum window in a given string which will contain all the characters of another given string. 

# # import collections
# # def min_window(str1, str2):
    # # result_char, missing_char = collections.Counter(str2), len(str2)
    # # i = p = q = 0
    # # for j, c in enumerate(str1, 1):
        # # missing_char -= result_char[c] > 0
        # # result_char[c] -= 1
        # # if not missing_char:
            # # while i < q and result_char[str1[i]] < 0:
                # # result_char[str1[i]] += 1
                # # i += 1
            # # if not q or j - i <= q - p:
                # # p, q = i, j
    # # return str1[p:q]
           
# # str1 = "PRWSOERIUSFK"
# # str2 = "OSU"
# # print("Original Strings:\n",str1,"\n",str2)
# # print("Minimum window:")
# # print(min_window(str1,str2))

# # #75. Write a Python program to find smallest window that contains all characters of a given string. 

# # from collections import defaultdict   

# # def find_sub_string(str): 
    # # str_len = len(str) 
      
    # # # Count all distinct characters. 
    # # dist_count_char = len(set([x for x in str])) 
  
    # # ctr, start_pos, start_pos_index, min_len = 0, 0, -1, 9999999999
    # # curr_count = defaultdict(lambda: 0) 
    # # for i in range(str_len): 
        # # curr_count[str[i]] += 1
 
        # # if curr_count[str[i]] == 1: 
            # # ctr += 1
  
        # # if ctr == dist_count_char: 
            # # while curr_count[str[start_pos]] > 1: 
                # # if curr_count[str[start_pos]] > 1: 
                    # # curr_count[str[start_pos]] -= 1
                # # start_pos += 1
  
            # # len_window = i - start_pos + 1
            # # if min_len > len_window: 
                # # min_len = len_window 
                # # start_pos_index = start_pos 
    # # return str[start_pos_index: start_pos_index + min_len] 
      
# # str1 = "asdaewsqgtwwsa"
# # print("Original Strings:\n",str1)
# # print("\nSmallest window that contains all characters of the said string:")
# # print(find_sub_string(str1)) 

# # #76. Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters. 

# # def count_k_dist(str1, k): 
	# # str_len = len(str1) 
	
	# # result = 0

	# # ctr = [0] * 27

	# # for i in range(0, str_len): 
		# # dist_ctr = 0

		# # ctr = [0] * 27

		# # for j in range(i, str_len): 
			
			# # if(ctr[ord(str1[j]) - 97] == 0): 
				# # dist_ctr += 1

			# # ctr[ord(str1[j]) - 97] += 1

			# # if(dist_ctr == k): 
				# # result += 1
			# # if(dist_ctr > k): 
				# # break

	# # return result 

# # str1 = input("Input a string (lowercase alphabets):")
# # k = int(input("Input k: "))
# # print("Number of substrings with exactly", k, "distinct characters : ", end = "") 
# # print(count_k_dist(str1, k))

# # #77. Write a Python program to count number of non-empty substrings of a given string. 

# # def number_of_substrings(str): 
	# # str_len = len(str); 
	# # return int(str_len * (str_len + 1) / 2); 

# # str1 = input("Input a string: ")
# # print("Number of substrings:") 
# # print(number_of_substrings(str1))

# # #78. Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet. 

# # def count_char_position(str1): 
    # # count_chars = 0
    # # for i in range(len(str1)):
        # # if ((i == ord(str1[i]) - ord('A')) or 
            # # (i == ord(str1[i]) - ord('a'))): 
            # # count_chars += 1
    # # return count_chars 
  
# # str1 = input("Input a string: ")
# # print("Number of characters of the said string at same position as in English alphabet:")
# # print(count_char_position(str1))

# # #79. Write a Python program to find smallest and largest word in a given string. 

# # def smallest_largest_words(str1):
    # # word = "";
    # # all_words = [];
    # # str1 = str1 + " ";
    # # for i in range(0, len(str1)):
        # # if(str1[i] != ' '):
            # # word = word + str1[i];  
        # # else:
            # # all_words.append(word);  
            # # word = "";  
          
    # # small = large = all_words[0];  
   
# # #Find smallest and largest word in the str1  
    # # for k in range(0, len(all_words)):
        # # if(len(small) > len(all_words[k])):
            # # small = all_words[k];
        # # if(len(large) < len(all_words[k])):
            # # large = all_words[k];
    # # return small,large;

# # str1 = "Write a Java program to sort an array of given integers using Quick sort Algorithm.";  
# # print("Original Strings:\n",str1)
# # small, large = smallest_largest_words(str1)  
# # print("Smallest word: " + small);  
# # print("Largest word: " + large); 

# # #80. Write a Python program to count number of substrings with same first and last characters of a given string. 

# # def no_of_substring_with_equalEnds(str1): 
	# # result = 0; 
	# # n = len(str1); 
	# # for i in range(n): 
		# # for j in range(i, n): 
			# # if (str1[i] == str1[j]): 
				# # result = result + 1
	# # return result 
# # str1 = input("Input a string: ")
# # print(no_of_substring_with_equalEnds(str1))

# # #81

# # #____________________________________ Dictonary __________________________________


# # #1. Write a Python script to sort (ascending and descending) a dictionary by value. 

# # import operator
# # d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # print('Original dictionary : ',d)
# # sorted_d = sorted(d.items(), key=operator.itemgetter(0))
# # print('Dictionary in ascending order by value : ',sorted_d)
# # sorted_d = dict( sorted(d.items(), key=operator.itemgetter(0),reverse=True))
# # print('Dictionary in descending order by value : ',sorted_d)

# # #2. Write a Python script to add a key to a dictionary. 

# # d = {0:10, 1:20}
# # print(d)
# # d.update({2:30})
# # print(d)

# # #3. Write a Python script to concatenate following dictionaries to create a new one. 

# # dic1={1:10, 2:20}
# # dic2={3:30, 4:40}
# # dic3={5:50,6:60}
# # dic4 = {}
# # for d in (dic1, dic2, dic3): dic4.update(d)
# # print(dic4)

# # #4. Write a Python script to check if a given key already exists in a dictionary. 

# # d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # def is_key_present(x):
  # # if x in d:
      # # print('Key is present in the dictionary')
  # # else:
      # # print('Key is not present in the dictionary')
# # is_key_present(5)
# # is_key_present(9)

# # #5. Write a Python program to iterate over dictionaries using for loops. 

# # d = {'x': 10, 'y': 20, 'z': 30} 
# # for dict_key, dict_value in d.items():
    # # print(dict_key,'->',dict_value)
	
# # #6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

# # n=int(input("Input a number "))
# # d = dict()

# # for x in range(1,n+1):
    # # d[x]=x*x

# # print(d) 

# # #7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 

# # d=dict()
# # for x in range(1,16):
    # # d[x]=x**2
# # print(d)  

# # #8. Write a Python script to merge two Python dictionaries. 

# # d1 = {'a': 100, 'b': 200}
# # d2 = {'x': 300, 'y': 200}
# # d = d1.copy()
# # d.update(d2)
# # print(d)

# # #9. Write a Python program to iterate over dictionaries using for loops. 

# # d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# # for color_key, value in d.items():
     # # print(color_key, 'corresponds to ', d[color_key]) 

# # #10. Write a Python program to sum all the items in a dictionary. 

# # my_dict = {'data1':100,'data2':-54,'data3':247}
# # print(sum(my_dict.values()))

# # #11. Write a Python program to multiply all the items in a dictionary. 

# # my_dict = {'data1':100,'data2':-54,'data3':247}
# # result=1
# # for key in my_dict:    
    # # result=result * my_dict[key]

# # print(result)

# # #12. Write a Python program to remove a key from a dictionary. 

# # myDict = {'a':1,'b':2,'c':3,'d':4}
# # print(myDict)
# # if 'a' in myDict: 
    # # del myDict['a']
# # print(myDict)

# # #13. Write a Python program to map two lists into a dictionary. 

# # keys = ['red', 'green', 'blue']
# # values = ['#FF0000','#008000', '#0000FF']
# # color_dictionary = dict(zip(keys, values))
# # print(color_dictionary)

# # #14. Write a Python program to sort a dictionary by key. 

# # color_dict = {'red':'#FF0000',
          # # 'green':'#008000',
          # # 'black':'#000000',
          # # 'white':'#FFFFFF'}

# # for key in sorted(color_dict):
    # # print("%s: %s" % (key, color_dict[key]))
	
# # #15. Write a Python program to get the maximum and minimum value in a dictionary. 

# # my_dict = {'x':500, 'y':5874, 'z': 560}

# # key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# # key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# # print('Maximum Value: ',my_dict[key_max])
# # print('Minimum Value: ',my_dict[key_min])

# # #16. Write a Python program to get a dictionary from an object's fields. 

# # class dictObj(object):
     # # def __init__(self):
         # # self.x = 'red'
         # # self.y = 'Yellow'
         # # self.z = 'Green'
     # # def do_nothing(self):
         # # pass
# # test = dictObj()
# # print(test.__dict__)

# # #17. Write a Python program to remove duplicates from Dictionary. 

# # student_data = {'id1': 
   # # {'name': ['Sara'], 
    # # 'class': ['V'], 
    # # 'subject_integration': ['english, math, science']
   # # },
 # # 'id2': 
  # # {'name': ['David'], 
    # # 'class': ['V'], 
    # # 'subject_integration': ['english, math, science']
   # # },
 # # 'id3': 
    # # {'name': ['Sara'], 
    # # 'class': ['V'], 
    # # 'subject_integration': ['english, math, science']
   # # },
 # # 'id4': 
   # # {'name': ['Surya'], 
    # # 'class': ['V'], 
    # # 'subject_integration': ['english, math, science']
   # # },
# # }

# # result = {}

# # for key,value in student_data.items():
    # # if value not in result.values():
        # # result[key] = value

# # print(result)

# # #18. Write a Python program to check a dictionary is empty or not. 

# # my_dict = {}

# # if not bool(my_dict):
    # # print("Dictionary is empty")
	
# # #19. Write a Python program to combine two dictionary adding values for common keys. 

# # from collections import Counter
# # d1 = {'a': 100, 'b': 200, 'c':300}
# # d2 = {'a': 300, 'b': 200, 'd':400}
# # d = Counter(d1) + Counter(d2)
# # print(d)

# # #20. Write a Python program to print all unique values in a dictionary. 

# # L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# # print("Original List: ",L)
# # u_value = set( val for dic in L for val in dic.values())
# # print("Unique Values: ",u_value)

# # #21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 

# # import itertools      
# # d ={'1':['a','b'], '2':['c','d']}
# # for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    # # print(''.join(combo))
	
# # #22. Write a Python program to find the highest 3 values in a dictionary. 

# # from heapq import nlargest
# # my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# # three_largest = nlargest(3, my_dict, key=my_dict.get)
# # print(three_largest) 

# # #23. Write a Python program to combine values in python list of dictionaries. 

# # from collections import Counter
# # item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# # result = Counter()
# # for d in item_list:
    # # result[d['item']] += d['amount']
# # print(result) 

# # #24. Write a Python program to create a dictionary from a string. 

# # from collections import defaultdict, Counter
# # str1 = 'w3resource' 
# # my_dict = {}
# # for letter in str1:
    # # my_dict[letter] = my_dict.get(letter, 0) + 1
# # print(my_dict)

# # #25. Write a Python program to print a dictionary in table format. 

# # my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# # for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    # # print(*row)

# # #26. Write a Python program to count the values associated with key in a dictionary. 

# # student = [{'id': 1, 'success': True, 'name': 'Lary'},
 # # {'id': 2, 'success': False, 'name': 'Rabi'},
 # # {'id': 3, 'success': True, 'name': 'Alex'}]
# # print(sum(d['success'] for d in student))

# # #27. Write a Python program to convert a list into a nested dictionary of keys. 

# # num_list = [1, 2, 3, 4]
# # new_dict = current = {}
# # for name in num_list:
    # # current[name] = {}
    # # current = current[name]
# # print(new_dict)

# # #28. Write a Python program to sort a list alphabetically in a dictionary. 

# # num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# # sorted_dict = {x: sorted(y) for x, y in num.items()}
# # print(sorted_dict)

# # #29. Write a Python program to remove spaces from dictionary keys. 

# # student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# # print("Original dictionary: ",student_list)
# # student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
# # print("New dictionary: ",student_dict)

# # #30. Write a Python program to get the top three items in a shop. 

# # from heapq import nlargest
# # from operator import itemgetter
# # items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# # for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    # # print(name, value)
	
# # #31. Write a Python program to get the key, value and item in a dictionary. 

# # dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # print("key  value  count")
# # for count, (key, value) in enumerate(dict_num.items(), 1):
    # # print(key,'   ',value,'    ', count)

# # #32. Write a Python program to print a dictionary line by line. 

# # students = {'Aex':{'class':'V',
        # # 'rolld_id':2},
        # # 'Puja':{'class':'V',
        # # 'roll_id':3}}
# # for a in students:
    # # print(a)
    # # for b in students[a]:
        # # print (b,':',students[a][b])
		
# # #33. Write a Python program to check multiple keys exists in a dictionary. 

# # student = {
  # # 'name': 'Alex',
  # # 'class': 'V',
  # # 'roll_id': '2'
# # }
# # print(student.keys() >= {'class', 'name'})
# # print(student.keys() >= {'name', 'Alex'})
# # print(student.keys() >= {'roll_id', 'name'})

# # #34. Write a Python program to count number of items in a dictionary value that is a list. 

# # dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# # ctr = sum(map(len, dict.values()))
# # print(ctr)

# # #35. Write a Python program to sort Counter by value. 

# # from collections import Counter
# # x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
# # print(x.most_common())

# # #36. Write a Python program to create a dictionary from two lists without losing duplicate values. 

# # from collections import defaultdict
# # class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# # id_list = [1, 2, 2, 3]
# # temp = defaultdict(set)
# # for c, i in zip(class_list, id_list):
    # # temp[c].add(i)
# # print(temp)

# # #37. Write a Python program to replace dictionary values with their sum. 

# # def sum_math_v_vi_average(list_of_dicts):
    # # for d in list_of_dicts:
        # # n1 = d.pop('V')
        # # n2 = d.pop('VI')
        # # d['V+VI'] = (n1 + n2)/2
    # # return list_of_dicts 
# # student_details= [
  # # {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  # # {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  # # {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# # ]
# # print(sum_math_v_vi_average(student_details))

# # #38. Write a Python program to match key values in two dictionaries. 

# # x = {'key1': 1, 'key2': 3, 'key3': 2}
# # y = {'key1': 1, 'key2': 2}
# # for (key, value) in set(x.items()) & set(y.items()):
    # # print('%s: %s is present in both x and y' % (key, value))



# # #_______________________ Functions ___________________________


# # #1. Write a Python function to find the Max of three numbers. 
# # def max_of_two( x, y ):
    # # if x > y:
        # # return x
    # # return y
# # def max_of_three( x, y, z ):
    # # return max_of_two( x, max_of_two( y, z ) )
# # print(max_of_three(3, 6, -5))

# # #2. Write a Python function to sum all the numbers in a list. 

# # def sum(numbers):
    # # total = 0
    # # for x in numbers:
        # # total += x
    # # return total
# # print(sum((8, 2, 3, 0, 7)))

# # #3. Write a Python function to multiply all the numbers in a list. 

# # def multiply(numbers):  
    # # total = 1
    # # for x in numbers:
        # # total *= x  
    # # return total  
# # print(multiply((8, 2, 3, -1, 7)))

# # #4. Write a Python program to reverse a string. 

# # def string_reverse(str1):

    # # rstr1 = ''
    # # index = len(str1)
    # # while index > 0:
        # # rstr1 += str1[ index - 1 ]
        # # index = index - 1
    # # return rstr1
# # print(string_reverse('1234abcd'))

# # #5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 

# # def factorial(n):
    # # if n == 0:
        # # return 1
    # # else:
        # # return n * factorial(n-1)
# # n=int(input("Input a number to compute the factiorial : "))
# # print(factorial(n))

# # #6. Write a Python function to check whether a number is in a given range. 

# # def test_range(n):
    # # if n in range(3,9):
        # # print( " %s is in the range"%str(n))
    # # else :
        # # print("The number is outside the given range.")
# # test_range(5)

# # #7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

# # def string_test(s):
    # # d={"UPPER_CASE":0, "LOWER_CASE":0}
    # # for c in s:
        # # if c.isupper():
           # # d["UPPER_CASE"]+=1
        # # elif c.islower():
           # # d["LOWER_CASE"]+=1
        # # else:
           # # pass
    # # print ("Original String : ", s)
    # # print ("No. of Upper case characters : ", d["UPPER_CASE"])
    # # print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# # string_test('The quick Brown Fox')

# # #8. Write a Python function that takes a list and returns a new list with unique elements of the first list. 

# # def unique_list(l):
  # # x = []
  # # for a in l:
    # # if a not in x:
      # # x.append(a)
  # # return x

# # print(unique_list([1,2,3,3,3,3,4,5])) 

# # #9. Write a Python function that takes a number as a parameter and check the number is prime or not. 

# # def test_prime(n):
    # # if (n==1):
        # # return False
    # # elif (n==2):
        # # return True;
    # # else:
        # # for x in range(2,n):
            # # if(n % x==0):
                # # return False
        # # return True             
# # print(test_prime(9))

# # #10. Write a Python program to print the even numbers from a given list. 

# # def is_even_num(l):
    # # enum = []
    # # for n in l:
        # # if n % 2 == 0:
            # # enum.append(n)
    # # return enum
# # print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# # #11. Write a Python function to check whether a number is perfect or not. 

# # def perfect_number(n):
    # # sum = 0
    # # for x in range(1, n):
        # # if n % x == 0:
            # # sum += x
    # # return sum == n
# # print(perfect_number(6))

# # #12. Write a Python function that checks whether a passed string is palindrome or not. 

# # def isPalindrome(string):
	# # left_pos = 0
	# # right_pos = len(string) - 1
	
	# # while right_pos >= left_pos:
		# # if not string[left_pos] == string[right_pos]:
			# # return False
		# # left_pos += 1
		# # right_pos -= 1
	# # return True
# # print(isPalindrome('aza')) 

# # #13. Write a Python function that prints out the first n rows of Pascal's triangle. 

# # def pascal_triangle(n):
   # # trow = [1]
   # # y = [0]
   # # for x in range(max(n,0)):
      # # print(trow)
      # # trow=[l+r for l,r in zip(trow+y, y+trow)]
   # # return n>=1
# # pascal_triangle(6) 

# # #14. Write a Python function to check whether a string is a pangram or not. 

# # import string, sys
# # def ispangram(str1, alphabet=string.ascii_lowercase):
    # # alphaset = set(alphabet)
    # # return alphaset <= set(str1.lower())
 
# # print ( ispangram('The quick brown fox jumps over the lazy dog')) 

# # #15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 

# # items=[n for n in input().split('-')]
# # items.sort()
# # print('-'.join(items))

# # #16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). 

# # def printValues():
	# # l = list()
	# # for i in range(1,21):
		# # l.append(i**2)
	# # print(l)
		
# # printValues()

# # #17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python. 

# # def make_bold(fn):
    # # def wrapped():
        # # return "<b>" + fn() + "</b>"
    # # return wrapped

# # def make_italic(fn):
    # # def wrapped():
        # # return "<i>" + fn() + "</i>"
    # # return wrapped

# # def make_underline(fn):
    # # def wrapped():
        # # return "<u>" + fn() + "</u>"
    # # return wrapped
# # @make_bold
# # @make_italic
# # @make_underline
# # def hello():
    # # return "hello world"
# # print(hello()) ## returns "<b><i><u>hello world</u></i></b>"

# # #18. Write a Python program to execute a string containing Python code. 

# # mycode = 'print("hello world")'
# # code = """
# # def mutiply(x,y):
    # # return x*y

# # print('Multiply of 2 and 3 is: ',mutiply(2,3))
# # """
# # exec(mycode)
# # exec(code)

# # #19. Write a Python program to access a function inside a function. 

# # def test(a):
        # # def add(b):
                # # nonlocal a
                # # a += 1
                # # return a+b
        # # return add
# # func= test(4)
# # print(func(4))

# # #20. Write a Python program to detect the number of local variables declared in a function. 

# # def abc():
    # # x = 1
    # # y = 2
    # # str1= "w3resource"
    # # print("Python Exercises")

# # print(abc.__code__.co_nlocals)

# # #

# # #____________________________ List _______________________________________



# # #1. Write a Python program to sum all the items in a list. 

# # def sum_list(items):
    # # sum_numbers = 0
    # # for x in items:
        # # sum_numbers += x    #sum_numbers=sum_numbers+x
    # # return sum_numbers
# # print(sum_list([1,2,-8]))

# # #2. Write a Python program to multiplies all the items in a list. 

# # def multiply_list(items):
    # # tot = 1
    # # for x in items:
        # # tot *= x
    # # return tot
# # print(multiply_list([1,2,-8]))

# # #3. Write a Python program to get the largest number from a list. 

# # def max_num_in_list( list ):
    # # max = list[ 0 ]
    # # for a in list:
        # # if a > max:
            # # max = a
    # # return max
# # print(max_num_in_list([1, 2, -8, 0]))

# # #4. Write a Python program to get the smallest number from a list. 

# # def smallest_num_in_list( list ):
    # # min = list[ 0 ]
    # # for a in list:
        # # if a < min:
            # # min = a
    # # return min
# # print(smallest_num_in_list([1, 2, -8, 0]))

# # #5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 

# # def match_words(words):
  # # ctr = 0

  # # for word in words:
    # # if len(word) > 1 and word[0] == word[-1]:
      # # ctr += 1
  # # return ctr

# # print(match_words(['abc', 'xyz', 'aba', '1221']))

# # #6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 

# # def last(n): return n[-1]

# # def sort_list_last(tuples):
  # # return sorted(tuples, key=last)

# # print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# # #7. Write a Python program to remove duplicates from a list. 

# # a = [10,20,30,20,10,50,60,40,80,50,40]

# # dup_items = set()
# # uniq_items = []
# # for x in a:
    # # if x not in dup_items:
        # # uniq_items.append(x)
        # # dup_items.add(x)

# # print(dup_items)

# # #8. Write a Python program to check a list is empty or not. 

# # l = []
# # if not l:
  # # print("List is empty")
  
# # #9. Write a Python program to clone or copy a list. 

# # original_list = [10, 22, 44, 23, 4]
# # new_list = list(original_list)
# # print(original_list)
# # print(new_list)

# # #10. Write a Python program to find the list of words that are longer than n from a given list of words. 

# # def long_words(n, str):
    # # word_len = []
    # # txt = str.split(" ")
    # # for x in txt:
        # # if len(x) > n:
            # # word_len.append(x)
    # # return word_len	
# # print(long_words(3, "The quick brown fox jumps over the lazy dog"))

# # #11. Write a Python function that takes two lists and returns True if they have at least one common member. 

# # def common_data(list1, list2):
     # # result = False
     # # for x in list1:
         # # for y in list2:
             # # if x == y:
                 # # result = True
                 # # return result
# # print(common_data([1,2,3,4,5], [5,6,7,8,9]))
# # print(common_data([1,2,3,4,5], [6,7,8,9]))

# # #12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 

# # color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# # print(color)

# # #13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 

# # array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
# # print(array)

# # #14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 

# # num = [7,8, 120, 25, 44, 20, 27]
# # num = [x for x in num if x%2!=0]
# # print(num)

# # #15. Write a Python program to shuffle and print a specified list. 

# # from random import shuffle
# # color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # shuffle(color)
# # print(color)

# # #16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 

# # def printValues():
	# # l = list()
	# # for i in range(1,21):
		# # l.append(i**2)
	# # print(l[:5])
	# # print(l[-5:])

# # printValues()

# # #17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 

# # def printValues():
	# # l = list()
	# # for i in range(1,21):
		# # l.append(i**2)
	# # print(l[5:])

# # printValues()

# # #18. Write a Python program to generate all permutations of a list in Python. 

# # import itertools
# # print(list(itertools.permutations([1,2,3])))

# # #19. Write a Python program to get the difference between the two lists. 

# # list1 = [1, 2, 3, 4]
# # list2 = [1, 2]
# # print(list(set(list1) - set(list2)))

# # #20. Write a Python program access the index of a list. 

# # nums = [5, 15, 35, 8, 98]
# # for num_index, num_val in enumerate(nums):
    # # print(num_index, num_val)
	
# # #21. Write a Python program to convert a list of characters into a string. 

# # s = ['a', 'b', 'c', 'd']
# # str1 = ''.join(s)
# # print(str1)

# # #22. Write a Python program to find the index of an item in a specified list. 

# # num =[10, 30, 4, -6]
# # print(num.index(30))

# # #23. Write a Python program to flatten a shallow list. 

# # import itertools
# # original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# # new_merged_list = list(itertools.chain(*original_list))
# # print(new_merged_list)

# # #24. Write a Python program to append a list to the second list. 

# # list1 = [1, 2, 3, 0]
# # list2 = ['Red', 'Green', 'Black']
# # final_list = list1 + list2
# # print(final_list)

# # #25. Write a Python program to select an item randomly from a list. 

# # import random
# # color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# # print(random.choice(color_list))

# # #26. Write a python program to check whether two lists are circularly identical. 

# # list1 = [10, 10, 0, 0, 10]
# # list2 = [10, 10, 10, 0, 0]
# # list3 = [1, 10, 10, 0, 0]

# # print('Compare list1 and list2')
# # print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# # print('Compare list1 and list3')
# # print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

# # #27. Write a Python program to find the second smallest number in a list. 

# # def second_smallest(numbers):
  # # if (len(numbers)<2):
    # # return
  # # if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    # # return
  # # dup_items = set()
  # # uniq_items = []
  # # for x in numbers:
    # # if x not in dup_items:
      # # uniq_items.append(x)
      # # dup_items.add(x)
  # # uniq_items.sort()    
  # # return  uniq_items[1]   

# # print(second_smallest([1, 2, -8, -2, 0, -2]))
# # print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# # print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# # print(second_smallest([2,2]))
# # print(second_smallest([2]))

# # #28. Write a Python program to find the second largest number in a list. 

# # def second_largest(numbers):
  # # if (len(numbers)<2):
    # # return
  # # if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    # # return
  # # dup_items = set()
  # # uniq_items = []
  # # for x in numbers:
    # # if x not in dup_items:
      # # uniq_items.append(x)
      # # dup_items.add(x)
  # # uniq_items.sort()    
  # # return  uniq_items[-2]   
# # print(second_largest([1,2,3,4,4]))
# # print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# # print(second_largest([2,2]))
# # print(second_largest([1]))

# # #29. Write a Python program to get unique values from a list. 

# # my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# # print("Original List : ",my_list)
# # my_set = set(my_list)
# # my_new_list = list(my_set)
# # print("List of unique numbers : ",my_new_list)

# # #30. Write a Python program to get the frequency of the elements in a list. 

# # import collections
# # my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# # print("Original List : ",my_list)
# # ctr = collections.Counter(my_list)
# # print("Frequency of the elements in the List : ",ctr)

# # #31. Write a Python program to count the number of elements in a list within a specified range. 

# # def count_range_in_list(li, min, max):
	# # ctr = 0
	# # for x in li:
		# # if min <= x <= max:
			# # ctr += 1
	# # return ctr

# # list1 = [10,20,30,40,40,40,70,80,99]
# # print(count_range_in_list(list1, 40, 100))

# # list2 = ['a','b','c','d','e','f']
# # print(count_range_in_list(list2, 'a', 'e'))

# # #32. Write a Python program to check whether a list contains a sublist. 

# # def is_Sublist(l, s):
	# # sub_set = False
	# # if s == []:
		# # sub_set = True
	# # elif s == l:
		# # sub_set = True
	# # elif len(s) > len(l):
		# # sub_set = False

	# # else:
		# # for i in range(len(l)):
			# # if l[i] == s[0]:
				# # n = 1
				# # while (n < len(s)) and (l[i+n] == s[n]):
					# # n += 1
				
				# # if n == len(s):
					# # sub_set = True

	# # return sub_set

# # a = [2,4,3,5,7]
# # b = [4,3]
# # c = [3,7]
# # print(is_Sublist(a, b))
# # print(is_Sublist(a, c))

# # #33. Write a Python program to generate all sublists of a list. 

# # from itertools import combinations
# # def sub_lists(my_list):
	# # subs = []
	# # for i in range(0, len(my_list)+1):
	  # # temp = [list(x) for x in combinations(my_list, i)]
	  # # if len(temp)>0:
	    # # subs.extend(temp)
	# # return subs


# # l1 = [10, 20, 30, 40]
# # l2 = ['X', 'Y', 'Z']
# # print("Original list:")
# # print(l1)
# # print("S")
# # print(sub_lists(l1))
# # print("Sublists of the said list:")
# # print(sub_lists(l1))
# # print("\nOriginal list:")
# # print(l2)
# # print("Sublists of the said list:")
# # print(sub_lists(l2))

# # #34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number. 

# # def prime_eratosthenes(n):
    # # prime_list = []
    # # for i in range(2, n+1):
        # # if i not in prime_list:
            # # print (i)
            # # for j in range(i*i, n+1, i):
                # # prime_list.append(j)

# # print(prime_eratosthenes(100))

# # #35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 

# # my_list = ['p', 'q']
# # n = 4
# # new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
# # print(new_list)

# # #36. Write a Python program to get variable unique identification number or string. 

# # x = 100
# # print(format(id(x), 'x'))
# # s = 'w3resource'
# # print(format(id(s), 'x')) 

# # #37. Write a Python program to find common items from two lists. 

# # color1 = "Red", "Green", "Orange", "White"
# # color2 = "Black", "Green", "White", "Pink"
# # print(set(color1) & set(color2))

# # #38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 

# # from itertools import zip_longest, chain, tee
# # def replace2copy(lst):
    # # lst1, lst2 = tee(iter(lst), 2)
    # # return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
# # n = [0,1,2,3,4,5]
# # print(replace2copy(n))

# # #39. Write a Python program to convert a list of multiple integers into a single integer. 

# # L = [11, 33, 50]
# # print("Original List: ",L)
# # x = int("".join(map(str, L)))
# # print("Single Integer: ",x)

# # #40. Write a Python program to split a list based on first character of word. 

# # from itertools import groupby
# # from operator import itemgetter

# # word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     # # 'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# # for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    # # print(letter)
    # # for word in words:
        # # print(word)

# # #41. Write a Python program to create multiple lists. 

# # obj = {}
# # for i in range(1, 21):
    # # obj[str(i)] = []
# # print(obj)

# # #42. Write a Python program to find missing and additional values in two lists. 

# # list1 = ['a','b','c','d','e','f']
# # list2 = ['d','e','f','g','h']
# # print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
# # print('Additional values in second list: ', ','.join(set(list2).difference(list1)))

# # #43. Write a Python program to split a list into different variables. 

# # color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         # # ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# # var1, var2, var3 = color
# # print(var1)
# # print(var2)
# # print(var3)

# # #44. Write a Python program to generate groups of five consecutive numbers in a list. 

# # l = [[5*i + j for j in range(1,6)] for i in range(5)]
# # print(l)

# # #45. Write a Python program to convert a pair of values into a sorted unique array. 

# # L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 # # (7, 8), (9, 10)]
# # print("Original List: ", L)
# # print("Sorted Unique Data:",sorted(set().union(*L)))

# # #46. Write a Python program to select the odd items of a list. 

# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(x[::2])

# # #47. Write a Python program to insert an element before each element of a list. 

# # color = ['Red', 'Green', 'Black']
# # print("Original List: ",color)
# # color = [v for elt in color for v in ('c', elt)]
# # print("Original List: ",color)

# # #48. Write a Python program to print a nested lists (each list on a new line) using the print() function. 

# # colors = [['Red'], ['Green'], ['Black']]
# # print('\n'.join([str(lst) for lst in colors]))

# # #49. Write a Python program to convert list to list of dictionaries. 

# # color_name = ["Black", "Red", "Maroon", "Yellow"]
# # color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# # print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])

# # #50. Write a Python program to sort a list of nested dictionaries. 

# # my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
# # print("Original List: ")
# # print(my_list)
# # my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
# # print("Sorted List: ")
# # print(my_list)

# # #51. Write a Python program to split a list every Nth element. 

# # C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# # def list_slice(S, step):
    # # return [S[i::step] for i in range(step)]
# # print(list_slice(C,3))

# # #52. Write a Python program to compute the similarity between two lists. 

# # from collections import Counter
# # color1 = ["red", "orange", "green", "blue", "white"]
# # color2 = ["black", "yellow", "green", "blue"]
# # counter1 = Counter(color1)
# # counter2 = Counter(color2)
# # print("Color1-Color2: ",list(counter1 - counter2))
# # print("Color2-Color1: ",list(counter2 - counter1))

# # #53. Write a Python program to create a list with infinite elements. 

# # import itertools
# # c = itertools.count()
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # print(next(c))

# # #54. Write a Python program to concatenate elements of a list. 

# # color = ['red', 'green', 'orange']
# # print('-'.join(color))
# # print(''.join(color))

# # #55. Write a Python program to remove key values pairs from a list of dictionaries. 

# # original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
# # print("Original List: ")
# # print(original_list)
# # new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
# # print("New List: ")
# # print(new_list)

# # #56. Write a Python program to convert a string to a list. 

# # import ast
# # color ="['Red', 'Green', 'White']"
# # print(ast.literal_eval(color))

# # #57. Write a Python program to check if all items of a list is equal to a given string. 

# # color1 = ["green", "orange", "black", "white"]
# # color2 = ["green", "green", "green", "green"]

# # print(all(c == 'blue' for c in color1))
# # print(all(c == 'green' for c in color2))

# # #58. Write a Python program to replace the last element in a list with another list. 

# # num1 = [1, 3, 5, 7, 9, 10]
# # num2 = [2, 4, 6, 8]
# # num1[-1:] = num2
# # print(num1)

# # #59. Write a Python program to check if the n-th element exists in a given list. 

# # x = [(4, 1), (1, 2), (6, 0)]
# # print(min(x, key=lambda n: (n[1], -n[0])))

# # #60. Write a Python program to find a tuple, the smallest second index value from a list of tuples. 

# # x = [(4, 1), (1, 2), (6, 0)]
# # print(min(x, key=lambda n: (n[1], -n[0])))

# # #61. Write a Python program to create a list of empty dictionaries. 

# # n = 5
# # l = [{} for _ in range(n)]
# # print(l)

# # #62. Write a Python program to print a list of space-separated elements. 

# # num = [1, 2, 3, 4, 5]
# # print(*num)

# # #63. Write a Python program to insert a given string at the beginning of all items in a list. 

# # num = [1,2,3,4]
# # print(['emp{0}'.format(i) for i in  num])

# # #64. Write a Python program to iterate over two lists simultaneously. 

# # num = [1, 2, 3]
# # color = ['red', 'white', 'black']
# # for (a,b) in zip(num, color):
     # # print(a, b)
	 
# # #65. Write a Python program to access dictionary keys element by index. 

# # num = {'physics': 80, 'math': 90, 'chemistry': 86}
# # print(list(num)[0])

# # #66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 

# # num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# # print(max(num, key=sum))

# # #67. Write a Python program to find all the values in a list are greater than a specified number. 

# # list1 = [220, 330, 500]
# # list2 = [12, 17, 21]
# # print(all(x >= 200 for x in list1))
# # print(all(x >= 25 for x in list2))

# # #68. Write a Python program to extend a list without append. 

# # x = [10, 20, 30]
# # y = [40, 50, 60]
# # x[:0] =y
# # print(x)

# # #69. Write a Python program to remove duplicates from a list of lists. 

# # import itertools
# # num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# # print("Original List", num)
# # num.sort()
# # new_num = list(num for num,_ in itertools.groupby(num))
# # print("New List", new_num)

# # #70. Write a Python program to get the depth of a dictionary. 

# # def dict_depth(d):
    # # if isinstance(d, dict):
        # # return 1 + (max(map(dict_depth, d.values())) if d else 0)
    # # return 0
# # dic = {'a':1, 'b': {'c': {'d': {}}}}
# # print(dict_depth(dic))

# # #71. Write a Python program to check if all dictionaries in a list are empty or not. 

# # my_list = [{},{},{}]
# # my_list1 = [{1,2},{},{}]
# # print(all(not d for d in my_list))
# # print(all(not d for d in my_list1))



# # # _________________________ Tuple ____________________
# # # 1. Write a Python program to create a tuple. 

# # #Create an empty tuple 
# # x = ()
# # print(x)
# # #Create an empty tuple with tuple() function built-in Python
# # tuplex = tuple()
# # print(tuplex)

# # #2. Write a Python program to create a tuple with different data types. 

# # #Create a tuple with different data types
# # tuplex = ("tuple", False, 3.2, 1)
# # print(tuplex)

# # #3. Write a Python program to create a tuple with numbers and print one item. 

# # #Create a tuple with numbers
# # tuplex = 5, 10, 15, 20, 25
# # print(tuplex)
# # #Create a tuple of one item
# # tuplex = 5,
# # print(tuplex)

# # #4. Write a Python program to unpack a tuple in several variables. 

# # #create a tuple
# # tuplex = 4, 8, 3 
# # print(tuplex)
# # n1, n2, n3 = tuplex
# # #unpack a tuple in variables
# # print(n1 + n2 + n3) 
# # #the number of variables must be equal to the number of items of the tuple
# # n1, n2, n3, n4= tuplex 

# # #5. Write a Python program to add an item in a tuple. 

# # #create a tuple
# # tuplex = (4, 6, 2, 8, 3, 1) 
# # print(tuplex)
# # #tuples are immutable, so you can not add new elements
# # #using merge of tuples with the + operator you can add an element and it will create a new tuple
# # tuplex = tuplex + (9,)
# # print(tuplex)
# # #adding items in a specific index
# # tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
# # print(tuplex)
# # #converting the tuple to list
# # listx = list(tuplex) 
# # #use different ways to add items in list
# # listx.append(30)
# # tuplex = tuple(listx)
# # print(tuplex)

# # #6. Write a Python program to convert a tuple to a string. 

# # tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# # str =  ''.join(tup)
# # print(str)

# # #7. Write a Python program to get the 4th element and 4th element from last of a tuple. 

# # #Get an item of the tuple
# # tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# # print(tuplex)
# # #Get item (4th element)of the tuple by index
# # item = tuplex[3]
# # print(item)
# # #Get item (4th element from last)by index negative
# # item1 = tuplex[-4]
# # print(item1)

# # #8. Write a Python program to create the colon of a tuple. 

# # from copy import deepcopy
# # #create a tuple
# # tuplex = ("HELLO", 5, [], True) 
# # print(tuplex)
# # #make a copy of a tuple using deepcopy() function
# # tuplex_colon = deepcopy(tuplex)
# # tuplex_colon[2].append(50)
# # print(tuplex_colon)
# # print(tuplex)

# # #9. Write a Python program to find the repeated items of a tuple. 

# # #create a tuple
# # tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
# # print(tuplex)
# # #return the number of times it appears in the tuple.
# # count = tuplex.count(4)
# # print(count)

# # #10. Write a Python program to check whether an element exists within a tuple. 

# # tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# # print("r" in tuplex)
# # print(5 in tuplex)

# # #11. Write a Python program to convert a list to a tuple. 

# # #Convert list to tuple
# # listx = [5, 10, 7, 4, 15, 3]
# # print(listx)
# # #use the tuple() function built-in Python, passing as parameter the list
# # tuplex = tuple(listx)
# # print(tuplex)

# # #12. Write a Python program to remove an item from a tuple. 

# # #create a tuple
# # tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
# # print(tuplex)
# # #tuples are immutable, so you can not remove elements
# # #using merge of tuples with the + operator you can remove an item and it will create a new tuple
# # tuplex = tuplex[:2] + tuplex[3:]
# # print(tuplex)
# # #converting the tuple to list
# # listx = list(tuplex) 
# # #use different ways to remove an item of the list
# # listx.remove("c") 
# # #converting the tuple to list
# # tuplex = tuple(listx)
# # print(tuplex)

# # #13. Write a Python program to slice a tuple. 

# # #create a tuple
# # tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# # #used tuple[start:stop] the start index is inclusive and the stop index
# # slice = tuplex[3:5]
# # #is exclusive
# # print(_slice)
# # #if the start index isn't defined, is taken from the beg inning of the tuple
# # _slice = tuplex[:6]
# # print(_slice)
# # #if the end index isn't defined, is taken until the end of the tuple
# # _slice = tuplex[5:]
# # print(_slice)
# # #if neither is defined, returns the full tuple
# # _slice = tuplex[:]
# # print(_slice)
# # #The indexes can be defined with negative values
# # _slice = tuplex[-8:-4]
# # print(_slice)
# # #create another tuple
# # tuplex = tuple("HELLO WORLD")
# # print(tuplex)
# # #step specify an increment between the elements to cut of the tuple
# # #tuple[start:stop:step]
# # _slice = tuplex[2:9:2]
# # print(_slice)
# # #returns a tuple with a jump every 3 items
# # _slice = tuplex[::4]
# # print(_slice)
# # #when step is negative the jump is made back
# # _slice = tuplex[9:2:-4]
# # print(_slice)

# # #14. Write a Python program to find the index of an item of a tuple. 

# # #create a tuple
# # tuplex = tuple("index tuple")
# # print(tuplex)
# # #get index of the first item whose value is passed as parameter
# # index = tuplex.index("p")
# # print(index)
# # #define the index from which you want to search
# # index = tuplex.index("p", 5)
# # print(index)
# # #define the segment of the tuple to be searched
# # index = tuplex.index("e", 3, 6)
# # print(index)
# # #if item not exists in the tuple return ValueError Exception
# # index = tuplex.index("y")

# # #15. Write a Python program to find the length of a tuple. 

# # #create a tuple
# # tuplex = tuple("w3resource")
# # print(tuplex)
# # #use the len() function to known the length of tuple
# # print(len(tuplex))

# # #16. Write a Python program to convert a tuple to a dictionary. 

# # #create a tuple
# # tuplex = ((2, "w"),(3, "r"))
# # print(dict((y, x) for x, y in tuplex))

# # #17. Write a Python program to unzip a list of tuples into individual lists. 

# # #create a tuple
# # x = ("w3resource")
# # # Reversed the tuple
# # y = reversed(x)
# # print(tuple(y))
# # #create another tuple
# # x = (5, 10, 15, 20)
# # # Reversed the tuple
# # y = reversed(x)
# # print(tuple(y))

# # #18. Write a Python program to reverse a tuple. 

# # #create a list
# # l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# # d = {}
# # for a, b in l:
    # # d.setdefault(a, []).append(b)
# # print (d)

# # #19. Write a Python program to convert a list of tuples into a dictionary. 

# # t = (100, 200, 300)
# # print('This is a tuple {0}'.format(t))


# # #20. Write a Python program to print a tuple with string formatting. 

# # l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# # print([t[:-1] + (100,) for t in l])

# # #
# # L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# # L = [t for t in L if t]
# # print(L)

# # #21. Write a Python program to replace last value of tuples in a list. 

# # price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# # print( sorted(price, key=lambda x: float(x[1]), reverse=True))

# # #22. Write a Python program to remove an empty tuple(s) from a list of tuples. 

# # num = [10,20,30,(10,20),40]
# # ctr = 0
# # for n in num:
    # # if isinstance(n, tuple):
        # # break
    # # ctr += 1
# # print(ctr)

# # #





# Create a Python program that verifies whether a provided positive integer is a multiple of two. Access the editor by clicking here. Sample input: 4 Expected output: True Click here to view the proposed solution.

# Create a program, python program , that verifies whether a positive integer is a multiple of three. For instance, if given the input "9," the output should be "True." To view a sample solution, click on the provided link.

# Create a Python script to verify whether a provided positive integer is a multiple of four. For example, when the input is 4, the program should return True. To view a sample solution, click the provided link.

# Create a Python code that determines whether a digit is a perfect square or not. For instance, if the input is 9, the output must be True. Click the link to view an example solution.

# Create a Python script that verifies whether an integer is a power of another integer. For example, providing the numbers 16 and 2 should return True. Check out the sample solution by clicking on the link.

# Create a Python program that verifies whether a number is a power of a specified base. The input to the program will be a number and a base. The program should output "True" if the number is a power of the given base. To get a sample solution, click on the provided link.

# Develop a Python script that can detect a missing number in a given list. The input values will be in the form of a list of numbers. The program should output the number that is missing from the sequence. For instance, if the given input is [1,2,3,4,6,7,8], the output should be 5. Click on the provided link to view a sample solution.

# This Python program helps in identifying the missing numbers from a given list. The input consists of a list of numbers, and the output is a list of the numbers that are missing from the given list. For example, if the input is [1,2,3,4,6,7,10], the output would be [5,8,9]. To see the sample solution, click on the provided link.

# Create a Python script that can detect three values from an array with a sum of zero. The given input is [-1,0,1,2,-1,-4], and the expected output is [[-1, -1, 2], [-1, 0, 1]]. It is important to locate the unique triplets in the array. Click on the link to view the example solution.

# Develop a Python code to identify a triplet of numbers from an array where their summation is equivalent to a specified number. The input array is [1, 0, -1, 0, -2, 2] and the target number is 0. The program should return three sets of quadruplets that satisfy this condition. An example of the output is [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]. Click on the link to view a potential solution.

# Create a Python script that calculates and outputs the square root of an 'integer' that is provided. The program should take the value '16' as input and return '4' as output. Keep in mind that the output value should always be an 'integer'. Click on the link to view a sample solution.

# Create a Python script that identifies the unique number in a list that does not appear twice. The program should take a given input list and output the singular number. For instance, if the input is [5, 3, 4, 3, 4], the output should be 5. You may refer to the sample solution by clicking the provided link.

# Create a Python script that can identify the unique element in a given list that occurs only once while all the other elements are repeated thrice. For instance, given the input [5, 3, 4, 3, 5, 5, 3], the program should output 4. Click on the link to view a sample solution.

# Develop a Python code that identifies the only element that appears once within a list of elements, where every item is repeated four times except for one. For instance, given the input [1, 1, 1, 2, 2, 2, 3], the output should be 3. Follow the link to view a sample solution.

# Develop a Python code to identify a pair of distinct elements from a list where every element is repeated twice in the list. The input list is provided as [1, 2, 1, 3, 2, 5] and the output should be [5, 3]. Click on the link to access a sample solution.

# Create a Python code that adds the digits of a positive integer repeatedly until the result as a single digit . The input value is 48 and the output value is 3. If the number is 59, the result would be 5, which is obtained by adding 5 and 9 to get 14, then adding 1 and 4 to get 5. Click the link to view a sample solution.

# Create a Python program to determine the existence of an additive sequence. An additive sequence is a series of numbers where the sum of the first two numbers equals the third number. For example, 6+6=12, 6+12=18, 12+18=30, which is an additive sequence. An additive sequence can also be formed by dividing a number into one or more digits. For instance, the number 66121830 can be divided into an additive sequence of 6+6=12, 6+12=18, 12+18=30. Keep in mind that an additive sequence cannot contain any numbers with leading zeros . Check out the sample solution by clicking the link.

# Create a reverse the digits of an integer program using Python, which takes input values of 234 and -234, and outputs their respective values of 432 and -432. For a sample solution, click on the provided link.

# Create a Python script that can reverse the bits of an unsigned 32-bit integer. For instance, if the input is 1234, the output should be 1260388352. This means that 1234 in binary form as 10011010010 when reversed, becomes 1001011001000000000000000000000. To see an example solution, click on the provided link.

# Create a Python script that verifies whether a sequence of numbers is an arithmetic progression or not. For instance, given the input [5, 7, 9, 11], the program should return True. In mathematics, an arithmetic progression, also known as arithmetic sequence , is a sequence where the difference between consecutive terms remains constant. Consider the following sequence: 5, 7, 9, 11, 13, 15... It is an arithmetic progression with a common difference of 2. Click here to check out a sample solution.

# Write a Python program that determines whether a sequence of numbers is a geometric progression or not. The input is a list of numbers, and the program should output True if the sequence is a geometric progression. In mathematics, a geometric progression is a sequence of numbers in which each term is obtained by multiplying the previous term by a fixed, non-zero number known as the common ratio. For instance, the sequence 2, 6, 18, 54, ... has a common ratio of 3, and it is a geometric progression. Similarly, 10, 5, 2.5, 1.25, ... is a geometric sequence with a common ratio of 1/2. Check out the sample solution by clicking the link.

# Create a Python script that calculates the sum of two numbers in their reversed form and shows the result in reverse order. For example, if the input is 13 and 14, the output should be 27. It's important to note that the result may not be unique since multiple numbers can have the same reverse form, such as 31, 130, 1300, etc. To account for this, leading zeros will be excluded. Check out the sample solution by clicking the link.

# The Collatz conjecture, also known as the 3n + 1 conjecture, is a mathematical conjecture named after Lothar Collatz. The conjecture states that given any positive integer n, if n is even, divide it by 2 to get n / 2, and if n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process, which is also called "Half Or Triple Plus One," indefinitely. The conjecture suggests that no matter what number you start with, you will always eventually reach 1. To illustrate, if we start with n = 12, we get the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1. However, n = 19 takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. Write a Python program that takes any positive integer n, and if n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process until you reach 1. For instance, if the input is 12, the output should be [12, 6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0].

# Create a Python script that verifies if a provided value is an ugly number, which means that it is a positive integer having only 2, 3, or 5 as its prime factors. The sequence of the first ten ugly numbers is 1, 2, 3, 4, 5, 6, 8, 9, 10, and 12. Keep in mind that 1 is generally included in the list of ugly numbers. Once the code is ready, you can click the link to view a sample solution.

# Develop a Python program to obtain the Hamming numbers up to a specified number and verify if a particular number is a Hamming number. For a given input of 7, the output is 0. Hamming numbers are represented in the form of H = 2^(i) x 3^(j) x 5^(k), where i, j, and k are equal to 0. The Hamming number sequence consists of numbers such as 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, and 27, which are calculated by multiplying 2, 3, and 5 to the power of their respective non-negative integers. Click on the link to view the sample solution.

# The task is to develop a Python program that verifies whether a provided string is an anagram of another given string. For instance, if the input is 'anagram' and 'nagaram', the output should be True. An anagram is a form of wordplay in which the letters of a term or phrase are rearranged to create a new word or phrase using all of the original letters just once. According to Wikipedia, the word anagram can be transformed into nag-a-ram. Click the link to obtain a sample solution.

# Create a Python script that will move the Push all zeros to the end of the items in a list. For instance, given the following input [0,2,3,4,6,7,10], the output should be [2, 3, 4, 6, 7, 10, 0]. Check out the sample solution by clicking on the provided link.

# Create a Python script that moves the initial number in a list to the end. Additionally, you can view the sample solution by clicking on the provided link.

# Develop a Python code to discover the majority element from a given list. For instance, consider the input list as [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]. The code should return 5 as output. Remember, the majority element refers to the element that appears more than n/2 times, where n is the total number of elements in the given list. Click on the link to view the sample solution.

# Develop a Python script that determines the length of the last word in a given input. For example, if the input is "Python Exercises," the output should be 9. To view a sample solution, click the provided link.

# In Python, create a program that takes Program to add two binary numbers as input and outputs their numerical value. For instance, if the input is ('11', '1'), the output should be 100. Click the provided link to view a sample solution.

# Create a Python script that can identify the lone number that appears an odd number of times while the rest of the numbers appear an even number of times. Check out the sample solution by clicking on the link provided.

# Create a Python code that calculates the total of numbers that are divisible by either 3 or 5 and are less than 500. For instance, if we consider all the natural numbers that are multiples of 3 or 5 and less than 12, we get 3, 5, 6, 9, and 10. Adding all these multiples up, we get the sum of 33. Click on the link to view the example solution.

# Create a Python script that adds up the even-valued numbers in the Fibonacci sequence sequence that are less than or equal to one million. Remember that Fibonacci series is formed by adding the two preceding integers together. The initial terms are 1 and 2, and the sequence's first ten terms are 1, 2, 3, 5, 8, 13, 21, 34, 55, and 89. To view the sample answer, click here.

# Develop a Python script that discovers the maximum prime factor of a provided number. For instance, the prime factors of 330 are 2, 3, 5, and 11. Hence, 11 is the largest prime factor of 330. Click on the link to view a sample solution.


# Create a Python script that outputs a set of colors from color_list_1, excluding those that are present in color_list_2. The program must use the following data: Test Data: color_list_1 = set(["White", "Black", "Red"]) color_list_2 = set(["Red", "Green"]) Expected Output: {'Black', 'White'} Click the link to view the sample solution.

# Develop a Python script that can calculate the area of a triangle based on its base and height. View the sample solution by clicking the link provided.

# Create a solution in Python that calculates the highest common divisor (GCD) between two affirmative whole numbers. Check out the provided sample solution by clicking the link.

# Design a Python code that returns the smallest common multiple (LCM between two given positive integers. Access the link to view an example solution.

# Create a Python code that can add up three integers, but if two of the values are equal sum , their sum will be equal to zero. You can refer to the provided sample solution by clicking the link.

# Design a Python script that computes the sum of two provided integers. Nonetheless, if the sum lies between 15 to 20, the program will return 20. To access the sample solution, click the following link.

# Create a Python script that will check if two integer values are equivalent or if their sum or difference equates to 5. To view the example solution, click on the provided link.

# Create a Python script that adds two integer objects together. To view the sample solution, click the provided link.

# Create a Python script that exhibits your personal information, such as your name, age, and address, in three separate lines. Additionally, a sample solution can be viewed by clicking on the provided link.

# Develop a Python code that can compute the value of (x + y) * (x + y). The input values for x and y are 4 and 3, respectively. The program should output the result of (4 + 3) ^ 2, which is 49. To view a sample solution, click the provided link.

# Create a Python script that calculates the future value of a specified principal amount along with the interest rate and duration in years. Here is the test data: amt = 10000, int = 3.5, years = 7. The expected output should be: 12722.79. To view the sample solution, click the provided link.

# Create a Python code that calculates the distance separating two points with coordinates (x1, y1) and (x2, y2). For reference, you can check out the sample solution by clicking on the provided link.

# Create a Python script that verifies the existence of a file by checking its presence. Access the editor by clicking on the given link to view a possible solution.

# Create a program in Python that can detect whether the Python shell is operating in 32-bit or 64-bit mode on the OS. Access the editor by clicking the link to view a sample solution.

# Develop a Python script to obtain details on the operating system, such as its name, platform, and release information. Visit the editor to view a sample solution.

# Create a Python script that installs locate Python in the package directory of your choice. Try it yourself by checking out the sample solution provided.

# Create a Python script that can execute an external command. The solution can be viewed by clicking on the provided link.

# Develop a Python program that retrieves the path and filename of the currently running file. Proceed to the editor by clicking the link below to view a sample solution.

# Create a Python code that determines the count of CPUs utilized. Check out the example solution by clicking the link provided.

# Create a Python code that can convert a string into either a floating-point number or an integer. Access the editor by clicking the provided link for a sample solution.

# 49. Access MSDT solution by clicking on write a python program to list all files in a directory in python .

# Create a Python script that outputs text without any spaces or line breaks. To view an example solution, click the provided link.

# Create a Python code that can evaluate the profiling of Python programs . It should be noted that profiling involves a collection of data that illustrates the frequency and duration of program execution. These data can be presented in reports with the use of the pstats library. Check out the sample solution by clicking the provided link.

# Create a Python script that outputs to the standard error stream. Access the editor by clicking the provided link to display a possible solution.

# Create a Python program that enables you to retrieve environment variables. Access the editor by clicking the provided link to view a sample solution.

# Create a Python script that retrieves the present username. Access the editor by clicking the link below to view a sample solution.

# Create a Python program that utilizes Python's standard library to locate nearby IP address es. Access the sample solution by clicking the provided link.

# Design a Python script that retrieves the dimensions of console window . Access the editor by clicking on the provided link to view a sample solution.

# Create a Python code that retrieves execution time of a specific Python function. Open the editor to view a possible solution.

# Create a Python code that can add up the initial n whole numbers that are positive. Click the link to view an example solution.

# Develop a Python code that can convert height from feet and inches to centimeters. Click the given link to access a sample solution.

# Create a Python script to draw a triangular shape using calculate the hypotenuse of a right angle . To view the example solution, click on the provided link.

# Create a Python script that can transform the distance in feet to inches, yards as well as miles. To view the sample solution, click on the provided link.

# Create a program in Python that can convert different time units into seconds. View the sample solution by clicking on the provided link.

# Create a Python code that retrieves the absolute value of file path without fail. To view the sample solution, click on the given link.

# Create a multiplication problem using the parameter python program to get file creation and modification date and proceed to the editor. To view a possible solution, click on the provided link.

# Create a Python script that can convert seconds into three different units: days, hour, minutes , and seconds. For a sample solution, click the provided link.

# Create a Python code that will display the solution for the index specified in calculate body mass . To view the sample answer, click on the provided link.

# Develop a Python script that transforms kilopascals into pounds per square inch, millimeter of mercury (mmHg), and atmospheric pressure. Access the sample solution by clicking on the link.

# Create a Python script that computes the sum of the digits in a given number. A sample solution is available by clicking the provided link.

# Develop a Python code to arrange a set of three integers, without utilizing loops or conditional statements. To view the example solution, click on the provided link.

# Design a Python code that arranges files in chronological order. Check out the example solution by clicking on the link.

# Create a Python script that can sort a directory listing by its date of creation. To access the sample solution, click the provided link.

# Create a Python script that retrieves the information regarding math module . To view the example solution, click on the provided link.

# Create a Python code that can determine the calculate midpoints of a given string. Access the editor by clicking the link to view the sample solution.

# Generate a hash value for a given word using Python. Access the sample solution by clicking the provided link.

# Develop a Python script to obtain the Python code's MSDT_A1 details and copyright information. Access the editor to review the sample solution.

# Create a Python script that retrieves the command-line input, including the script's name, the number of arguments, and the arguments themselves. Access the editor by clicking the link to view the sample solution.

# Create a Python script to determine if the platform is little-endian or big-endian. Access the sample solution by clicking on the provided link.

# Create a Python script that can detect the built-in modules that are available. Click the link provided to view an example solution.

# Python code can be written to determine the size of an object in bytes. A sample solution can be viewed by clicking on the provided link.

# Develop a Python script that retrieves the present recursion limit value. Access the sample solution by clicking here.

# Create a Python code that concatenates multiple strings, where the number of strings to be concatenated is denoted by N. To view a possible solution, click on the provided link.

# Create a Python script that adds up the elements in a collection (such as a tuple, list, set, or dictionary). To view a possible solution, click the provided link.

# Create a Python script that checks if every element in a list is larger than a specific value. Access the sample solution by clicking the provided link.

# Create a Python script that tallies the frequency of a specific string, denoted as specific character , within a given input string. Access the provided example implementation by clicking the designated link.

# Create a Python script that can determine if a given path is a file or a directory. To accomplish this task, refer to the example solution provided by clicking on the link.

# Create a Python code that retrieves the ASCII code of a character. You may refer to the sample solution by clicking the provided link.

# Develop a Python program to determine the dimensions of a file. Access the editor by selecting the link to view the sample solution.

# Create a Python program that utilizes the variables x=30 and y=20 to display the text "30+20=50". Access the sample solution by clicking the provided link.

# In Python, create a program that executes a task when a particular condition is met. Specifically, if a variable's value is 1, output the message "First day of a Month!" Otherwise, take no action. Access the sample solution by clicking the provided link.

# Create a Python script that duplicates its source code. To see an example solution, click the provided link.

# Create a Python program with the identifier Program to Swap Two Variables . Access the editor by clicking the provided link to view a possible solution.

# Create a Python script that declares a string with diverse representations of special characters. Check the sample solution by clicking on the link.

# Create a Python script that retrieves the Type, Value, and Identity of an object. Access the editor by clicking on the link to view the example solution.

# Create a Python script that transforms a byte string into a collection of whole numbers. Access the editor by clicking the provided link to view a sample solution.

# Create a Python script that can verify if a given string is a numeric value. See the sample solution by clicking the link provided.

# Create a Python code that displays the existing call stack. Click on the link to view a potential solution.

# List the special variables used within the language in a Python program by referring to the sample solution provided by clicking on the link.

# Create a Python script that retrieves the current system time.

# The importance of system time cannot be overstated, as it is crucial for various tasks such as debugging, network information, generating random number seeds, and even monitoring program performance. Check out the sample solution by clicking on the provided link.

# Create a Python code that can clear the terminal or screen. To view a sample solution, click on the provided link.

# Create a Python script that retrieves the name of the current host where the program is executed. Access the editor by clicking the link provided.

# Develop a Python script to retrieve and display the content of a URL on the console. Access the editor by clicking here to view an example solution.

# Develop a Python code that retrieves the command output of the system. You may refer to the sample solution by clicking the link provided.

# Create a Python code that can retrieve the name of a file from a specified path. Access the editor by clicking the link to view a possible solution.

# Create a Python code that retrieves the effective user id, effective group id, and real group id along with a roster of the supplementary group ids associated with the present process. It is essential to note that the functionality is only available on Unix. For a sample solution, click the link.

# Create a Python script that retrieves information about the user's environment. Access the editor by clicking the link to view an example solution.

# Create a Python script that can split a path using the extension separator. Access the editor by clicking on the link provided below for a sample solution.

# Create a solution in Python to perform retrieve file properties . Access the editor by clicking the provided link to view a sample solution.

# Develop a Python script that can detect whether a path name refers to a file or a directory. Click the link to view a sample solution.

# Create a Python script that determines whether a value is negative, positive, or zero. To view a solution example, click on the link provided.

# Create a Python code utilizing an unidentified function to extract the integers that are divisible by fifteen from a given list. To view the example solution, click on the provided link.

# Create a Python script that generates lists of files using a wildcard from current directory . Access the editor by clicking on the provided link to view a sample solution.

# Develop a Python code that eliminates the initial element of a given list. To view the sample solution, click on the provided link.

# Create a Python code that prompts the user to input a number. In case the input is not a number, display an error message. Check out the sample solution by clicking the link provided.

# Create a program in Python that can extract positive numbers from a list. You may refer to the sample solution by clicking on the link provided.

# Develop a Python script to calculate product of a list of integers without the utilization of a for loop. Click on the provided link to view a sample solution.

# Create a Python code that accomplishes print Unicode characters by clicking on the provided link to view a sample solution.

# Create a Python code that will allocate two variables in the same memory location. To see the example solution, click the provided link.

# Create a bytearray in Python by converting a list using a program. Click on the link to view the sample solution.

# Create a Python script that can round a given floating-point value to a particular number of decimal places. Check out the sample solution by clicking the provided link.

# Develop a Python application to format a given string while restricting the string's length. Check out the sample solution by clicking on the provided link.

# Create a Python code that determines whether Determine whether variable is defined is true or false. You can refer to the provided solution by clicking the link.

# Create a Python code that clears a variable without causing its destruction.

# Given a sample dataset with a size of 20, and a dictionary containing a single key-value pair where the key is "x" and the value is 200, the expected output is an empty dictionary with a value of 0.

# Click me to see the sample solution

# Create a Python code that can identify the minimum and maximum value of integers, longs, floats . To view a possible resolution, click on the provided link.

# Create a Python script that verifies if various variables possess identical values. Access the editor by clicking the following link to observe a sample solution.

# Create a Python code that computes the total count from a collection of numbers. To view the solution, click on the provided link.

# Create a Python code that retrieves the module object corresponding to a specified object. This program should be able to obtain the actual module object for a given input. To view the sample solution, click the provided link.

# Create a Python code that verifies if integer fits is present in 64 bits . You may refer to the sample solution by clicking the provided link.

# Create a Python script to verify if a given string contains lowercase letters exist . Use the editor to view a potential solution.

# Create a Python script that adds add leading zeroes to a given string. You may refer to the sample solution by clicking the provided link.

# Create a Python code that utilizes double quotes for presenting strings. Click on the given link to view an example solution.

# Create a Python code that can divide a string of varying length into separate variables. See an example solution by clicking the provided link.

# Create a Python script that displays the contents of a user's home directory, excluding absolute path . Access the editor by clicking on the provided link to view a possible solution.

# Create a Python code that determines the duration of a program by computing the time elapsed between its start and current state. Access the sample solution by clicking the provided link.

# Create a Python code that lets the user input two integers on a single line. See the sample solution by clicking on the provided link.

# Create a Python script that can display the value of a variable without any gaps between them. For instance, if the variable is x and its value is 30, the program should output "Value of x is 30". Check out the sample solution by clicking the provided link.

# Create a Python script that can identify files in a specific directory, while excluding any directories. Access the editor by clicking the provided link to view a potential solution.

# Create a Python script that retrieves a single key-value pair from a dictionary and assigns it to variables. Here's a link to view a sample solution.

# Create a Python script that changes the values of true and false to 1 and 0, correspondingly. To view the solution, click on the provided link.

# Create a Python code that verifies the validity of an IP address. To view a possible solution, click on the provided link.

# Create a Python script that can convert an integer to binary keep leading zeros using the following sample data: x=12. The expected output should be 00001100 followed by 0000001100. Click on the provided link to view the sample solution.

# Create a Python script that converts convert decimal to its corresponding hexadecimal representation. The program should convert decimal numbers such as 30 and 4 to their respective hexadecimal values, which are 1e and 04. For a sample solution, please click the provided link.

# Write a Python program that determines if every sequence of ones of the same length as consecutive sequence in a given string is followed by a consecutive sequence of zeroes. The function should return True if this is the case and False otherwise. To illustrate, the program should be able to determine if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in a given string. For instance, if the original sequence is 01010101, the program should return True. However, if the original sequence is 00, the program should return False. Similarly, if the original sequence is 000111000111, the program should return True, while it should return False if the original sequence is 00011100011. To see a sample solution, click on the provided link.

# Develop a Python code that can identify if the operating system is running in 32bit or 64bit mode when executing the python shell. Click on the link to view a possible solution.

# Create a Python code that can determine if a variable is a string or an integer. To view the solution, simply click the provided link.

# Create a Python code that can verify whether a certain variable is categorized as a list, tuple, or set. Check out the sample solution by clicking the provided link.

# Create a Python code to locate the position of Python module sources . Access the editor by clicking the provided link to view a possible solution.

# In task 147, create a Python function that verifies if one number is divisible by another. The program should request two integer inputs from the user. Access the editor by clicking on the provided link to view a sample solution.

# Create a Python function that identifies the highest and lowest values from a series of numbers, without utilizing pre-existing functions. Access the sample solution by clicking on the provided link.

# Create a Python function that calculates the sum of the cubes of all positive integers below a given number. The input for this function should be a positive integer. To view a sample solution, click on the provided link.

# Create a Python function that verifies the existence of a unique pair of numbers in a series of integers whose multiplication results in an odd number. To view an example solution, click on the provided link.

# More to Come !

# NumPy Python Challenge For Beginners, Python Puzzles, In this NumPy Python Challenge For Beginners, Solve NumPy and Python Questions Using Jupyterlab. Watch Python 3 Interview Teaser Questions and …





