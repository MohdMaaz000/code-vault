# Day 13: Abstract Classes

> Tutorials | 30 Days of Code | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Tutorials
- Track: 30 Days of Code
- Difficulty: Easy
- Problem ID: 17166
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/30-abstract-classes/problem](https://www.hackerrank.com/challenges/30-abstract-classes/problem)

## Problem

**Objective**	
Today, we will extend what we learned yesterday about [*Inheritance*](https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html) to [*Abstract Classes*](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html). Because this is a very specific object oriented concept, submissions are limited to the few languages that use this construct. Check out the [Tutorial](/challenges/30-abstract-classes/tutorial) tab for learning materials and an instructional video.

**Task**	
Given a *Book* class and a *Solution* class, write a *MyBook* class that does the following:

- Inherits from *Book*
- Has a parameterized constructor taking these $3$ parameters:
	1. string $title$
    2. string $author$
    3. int $price$
- Implements the *Book* class' abstract *display()* method so it prints these $3$ lines:
	1. $\scriptsize{\texttt{Title:}}$, a space, and then the current instance's $title$.
    2. $\scriptsize{\texttt{Author:}}$, a space, and then the current instance's $author$.
    3. $\scriptsize{\texttt{Price:}}$, a space, and then the current instance's $price$.

**Note:** Because these classes are being written in the same file, you must not use an access modifier (e.g.: $\scriptsize{\texttt{public}}$) when declaring *MyBook* or your code will not execute.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 3/3 passed |
| Submission ID | 478631189 |

---

_Synced with AlgorithmHub_