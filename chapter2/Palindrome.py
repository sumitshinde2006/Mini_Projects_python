"""Find palindromes and palingrams in a dictionary file."""

import load_dictionary

# Load dictionary
word_list = load_dictionary.load('2of4brif.txt')
print(f"Loaded {len(word_list)} words from dictionary")

# -------------------------------
# 🔹 Palindromes Code
# -------------------------------
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')


# -------------------------------
# 🔹 Palingrams Code
# -------------------------------
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]

        if end > 1:
            for i in range(end):

                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))

                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))

    return pali_list


# Run palingram finder
palingrams = find_palingrams()

# Sort results
palingrams_sorted = sorted(palingrams)

# Print results
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))

for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
