# Codeland Username Validation
Problem Source: [CoderByte Link](https://coderbyte.com/editor/Codeland%20Username%20Validation:Python3)

# Success Criteria
Have the function `CodelandUsernameValidation(str)` take the `strParam` string parameter being passed and determine if the string is a valid username according to the following rules: 

1. The username is between 4 and 25 characters.
2. It must start with a letter. 
3. It can only contain letters, numbers, and the underscore character. 
4. It cannot end with an underscore character. 

If the username is valid then your program should return the string `true`, otherwise return the string `false`.

# Success Examples
```
Input: "aa_" 
Output: false
```
```
Input: "u__hello_world123" 
Output: true
```

# Unittest

```
cd <path>/<to>/<project>/pythonPlay
python -m unittest discover codelandUsernameValidation/tests
python -m unittest codelandUsernameValidation/tests/test_codelandUsernameValidation.py
```

# Script Details

- Python 3.8.10