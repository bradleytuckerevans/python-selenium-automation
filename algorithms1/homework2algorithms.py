#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_in_half(s):

    if len(s) > 1:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2:]
        return(s2 + s1)

    else:
        if len(s) <= 1:
         return s


test_1 = ''
test_2 = 'a'
test_3 = 'aaaAaBCCC'

print(split_in_half(test_1))
print(split_in_half(test_2))
print(split_in_half(test_3))

#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

def unique_string(st):
    if len(st) > 256:
        return False

    char_set = [False] * 128

    for i in range(0, len(st)):

      val = ord(st[i])
      if char_set[val]:
         return False
      char_set[val] = True
    return True





test_1a = ''
test_2a = 'a'
test_3a = 'aaaAaBCCC'

print(unique_string(test_1a))
print(unique_string(test_2a))
print(unique_string(test_3a))



#def compress_string(s):
 #   if len(s) == 0:
  #      return ""

   # if len(s) == 1:
    #    return s + "1"

    #compressed = ""
    #cnt = 1
    #i = 1

    #while i < len(s):
     #   if s[i] == s[i -1]:
      #      cnt += 1
       # else:
        #    compressed = compressed + s[i - 1] + str(cnt)
         #   cnt = 1
        #i += 1

    #compressed = compressed + s[i - 1] + str(cnt)

    #return compressed

#test_1 = ''
#test_2 = 'a'
#test_3 = 'aaaAaBCCC'
#print(compress_string(test_1))
#print(compress_string(test_2))
#print(compress_string(test_3))



#def reverse_string(fx):
 #   return fx[::-1]

#def reverse_string(fx):
 #   result = ''
  #  index = len(fx) -1
   # while index >= 0:
    #    result += fx[index]
     #   index -= 1

    #return result

#print(reverse_string("abcde"))







#def is_almost(s):
 #   for i in range(len(s)):
  #      s_temp = s[:i] + s[i + 1:]
   #     if s_temp == s_temp[::-1]:
    #return True

    #return False

#strin_posi = "radkar"
#strin_nega = "radario"
#print(is_almost(strin_posi))
#print(is_almost(strin_nega))








#def is_palindrome(s):
 #   return s == s[::-1]

#pos_strin = "radar"
#neg_strin = "xadar"

#print(is_palindrome(pos_strin))
#print(is_palindrome(neg_strin))




#{start:end:step]
#string = "string"

#how to reverse string
# print(string[::-1])









#def is_anagram(s1, s2):
 #   if len(s1) != len(s2):
  #      return False

 #easy   return sorted(s1) == sorted(s2)

   # count = {}
    #for letter in s1:
     #   if letter in count:
      #      count[letter] += 1
       # else:
        #    count[letter] = 1

    #for letter in s2:
     #    if letter in count:
      #       count[letter] -= 1
       #  else:
        #  count[letter] = 1


    #for k in count:
     #   if count[k] != 0:
      #      return False

    #return True


#str_1 = "abcde"
#str_2 = "abced"
#print(is_anagram(str_1, str_2))


#list_of_strings = ["This", "is", "my"]
#string = "".join(list_of_strings)

#print(list_of_strings)
#print(string)







#string = "bbbbbcaaaaa"
#string_list = string.split()
#string_list_by_i = string.split(":")

#print(string_list_by_i)

