# collections.Counter()

> Python | Collections | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Collections
- Difficulty: Easy
- Problem ID: 11694
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/collections-counter/problem](https://www.hackerrank.com/challenges/collections-counter/problem)

## Problem

__[collections.Counter()](https://docs.python.org/2/library/collections.html#collections.Counter)__  
 A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
 
 <sub> __Sample Code__ </sub>
 
    >>> from collections import Counter
    >>> 
    >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    >>> print Counter(myList)
    Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    >>>
    >>> print Counter(myList).items()
    [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
    >>> 
    >>> print Counter(myList).keys()
    [1, 2, 3, 4, 5]
    >>> 
    >>> print Counter(myList).values()
    [3, 4, 4, 2, 1]

---
__Task__

$Raghu$ is a shoe shop owner. His shop has $X$ number of shoes.  
He has a list containing the size of each shoe he has in his shop.  
There are $N$ number of customers who are willing to pay $x_i$ amount of money only if they get the shoe of their desired size.

Your task is to compute how much money $Raghu$ earned.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 477568455 |

---

_Synced with AlgorithmHub_