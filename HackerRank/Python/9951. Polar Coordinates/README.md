# Polar Coordinates

> Python | Math | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Math
- Difficulty: Easy
- Problem ID: 9951
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/polar-coordinates/problem](https://www.hackerrank.com/challenges/polar-coordinates/problem)

## Problem

[__Polar coordinates__](https://en.wikipedia.org/wiki/Polar_coordinate_system) are an alternative way of representing Cartesian coordinates or [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number).

A complex number $z$ 
<img src="http://i.picresize.com/images/2015/08/21/OUzGu.png" title="Capture.PNG"/>
$$z = x + yj$$
is completely determined by its real part $x$ and imaginary part $y$.  
Here, $j$ is the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit).


A polar coordinate ($r , φ$)
<img src="https://s3.amazonaws.com/hr-challenge-images/9951/1440141121-5b051fd241-Capture.PNG" title="Capture.PNG" />

is completely determined by modulus $r$ and phase angle $φ$.<br><br>
If we convert complex number $z$ to its polar coordinate, we find:<br>
$r$: Distance from $z$ to origin, i.e., $\sqrt{x^2 + y^2}$<bR>
$φ$: Counter clockwise angle measured from the positive $x$-axis to the line segment that joins $z$ to the origin.

Python's [cmath](https://docs.python.org/2/library/cmath.html) module provides access to the mathematical functions for complex numbers.

$cmath.phase$  
This tool returns the phase of complex number $z$ (also known as the argument of $z$).
```python2
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
```  
$abs$  
This tool returns the modulus (absolute value) of complex number $z$.
```python2
>>> abs(complex(-1.0, 0.0))
1.0
```
  
__Task__  
You are given a complex $z$. Your task is to convert it to polar coordinates.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 6/6 passed |
| Submission ID | 479376593 |

---

_Synced with AlgorithmHub_