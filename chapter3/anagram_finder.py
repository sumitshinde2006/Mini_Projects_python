"""Find anagrams in a dictionary file."""

import load_dictionary

# Load dictionary
word_list = load_dictionary.load('2of4brif.txt')


def find_anagrams(word, word_list):
    """Find all anagrams of a given word from the word list."""
    sorted_word = sorted(word.lower())
    anagrams = []
    
    for dict_word in word_list:
        if len(dict_word) == len(word) and sorted(dict_word) == sorted_word:
            if dict_word.lower() != word.lower():
                anagrams.append(dict_word)
    
    return anagrams


def find_all_anagrams():
    """Find all anagram groups in the dictionary."""
    anagram_groups = {}
    
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word)
    
    # Filter groups with more than one word (actual anagrams)
    result = {k: v for k, v in anagram_groups.items() if len(v) > 1}
    return result


# Run anagram finder
anagram_groups = find_all_anagrams()

# Print results
print("\nAnagram Groups Found:\n")
for sorted_word, words in sorted(anagram_groups.items()):
    print(f"{', '.join(words)}")

print(f"\nTotal anagram groups: {len(anagram_groups)}")
