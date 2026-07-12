# Find a string

> Python | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Strings
- Difficulty: Easy
- Problem ID: 1373
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/find-a-string/problem](https://www.hackerrank.com/challenges/find-a-string/problem)

## Problem

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 

**NOTE:** String letters are case-sensitive.

**Input Format**  

The first line of input contains the original string. The next line contains the substring.

**Constraints**  

$1 \le len(string) \le 200$  
Each character in the string is an *ascii* character. 

**Output Format** 

Output the integer number indicating the total number of occurrences of the substring in the original string. 

**Sample Input**

	ABCDCDC
	CDC

**Sample Output**

	2

**Concept**
 
There are a couple of new concepts:  
In Python, the length of a string is found by the function `len(s)`, where $s$ is the string.  
To traverse through the length of a string, use a *for* loop:  

    for i in range(0, len(s)):
        print (s[i])

A range function is used to loop over some length: 

    range (0, 5)

Here, the range loops over $0$ to $4$. $5$ is excluded.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 10/10 passed |
| Submission ID | 476800154 |

---

_Synced with AlgorithmHub_