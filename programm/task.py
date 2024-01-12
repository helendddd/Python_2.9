#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import functools


def factorial_iterative(n):
    """
    Итеративная версия функции factorial.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Рекурсивная версия функции factorial.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def fib_iterative(n):
    """
    Итеративная версия функции Fibonacci.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n):
    """
    Рекурсивная версия функции Fibonacci.
    """
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


@functools.lru_cache(maxsize=None)
def fib_recursive_cached(n):
    """
    Рекурсивная версия функции Fibonacci с использованием декоратора lru_cache.
    """
    if n <= 1:
        return n
    else:
        return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)


@functools.lru_cache(maxsize=None)
def factorial_recursive_cached(n):
    """
    Рекурсивная версия функции factorial с использованием декоратора lru_cache.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def main():
    """Оценка скорости работы итеративной версии функции factorial"""
    iterative_factorial_time = timeit.timeit(
        "factorial_iterative(10)",
        globals=globals(),
        number=100000
    )
    print(
        "Итеративная версия функции factorial:",
        iterative_factorial_time
    )

    """Оценка скорости работы рекурсивной версии функции factorial"""
    recursive_factorial_time = timeit.timeit(
        "factorial_recursive(10)",
        globals=globals(),
        number=1000
    )
    print(
        "Рекурсивная версия функции factorial:",
        recursive_factorial_time
    )

    """Оценка скорости работы итеративной версии функции fib"""
    recursive_fib_time = timeit.timeit(
        "fib_iterative(10)",
        globals=globals(),
        number=1000
    )
    print(
        "Итеративная версия функции fib:",
        recursive_fib_time
    )

    """Оценка скорости работы рекурсивной версии функции fib"""
    recursive_fib_time = timeit.timeit(
        "fib_recursive(10)",
        globals=globals(),
        number=1000
    )
    print(
        "Рекурсивная версия функции fib:",
        recursive_fib_time
    )

    """
    Оценка скорости работы рекурсивной версии функции fib
    с использованием декоратора lru_cache
    """
    cached_fib_time = timeit.timeit(
        "fib_recursive_cached(10)",
        globals=globals(),
        number=1000
    )
    print(
        "Рекурсивная версия функции fib с lru_cache:",
        cached_fib_time
    )

    """
    Оценка скорости работы рекурсивной версии функции fib
    с использованием декоратора lru_cache
    """
    cached_fib_time = timeit.timeit(
        "factorial_recursive_cached(10)",
        globals=globals(),
        number=1000
    )
    print(
        "Рекурсивная версия функции factorial с lru_cache:",
        cached_fib_time
    )


if __name__ == "__main__":
    main()
