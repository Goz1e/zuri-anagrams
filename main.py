# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    check = []
    if len(word) == len(anagram):
        word = list(word)
        anagram = list(anagram)
        for x in word:
            if x in anagram:
                check.append('a')
            else:
                check.append('b')
        if 'b' in check:
            return False
        else:
            return True
    else:
        return False



find_anagram("debitcard", "badcredit")