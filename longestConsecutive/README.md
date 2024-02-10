# Longest Consecutive
Problem Source: [CoderByte Link](https://coderbyte.com/information/Longest%20Consecutive)

# Success Criteria
When given a list of numbers, for example, `4 3 8 1 2 6 100 9`, break the list into consecutive number lists.

Example: `[1, 2, 3, 4]`, `[6]`, `[8, 9]`, `[100]`

Then, count how many numbers are in the longest consecutive string.  In this example, `4` will be returned.

# Success Examples
```
Input: 77 80 79 21 20 2 3 1 81 
Output: 3
```
```
Input: 6 7 14 5 15 9 64 78 8 32
Output: 5
```

# Unittest

```
cd <path>/<to>/<project>/pythonPlay
python -m unittest discover longestConsecutive/tests
python -m unittest longestConsecutive/tests/test_longest_consecutive.py
```

# Script Details

- Python 3.8.10