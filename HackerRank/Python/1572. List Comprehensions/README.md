# List Comprehensions

> Python | Basic Data Types | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Basic Data Types
- Difficulty: Easy
- Problem ID: 1572
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/list-comprehensions/problem](https://www.hackerrank.com/challenges/list-comprehensions/problem)

## Problem

Let's learn about list comprehensions! You are given three integers $x, y$ and $z$ representing the dimensions of a cuboid along with an integer $n$. Print a list of all possible coordinates given by $(i, j, k)$ on a 3D grid where the sum of $i + j + k$ is not equal to $n$. Here, $0 \le i \le x; 0 \le j \le y; 0 \le k \le z$.  Please use list comprehensions rather than multiple loops, as a learning exercise.  

 **Example**  
 $x = 1$  
 $y = 1$  
 $z = 2$  
 $n = 3$
 
 All permutations of $[i, j, k]$ are:  
$[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]$. 
 
 Print an array of the elements that do not sum to $n = 3$.  
 
$[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]$

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 10/10 passed |
| Submission ID | 476761504 |

---

_Synced with AlgorithmHub_