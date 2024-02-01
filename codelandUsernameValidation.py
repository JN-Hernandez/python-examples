# JN Hernández
# Thu, Feb 1, 2024
# Python 3.8.1
# Problem: https://coderbyte.com/editor/Codeland%20Username%20Validation:Python3
import re


def codelandUsernameValidation(strParam):

    # Check if the username is between 4 and 25 characters
    count = len(strParam)
    if count >= 4 and count <= 25:
        # Check if string starts with a letter
        first_letter = strParam[0]
        if first_letter.isalpha():
            # Check if only contains letters, numbers, underscore
            regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
            if regex.search(strParam) == None:
                # Check it does not end with underscore
                last_letter = strParam[-1]
                if last_letter != "_":
                    return True
    # code goes here
    return False


# keep this function call here
print(codelandUsernameValidation(input()))
