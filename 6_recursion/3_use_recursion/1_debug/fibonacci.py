#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0

    if n == 1:
        return 0

    return fibonacci(n - 1) + fibonacci(n - 2)
