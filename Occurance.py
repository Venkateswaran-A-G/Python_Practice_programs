#Count the occurrence of each word in a sentence.
sentence = input("Enter a Sentence: ")
words = sentence.split()
wordCount = {}
for word in words:
    if word in wordCount.keys():
        continue
    else:
        wordCount[word] = sentence.count(word)
for w,c in wordCount.items():
    print(f"{w} : {c}")