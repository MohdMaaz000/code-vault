# itertools.permutations()

> Python | Itertools | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Itertools
- Difficulty: Easy
- Problem ID: 11685
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/itertools-permutations/problem](https://www.hackerrank.com/challenges/itertools-permutations/problem)

## Problem

__[itertools.permutations(iterable[, r])](https://docs.python.org/2/library/itertools.html#itertools.permutations)__

This tool returns successive $r$ length permutations of elements in an iterable.  

If $r$ is not specified or is `None`, then $r$ defaults to the length of the iterable, and all possible full length permutations are generated.  

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

<sub>__Sample Code__</sub>

    >>> from itertools import permutations
    >>> print permutations(['1','2','3'])
    <itertools.permutations object at 0x02A45210>
    >>> 
    >>> print list(permutations(['1','2','3']))
    [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
    >>> 
    >>> print list(permutations(['1','2','3'],2))
    [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
    >>>
    >>> print list(permutations('abc',3))
	[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
    
__Task__  

You are given a string $S$.  
Your task is to print all possible permutations of size $k$ of the string in lexicographic sorted order.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 481663110 |

---

_Synced with AlgorithmHub_