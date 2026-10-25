# Zipped!

> Python | Built-Ins | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Built-Ins
- Difficulty: Easy
- Problem ID: 11741
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/zipped/problem](https://www.hackerrank.com/challenges/zipped/problem)

## Problem

__[zip([iterable, ...])](https://docs.python.org/2/library/functions.html#zip)__

This function returns a list of tuples. The $i$<sup>th</sup> tuple contains the $i$<sup>th</sup> element from each of the argument sequences or iterables. 

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence. 

<sub>__Sample Code__</sub>

    >>> print zip([1,2,3,4,5,6],'Hacker')
    [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
    >>> 
    >>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
    [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
    >>> 
    >>> A = [1,2,3]
    >>> B = [6,5,4]
    >>> C = [7,8,9]
    >>> X = [A] + [B] + [C]
    >>> 
    >>> print zip(*X)
    [(1, 6, 7), (2, 5, 8), (3, 4, 9)]

---

__Task__

The National University conducts an examination of $N$ students in $X$ subjects.  
Your task is to compute the *average scores* of each student.

$$ Average \ score = \frac{Sum \ of \ scores \ obtained \ in \ all \ subjects \ by \ a \ student}{Total \ number \ of \ subjects}$$

The format for the general mark sheet is:

	Student ID → ___1_____2_____3_____4_____5__               
    Subject 1   |  89    90    78    93    80
    Subject 2   |  90    91    85    88    86  
    Subject 3   |  91    92    83    89    90.5
                |______________________________
    Average        90    91    82    90    85.5

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 485970943 |

---

_Synced with AlgorithmHub_