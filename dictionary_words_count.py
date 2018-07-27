def count_words(string):
    result = {}
    for word in string.lower().strip().split():
        if word not in result.keys():
            result[word] = 1
        else:
            result[word] = result[word] + 1
    return result




example = "I am tall when I am young and I am short when I am old"
print(count_words(example))