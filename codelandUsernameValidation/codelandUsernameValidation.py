# JN Hernández
# Thu, Feb 1, 2024
# Python 3.8.1
# Problem: https://coderbyte.com/editor/Codeland%20Username%20Validation:Python3
import re


def checkEndsWithUnderscore(userInput):
    regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
    if regex.search(userInput) is None:
        last_letter = userInput[-1]
        if last_letter != "_":
            return True
        else:
            return False
    else:
        return False


def checkStartsWithLetter(userInput):
    first_letter = userInput[0]
    if first_letter.isalpha():
        return True
    else:
        return False


def checkUsernameLength(userInput):
    count = len(userInput)
    if 4 <= count <= 25:
        return True
    else:
        return False


def codelandUsernameValidation(strParam):
    if checkUsernameLength(strParam):
        if checkStartsWithLetter(strParam):
            return checkEndsWithUnderscore(strParam)
        else:
            return False
    else:
        return False


print(codelandUsernameValidation(input()))
