# Day 20: Sorting

> Tutorials | 30 Days of Code | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Tutorials
- Track: 30 Days of Code
- Difficulty: Easy
- Problem ID: 19055
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/30-sorting/problem](https://www.hackerrank.com/challenges/30-sorting/problem)

## Problem

**Objective** 	
Today, we're discussing a simple sorting algorithm called *Bubble Sort*. Check out the [Tutorial](/challenges/30-sorting/topics) tab for learning materials and an instructional video!	

----

Consider the following version of Bubble Sort:

```java
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
```

**Task**	
Given an array, $a$, of size $n$ distinct elements, sort the array in *ascending* order using the *Bubble Sort* algorithm above. Once sorted, print the following $3$ lines:

1. `Array is sorted in numSwaps swaps.`		
    where $numSwaps$ is the number of swaps that took place.		
2. `First Element: firstElement`		
    where $firstElement$ is the *first* element in the sorted array.
3. `Last Element: lastElement`		
	where $lastElement$ is the *last* element in the sorted array.
    
**Hint:** To complete this challenge, you will need to add a variable that keeps a running tally of *all* swaps that occur during execution. 

**Example**  

$a = [4, 3, 1, 2]$  
```
original a: 4 3 1 2
round 1  a: 3 1 2 4 swaps this round: 3
round 2  a: 1 2 3 4 swaps this round: 2
round 3  a: 1 2 3 4 swaps this round: 0
```

In the first round, the $4$ is swapped at each of the $3$ comparisons, ending in the last position.  In the second round, the $3$ is swapped at $2$ of the $3$ comparisons.  Finally, in the third round, no swaps are made so the iterations stop.  The output is the following:  
```
Array is sorted in 5 swaps.
First Element: 1
Last Element: 4
```

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 3/3 passed |
| Submission ID | 479185411 |

---

_Synced with AlgorithmHub_