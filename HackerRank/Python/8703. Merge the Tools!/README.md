# Merge the Tools!

> Python | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Strings
- Difficulty: Medium
- Problem ID: 8703
- Max Score: 40
- Problem Link: [https://www.hackerrank.com/challenges/merge-the-tools/problem](https://www.hackerrank.com/challenges/merge-the-tools/problem)

## Problem

Consider the following:

- A string, $s$, of length $n$ where $s = c_0 c_1 \ldots c_{n - 1}$.
- An integer, $k$, where $k$ is a factor of $n$.

We can split $s$ into $\frac{n}{k}$ substrings where each subtring, $t_i$, consists of a contiguous block of $k$ characters in $s$. Then, use each $t_i$ to create string $u_i$ such that:

- The characters in $u_i$ are a subsequence of the characters in $t_i$. 
- Any repeat occurrence of a character is removed from the string such that each character in $u_i$ occurs exactly once. In other words, if the character at some index $j$ in $t_i$ occurs at a previous index $\lt j$ in $t_i$, then do not include the character in string $u_i$.

Given $s$ and $k$, print $\frac{n}{k}$ lines where each line $i$ denotes string $u_i$.  

**Example**  
$s = \text{'AAABCADDE'}$  
$k = 3$  

There are three substrings of length $3$ to consider: 'AAA', 'BCA' and 'DDE'.  The first substring is all 'A' characters, so $u_1 = \text{'A'}$.  The second substring has all distinct characters, so $u_2 = \text{'BCA'}$.  The third substring has $2$ different characters, so $u_3 = \text{'DE'}$.  Note that a subsequence maintains the original order of characters encountered.  The order of characters in each subsequence shown is important.  

**Function Description**  

Complete the *merge_the_tools* function in the editor below.  

*merge_the_tools* has the following parameters:  

- *string s:* the string to analyze  
- *int k:* the size of substrings to analyze  

**Prints**  

Print each subsequence on a new line.  There will be $\frac{n}{k}$ of them.  No return value is expected.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 40.0 |
| Testcases | 17/17 passed |
| Submission ID | 476800818 |

---

_Synced with AlgorithmHub_