# Grouping anagrams
# This programme writes a function that takes in a list of words and groups them into anagrams. The output is a dictionary of grouped anagrams.

def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return anagrams

group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])