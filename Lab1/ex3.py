import math
import statistics
from functools import reduce

from ex1 import generate_random_list_of_ints


def get_avg(lst):
    return sum(lst) / len(lst)


def main():
    lst = generate_random_list_of_ints(1000)
    avg = get_avg(lst)
    std_dev = math.sqrt(reduce(lambda x, y: x + y, map(lambda x: (x - avg) ** 2, lst)) / len(lst))
    print("Standard deviation:", std_dev)
    print("Standard deviation (using stdev):", statistics.stdev(lst))


if __name__ == "__main__":
    main()
