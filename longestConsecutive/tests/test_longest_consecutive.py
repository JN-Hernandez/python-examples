import unittest
import longestConsecutive.longest_consecutive as lc

INPUT_EMPTY = ""
INPUT_MIX_INTEGERS_LETTERS = "4 -3 a 1 2 c 100 b"
INPUT_NEGATIVE_INTEGERS = "4 -3 8 1 2 6 100 9"
INPUT_SQL_STRING = "select *"
INPUT_STRING_LETTERS = "a b c d e f g"
INPUT_STRING_WORDS = "alpha bravo charlie delta echo"
INPUT_VALID_INTEGERS = "4 3 8 1 2 6 100 9"


class TestLongestConsecutive(unittest.TestCase):
    def test_convert_user_input_to_array_valid_integers(self):
        """Test if valid user input of integers will return an integer array"""
        result = lc.convert_user_input_to_array(INPUT_VALID_INTEGERS)
        self.assertTrue(result)

    def test_convert_user_input_to_array_negative_integers(self):
        """Test if user input with negative integers will still return an integer array"""
        result = lc.convert_user_input_to_array(INPUT_NEGATIVE_INTEGERS)
        self.assertTrue(result)

    def test_convert_user_input_to_array_letters(self):
        """Test if user input with a string of letters will not return an integer array"""
        result = lc.convert_user_input_to_array(INPUT_STRING_LETTERS)
        self.assertFalse(result)

    def test_convert_user_input_to_array_words(self):
        """Test if user input with a string of words will not return an integer array"""
        result = lc.convert_user_input_to_array(INPUT_STRING_WORDS)
        self.assertFalse(result)

    def test_convert_user_input_to_array_mixed_integers_letters(self):
        """Test if user input with a string of mixed integers and letters will not return an integer array"""
        result = lc.convert_user_input_to_array(INPUT_MIX_INTEGERS_LETTERS)
        self.assertFalse(result)

    def test_convert_user_input_to_array_sql_statement(self):
        """Test if user input with a sql statement will not return an integer array"""
        result = lc.convert_user_input_to_array(INPUT_SQL_STRING)
        self.assertFalse(result)

    def test_convert_user_input_to_array_empty_string(self):
        """Test if user input of an empty string will not return an integer array"""
        result = lc.convert_user_input_to_array(INPUT_EMPTY)
        self.assertFalse(result)

    def test_convert_user_input_to_array_none(self):
        """Test if user input of 'None' will not return an integer array"""
        result = lc.convert_user_input_to_array(None)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
