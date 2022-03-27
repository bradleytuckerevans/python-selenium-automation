#hw question 1 given a list return list of all elements below original mean
import collections

def under_mean(arr):
    number_of_elements = len(arr)
    total_num = sum(arr)
    mean_num = total_num / number_of_elements

    if all(arr) < mean_num:
        return arr





testlist = [1, 2, 4]

print(under_mean(testlist))


#hw2 question 2 find two lowest elements in a list

def two_low(min2):
     min2.sort()

     return min2[:2]

testlist1 = [9, 1, 3, 6, 8]

print(two_low(testlist1))






# 2nd array formed by shuffling elements of first array and deleting a random element.
# Find element missing in second array

#Solution 1

#def find_element(list1, list2):
 #   list1.sort()
  #  list2.sort()

   # for num1, num2 in zip(list1, list2):
    #    if num1 != num2:
     #       return num1

    #return list[-1]

#test_list1 = [1, 2, 3]
#test_list2 = [1, 3]

#print(str(find_element(test_list1, test_list2)) + " is the missing number")

#solution2
#import collections

#def find_element(list1, list2):
 #   dict = collections.defaultdict(int)

  #  for num in list2:
   #     dict[num] += 1

    #for num in list1:
     #   if dict[num] == 0:
      #      return num
       # else:
        #    dict[num] -= 1


#test_list1 = [1, 2, 3]
#test_list2 = [1, 3]


#print(str(find_element(test_list1, test_list2)) + " is the missing number")

#array of integers(positive and negative) find largest continous sum

#def findsum(arr):
 #   if len(arr) == 0:
  #      return 0

   # maxsum = currentsum = arr[0]

    #for num in arr[1:]:
     #   currentsum = max(currentsum + num, num)
      #  maxsum = max(currentsum, maxsum)

    #return maxsum

#testlist = [1, 2, -1, 3, 4, 10, 10, -10, -1, 32]
#print(findsum(testlist))

# given an array of integers return true if
# length of array is bigger or equal to 3
# and theres an increasing subarray followed by a decreasing subarray

#def mountainarray(arr):
 #   if len(arr) < 3:
  #      return False

   # i = 1
    #while i < len(arr) and arr[i] > arr[i - 1]:
     #   i += 1

    #if i == len(arr):
     #   return False

    #while i < len(arr) and arr[i] < arr[i - 1]:
     #   i += 1

    #return i == len(arr)

#testlistposi = [1,5, 9, 2]
#testlistneg = [1, 4, 7]

#print(mountainarray(testlistposi))

# given an array of integers, write a function to move all 0's to the end while rest stay in order

#def movezeros(arr):
 #   j = 0
  #  for num in arr:
   #     if num != 0:
    #        arr[j] = num
     #       j += 1

    #while j < len(arr):
     #   arr[j] = 0
      #  j += 1

    #return arr

#testlist = [0, 4, 0, 12, 3]

#print(movezeros(testlist))

# given an array of integers nums and an integer target.
# return 2 numbers for the array that add up to target.
# you assume has only one solution and not use same element twice

#def twosums(nums, target):
 #   if len(nums) == 2:
  #      return nums

   # sumset = set()

    #for num in nums:
     #   targetelement = target - num
      #  if targetelement not in sumset:
       #     sumset.add(num)
        #else:
         #    return [num, targetelement]

#testlist = [1, 4, 7, 8, 3, 11]
#testtarget = 8
#print(twosums(testlist, testtarget))

#hw question 1 given a list return list of all elements below original mean
import collections

#def under_mean(arr):
 #   number_of_elements = len(arr)
  #  total_num = sum(arr)
   # mean_num = total_num / number_of_elements


    #    return any(arr) < mean_num





#testlist = [1, 2, 4]

#print(under_mean(testlist))


#hw2 question 2 find two lowest elements in a list

#def two_low(min2):
 #    min2.sort()

  #   return min2[:2]

#testlist1 = [9, 1, 3, 6, 8]

#print(two_low(testlist1))

#l = [5,7,3,-42]

#min1,min2 = sorted(l)[:2]

#print(min1,min2)





















#Reverse a Statement
#Build an algorithm that will print the given statement in reverse.
#Example: Initial string = Everything is hard before it is easy
#Reversed string = easy is it before hard is Everything

#Permutations
#Write a solution that will print all permutations of a string.
#A permutation is an act of changing the arrangement of characters.
#Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

#Count Characters
#Create a program that will count vowels and consonants in a string.
#Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
