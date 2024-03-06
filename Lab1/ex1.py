import random
from functools import reduce


def generate_random_list_of_ints(size):
    return [random.randint(0, 100) for _ in range(size)]


def solve_iterative(list_of_sequences):
    # bucle for
    max_length = -1
    for lst in list_of_sequences:
        # size = len(lst)
        size = 0
        for _ in lst:
            size += 1
        if size > max_length:
            max_length = size
    return max_length


def solve_map_reduce(list_of_sequences):
    result = reduce(lambda x, y: max(x, y), map(lambda seq: len(seq), list_of_sequences))
    return result


def main():
    list_of_sequences = [generate_random_list_of_ints(random.randint(1, 100)) for _ in range(10)]
    solution = solve_iterative(list_of_sequences)
    print("Lungime maxima (bucle for):", solution)
    solution = solve_map_reduce(list_of_sequences)
    print("Lungime maxima (map reduce):", solution)


if __name__ == "__main__":
    main()
