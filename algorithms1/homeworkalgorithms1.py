#HW 1
import math
#n = int(input('Input value n: '))

#result = 0
#if n != 0:
 #   for i in range(1, n + 1):
  #      result += i

#print(result)

# 2....Find max number from 3 values,
# entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.

import math
#a = int(input('value a: '))
#b = int(input('value b: '))
#c = int(input('value c: '))

#if (a > b) and (a > c):
 #   maxnum = a
#elif (b > a) and (b > c):
 #   maxnum = b
#else:
 #   maxnum = c

#print("The largest number is", maxnum)

# 3.... Count odd and even numbers.
# Count odd and even digits of the whole number.
#Example: entered number is 34560,
# then 3 digits will be even (4, 6, and 0)
# and 2 odd digits (3 and 5)

numb = 13579
d = [int(d) for d in str(numb)]

odd_count = 0
even_count = 0

for number in d:
    if (numb % 2) == 0:
        even_count += 1
        print("{0} is Even number".format(d))
    else:
        odd_count += 1
        print("{0} is Odd number".format(d))

print(f'odd count: {odd_count} and even count: {even_count}')

