# Set .intersection() Operation

> Python | Sets | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Sets
- Difficulty: Easy
- Problem ID: 9419
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/py-set-intersection-operation/problem](https://www.hackerrank.com/challenges/py-set-intersection-operation/problem)

## Problem

<img src="https://s3.amazonaws.com/hr-challenge-images/9419/1437830945-a56a63892c-AB.png" title="A&B.png" />
__.intersection()__<br>  

The *.intersection()* operator returns the intersection of a set and the set of elements in an iterable.<br>
Sometimes, the *&* operator is used in place of the *.intersection()* operator, but it only operates on the set of elements in _set_.<br>
The set is immutable to the *.intersection()* operation (or *&* operation).

    >>> s = set("Hacker")
    >>> print s.intersection("Rank")
    set(['a', 'k'])

    >>> print s.intersection(set(['R', 'a', 'n', 'k']))
    set(['a', 'k'])

    >>> print s.intersection(['R', 'a', 'n', 'k'])
    set(['a', 'k'])

    >>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
    set([])

    >>> print s.intersection({"Rank":1})
    set([])

    >>> s & set("Rank")
    set(['a', 'k'])

---
__Task__<br>  

The students of District College have subscriptions to *English* and *French* newspapers. Some students have subscribed only to *English*, some have subscribed only to *French*, and some have subscribed to both newspapers.  


You are given two sets of student roll numbers. One set has subscribed to the *English* newspaper, one set has subscribed to the *French* newspaper. Your task is to find the total number of students who have subscribed to _both_ newspapers.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 478628206 |

---

_Synced with AlgorithmHub_