# Exceptions

> Python | Errors and Exceptions | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Errors and Exceptions
- Difficulty: Easy
- Problem ID: 11765
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/exceptions/problem](https://www.hackerrank.com/challenges/exceptions/problem)

## Problem

###<sub>[Exceptions](https://docs.python.org/2/tutorial/errors.html#exceptions)</sub>   
Errors detected during execution are called *exceptions*.

**Examples**:

[__*ZeroDivisionError*__](https://docs.python.org/2/library/exceptions.html#exceptions.ZeroDivisionError)  
This error is raised when the second argument of a division or modulo operation is zero.

```python
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
```
    
[__*ValueError*__](https://docs.python.org/2/library/exceptions.html#exceptions.ValueError)   
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value. 

```python
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
```
    
<sub> To learn more about different built-in exceptions __[click here](https://docs.python.org/2/library/exceptions.html#module-exceptions)__.</sub>    
###<sub>[Handling Exceptions](https://docs.python.org/2/tutorial/errors.html#handling-exceptions)</sub>    

The statements *try* and *except* can be used to handle selected exceptions. A *try* statement may have more than one except clause to specify handlers for different exceptions.

```python
#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
```

**Output**

Error Code: integer division or modulo by zero
    
---
__Task__

You are given two values $a$ and $b$.  
Perform integer division and print $a/b$.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 3/3 passed |
| Submission ID | 484861553 |

---

_Synced with AlgorithmHub_