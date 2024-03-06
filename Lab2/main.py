import string
from functools import reduce


def get_word_list(sample_text):
    exclude = set(string.punctuation)
    sample_text = ''.join(ch for ch in sample_text.lower() if ch not in exclude)
    return sample_text.split()


def group_by_key(pairs):
    groups = {}
    for pair in pairs:
        key = list(pair.keys())[0]
        value = list(pair.values())[0]
        if key in groups.keys():
            groups[key].append(value)
        else:
            groups[key] = [value]
    return groups

def reduce

def main():
    with open("sample.txt", "r") as f:
        sample_text = f.read()

    # pre mapping
    words = get_word_list(sample_text)
    # mapping
    pairs = list(map(lambda word: {word: 1}, words))
    # shuffling
    groups = group_by_key(pairs)
    # reduce
    results = map()

if __name__ == '__main__':
    main()
