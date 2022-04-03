#question 1 Even First
#Your input is an array of integers,
# and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input array).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(arr):
    even_num = 0
    odd_num = len(arr) - 1
    while even_num < odd_num:
        if arr[even_num] % 2 == 0:
            even_num += 1
        else:
            arr[even_num], arr[odd_num] = arr[odd_num], arr[even_num]
            odd_num -= 1

    return arr

"""""
def even_first(arr):
    even_array = 0
    odd_array = len(arr) -1
    while i < len(arr):
        if arr[i] % 2 == 0:
            even_array.append(arr[i])
        if arr[i] % 2 != 0:
            odd_array.append(arr[i])
        i = i + 1
    return (even_array + odd_array)

"""""



list_even = [7, 3, 5, 6, 4, 10, 3, 2]

print(even_first(list_even))



#question 2Increment a Number
#Write a program that takes as input an array of digits
# encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def add_one(arr1):
    e = 0

    for e in range(len(arr1)):
         if arr1[e] == 9:
            arr1[e] = 0

         elif arr1[e] < 9:
            arr1[e] = arr1[e] + 1

    return arr1


arr1_list = [1, 2, 9]
print(add_one(arr1_list))





#1 array. calculate sum and multiplication of elements.
#print the list, calculated sum and multiplication of elements

#def sum_multi(arr):
 #   sum_results = 0
  #  sums_result = 1

   # for element in arr:
    #    sum_results += element
     #   sums_result *= element

    #return(sum_results, sums_result)

#test_list = [1, 7, 3]

#print(sum_multi(test_list))

#2 list of random numbers. Find and print max element and index

#def find_max(arr):
 #   max_num = arr[0]
  #  max_index = 0

   # for i in range(1, len(arr)):
    #    if arr[i] > max_num:
     #       max_num = arr[i]
      #      max_index = i

    #return(max_index, max_num)

#test_list = [1, 45, 33, 76, 9, 10]

#print(find_max(test_list))

#3 find sum between min and max elements.
# min and max not included and all numbers are unique.

#def sum_between(arr):
 #   if len(arr) <= 2:
  #      return -1

   # min_value = max_value = arr[0]
    #min_index = max_index = 0
    #i = 1

    #while i < len(arr):
     #   if arr[i] > max_value:
      #      max_index = i
       #     max_value = arr[i]
        #if arr[i] < min_value:
         #   min_index = i
          #  min_value = arr[i]
        #i += i

    #return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])

#test_list1 = [1, 2, 7, 3]
#print(sum_between(test_list1))

#test_list2 = [8, 3, 2, 1]
#print(sum_between(test_list2))

#4 input of sorted arr and updates it so duplicates
# are removed and remaining elements shift left to fill
#emptied spaces. Fill remaining with zeros
#return number of valid elements. No sets can be used

#def delete_dups(arr):
 #   write_index = 1

  #  for i in range(1, len(arr)):
   #     if arr[write_index - 1] != arr[i]:
    #        arr[write_index] = arr[i]
     #       write_index += 1

    #for i in range(write_index, len(arr)):
     #   arr[i] = 0

    #return write_index


#test_list = [1, 3, 4, 4, 5, 8, 9, 9, 11]
#print(test_list)
#print(delete_dups(test_list))
#print(test_list)


#5 integer argument and retursn all the
#primes between 1 and that integer

#def get_primes(n):
 #   primes = []

  #  for i in range(2, n + 1):
   ##        if p == i:
     #           primes.append(i)
      #          break
       #     if i % p == 0:
        #        break

    #return primes

#test_n = 18
#print(get_primes(test_n))

#6 array where prics of stock equals the day.
#maximize profit by choosing single day to buy
#and different day in future to sell.
#return max profit if no profit return 0

#def buy_sell(prices):
 #   max_sum = 0
  #  current_sum = 0

   # for i in range(len(prices) - 1):
    #    current_sum = current_sum + prices[i + 1] - prices[i]
     #   if current_sum > max_sum:
      #      max_sum = current_sum
       # if current_sum < 0:
        #    current_sum = 0

    #return max_sum

#test_prices = [7, 1, 5, 3, 6, 4]

#print(buy_sell(test_prices))

#7 array of prices and stock on given day.
#max profit. Multiple transactions

#def buy_sellmax(prices):
 #   maximum = 0
  #  for i in range(len(prices) - 1):
   #     if prices[i + 1] > prices[i]:
    #        maximum = maximum + prices[i + 1] - prices[i]

    #return maximum

#print(buy_sellmax(test_prices))