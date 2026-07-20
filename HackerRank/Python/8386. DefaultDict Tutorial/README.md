# DefaultDict Tutorial

> Python | Collections | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Collections
- Difficulty: Easy
- Problem ID: 8386
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/defaultdict-tutorial/problem](https://www.hackerrank.com/challenges/defaultdict-tutorial/problem)

## Problem

The *defaultdict* tool is a container in the collections class of Python. It's similar to the usual dictionary (*dict*) container, but the only difference is that a defaultdict will have a _default_ value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.    
**For example:**

    from collections import defaultdict
    d = defaultdict(list)
    d['python'].append("awesome")
    d['something-else'].append("not relevant")
    d['python'].append("language")
    for i in d.items():
    	print i
        
This prints:

	('python', ['awesome', 'language'])
	('something-else', ['not relevant'])
    
In this challenge, you will be given $2$ integers, $n$ and $m$. There are $n$ words, which might repeat, in word group $A$. There are $m$ words belonging to word group $B$. For each  $m$ words, check whether the word has appeared in group $A$ or not. Print the indices of each occurrence of $m$ in group $A$. If it does not appear, print $-1$.

**Example**  

Group A contains 'a', 'b', 'a'
Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions $1$ and $3$ in group A.
The second word, 'c', does not appear in group A, so print $-1$.

Expected output:

    1 3
    -1

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 10/10 passed |
| Submission ID | 477568710 |

---

_Synced with AlgorithmHub_