# Set .discard(), .remove() & .pop()

> Python | Sets | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Sets
- Difficulty: Easy
- Problem ID: 9415
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem)

## Problem

__.remove(x)__<bR>  

This operation removes element $x$ from the set.  
If element $x$ does not exist, it raises a __`KeyError`__.<br>
The *.remove(x)* operation returns __`None`__.

**Example**
<pre>
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
</pre>
---
__.discard(x)__<br>  

This operation also removes element $x$ from the set.  
If element $x$ does not exist, it __does not__ raise a `KeyError`.<br>
The *.discard(x)* operation returns __`None`__.

**Example**
<pre>
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
</pre>
---
__.pop()__<br>  

This operation removes and return an arbitrary element from the set.  
If there are no elements to remove, it raises a __`KeyError`__.

**Example**
<pre>
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
</pre>  
---  
  
__Task__<br>  

You have a non-empty set $s$, and you have to execute $N$ commands given in $N$ lines.

The commands will be *pop, remove* and *discard*.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 477917460 |

---

_Synced with AlgorithmHub_