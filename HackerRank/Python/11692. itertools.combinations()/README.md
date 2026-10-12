# itertools.combinations()

> Python | Itertools | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Itertools
- Difficulty: Easy
- Problem ID: 11692
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/itertools-combinations/problem](https://www.hackerrank.com/challenges/itertools-combinations/problem)

## Problem

__[itertools.combinations(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations)__  
This tool returns the $r$ length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

<sub> __Sample Code__ </sub>

    >>> from itertools import combinations
    >>> 
    >>> print list(combinations('12345',2))
    [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
    >>> 
    >>> A = [1,1,3,3,3]
    >>> print list(combinations(A,4))
    [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
    
---

__Task__

You are given a string $S$.  
Your task is to print all possible combinations, up to size $k$, of the string in lexicographic sorted order.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 485063872 |

---

_Synced with AlgorithmHub_