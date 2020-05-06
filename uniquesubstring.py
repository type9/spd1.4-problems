# Find the longest substring of unique letters in a given string of n letters.
# LAMEN
# longest combination of non-repeating letters in a row
# aabbc
# -> ab, bc (edge case, 2 results. default the first instance)
# abb
# -> ab
# APPROACH
# for char, check the char afterwards, if it is  a duplicate, if our current count > chars, then replace with current string, break, if not, recursively start again
# while doing above, everytime we recursively call we add a count and append the letter to a final string
# funct(string, index, chars)

def unique_letters(string, index, chars):
    cur_chars = []
    for cur_index, char in enumerate(string): # abb -> [(0, a), (1, b), (2, b)
        if string[cur_index  + 1] == char:
            if len(cur_chars) > len(chars):
                return cur_chars
            else:
                return chars
        else:
            cur_chars.append(char)

unique_letters("abb", 0, [])
# 