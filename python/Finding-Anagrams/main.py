# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if sorted(word) != sorted(anagram):
        return False
    return True


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
