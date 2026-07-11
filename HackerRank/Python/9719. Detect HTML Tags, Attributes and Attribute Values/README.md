# Detect HTML Tags, Attributes and Attribute Values

> Python | Regex and Parsing | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Regex and Parsing
- Difficulty: Easy
- Problem ID: 9719
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem)

## Problem

You are given an *HTML* code snippet of $N$ lines.<br> Your task is to detect and print all the *HTML* tags, attributes and attribute values.

Print the detected items in the following format:

```
Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]
```

<br>

The `->` symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. <br>
The ` > ` symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

**Note:** Do not detect any *HTML* tag, attribute or attribute value inside the *HTML* comment tags (`<!-- Comments -->`). Comments can be multiline.<bR>
All attributes have an attribute value.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 6/6 passed |
| Submission ID | 476762322 |

---

_Synced with AlgorithmHub_