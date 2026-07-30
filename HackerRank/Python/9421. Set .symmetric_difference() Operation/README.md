# Set .symmetric_difference() Operation

> Python | Sets | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Sets
- Difficulty: Easy
- Problem ID: 9421
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem](https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem)

## Problem

<img src="https://s3.amazonaws.com/hr-challenge-images/9421/1437912471-534f33cf60-AB.png" title="A^B.png" />
__.symmetric_difference()__<br>  

The *.symmetric\_difference()* operator returns a set with all the elements that are in the set and the iterable but not both.<br>
Sometimes, a `^` operator is used in place of the *.symmetric\_difference()* tool, but it only operates on the set of elements in _set_.<br>
The set is immutable to the *.symmetric\_difference()* operation (or `^` operation).

    >>> s = set("Hacker")
    >>> print s.symmetric_difference("Rank")
    set(['c', 'e', 'H', 'n', 'R', 'r'])

    >>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
    set(['c', 'e', 'H', 'n', 'R', 'r'])

    >>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
    set(['c', 'e', 'H', 'n', 'R', 'r'])

    >>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
    set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

    >>> print s.symmetric_difference({"Rank":1})
    set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

    >>> s ^ set("Rank")
    set(['c', 'e', 'H', 'n', 'R', 'r'])

---
__Task__<br>  

Students of District College have subscriptions to *English* and *French* newspapers. Some students have subscribed to *English* only, some have subscribed to *French* only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the *English* newspaper, and one set has subscribed to the *French* newspaper. Your task is to find the total number of students who have subscribed to either the *English* or the *French* newspaper but *not both*.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 478630666 |

---

_Synced with AlgorithmHub_