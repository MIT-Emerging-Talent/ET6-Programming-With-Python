#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reverse_list(to_reverse: list) -> list:
    if to_reverse == 0:
        return []

    return reverse_list(to_reverse[1]) + [to_reverse[0]]
