# Piling Up!

> Python | Collections | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Collections
- Difficulty: Medium
- Problem ID: 8380
- Max Score: 50
- Problem Link: [https://www.hackerrank.com/challenges/piling-up/problem](https://www.hackerrank.com/challenges/piling-up/problem)

## Problem

There is a horizontal row of $n$ cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if $cube[i]$ is on top of $cube[j]$ then $sideLength[j]\ge sideLength[i]$. 

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print `Yes` if it is possible to stack the cubes. Otherwise, print `No`.  

**Example**   
$blocks = [1, 2, 3, 8, 7]$   

Result: `No`  

After choosing the rightmost element, $7$, choose the leftmost element, $1$.  After than, the choices are $2$ and $8$.  These are both larger than the top block of size $1$.

$blocks = [1, 2, 3, 7, 8]$   

Result: `Yes`

Choose blocks from right to left in order to successfully stack the blocks.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 50.0 |
| Testcases | 5/5 passed |
| Submission ID | 485587765 |

---

_Synced with AlgorithmHub_