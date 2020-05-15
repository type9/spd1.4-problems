def count_words(sentence):
    sentence = sentence.lower()
    sentence = sentence[0].split()
    count = {}
    for word in sentence:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return sentence

'''
VARIABLE TABLE
INPUT: "I AM GABRIEL"

word:
I
AM
GABRIEL
count:
I: 1
I: 1, AM: 1
I: 1, AM: 1, GABRIEL: 1
'''

def two_sum(list, target):
    list = enumerate(list)
    for index, ele in list:
        for other_index, other_ele in list:
            if index == other_index:
                continue
            if ele + other_ele == target:
                return (ele, other_ele)

'''
VARIABLE TABLE
INPUT: [1, 2, 4], target: 6

ele:
1
1
1
2
2
2
other_ele:
1
2
4
1
2
4
sum:
2
3
5
3
4
6
'''