import string
from functools import reduce


def reduce_dict(x, y):
    x_keys = list(x.keys())
    y_key = list(y.keys())[0]
    if y_key in x_keys:
        x[y_key] += 1
        return x
    x[y_key] = 1
    return x


sample_text = ('I love Python programming. Python is the best thing in programming.'
               ' Python is a good programming language. Python is great at programming.'
               ' Love the best programming language.')

exclude = set(string.punctuation)
sample_text = ''.join(ch for ch in sample_text.lower() if ch not in exclude)

words = sample_text.split()
# print(words)

pairs = map(lambda word: {word: 1}, words)
result = reduce(reduce_dict, pairs)

for key, value in result.items():
    print(key, value)
