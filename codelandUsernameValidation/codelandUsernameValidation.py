"""
Codeland Username Validation exercise
"""
import re


def check_special_characters(user_input):
    """Ensure only special character in username is underscore"""
    regex = re.compile('[@!#$%^&*()<\\\\">?/|}\'{~:]')
    return not bool(regex.search(user_input))


def check_ends_with_underscore(user_input):
    """Ensure username does not end with underscore"""
    last_letter = user_input[-1]
    return bool(last_letter != "_")


def check_starts_with_letter(user_input):
    """Ensure username starts with a letter"""
    first_letter = user_input[0]
    return bool(first_letter.isalpha())


def check_username_length(user_input):
    """Ensure username is between 4 and 25 characters"""
    count = len(user_input)
    return bool(4 <= count <= 25)


def codeland_username_validation(str_param):
    """Ensure username is valid according to exercise criteria"""
    if not check_username_length(str_param):
        return False
    if not check_starts_with_letter(str_param):
        return False
    if not check_special_characters(str_param):
        return False
    return check_ends_with_underscore(str_param)


print(codeland_username_validation(input()))
