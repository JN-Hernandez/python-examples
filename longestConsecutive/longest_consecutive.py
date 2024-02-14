"""
Codeland Longest Consecutive exercise
"""


def convert_user_input_to_array(user_input):
    """Take user input and convert to array"""
    integer_array = []
    if user_input:
        input_list = user_input.split()
        try:
            integer_array = [int(num) for num in input_list]
            integer_array = [num for num in integer_array if num > 0]
            return integer_array

        except ValueError:
            return integer_array
    else:
        return integer_array


def check_array_valid(array):
    """Check to see if the array is valid"""
    if not array:
        array_validity = "Invalid input! Please enter positive integers separated by spaces."
    else:
        array_validity = find_longest_consecutive(array)
    return array_validity


def find_longest_consecutive(array):
    """Find the longest consecutive list of numbers"""
    array.sort()
    current_length = 1
    longest_length = 1
    for i in range(1, len(array)):
        if array[i] == array[i - 1] + 1:
            current_length += 1
        elif array[i] != array[i - 1]:
            current_length = 1
        longest_length = max(longest_length, current_length)

    return longest_length

if __name__ == '__main__':
    original_user_input = input()
    array_to_test = convert_user_input_to_array(original_user_input)
    result = check_array_valid(array_to_test)
    print(result)
