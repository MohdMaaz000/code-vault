# Text Alignment

> Python | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Strings
- Difficulty: Easy
- Problem ID: 9953
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/text-alignment/problem](https://www.hackerrank.com/challenges/text-alignment/problem)

## Problem

In Python, a string of text can be aligned *left, right* and *center*.

__.ljust(width)__

This method returns a left aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.ljust(width,'-')
    HackerRank----------  

---    
__.center(width)__

This method returns a centered string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.center(width,'-')
    -----HackerRank-----

---
__.rjust(width)__

This method returns a right aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.rjust(width,'-')
    ----------HackerRank
    
---
__Task__

You are given a partial code that is used for generating the _HackerRank Logo_ of variable _thickness_.  
Your task is to replace the blank (`______`) with *rjust, ljust* or *center*.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 476800399 |

---

_Synced with AlgorithmHub_