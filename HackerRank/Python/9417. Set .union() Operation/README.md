# Set .union() Operation

> Python | Sets | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Sets
- Difficulty: Easy
- Problem ID: 9417
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/py-set-union/problem](https://www.hackerrank.com/challenges/py-set-union/problem)

## Problem

<img src="https://s3.amazonaws.com/hr-challenge-images/9417/1437829708-707212e33e-AuB.png" title="AuB.png" />
__.union()__

The *.union()* operator returns the union of a set and the set of elements in an iterable. <br>
Sometimes, the *|* operator is used in place of *.union()* operator, but it operates only on the set of elements in _set_.<br> 
Set is immutable to the *.union()* operation (or *|* operation).

__Example__

    >>> s = set("Hacker")
    >>> print s.union("Rank")
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print s.union(set(['R', 'a', 'n', 'k']))
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print s.union(['R', 'a', 'n', 'k'])
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print s.union(enumerate(['R', 'a', 'n', 'k']))
    set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

    >>> print s.union({"Rank":1})
    set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

    >>> s | set("Rank")
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

---
__Task__<br>  

The students of District College have subscriptions to *English* and *French* newspapers. Some students have subscribed only to *English*, some have subscribed to only *French* and some have subscribed to both newspapers. 

You are given two sets of student roll numbers. One set has subscribed to the *English* newspaper, and the other set is subscribed to the *French* newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to _at least one_ newspaper.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 478333276 |

---

_Synced with AlgorithmHub_