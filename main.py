# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
def convert_to_lower(x,y):
    return x.lower(), y.lower()

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word, anagram = convert_to_lower(word,anagram)
    first_dict = {}
    sec_dict = {}
    for i in word:
        first_dict[i] = anagram.count(i)

    for a in anagram:
        sec_dict[a] = word.count(a)

    if first_dict == sec_dict:
        return True
    else:
        return False

print(find_anagram('below','elbow'))



