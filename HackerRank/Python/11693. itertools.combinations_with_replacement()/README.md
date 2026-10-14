# itertools.combinations_with_replacement()

> Python | Itertools | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Itertools
- Difficulty: Easy
- Problem ID: 11693
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem](https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem)

## Problem

__[itertools.combinations_with_replacement(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations_with_replacement)__  
This tool returns $r$ length subsequences of elements from the input iterable allowing individual elements to be _repeated more than once_.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

<sub> __Sample Code__ </sub>

    >>> from itertools import combinations_with_replacement
    >>> 
    >>> print list(combinations_with_replacement('12345',2))
    [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
    >>> 
    >>> A = [1,1,3,3,3]
    >>> print list(combinations(A,2))
    [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
    
---
__Task__

You are given a string $S$.  
Your task is to print all possible size $k$ replacement combinations of the string in lexicographic sorted order.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | pypy3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 485245751 |

---

_Synced with AlgorithmHub_