#Find all palindrome words in a list.
words = ["madam", "racecar", "hello", "level", "world", "noon", "python", "civic", "refer", "deed"]
res = []
for i in words:
  if i == i[::-1]:
    res.append(i)
print(res)
  
