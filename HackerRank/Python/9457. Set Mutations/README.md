# Set Mutations

> Python | Sets | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Sets
- Difficulty: Easy
- Problem ID: 9457
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/py-set-mutations/problem](https://www.hackerrank.com/challenges/py-set-mutations/problem)

## Problem

We have seen the applications of *union, intersection, difference* and *symmetric difference* operations, but these operations do not make any changes or mutations to the set.  

**We can use the following operations to create mutations to a set:**

__.update()__ or __`|=`__ <br>
Update the set by adding elements from an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
```

__.intersection_update()__ or __`&=`__<br>
Update the set by keeping only the elements found in it and an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
```

__.difference_update()__ or __`-=`__<br>
Update the set by removing elements found in an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
```

__.symmetric_difference_update()__ or __`^=`__<br>
Update the set by only keeping the elements found in either set, but not in both.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
```

---

__TASK__<br>
You are given a set $A$ and $N$ number of other sets. These $N$ number of sets have to perform some specific mutation operations on set $A$.

Your task is to execute those operations and print the sum of elements from set $A$.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 479022232 |

---

_Synced with AlgorithmHub_