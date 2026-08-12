# Day 26: Nested Logic

> Tutorials | 30 Days of Code | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Tutorials
- Track: 30 Days of Code
- Difficulty: Easy
- Problem ID: 17179
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/30-nested-logic/problem](https://www.hackerrank.com/challenges/30-nested-logic/problem)

## Problem

**Objective**	
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the [Tutorial](/challenges/30-nested-logic/tutorial) tab for a video on testing.	

**Task**	
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:	

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: $fine = 0)$.
2. If the book is returned after the expected return *day* but still within the same calendar month and year as the expected return date, $fine = 15 \text{ Hackos } \times \text{ (the number of days late)}$.	
3. If the book is returned after the expected return *month* but still within the same calendar year as the expected return date, the $fine = 500 \text{ Hackos } \times \text{ (the number of months late)}$.   
4. If the book is returned after the calendar *year* in which it was expected, there is a fixed fine of $10000 \text{ Hackos}$.

**Example**  
$d1, m1, y1 = 12 31 2014$ returned date  
$d2, m2, y2 = 1 1 2015$ due date  

The book is returned on time, so no fine is applied.  

$d1, m1, y1 = 1 1 2015$ returned date  
$d2, m2, y2 = 12 31 2014$ due date  

The book is returned in the following year, so the fine is a fixed 10000.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 10/10 passed |
| Submission ID | 479961315 |

---

_Synced with AlgorithmHub_