# @#$!@#$@!#$ hhhh### << ///Nov_2023..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$@
# # !!!!! don't stay at one part for more than 1 weekds...!!!!
# # !!!!! proceed as you go through by commenting .. for furhter refirinement..
# # https://sololearn.com/




exit()
print("#Intro_python_______________ Introduction to Python____________________________")


# print(7//2) # floor quoteent
# print(13%2) # modular operator remainder
# print("Welcome to the Code Playground")


# exit()

print("#Intro_python_______________ Getting Started with Python__________________________")


#print("#working with Numberical data")
#6.17. Operator precedence  #https://docs.python.org/3/reference/expressions.html
# print(6/2*3**2)
# print(6/2*3)
# print(5+6/2*3)
# print(7-5+6/2*3)
# print()
# print()

# print("Workign with Text data")

# print("".join(['h','i']))

# x=1024
# print(isinstance(x,str))

# print("{}{}".format(*['h','i']))

# print("helower"+"pyton user")

# str="3434 this is a string"

# print(str.partition('is'))  # creates a partition.. add to tuples..

# print(True+ False)

# s='abc'   
# i=iter(s)
# print(next(i))   #https://www.geeksforgeeks.org/python-next-method/
# print(next(i))
# print(next(i))




# print("Mixing things up")
# print(9 + 4 - 7)
# print(9//4) #divide 9 how much to 4....that is...becomes...2
# print(9%2)  #modular..///remander.. left for 9 to 2.. that is becomes...1

# print()

# # #data types... 
# print(type("0"))
# print(type(2.04))
# print(type(2))
# print(float(4))       #float
# print(str(6)+str(5))  #string
# print(int(5.0))       #integer 
# print(chr(71))        # chr() builtin function
# print("hey man"+ "i am good") #concatination

# print()
# print("Balance", 5000,sep=":")
# print(4%5) #is 4 .. any thing less than ... would be itself

# x=(1,2,3)
# print(*x)
# print(*x,sep="1")
# print(*x,sep="1",end="3")

# exit()

# print("Iron", "Man", sep ="-")



#print("Labeling, Storing and Handling Data with Variables")
# x = 42       #integer
# y = "Hello"  #string
# z = 3.14     #float



# exit()


print("#Intro_python_______________ Interacting with the User__________________________")

#print("# taking user Input")
# hey=input()
# print(hey,"<<< this is string don't forget that")

# #working with input
# print("input weight:")
# wht=float(input())
# print("input height:")
# ht=float(input())

# whq=12      #wht/(ht**2)
# whq=wht/(ht**2)
# if whq < 18.5:
    # print("under wight")     #..// find this caracter.. it is not compatable to sololearns.. 
# elif whq > 18.5 and whq<25 :
    # print("Normal")
# elif whq > 25 and whq<30:
    # print("over weight")
# elif whq>30:
    # print("obesity")



# print()
# x="2"
# print(int(x)) #convert to string
# print(float(x)) # convert to float
# print(int(9.04)) # convert to int
# print("name:")
# name =input()
# print("age:")
# age=input()
# print(name+ "is"+ age)

# print()
# print()

#print("#In-Place Operator")
# x = 2
# print(x)

# x += 3
# print("x+=2",x)

# x *= 3
# print("x*=2",x)

# x **= 3
# print("x**=2",x)
# x %= 2
# print("x%=2",x)

# print()
# x = "spam"
# print("x = \"spam\"",x)

# x += "eggs"
# print("x = \"egg\"",x)

# x = "a"
# x *= 3
# print("x *= 3",x)


# print()



# exit()



print("#Intro_python_______________ Control Flow_________________________")

exit()
print()
print("# # Booleans  and comparision")
print()
print("2==3",2 == 3)           #equal.......... not assign
print("2 > 3 and 2<2",2 > 3 and 2<2)    #and 
print("2 > 3 and 2==2",2 > 3 and 2==2)   #lessthan ..... greaterthan ......comparative
print("2 == 3 or 2>=2",2 == 3 or 2>=2)   #greater or equal
print("0== 0 or 2 != 3",0== 0 or 2 != 3)  #the not equal to operator
print()
print("0  == 0 or True)",0  == 0 or True)#2 <>3)   #the not equal to operator

print()

print("alphabetical order of their component letters")
print("ord('a')",ord('a'))
print("ord('b')",ord('b'))
print("'a' > 'b'",'a' > 'b')

print("\"Bob\" > \"Dave\"","Bob" > "Dave")

print()
print()

x = (7 > 5)
print("int(7 > 5)",int(x))
print("int not(7 > 5)",int(not x))
print()
print("joining by converting each string to ord of \"hello world\"")
s = "hello world"
print(''.join(str(ord(c)) for c in s))

print()

print("#if statement")
print()

print("if #condition:")
print("   #statements    ")

x = 42
if x > 5:
    print("x is greater than 5")


print()

print(" else statment")
print()

x = 4
if x == 5:
    print("Yes")
else:
    print("No")

print()   
print("# Boolean Logic")
print()   

print("#and")
print("1 == 1 and 2 == 2",1 == 1 and 2 == 2)
print("1 == 1 and 2 == 3",1 == 1 and 2 == 3)
print("1 != 1 and 2 == 2",1 != 1 and 2 == 2)
print("2 < 1 and 3 > 6",2 < 1 and 3 > 6)
print()
print("#or")
print( "1 == 1 or 2 == 2",1 == 1 or 2 == 2)
print( "1 == 1 or 2 == 3 ",1 == 1 or 2 == 3 )
print( "1 != 1 or 2 == 2 ",1 != 1 or 2 == 2 )
print( "2 < 1  or 3 > 6 ",2 < 1  or 3 > 6 )
print()
print(" Boolean Not")

print("not 1 == 1",not 1 == 1)

print()
print(" Boolean Operator preccedance      NOT > XOR > AND > OR    derived from C")

print("2>3 and 4<2 or 3>3 and 2>3 or not(3>3)",2>3 and 4<2 or 3>3 and 2>3 or not(3>3))
print()


print("# while loops")

print()

print("#Loops")


i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")

print()

print("cummulative finder")
sum = 0
x = 10
while x > 0:
  sum += x
  x -= 1

print(sum)

# other possilble way
print()
i=0
for x in range(8):
    if x%2==0:
        # print(x)
        i+=x
     # i+=1   

print(i)

print()
func=lambda x:x%2==0
abc=list(filter(func,range(8)))
print(sum(abc))


print()
x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

print()

print(" # break continue")
print()

print("break statment")
i = 0
while True:
  print(i)
  i = i + 1
  
  if i >= 5:
    print("Breaking")
    break

print("Finished")
print()
print("continue statment")

i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)



print()

print(" Now this could be considered perfect:  # ticket issue ")
print(" While loop exit problem.... help .. for calculator .. a sorth.. tinkitner")

i = 1
ticket_cost = 100 
total = 0 


print("input 5  numbers")
while i<=5: 
    age = int(input()) 
    if age < 3: 
        i += 1
        continue 
    # break 
    else: 
        total += ticket_cost 
        #print("$" + str(total)) 
        i += 1
print(total) 


exit()


print("#Intro_python_______________ Lists______________________________")


# exit()

# words = ["Hello", "world", "!"]
# print(words[0])
# print(words[1])
# print(words[2])




# exit()
# a=[1,2,3,4]
# b=a.copy()
# print(b)
# b.append(a)
# print(b)
# a.append(b)
# print(a)
# print(len(a))
# print(len(b))


# m = [
    # [1, 2, 3],
    # [4, 5, 6]
    # ]
# print(m)

# strt = "Hello world!"
# print(strt[6])

# print()
# print()
# print()

# # # iterate throguh a list and dump the list

# x=[2,8]#,7,1,0,124,8897,55,3,67,99]
# nums=0


# for i in range (10):
    # if i>10:
        # print("nope")
    # else:
        # print("done" + str(i))



# y=[x if x==1 else x*2 for x in ["1","2"]][0]

# print([x if x==1 else x*2 for x in ["1","2"]])


# a=[2,4,6,8]
# b=a
# print(b)


# b[0]=7
# a[3]=9

# print(a)

# b.append(5)


# print(a)





# L=list(range(10))

# print(L)
# print(L.pop())#remove the last
# print(L)
# print(max(L))


# word="bringback"
# print(word[::-2])


# iterate throguh a list and dump the list
# for nums in len(x):
    # nums+=1
    
    
    
    
# # iterate throguh a list and dump the list
# print(list(range(len(x))))



# #diffrence b/n list and map>>???
# abc=list(range(5))
# sq=list(map(lambda x:x**2,range(5)))
# print(abc)
# print(sq)

# for i in range(len(x)):
    # print(x[i])
    # i+=i 

# # iterate throguh a list find cummmulative
# sum=0
# for num in x:
    # sum+=num
    
# print(sum)


# # to add all odd nubmer in list...

# b=[1,2,3,4,5]
# print(b[1:-2])
# print(b[1:-1])


# nums = [1,2,3,4]
# res=0

# for x in nums:
    # if x%2==nums:
        # continue
    # else:
        # print(x)    #res+=x #res = res+x
        # res+=x      #res = res+x
        
# print(res)



# i=list(range(1,4))
# # i=list(range(4))
# print(i)
# # s=list(map(lambda x:x**2,i)) 
# s=list(filter(lambda x:x**2,i))
# print(s)
# print(sum(s))




# i=1
# while i<=5:
    # print(i)
    # i+=1


#Python next() method
# list=[1,2,3,4]
# a=(i**2 for i in list)
# print(a)
# print(next(a),next(a))  #https://www.geeksforgeeks.org/python-next-method/



# fib=[0,1,1,2,3,5,8,13]
# # print(fib[::2])
# print(fib[2::2])



# # https://www.geeksforgeeks.org/python-range-function/       #Syntax of Python range() function

# # Syntax: range(start, stop, step)
# # In the given example, we are printing the number from 0 to 4.

# for i in range(5):
	# print(i, end=" ")
# print()

## The remove method working 
# l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

# l.remove('Alice')
# print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']


# # In this example, we are printing the number from 0 to 5. We are using the range function in which we are passing the stopping of the loop... printing first 6  whole number
# for i in range(6):
	# print(i, end=" ")
# print()


# for i in range(5, 20): # printing a naturar number from 5 to 20
	# print(i, end=" ")


# for i in range(0, 10, 2): # Example of Python range (start, stop, step)
	# print(i, end=" ")
# print()



# for i in range(0, 30, 4): #incremented by 4
	# print(i, end=" ")
# print()


# for i in range(25, 2, -2): #incremented by -2
	# print(i, end=" ")
# print()



# for i in range(3.3): #using a float number
	# print(i)

# # Concatenation of two range() functions using itertools chain() method

# from itertools import chain

# # Using chain method
# print("Concatenating the result")
# res = chain(range(5), range(10, 20, 2))

# for i in res:
	# print(i, end=" ")




# ele = range(10)[0]  # Accessing range() with an Index Value
# print("First element:", ele)

# ele = range(10)[-1]
# print("\nLast element:", ele)

# ele = range(10)[4]
# print("\nFifth element:", ele)

# range() function with List in Python

# fruits = ["apple", "banana", "cherry", "date"]

# for i in range(len(fruits)):
	# print(fruits[i])

# # Return Type in range() vs xrange()
# # initializing a with range()

# a = range(1, 10000)

# # initializing a with xrange()
# x = xrange(1, 10000)

# # testing the type of a
# print("The return type of range() is : ")
# print(type(a))

# # testing the type of x
# print("The return type of xrange() is : ")
# print(type(x))

# # Speed of xrange() and range() Function
# import sys

# # initializing a with range()
# a = range(1,10000)

# # initializing a with xrange()
# x = xrange(1,10000)

# # testing the size of a
# range() takes more memory
# print ("The size allotted using range() is : ")
# print (sys.getsizeof(a))

# # testing the size of x
# xrange() takes less memory
# print ("The size allotted using xrange() is : ")
# print (sys.getsizeof(x))


# # Operations Usage of xrange() and range() Function
# # initializing a with range()
# a = range(1,6)

# # initializing a with xrange()
# x = xrange(1,6)

# # testing usage of slice operation on range() prints without error
# print ("The list after slicing using range is : ")
# print (a[2:5])

# # testing usage of slice operation on xrange() raises error
# print ("The list after slicing using xrange is : ")
# print (x[2:5])

# # Python – Test if List contains elements in Range


# # Method #1 : 
    # # Using loop This is brute force method in which this task can be performed. In this, we just check using if condition if element falls in range, and break if we find even one occurrence out of range. 

# # Python3 code to demonstrate 
# # Test if List contains elements in Range
# # using loop

# # Initializing loop 
# test_list = [4, 5, 6, 7, 3, 9]

# # printing original list 
# print("The original list is : " + str(test_list))

# # Initialization of range 
# i, j = 3, 10

# # Test if List contains elements in Range using loop
# res = True
# for ele in test_list:
	# if ele < i or ele >= j :
		# res = False
		# break

# # printing result 
# print ("Does list contain all elements in range : " + str(res))


# # Method #2 : 
    # # Using all() This is alternative and shorter way to perform this task. In this we use check operation as a parameter to all() and returns True when all elements in range. 


# # Python3 code to demonstrate 
# # Test if List contains elements in Range
# # using all()

# # Initializing loop 
# test_list = [4, 5, 6, 7, 3, 9]

# # printing original list 
# print("The original list is : " + str(test_list))

# # Initialization of range 
# i, j = 3, 10

# # Test if List contains elements in Range
# # using all()
# res = all(ele >= i and ele < j for ele in test_list) 

# # printing result 
# print ("Does list contain all elements in range : " + str(res))


# # Method #3 : Using list comprehension and len()

# # Python3 code to demonstrate
# # Test if List contains elements in Range
# # using List Comprehension and len()
# # Initializing list


# test_list = [4, 5, 6, 7, 3, 9]

# # printing original list
# print("The original list is : " + str(test_list))

# # Initialization of range
# i, j = 3, 10

# # Test if List contains elements in Range
# # using List Comprehension and len()
# out_of_range = len([ele for ele in test_list if ele < i or ele >= j])==0

# # printing result
# print ("Does list contain all elements in range : " + str(out_of_range))


# # Python3 code to demonstrate
# # Test if List contains elements in Range
# # using any()

# # Initializing list and range boundaries
# test_list = [4, 5, 6, 7, 3, 9]
# i, j = 3, 10

# # Checking if any element in the list is within the range
# res = any(i <= x < j for x in test_list)

# # Printing the result
# print("Does list contain any element in range: " + str(res))


# # Method 5: Using filter() function

# # Python3 code to demonstrate
# # Test if List contains elements in Range
# # using filter()

# # Initializing list and range boundaries
# test_list = [4, 5, 6, 7, 3, 9]
# i, j = 3, 10

# # Function to check if x lies within the given range
# def in_range(x):
	# return i <= x < j

# # Filtering out the elements that lie within the range
# # filtered_list = list(filter(in_range, test_list))

# # Checking if the filtered list is not empty
# res = bool(filtered_list)

# # Printing the result
# print("Does list contain any element in range: " + str(res))


# Python – Test if elements of list are in Min/Max range from other list


# # Method #1 : Using loop + min() + max()
# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using loop + min() + max()

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original lists
# print("The original list is : " + str(test_list))

# # initializing range_list
# range_list = [4, 7, 9, 6]

# res = True
# for ele in range_list:

	# flag off list in case of any off range element
	# if ele max(test_list):
		# res = False
		# break

# # printing result
# print("Are all elements in min/max range? : " + str(res))



# # Method #2 : Using all() + min() + max()

# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using all() + min() + max()

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original lists
# print("The original list is : " + str(test_list))

# # initializing range_list
# range_list = [4, 7, 9, 6]

# # checking for all values in range using all()
# res = all(ele >= min(test_list) and ele <= max(test_list)
		# for ele in range_list)

# # printing result
# print("Are all elements in min/max range? : " + str(res))


# # Method #3: Using set intersection


# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using set intersection

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original lists
# print("The original list is : " + str(test_list))

# # initializing range_list
# range_list = [4, 7, 9, 6]

# # using set intersection to find common elements between test_list and range_list
# # common_elements = set(test_list).intersection(set(range_list))

# # checking if all common elements are within the range

# res = all(ele >= min(test_list) and ele <= max(test_list)
		# for ele in common_elements)

# # printing result
# print("Are all elements in min/max range? : " + str(res))

# # Method #4: Use list comprehension

# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using list comprehension

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original list
# print("The original list is : " + str(test_list))

# # initializing range list
# range_list = [4, 7, 9, 6]

# # filtering range list to remove elements outside of min/max range
# # filtered_list = [x for x in range_list if min(test_list) <= x <= max(test_list)]

# # checking if filtered list is the same as range list
# res = filtered_list == range_list

# # printing result
# print("Are all elements in min/max range? : " + str(res))










# # Python | Generate random numbers within a given range and store in a list

# import random


# print("Random integers between 0 and 9: ")
# for i in range(4, 15):
	# y = random.randrange(9)
	# print(y)

# # Method 1: Generate random integers using random.randrange() method
# import random


# print("Random integers between 0 and 9: ")
# for i in range(4, 15):
	# y = random.randrange(9)
	# print(y)

# # Method 2: Generate random integers using random.uniform() method
# import random


# print("Random integers between 0 and 9: ")
# for i in range(4, 11):
	# y = random.uniform(4, 10)
	# print(y)


# # Method 3: Generate random integers using randbelow() method
# from secrets import randbelow

# for _ in range(3, 9):

	# print(randbelow(15))


# # Method 4: Generate random integers using the random.randint() method

# # Python code to generate
# # random numbers and
# # append them to a list


# import random

# # Function to generate
# # and append them 
# # start = starting range,
# # end = ending range
# # num = number of 
# # elements needs to be appended


# def Rand(start, end, num):
	# res = []

	# for j in range(num):
		# res.append(random.randint(start, end))

	# return res

# Driver Code
# num = 10
# start = 20
# end = 40
# print(Rand(start, end, num))


# # Using random.sample() function:
# import random

# num = 10
# start = 20
# end = 40

# result = random.sample(range(start, end + 1), num)

# print(result)



# # Python | Contiguous Boolean Range


# # Method #1 : Using enumerate() + zip() + list comprehension By using combination of above three functions, this task can easily be accomplished. The enumerate function handles the role of iteration, zip function groups the like values and the logic part is handled by list comprehension. 
# # Python3 code to demonstrate
# # Contiguous Boolean Ranging
# # using enumerate() + zip() + list comprehension

# # initializing list 
# test_list = [True, True, False, False, True,
			# True, True, True, False, True]

# # printing the original list 
# print ("The original list is : " + str(test_list))

# # using enumerate() + zip() + list comprehension
# # for Contiguous Boolean Ranging
# # res = [x for x, (i , j) in enumerate(zip( [2]
		# # + test_list, test_list + [2])) if i != j]

# # printing result
# print ("The boolean range list is : " + str(res))



  # # Method #2 : Using sum() + accumulate() + groupby() The above three functions can also be clubbed together to achieve the particular task, as they use the iterators to achieve it. The sum function counts each value, groupby groups each one and all together are accumulated by the accumulate function. 

# # Python3 code to demonstrate
# # Contiguous Boolean Ranging
# # using sum() + accumulate() + groupby()
# # from itertools import accumulate, groupby

# # initializing list 
# test_list = [True, True, False, False, False,
			# True, True, True, False, False]

# # printing the original list 
# print ("The original list is : " + str(test_list))

# # using sum() + accumulate() + groupby()
# # for Contiguous Boolean Ranging
# # res = [0] + list(accumulate(sum(1 for i in j) 
			# # for i, j in groupby(test_list)))

# # printing result
# print ("The boolean range list is : " + str(res))


# # Method #3 : Using looping


# # Python3 code to demonstrate
# # Contiguous Boolean Ranging
# # using for loop and if statement

# # initializing list 
# test_list = [True, True, False, False, False,
			# True, True, True, False, False]

# # printing the original list 
# print("The original list is:", test_list)

# # using for loop and if statement
# # for Contiguous Boolean Ranging

# res = []
# for i, v in enumerate(test_list):
	# if i == 0 or v != test_list[i-1]:
		# res.append(i)
# res.append(len(test_list))
# # printing result
# print("The boolean range list is:", res)
# # This code is contributed by Edula Vinay Kumar Reddy
# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
# print(sqs[4:7])




exit()















print("Intro_python_______________ Functions________________________________")



# #from challenges..Function..??
# a=()
# def func(n):
    # k=()
    # k=k+n
    # return k
    # return k
# for i in range(0,5,2):
    # a+=func((i,i+1))
# print(len(a))


# def count(n=0):
    # while True:
        # yield(yield n)
        # n+=1
# a=count()
# next(a)
# print(a.send(5),end="")
# print(a.send('a'))

# def gen():
    # global a
    # for num in [2,4,8]:
        # a+=1
        # yield (num*0.5)
# a=0.0

# # print(gen())

# lst=[]
# for val in gen():
    # lst.append(int(a==val))
# print(sum(lst))


# def fun(n):
    # if(n>100):
        # return n-5
    # return fun(fun(n+11))

# print(fun(2))
# # print(fun(105))


# Use Pop In Python to Remove an Item and Return It

# a=list(range(0,100))
# def function(x):
    # a.pop(x-1):
    # return(a)
# for i in range(0,100):
    # n=101-i
    # function(n)
# print(len(a))


cars = ['Mercedes Benz', 'BMW', 'Jeep', 'Mahindra', 'Maserati']

print(cars)

# Using pop() and storing the return value

ret_val = cars.pop(2)

print('The return value is:', ret_val)

# Updated List

print('The updated list is:', cars)



# import numpy as np
 # # b=np.array([[2,5],[3,7]])
# ak=np.array([[11,[2,2],[2,2],34],[34,34,3]])
# ak=ak.transpose();

# print(ak)

# ar1=np.array([[2,5],[3,7]])
# ar1=ar1.transpose();
# print(ar1)



# arr1=np.array([[1,2,3],[4,5,6]])

# print(arr1)


# # # #_______List function



 # # # # 
# # # nums = [1, 3, 5, 2, 4]
# # # print(len(nums))



 # # # # 
# # # letters = ["a", "b", "c"]
# # # letters += ["d"]
# # # print(len(letters))



 # # # # 
# # # str = "some text"
# # # x = len(str)
# # # print(x)

# # # #
# # # x ="abc"
# # # x *= 2
# # # print(len(x))



# # # nums = [1, 2, 3]
# # # nums.append(4)
# # # print(nums)




# # # nums = [9, 8, 7, 6, 5]
# # # nums.append(4)
# # # nums.insert(2, 11)
# # # print(len(nums))



# # # #index
# # # letters = ['p', 'q', 'r', 's', 'p', 'u']
# # # print(letters.index('r'))
# # # print(letters.index('p'))
# # # print(letters.index('q'))




# # # # max min
# # # x = [1, 8, 42, 3]
# # # print(min(x))
# # # print(max(x))



# # # # count remove and reverse
# # # x = [2, 4, 6, 2, 7, 2, 9]
# # # print(x.count(2))
# # # x.remove(4)
# # # print(x)

# # # x.reverse()
# # # print(x)




# # # list = [8, 4, 2, 6]
# # # list.remove(2)
# # # print(len(list)+list.count(6))






# # # x = [2, 4, 6, 2, 7, 2, 9]
# # # print(x.count(2))

# # # x.remove(4)
# # # print(x)

# # # x.reverse()
# # # print(x)


# # # queue = ['John', 'Amy', 'Bob', 'Adam']
# # # take=input()
# # # queue.append(take)
# # # print(queue)



# # # # string format format()



# # # nums = [4, 5, 6]
# # # msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
# # # print(msg)




# # # a = "{x}, {y}".format(x=5, y=12)
# # # print(a


# # # # join()

# # # x = ", ".join(["spam", "eggs", "ham"])
# # # print(x)
# # # #prints "spam, eggs, ham"



# # # #python excercise for beginners...

# # # # https://holypython.com/beginner-python-exercises/exercise-1-print/



# # # s = input()
# # # words = [word for word in s.split(" ")]# send it to list..

# # # print(words) # that w/h dumps like i say go to list and see more examples..

# # # # exit()
# # # print(" ".join(sorted(list(set(words)))))



# # # for i in range(3.3): #using a float number
	# # # print(i)



# # # # print(4%5)
# # # # # print(1+2+3+4%5)

# # # # # print(int('3'))
# # # # print(int('4.0'))


# # # # # print(int('4.0')+int('3'))    





print("Inter_Python_____________Dictonary// ___________________")


# #tuples inside function..

# def calc(x):
    # #your code goes here
    # return (x*4,x**2)

# side = int(input())
# p, a = calc(side)

# print("Perimeter: " + str(p))
# print("Area: " + str(a))






# # from math import pi
# my="one","tw","thre"

# print(my[0])


print("Inter_Python_____________Tuples// ___________________")

# # to convert list to dictoinary..
# contacts = [
    # ('James', 42),
    # ('Amy', 24),
    # ('John', 31),
    # ('Amanda', 63),
    # ('Bob', 18)
# ]

# contacts=dict(contacts)    #let it be taught/ treated...as dictonary.. ignoring .get(amanda)
# name=input()
# if name in contacts:
    # print(name, 'is', contacts[name])
# else:
    # print('not found')










print("Inter_python _______________ sets_________________")










# # https://sparkbyexamples.com/python/convert-python-range-to-list/
# rang=range(20)
# mylist=[*rang]
# print(mylist)


































