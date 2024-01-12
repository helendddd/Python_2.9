#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_subsets(s, current_set=[]):
    """
    Рекурсивная функция, печатающая все подмножества множества.
    """
    if not s:
        print(current_set)
        return

    print_subsets(s[1:], current_set + [s[0]])
    print_subsets(s[1:], current_set)


if __name__ == "__main__":
    input_set = input("Введите элементы множества через пробел: ")
    example_set = input_set.split()

    print_subsets(example_set)
