#Anagram check

word1 = input("Enter the first letter:")
word2 = input("Enter the second letter:")

if sorted(word1) == sorted(word2):
    print("anagram")
else:
    print("not anagram")