# # # @#$!@#$@!#$upwork### << ///Oct_2023..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$@
# # # !!!!! don't stay at one part for more than 1 weekds...!!!!
# # # !!!!! proceed as you go through by commenting .. for furhter refirinement..

# #1.Write a Python program for binary search.Go to the editor

# def binary_search(item_list,item):
	# first = 0
	# last = len(item_list)-1
	# found = False
	# while( first<=last and not found):
		# mid = (first + last)//2
		# if item_list[mid] == item :
			# found = True
		# else:
			# if item < item_list[mid]:
				# last = mid - 1
			# else:
				# first = mid + 1	
	# return found
	
# print(binary_search([1,2,3,5,8], 6))
# print(binary_search([1,2,3,5,8], 5))

# #2.Write a Python program for sequential search.Go to the editor

# def Sequential_Search(dlist, item):

    # pos = 0
    # found = False
    
    # while pos < len(dlist) and not found:
        # if dlist[pos] == item:
            # found = True
        # else:
            # pos = pos + 1
    
    # return found, pos

# print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))

# #3.Write a Python program for binary search for an ordered list.Go to the editor

# def Ordered_binary_Search(olist, item):
    
    # if len(olist) == 0:
        # return False
    # else:
        # midpoint = len(olist) // 2
        # if olist[midpoint] == item:
            # return True
        # else:
            # if item < olist[midpoint]:
                # return binarySearch(olist[:midpoint], item)
            # else:
                # return binarySearch(olist[midpoint+1:], item)

# def binarySearch(alist, item):

    # first = 0
    # last = len(alist) - 1
    # found = False

    # while first <= last and not found:
        # midpoint = (first + last) // 2
        # if alist[midpoint] == item:
            # found = True
        # else:
            # if item < alist[midpoint]:
                # last = midpoint - 1
            # else:
                # first = midpoint + 1

    # return found

# print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
# print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))

# #4.Write a Python program to sort a list of elements using the bubble sort algorithm.Go to the editor

# def bubbleSort(nlist):
    # for passnum in range(len(nlist)-1,0,-1):
        # for i in range(passnum):
            # if nlist[i]>nlist[i+1]:
                # temp = nlist[i]
                # nlist[i] = nlist[i+1]
                # nlist[i+1] = temp

# nlist = [14,46,43,27,57,41,45,21,70]
# bubbleSort(nlist)
# print(nlist)

# #5.Write a Python program to sort a list of elements using the selection sort algorithm.Go to the editor

# def selectionSort(nlist):
   # for fillslot in range(len(nlist)-1,0,-1):
       # maxpos=0
       # for location in range(1,fillslot+1):
           # if nlist[location]>nlist[maxpos]:
               # maxpos = location

       # temp = nlist[fillslot]
       # nlist[fillslot] = nlist[maxpos]
       # nlist[maxpos] = temp

# nlist = [14,46,43,27,57,41,45,21,70]
# selectionSort(nlist)
# print(nlist)

# #6.Write a Python program to sort a list of elements using the insertion sort algorithm.Go to the editor

# def insertionSort(nlist):
   # for index in range(1,len(nlist)):

     # currentvalue = nlist[index]
     # position = index

     # while position>0 and nlist[position-1]>currentvalue:
         # nlist[position]=nlist[position-1]
         # position = position-1

     # nlist[position]=currentvalue

# nlist = [14,46,43,27,57,41,45,21,70]
# insertionSort(nlist)
# print(nlist)

# #7.Write a Python program to sort a list of elements using shell sort algorithm.Go to the editor

# def shellSort(alist):
    # sublistcount = len(alist)//2
    # while sublistcount > 0:
      # for start_position in range(sublistcount):
        # gap_InsertionSort(alist, start_position, sublistcount)

      # print("After increments of size",sublistcount, "The list is",nlist)

      # sublistcount = sublistcount // 2

# def gap_InsertionSort(nlist,start,gap):
    # for i in range(start+gap,len(nlist),gap):

        # current_value = nlist[i]
        # position = i

        # while position>=gap and nlist[position-gap]>current_value:
            # nlist[position]=nlist[position-gap]
            # position = position-gap

        # nlist[position]=current_value


# nlist = [14,46,43,27,57,41,45,21,70]
# shellSort(nlist)
# print(nlist)

# #8.Write a Python program to sort a list of elements using the merge sort algorithm.Go to the editor

# def mergeSort(nlist):
    # print("Splitting ",nlist)
    # if len(nlist)>1:
        # mid = len(nlist)//2
        # lefthalf = nlist[:mid]
        # righthalf = nlist[mid:]

        # mergeSort(lefthalf)
        # mergeSort(righthalf)
        # i=j=k=0       
        # while i < len(lefthalf) and j < len(righthalf):
            # if lefthalf[i] < righthalf[j]:
                # nlist[k]=lefthalf[i]
                # i=i+1
            # else:
                # nlist[k]=righthalf[j]
                # j=j+1
            # k=k+1

        # while i < len(lefthalf):
            # nlist[k]=lefthalf[i]
            # i=i+1
            # k=k+1

        # while j < len(righthalf):
            # nlist[k]=righthalf[j]
            # j=j+1
            # k=k+1
    # print("Merging ",nlist)

# nlist = [14,46,43,27,57,41,45,21,70]
# mergeSort(nlist)
# print(nlist)

# #9.Write a Python program to sort a list of elements using the quick sort algorithm.Go to the editor

# def quickSort(data_list):
   # quickSortHlp(data_list,0,len(data_list)-1)

# def quickSortHlp(data_list,first,last):
   # if first < last:

       # splitpoint = partition(data_list,first,last)

       # quickSortHlp(data_list,first,splitpoint-1)
       # quickSortHlp(data_list,splitpoint+1,last)


# def partition(data_list,first,last):
   # pivotvalue = data_list[first]

   # leftmark = first+1
   # rightmark = last

   # done = False
   # while not done:

       # while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           # leftmark = leftmark + 1

       # while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           # rightmark = rightmark -1

       # if rightmark < leftmark:
           # done = True
       # else:
           # temp = data_list[leftmark]
           # data_list[leftmark] = data_list[rightmark]
           # data_list[rightmark] = temp

   # temp = data_list[first]
   # data_list[first] = data_list[rightmark]
   # data_list[rightmark] = temp


   # return rightmark

# data_list = [54,26,93,17,77,31,44,55,20]
# quickSort(data_list)
# print(data_list)

# #10.Write a Python program for counting sort.Go to the editor

# def counting_sort(array1, max_val):
    # m = max_val + 1
    # count = [0] * m                
    
    # for a in array1:
    # # count occurences
        # count[a] += 1             
    # i = 0
    # for a in range(m):            
        # for c in range(count[a]):  
            # array1[i] = a
            # i += 1
    # return array1

# print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))

# #11.Write a Python code to create a program for Bitonic Sort.Go to the editor

# License:  https://bit.ly/2InTS3W 
# # Python program for Bitonic Sort. Note that this program 
# # works only when size of input is a power of 2. 
# # The parameter dir indicates the sorting direction, ASCENDING 
# # or DESCENDING; if (a[i] > a[j]) agrees with the direction, 
# # then a[i] and a[j] are interchanged.*/ 
# def compAndSwap(a, i, j, dire):
    # if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        # a[i], a[j] = a[j], a[i]
        # # It recursively sorts a bitonic sequence in ascending order,
# # if dir = 1, and in descending order otherwise (means dir=0).
# # The sequence to be sorted starts at index position low, 
# # the parameter cnt is the number of elements to be sorted. 
# def bitonicMerge(a, low, cnt, dire):
    # if cnt > 1:
        # k = int(cnt / 2)
        # for i in range(low, low + k):
            # compAndSwap(a, i, i + k, dire)
        # bitonicMerge(a, low, k, dire)
        # bitonicMerge(a, low + k, k, dire)

        # # This funcion first produces a bitonic sequence by recursively


# # sorting its two halves in opposite sorting orders, and then
# # calls bitonicMerge to make them in the same order 
# def bitonicSort(a, low, cnt, dire):
    # if cnt > 1:
        # k = int(cnt / 2)
        # bitonicSort(a, low, k, 1)
        # bitonicSort(a, low + k, k, 0)
        # bitonicMerge(a, low, cnt, dire)

        # # Caller of bitonicSort for sorting the entire array of length N


# # in ASCENDING order
# def sort(a, N, up):
    # bitonicSort(a, 0, N, up)


# # Driver code to test above
# a = []
# print("How many numbers u want to enter?");
# n = int(input())
# print("Input the numbers:");
# for i in range(n):
    # a.append(int(input()))
# up = 1

# sort(a, n, up)
# print("\n\nSorted array is:")
# for i in range(n):
    # print("%d" % a[i])

# #12.Write a Python program to sort a list of elements using Bogosort sort.Go to the editor

# import random

# def bogosort(nums):
    # def isSorted(nums):
        # if len(nums) < 2:
            # return True
        # for i in range(len(nums) - 1):
            # if nums[i] > nums[i + 1]:
                # return False
        # return True

    # while not isSorted(nums):
        # random.shuffle(nums)
    # return nums
# num1 = input('Input  comma separated numbers:\n').strip()
# nums = [int(item) for item in num1.split(',')]
# print(bogosort(nums))

# #13.Write a Python program to sort a list of elements using Gnome sort.Go to the editor

# def  gnome_sort(nums):
    # if len(nums) <= 1:
        # return nums
        
    # i = 1
    
    # while i < len(nums):
        # if nums[i-1] <= nums[i]:
            # i += 1
        # else:
            # nums[i-1], nums[i] = nums[i], nums[i-1]
            # i -= 1
            # if (i == 0):
                # i = 1
           
# user_input = input("Input numbers separated by a comma:\n").strip()
# nums = [int(item) for item in user_input.split(',')]
# gnome_sort(nums)
# print(nums)

# #14.Write a Python program to sort a list of elements using Cocktail shaker sort.Go to the editor

# def cocktail_shaker_sort(nums):
    # for i in range(len(nums)-1, 0, -1):
        # is_swapped = False
        
        # for j in range(i, 0, -1):
            # if nums[j] < nums[j-1]:
                # nums[j], nums[j-1] = nums[j-1], nums[j]
                # is_swapped = True

        # for j in range(i):
            # if nums[j] > nums[j+1]:
                # nums[j], nums[j+1] = nums[j+1], nums[j]
                # is_swapped = True
        
        # if not is_swapped:
            # return nums
 
# num1 = input('Input comma separated numbers:\n').strip()
# nums = [int(item) for item in num1.split(',')]
# print(cocktail_shaker_sort(nums))

# #15.Write a Python program to sort a list of elements using Comb sort.Go to the editor

# def comb_sort(nums):
    # shrink_fact = 1.3
    # gaps = len(nums)
    # swapped = True
    # i = 0

    # while gaps > 1 or swapped:
        # gaps = int(float(gaps) / shrink_fact)

        # swapped = False
        # i = 0

        # while gaps + i < len(nums):
            # if nums[i] > nums[i+gaps]:
                # nums[i], nums[i+gaps] = nums[i+gaps], nums[i]
                # swapped = True
            # i += 1
    # return nums

# num1 = input('Input comma separated numbers:\n').strip()
# nums = [int(item) for item in num1.split(',')]
# print(comb_sort(nums))

# #16.Write a Python program to sort a list of elements using Cycle sort.Go to the editor

# # License: https://bit.ly/2V5W81t 
# def cycleSort(vector):
    # "Sort a vector in place and return the number of writes."
    # writes = 0
 
    # # Loop through the vector to find cycles to rotate.
    # for cycleStart, item in enumerate(vector):
 
        # # Find where to put the item.
        # pos = cycleStart
        # for item2 in vector[cycleStart + 1:]:
            # if item2 < item:
                # pos += 1
 
        # # If the item is already there, this is not a cycle.
        # if pos == cycleStart:
            # continue
 
        # # Otherwise, put the item there or right after any duplicates.
        # while item == vector[pos]:
            # pos += 1
        # vector[pos], item = item, vector[pos]
        # writes += 1
 
        # # Rotate the rest of the cycle.
        # while pos != cycleStart:
 
            # # Find where to put the item.
            # pos = cycleStart
            # for item2 in vector[cycleStart + 1:]:
                # if item2 < item:
                    # pos += 1
 
            # # Put the item there or right after any duplicates.
            # while item == vector[pos]:
                # pos += 1
            # vector[pos], item = item, vector[pos]
            # writes += 1
 
    # return writes
 
 
# if __name__ == '__main__':
    # x = [0, 1, 2, 2, 2, 2, 1, 9, 3.5, 5, 8, 4, 7, 0, 6]
    # xcopy = x[::]
    # writes = cycleSort(xcopy)
    # if xcopy != sorted(x):
        # print('Wrong order!')
    # else:
        # print('%r\nIs correctly sorted using cycleSort to'
              # '\n%r\nUsing %i writes.' % (x, xcopy, writes))

# #17.Write a Python program to sort a list of elements using Heap sort.Go to the editor

# def heap_data(nums, index, heap_size):
    # largest_num = index
    # left_index = 2 * index + 1
    # right_index = 2 * index + 2
    # if left_index < heap_size and nums[left_index] > nums[largest_num]:
        # largest_num = left_index

    # if right_index < heap_size and nums[right_index] > nums[largest_num]:
        # largest_num = right_index
    # if largest_num != index:
        # nums[largest_num], nums[index] = nums[index], nums[largest_num]
        # heap_data(nums, largest_num, heap_size)
# def heap_sort(nums):
    # n = len(nums)
    # for i in range(n // 2 - 1, -1, -1):
        # heap_data(nums, i, n)
    # for i in range(n - 1, 0, -1):
        # nums[0], nums[i] = nums[i], nums[0]
        # heap_data(nums, 0, i)
    # return nums
# user_input = input("Input numbers separated by a comma:\n").strip()
# nums = [int(item) for item in user_input.split(',')]
# heap_sort(nums)
# print(nums)

# #18.Write a Python program to sort a list of elements using Pancake sort.Go to the editor

# def pancake_sort(nums):
    # arr_len = len(nums)
    # while arr_len > 1:
        # mi = nums.index(max(nums[0:arr_len]))
        # nums = nums[mi::-1] + nums[mi+1:len(nums)]
        # nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        # arr_len -= 1
    # return nums

# user_input = input("Input numbers separated by a comma:\n").strip()
# nums = [int(item) for item in user_input.split(',')]
# print(pancake_sort(nums))

# #19.Write a Python program to sort a list of elements using Radix sort.Go to the editor

# def radix_sort(nums):
    # RADIX = 10
    # placement = 1
    # max_digit = max(nums)

    # while placement < max_digit:
      # buckets = [list() for _ in range( RADIX )]
      # for i in nums:
        # tmp = int((i / placement) % RADIX)
        # buckets[tmp].append(i)
      # a = 0
      # for b in range( RADIX ):
        # buck = buckets[b]
        # for i in buck:
          # nums[a] = i
          # a += 1
      # placement *= RADIX
    # return nums
# user_input = input("Input numbers separated by a comma:\n").strip()
# nums = [int(item) for item in user_input.split(',')]
# print(radix_sort(nums))

# #20.Write a Python program to sort a list of elements using Selection sort.Go to the editor

# def selection_sort(nums):
    # for i, n in enumerate(nums):
        # mn = min(range(i,len(nums)), key=nums.__getitem__)
        # nums[i], nums[mn] = nums[mn], n
    # return nums
# user_input = input("Input numbers separated by a comma:\n").strip()
# nums = [int(item) for item in user_input.split(',')]
# print(selection_sort(nums))

# #21.Write a Python program to sort a list of elements using Time sort.Go to the editor

# # License https://bit.ly/2InTS3W
# def binary_search(lst, item, start, end):
    # if start == end:
        # if lst[start] > item:
            # return start
        # else:
            # return start + 1
    # if start > end:
        # return start

    # mid = (start + end) // 2
    # if lst[mid] < item:
        # return binary_search(lst, item, mid + 1, end)
    # elif lst[mid] > item:
        # return binary_search(lst, item, start, mid - 1)
    # else:
        # return mid
# def insertion_sort(lst):
    # length = len(lst)

    # for index in range(1, length):
        # value = lst[index]
        # pos = binary_search(lst, value, 0, index - 1)
        # lst = lst[:pos] + [value] + lst[pos:index] + lst[index+1:]
    # return lst


# def merge(left, right):
    # if not left:
        # return right

    # if not right:
        # return left

    # if left[0] < right[0]:
        # return [left[0]] + merge(left[1:], right)

    # return [right[0]] + merge(left, right[1:])

# def time_sort(lst):
    # runs, sorted_runs = [], []
    # length = len(lst)
    # new_run = [lst[0]]
    # sorted_array = []

    # for i in range(1, length):
        # if i == length - 1:
            # new_run.append(lst[i])
            # runs.append(new_run)
            # break

        # if lst[i] < lst[i - 1]:
            # if not new_run:
                # runs.append([lst[i - 1]])
                # new_run.append(lst[i])
            # else:
                # runs.append(new_run)
                # new_run = []
        # else:
            # new_run.append(lst[i])

    # for run in runs:
        # sorted_runs.append(insertion_sort(run))

    # for run in sorted_runs:
        # sorted_array = merge(sorted_array, run)

    # return sorted_array

# user_input = input("Input numbers separated by a comma:\n").strip()
# nums = [int(item) for item in user_input.split(',')]
# print(time_sort(nums))

# #22.Write a Python program to sort a list of elements using Topological sort.Go to the editor

# # License https://bit.ly/2InTS3W
# #     a
# #    / \
# #   b  c
# #  / \
# # d  e
# edges = {'a': ['c', 'b'], 'b': ['d', 'e'], 'c': [], 'd': [], 'e': []}
# vertices = ['a', 'b', 'c', 'd', 'e']
# def topological_sort(start, visited, sort):
    # """Perform topolical sort on a directed acyclic graph."""
    # current = start
    # # add current to visited
    # visited.append(current)
    # neighbors = edges[current]
    # for neighbor in neighbors:
        # # if neighbor not in visited, visit
        # if neighbor not in visited:
            # sort = topological_sort(neighbor, visited, sort)
    # # if all neighbors visited add current to sort
    # sort.append(current)
    # # if all vertices haven't been visited select a new one to visit
    # if len(visited) != len(vertices):
        # for vertice in vertices:
            # if vertice not in visited:
                # sort = topological_sort(vertice, visited, sort)
    # # return sort
    # return sort

# sort = topological_sort('a', [], [])
# print(sort)

# #23.Write a Python program to sort a list of elements using Tree sort.Go to the editor

# # License https://bit.ly/2InTS3W
# # Tree_sort algorithm
# # Build a BST and in order traverse.
# class node():
    # # BST data structure
    # def __init__(self, val):
        # self.val = val
        # self.left = None 
        # self.right = None 
    
    # def insert(self,val):
        # if self.val:
            # if val < self.val:
                # if self.left is None:
                    # self.left = node(val)
                # else:
                    # self.left.insert(val)
            # elif val > self.val:
                # if self.right is None:
                    # self.right = node(val)
                # else:
                    # self.right.insert(val)
        # else:
            # self.val = val

# def inorder(root, res):
    # # Recursive travesal 
    # if root:
        # inorder(root.left,res)
        # res.append(root.val)
        # inorder(root.right,res)

# def treesort(arr):
    # # Build BST
    # if len(arr) == 0:
        # return arr
    # root = node(arr[0])
    # for i in range(1,len(arr)):
        # root.insert(arr[i])
    # # Traverse BST in order. 
    # res = []
    # inorder(root,res)
    # return res

# print(treesort([7,1,5,2,19,14,17]))

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #
