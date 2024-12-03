#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci_memo(n: int, memo: dict = {}) -> int:
    if n < 0:
        return 0

    if n < 1:
        return 1

    if n in memo:
        return memo

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
