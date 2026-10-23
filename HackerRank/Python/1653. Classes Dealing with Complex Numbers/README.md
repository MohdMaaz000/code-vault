# Classes: Dealing with Complex Numbers

> Python | Classes | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Classes
- Difficulty: Medium
- Problem ID: 1653
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem)

## Problem

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations. 

The real and imaginary precision part should be correct up to two decimal places.

**Input Format**

One line of input: The real and imaginary part of a number separated by a space.

**Output Format**

For two complex numbers $C$ and $D$, the output should be in the following sequence on separate lines:<br>

- $C + D$
- $C - D$
- $C * D$
- $C / D$
- $mod(C)$
- $mod(D)$
<br>

For complex numbers with non-zero real$(A)$ and complex part$(B)$, the output should be in the following format: <br>
$A+Bi$<br>
Replace the plus symbol $(+)$ with a minus symbol $(-)$ when $B < 0$.

For complex numbers with a zero complex part i.e. real numbers, the output should be: <br>
$A+0.00i$  

For complex numbers where the real part is zero and the complex part$(B)$ is non-zero, the output should be:<br>
$0.00+Bi$

**Sample Input**

	2 1
    5 6
    
**Sample Output**

    7.00+7.00i
    -3.00-5.00i
    4.00+17.00i
    0.26-0.11i
    2.24+0.00i
    7.81+0.00i

**Concept**

Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer [here](http://www.diveintopython3.net/iterators.html#defining-classes).
<br><br>
Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality. <br>
<pre>__add__-> Can be overloaded for + operation</pre><br>
<pre>__sub__ -> Can be overloaded for - operation</pre><br>
<pre>__mul__ -> Can be overloaded for * operation</pre>
<br><br>
For more information on operator overloading in Python, refer [here](http://docs.python.org/3.2/reference/datamodel.html).

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 10/10 passed |
| Submission ID | 485845576 |

---

_Synced with AlgorithmHub_