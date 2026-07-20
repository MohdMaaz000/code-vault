# Collections.namedtuple()

> Python | Collections | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Collections
- Difficulty: Easy
- Problem ID: 11955
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/py-collections-namedtuple/problem](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem)

## Problem

###<sub>__[collections.namedtuple()](https://docs.python.org/2/library/collections.html#collections.namedtuple)__</sub>  

Basically, _namedtuples_ are easy to create, lightweight object types.  
They turn tuples into convenient containers for simple tasks.  
With *namedtuples*, you don’t have to use integer indices for accessing members of a tuple.


**Example**

<sub>__Code 01__</sub>

	>>> from collections import namedtuple
    >>> Point = namedtuple('Point','x,y')
    >>> pt1 = Point(1,2)
    >>> pt2 = Point(3,4)
    >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
    >>> print dot_product
    11
    
<sub>__Code 02__</sub>

    >>> from collections import namedtuple
    >>> Car = namedtuple('Car','Price Mileage Colour Class')
    >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
    >>> print xyz
    Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
    >>> print xyz.Class
    Y

---
__Task__

Dr. John Wesley has a spreadsheet containing a list of student's $IDs$, $marks$, $class$ and $name$.  

Your task is to help Dr. Wesley calculate the average marks of the students.

<sub>$$Average = \frac{Sum \ of \ all \ marks }{ Total \ Students }$$</sub>

__<sub>Note:  
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.  
2. Column names are `ID`, `MARKS`, `CLASS` and `NAME`. (The spelling and case type of these names won't change.)</sub>__

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 6/6 passed |
| Submission ID | 477569410 |

---

_Synced with AlgorithmHub_