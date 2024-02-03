import re


def check_special_characters(user_input):
    regex = re.compile('[@!#$%^&*()<\\\\">?/|}\'{~:]')
    if regex.search(user_input) is None:
        return True
    else:
        return False


def check_ends_with_underscore(user_input):
    last_letter = user_input[-1]
    if last_letter != "_":
        return True
    else:
        return False


def check_starts_with_letter(user_input):
    first_letter = user_input[0]
    if first_letter.isalpha():
        return True
    else:
        return False


def check_username_length(user_input):
    count = len(user_input)
    if 4 <= count <= 25:
        return True
    else:
        return False


def codeland_username_validation(str_param):
    if check_username_length(str_param):
        if check_starts_with_letter(str_param):
            if check_special_characters(str_param):
                return check_ends_with_underscore(str_param)
            else:
                return False
        else:
            return False
    else:
        return False


print(codeland_username_validation(input()))
