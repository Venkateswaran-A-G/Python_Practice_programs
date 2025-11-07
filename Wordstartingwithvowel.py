#Given a sentence, print all words that start with a vowel.
sentence = input("Enter a sentence: ")
split_sentence= sentence.split(" ")
vowels = []
for i in split_sentence:
    if i[0].upper() in ['A','E','I','O','U']:
        vowels.append(i)
print("The words starting with a vowels are: ")
for i in vowels:
    print(i)