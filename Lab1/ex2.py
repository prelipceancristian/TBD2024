from functools import reduce
import time

from ex1 import generate_random_list_of_ints


def solve_iterative(lst):
    s = 0
    for elem in lst:
        s += elem * elem
    return s


def solve_list_comprehensions(lst):
    return sum([x * x for x in lst])


def solve_map_reduce(lst):
    return reduce(lambda x, y: x + y, map(lambda e: e * e, lst))


def main():
    methods = {
        'solve_iterative': solve_iterative,
        'solve_list_comprehensions': solve_list_comprehensions,
        'solve_map_reduce': solve_map_reduce
    }
    for size in [10, 1000, 10000, 100000]:
        print("List size:", size)
        lst = generate_random_list_of_ints(size)
        for method_type in methods:
            start_time = time.perf_counter()
            _ = methods[method_type](lst)
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000
            print(f"{method_type:<25}:{elapsed_time} ms")


if __name__ == '__main__':
    main()
