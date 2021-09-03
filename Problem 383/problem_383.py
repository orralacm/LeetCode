#Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.

ransomNote = "aa"
magazine = "aab"

a = 0

for i in set(ransomNote) :
    print(i)
    if ransomNote.count(i) > magazine.count(i) :
        print("False")
        a = 1

if a == 0 :
    print("True")
