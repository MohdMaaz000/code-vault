# HTML Parser - Part 2

> Python | Regex and Parsing | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Python
- Track: Regex and Parsing
- Difficulty: Easy
- Problem ID: 11665
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/html-parser-part-2/problem](https://www.hackerrank.com/challenges/html-parser-part-2/problem)

## Problem

<sup>`*`This section assumes that you understand the basics discussed in __HTML Parser - Part 1__</sup>


[*.handle\_comment(data)*](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_comment)  
This method is called when a comment is encountered (e.g. &lt;!--comment-->).  
The *data* argument is the content inside the comment tag:

	from html.parser import HTMLParserr

	class MyHTMLParser(HTMLParser):
    	def handle_comment(self, data):
    	  	  print("Comment  :", data)
<br>

[*.handle\_data(data)*](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_data)  
This method is called to process arbitrary data (e.g. text nodes and the content of &lt;script>...&lt;/script> and &lt;style>...&lt;/style>).  
The *data* argument is the text content of HTML.

	from html.parser import HTMLParserr

	class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
        	print("Data     :", data)
            
---
__Task__

You are given an *HTML* code snippet of $N$ lines.  
Your task is to print the *single-line comments, multi-line comments* and the *data*. 

Print the result in the following format:

	>>> Single-line Comment  
    Comment
    >>> Data                 
    My Data
    >>> Multi-line Comment  
    Comment_multiline[0]
    Comment_multiline[1]
    >>> Data
    My Data
    >>> Single-line Comment:  
    
    
**Note**: Do not print *data* if `data == '\n'`.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 6/6 passed |
| Submission ID | 476762022 |

---

_Synced with AlgorithmHub_