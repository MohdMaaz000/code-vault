# Detect Floating Point Number

> Python | Regex and Parsing | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Regex and Parsing
- Difficulty: Easy
- Problem ID: 12177
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/introduction-to-regex/problem](https://www.hackerrank.com/challenges/introduction-to-regex/problem)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/introduction-to-regex/tutorial) tab to know how to to solve.</sub>  

You are given a string $N$.  
Your task is to verify that $N$ is a floating point number.  

In this task, a valid float number must satisfy *all* of the following requirements:  

$\gt$ Number can start with **`+`**, **`-`** or **`.`** symbol.  
$ \ \ \ \ $For example:  
$ \ \ \ \ ✔ \ $+4.50   
$ \ \ \ \ ✔ \ $-1.0   
$ \ \ \ \ ✔ \ $.5   
$ \ \ \ \ ✔ \ $-.7   
$ \ \ \ \ ✔ \ $+.4   
$ \ \ \ \ ✖ $ __`-+4.5`__    

$\gt$ Number must contain *at least* $1$ decimal value.  
$ \ \ \ \ $For example:  
$ \ \ \ \ ✖ $ __`12.`__  
$ \ \ \ \ ✔ \ $12.0     

$\gt$ Number must have exactly one __`.`__ symbol.  
$\gt$ Number must not give any exceptions when converted using $float(N)$.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 18/18 passed |
| Submission ID | 476762390 |

---

_Synced with AlgorithmHub_