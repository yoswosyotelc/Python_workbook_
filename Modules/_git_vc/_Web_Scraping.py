# # @#$!@#$@!#$upwork### << ///Oct_2023..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$@
# # !!!!! don't stay at one part for more than 1 weekds...!!!!
# # !!!!! proceed as you go through by commenting .. for furhter refirinement..


#1.Write a Python program to create an Enum object and display a member name and value.Go to the editor

from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('\nMember name: {}'.format(Country.Albania.name))
print('Member value: {}'.format(Country.Albania.value))

# #2.Write a Python program to iterate over an enum class and display individual member and their value.Go to the editor

# from enum import Enum
# class Country(Enum):
    # Afghanistan = 93
    # Albania = 355
    # Algeria = 213
    # Andorra = 376
    # Angola = 244
    # Antarctica = 672
# for data in Country:
    # print('{:15} = {}'.format(data.name, data.value))
	
# #3.Write a Python program to display all the member name of an enum class ordered by their values.Go to the editor

# import enum
# class Country(enum.IntEnum):
    # Afghanistan = 93
    # Albania = 355
    # Algeria = 213
    # Andorra = 376
    # Angola = 244
    # Antarctica = 672
# print('Country Name ordered by Country Code:')
# print('\n'.join('  ' + c.name for c in sorted(Country)))

# #4.Write a Python program to get all values from an enum class.Go to the editor

# from enum import IntEnum
# class Country(IntEnum):
    # Afghanistan = 93
    # Albania = 355
    # Algeria = 213
    # Andorra = 376
    # Angola = 244
    # Antarctica = 672
# country_code_list = list(map(int, Country))
# print(country_code_list)

# #5.Write a Python program to count the most common words in a dictionary.Go to the editor

# words = [
   # 'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   # 'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   # 'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   # 'white', 'orange', "orange", 'red'
# ]
# from collections import Counter
# word_counts = Counter(words)
# top_four = word_counts.most_common(4)
# print(top_four)

# #6.Write a Python program to find the class wise roll number from a tuple-of-tuples.Go to the editor

# from collections import defaultdict
# classes = (
    # ('V', 1),
    # ('VI', 1),
    # ('V', 2),
    # ('VI', 2),
    # ('VI', 3),
    # ('VII', 1),
# )

# class_rollno = defaultdict(list)

# for class_name, roll_id in classes:
    # class_rollno[class_name].append(roll_id)

# print(class_rollno)

# #7.Write a Python program to count the number of students of individual class.Go to the editor

# from collections import Counter
# classes = (
    # ('V', 1),
    # ('VI', 1),
    # ('V', 2),
    # ('VI', 2),
    # ('VI', 3),
    # ('VII', 1),
# )
# students = Counter(class_name for class_name, no_students in classes)
# print(students)

# #8.Write a Python program to get the unique enumeration values.Go to the editor

# import enum
# class Countries(enum.Enum):
    # Afghanistan = 93
    # Albania = 355
    # Algeria = 213
    # Andorra = 376
    # Angola = 244
    # India = 355
    # USA = 213
# for result in Countries:
    # print('{:15} = {}'.format(result.name, result.value))

# #9.Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.Go to the editor

# from collections import OrderedDict
# dict = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
# new_dict = OrderedDict(dict.items())
# for key in new_dict:
    # print (key, new_dict[key])

# print("\nIn reverse order:")
# for key in reversed(new_dict):
    # print (key, new_dict[key])

# #10.Write a Python program to group a sequence of key-value pairs into a dictionary of lists.Go to the editor

# from collections import defaultdict
# class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
# d = defaultdict(list)
# for k, v in class_roll:
    # d[k].append(v)
# print(sorted(d.items()))

# #11.Write a Python program to compare two unordered lists (not sets).Go to the editor

# from collections import Counter
# def compare_lists(x, y):
    # return Counter(x) == Counter(y)
# n1 = [20, 10, 30, 10, 20, 30]
# n2 = [30, 20, 10, 30, 20, 50]
# print(compare_lists(n1, n2))

# #12.Write a Python program to create an array contains six integers. Also print all the members of the array.Go to the editor

# from array import array
# my_array = array('i', [10, 20, 30, 40, 50])
# for i in my_array:
    # print(i)

# #13.Write a Python program to get the array size of types unsigned integer and float.Go to the editor

# from array import array
# a = array("I", (12,25))
# print(a.itemsize)
# a = array("f", (12.236,36.36))
# print(a.itemsize)

# #14.Write a Python program to get an array buffer information.Go to the editor

# from array import array
# a = array("I", (12,25))
# print("Array buffer start address in memory and number of elements.")
# print(a.buffer_info())

# #15.Write a Python program to get the length of an array.Go to the editor

# from array import array
# num_array = array('i', [10,20,30,40,50])
# print("Length of the array is:")
# print(len(num_array))

# #16.Write a Python program to convert an array to an ordinary list with the same items.Go to the editor

# from array import array
# arra1 = array('b', [1,2,3,4])
# print("Original array: ")
# print(arra1)
# print("Array to list: ")
# print(arra1.tolist())

# #17.Write a Python program to convert an array to an array of machine values and return the bytes representation.Go to the editor

# import array
# import binascii
# a = array.array('i', [1,2,3,4,5,6])
# print("Original array:")
# print('A1:', a)
# bytes_array = a.tobytes()
# print('Array of bytes:', binascii.hexlify(bytes_array))

# #18.Write a Python program to read a string and interpreting the string as an array of machine values.Go to the editor

# from array import array
# import binascii
# array1 = array('i', [7, 8, 9, 10])
# print('array1:', array1)
# as_bytes = array1.tobytes()
# print('Bytes:', binascii.hexlify(as_bytes))
# array2 = array('i')
# array2.frombytes(as_bytes)
# print('array2:', array2)

# #19.Write a Python program to push three items into the heap and print the items from the heap.Go to the editor

# import heapq
# heap = []
# heapq.heappush(heap, ('V', 1))
# heapq.heappush(heap, ('V', 2))
# heapq.heappush(heap, ('V', 3))
# for a in heap:
	# print(a)
	
# #20.Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap.Go to the editor

# import heapq
# heap = []
# heapq.heappush(heap, ('V', 3))
# heapq.heappush(heap, ('V', 2))
# heapq.heappush(heap, ('V', 1))
# print("Items in the heap:")
# for a in heap:
	# print(a)
# print("----------------------")
# print("The smallest item in the heap:")
# print(heap[0])
# print("----------------------")
# print("Pop the smallest item in the heap:")
# heapq.heappop(heap)
# for a in heap:
	# print(a)

# #21.Write a Python program to push an item on the heap, then pop and return the smallest item from the heap.Go to the editor

# import heapq
# heap = []
# heapq.heappush(heap, ('V', 3))
# heapq.heappush(heap, ('V', 2))
# heapq.heappush(heap, ('V', 1))
# print("Items in the heap:")
# for a in heap:
	# print(a)
# print("----------------------")
# print("Using heappushpop push item on the heap and return the smallest item.")
# heapq.heappushpop(heap, ('V', 6))
# for a in heap:
	# print(a)
	
# #22.Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time.Go to the editor

# import heapq
# def heapsort(h):
    # heap = []
    # for value in h:
        # heapq.heappush(heap, value)
    # return [heapq.heappop(heap) for i in range(len(heap))]

# print(heapsort([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))

# #23.Write a Python program to get the two largest and three smallest items from a dataset.Go to the editor

# import heapq
# h = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
# print(heapq.nlargest(2,h))
# print(heapq.nsmallest(3,h))

# #24.Write a Python program to locate the left insertion point for a specified value in sorted order.Go to the editor

# import bisect
# def index(a, x):
    # i = bisect.bisect_left(a, x)
    # return i
    
# a = [1,2,4,5]
# print(index(a, 6))
# print(index(a, 3))

# #25.Write a Python program to locate the right insertion point for a specified value in sorted order.Go to the editor

# import bisect
# def index(a, x):
    # i = bisect.bisect_right(a, x)
    # return i
    
# a = [1,2,4,7]
# print(index(a, 6))
# print(index(a, 3))

# #26.Write a Python program to insert items into a list in sorted order.Go to the editor

# import bisect
# # Sample list
# my_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

# print("Original List:")
# print(my_list)
# sorted_list = []
# for i in my_list:
    # position = bisect.bisect(sorted_list, i)
    # bisect.insort(sorted_list, i)
# print("Sorted List:")
# print(sorted_list)

# #27.a Python program to create a queue and display all the members and size of the queue.Go to the editor

# import queue
# q = queue.Queue()
# for x in range(4):
    # q.put(x)
# print("Members of the queue:")
# y=z=q.qsize()

# for n in list(q.queue):
    # print(n, end=" ")
# print("\nSize of the queue:")
# print(q.qsize())

# #28.Write a Python program to find whether a queue is empty or not.Go to the editor

# import queue
# p = queue.Queue()
# q = queue.Queue()
# for x in range(4):
    # q.put(x)
# print(p.empty())
# print(q.empty())

# #29.Write a Python program to create a FIFO queue.Go to the editor

# import queue
# q = queue.Queue()
# #insert items at the end of the queue 
# for x in range(4):
    # q.put(str(x))
# #remove items from the head of the queue 
# while not q.empty():
    # print(q.get(), end=" ")
# print("\n")

# #30.Write a Python program to create a LIFO queue.Go to the editor

# import queue
# q = queue.LifoQueue()
# #insert items at the head of the queue 
# for x in range(4):
    # q.put(str(x))
# #remove items from the head of the queue 
# while not q.empty():
    # print(q.get(), end=" ")
# print()

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

