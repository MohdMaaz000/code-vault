# Set .difference() Operation

> Python | Sets | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Sets
- Difficulty: Easy
- Problem ID: 9420
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/py-set-difference-operation/problem](https://www.hackerrank.com/challenges/py-set-difference-operation/problem)

## Problem

<img src="https://s3.amazonaws.com/hr-challenge-images/9420/1437904659-11e4bef847-A-B.png" title="A-B.png" />
__.difference()__<br>  

The tool *.difference()* returns a set with all the elements from the set that are not in an iterable.<br>
Sometimes the `-` operator is used in place of the *.difference()* tool, but it only operates on the set of elements in _set_.<br>
Set is immutable to the *.difference()* operation (or the `-` operation).

    >>> s = set("Hacker")
    >>> print s.difference("Rank")
    set(['c', 'r', 'e', 'H'])

    >>> print s.difference(set(['R', 'a', 'n', 'k']))
    set(['c', 'r', 'e', 'H'])

    >>> print s.difference(['R', 'a', 'n', 'k'])
    set(['c', 'r', 'e', 'H'])

    >>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
    set(['a', 'c', 'r', 'e', 'H', 'k'])

    >>> print s.difference({"Rank":1})
    set(['a', 'c', 'e', 'H', 'k', 'r'])

    >>> s - set("Rank")
    set(['H', 'c', 'r', 'e'])

---
__Task__<br>  

Students of District College have a subscription to *English* and *French* newspapers. Some students have subscribed to only the *English* newspaper, some have subscribed to only the *French* newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the *English* newspaper, and one set has subscribed to the *French* newspaper. Your task is to find the total number of students who have subscribed to *only English* newspapers.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 478629276 |

---

_Synced with AlgorithmHub_