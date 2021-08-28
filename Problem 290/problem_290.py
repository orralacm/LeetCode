#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

pattern = "abba"
s = "dog cat cat dog"

a = 0

words = s.split()

if len(pattern) != len(words):
    print("False")
    a = 1
d1 = {}
d2 = {}
for ch, word in zip(pattern, words):
    if ch not in d1 and word not in d2:
        d1[ch] = word
        d2[word] = ch
    elif (ch not in d1 and word in d2):
        print("False")
        a = 1
    elif (ch in d1 and d1[ch] != word):
        print("False")
        a = 1
if (a != 1) :
    print("True")