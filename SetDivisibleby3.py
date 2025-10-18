#Create a set of numbers divisible by 3 from 1–50.
s = set()
for i in range(1,51):
    if i%3==0:
        s.add(i)
print(s)