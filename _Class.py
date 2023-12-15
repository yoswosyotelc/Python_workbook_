# # # @#$!@#$@!#$upwork### << ///Oct_2023..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$@
# # # !!!!! don't stay at one part for more than 1 weekds...!!!!
# # # !!!!! proceed as you go through by commenting .. for furhter refirinement..

# #1. Write a Python class to convert an integer to a roman numeral. - Go to the editor

# class py_solution:
    # def int_to_Roman(self, num):
        # val = [
            # 1000, 900, 500, 400,
            # 100, 90, 50, 40,
            # 10, 9, 5, 4,
            # 1
            # ]
        # syb = [
            # "M", "CM", "D", "CD",
            # "C", "XC", "L", "XL",
            # "X", "IX", "V", "IV",
            # "I"
            # ]
        # roman_num = ''
        # i = 0
        # while  num > 0:
            # for _ in range(num // val[i]):
                # roman_num += syb[i]
                # num -= val[i]
            # i += 1
        # return roman_num


# print(py_solution().int_to_Roman(1))
# print(py_solution().int_to_Roman(4000))

# #2. Write a Python class to convert a roman numeral to an integer. - Go to the editor

# class py_solution:
    # def roman_to_int(self, s):
        # rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # int_val = 0
        # for i in range(len(s)):
            # if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                # int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            # else:
                # int_val += rom_val[s[i]]
        # return int_val

# print(py_solution().roman_to_int('MMMCMLXXXVI'))
# print(py_solution().roman_to_int('MMMM'))
# print(py_solution().roman_to_int('C'))

# #3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. - Go to the editor

# class py_solution:
   # def is_valid_parenthese(self, str1):
        # stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        # for parenthese in str1:
            # if parenthese in pchar:
                # stack.append(parenthese)
            # elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                # return False
        # return len(stack) == 0

# print(py_solution().is_valid_parenthese("(){}[]"))
# print(py_solution().is_valid_parenthese("()[{)}"))
# print(py_solution().is_valid_parenthese("()"))

# #4. Write a Python class to get all possible unique subsets from a set of distinct integers. - Go to the editor

# class py_solution:
    # def sub_sets(self, sset):
        # return self.subsetsRecur([], sorted(sset))
    
    # def subsetsRecur(self, current, sset):
        # if sset:
            # return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        # return [current]

# print(py_solution().sub_sets([4,5,6]))

# #5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. - Go to the editor

# class py_solution:
   # def twoSum(self, nums, target):
        # lookup = {}
        # for i, num in enumerate(nums):
            # if target - num in lookup:
                # return (lookup[target - num], i )
            # lookup[num] = i
# print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))

# #6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. - Go to the editor

# class py_solution:
 # def threeSum(self, nums):
        # nums, result, i = sorted(nums), [], 0
        # while i < len(nums) - 2:
            # j, k = i + 1, len(nums) - 1
            # while j < k:
                # if nums[i] + nums[j] + nums[k] < 0:
                    # j += 1
                # elif nums[i] + nums[j] + nums[k] > 0:
                    # k -= 1
                # else:
                    # result.append([nums[i], nums[j], nums[k]])
                    # j, k = j + 1, k - 1
                    # while j < k and nums[j] == nums[j - 1]:
                        # j += 1
                    # while j < k and nums[k] == nums[k + 1]:
                        # k -= 1
            # i += 1
            # while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                # i += 1
        # return result

# print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

# #7. Write a Python class to implement pow(x, n). - Go to the editor

# class py_solution:
   # def pow(self, x, n):
        # if x==0 or x==1 or n==1:
            # return x 

        # if x==-1:
            # if n%2 ==0:
                # return 1
            # else:
                # return -1
        # if n==0:
            # return 1
        # if n<0:
            # return 1/self.pow(x,-n)
        # val = self.pow(x,n//2)
        # if n%2 ==0:
            # return val*val
        # return val*val*x

# print(py_solution().pow(2, -3));
# print(py_solution().pow(3, 5));
# print(py_solution().pow(100, 0));

# #8. Write a Python class to reverse a string word by word. - Go to the editor

# class py_solution:
    # def reverse_words(self, s):
        # return ' '.join(reversed(s.split()))


# print(py_solution().reverse_words('hello .py'))

# #9. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case. - Go to the editor

# class IOString():
    # def __init__(self):
        # self.str1 = ""

    # def get_String(self):
        # self.str1 = input()

    # def print_String(self):
        # print(self.str1.upper())

# str1 = IOString()
# str1.get_String()
# str1.print_String()

# #10. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. - Go to the editor

# class Rectangle():
    # def __init__(self, l, w):
        # self.length = l
        # self.width  = w

    # def rectangle_area(self):
        # return self.length*self.width

# newRectangle = Rectangle(12, 10)
# print(newRectangle.rectangle_area())

# #11. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. - Go to the editor

# class Circle():
    # def __init__(self, r):
        # self.radius = r

    # def area(self):
        # return self.radius**2*3.14
    
    # def perimeter(self):
        # return 2*self.radius*3.14

# NewCircle = Circle(8)
# print(NewCircle.area())
# print(NewCircle.perimeter())

# #12. Write a Python program to get the class name of an instance in Python. - Go to the editor

# import itertools
# x = itertools.cycle('ABCD')
# print(type(x).__name__)

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

# #

