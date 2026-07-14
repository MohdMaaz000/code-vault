# itertools.product()

> Python | Itertools | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Itertools
- Difficulty: Easy
- Problem ID: 11684
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/itertools-product/problem](https://www.hackerrank.com/challenges/itertools-product/problem)

## Problem

__[itertools.product()](https://docs.python.org/2/library/itertools.html#itertools.product)__

This tool computes the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of input iterables.  
It is equivalent to nested *for-loops*.  
For example, `product(A, B)` returns the same as `((x,y) for x in A for y in B)`.  
  
__<sub>Sample Code</sub>__

	>>> from itertools import product
    >>>
    >>> print list(product([1,2,3],repeat = 2))
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    >>>
    >>> print list(product([1,2,3],[3,4]))
    [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
    >>>
    >>> A = [[1,2,3],[3,4,5]]
    >>> print list(product(*A))
    [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
    >>>
    >>> B = [[1,2,3],[3,4,5],[7,8]]
    >>> print list(product(*B))
    [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]

---

__Task__


You are given a two lists $A$ and $B$. Your task is to compute their cartesian product [$A$X$B$](https://en.wikipedia.org/wiki/Cartesian_product).

__<sub>Example</sub>__  

	A = [1, 2]
    B = [3, 4]
         
    AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

**Note**: $A$ and $B$ are sorted lists, and the cartesian product's tuples should be output in sorted order.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 477002879 |

---

_Synced with AlgorithmHub_