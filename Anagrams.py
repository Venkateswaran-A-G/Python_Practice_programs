#Check if two strings are anagrams.
str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")
str1_sorted = sorted(str1)
str2_sorted = sorted(str2)
if str1_sorted==str2_sorted:
  print("Anagram")
else:
  print("Not an Anagram")
