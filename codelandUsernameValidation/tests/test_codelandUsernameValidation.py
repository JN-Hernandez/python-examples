import unittest
import codelandUsernameValidation.codelandUsernameValidation as cuv

USERNAME_EMPTY = ""
USERNAME_ENDS_WITH_UNDERSCORE = "test1_"
USERNAME_LONG = "test_username_is_way_too_long"
USERNAME_NONE = None
USERNAME_SHORT = "te"
USERNAME_START_NUMBER = "1_test"
USERNAME_START_SPECIAL_CHARACTER = "*_test"
USERNAME_VALID = "test_1"
USERNAME_WITH_BACKSLASH = "test\\1"
USERNAME_WITH_DOUBLE_QUOTE = "test\"1"
USERNAME_WITH_SPECIAL_CHARACTER = "test*1"
USERNAME_WITH_SINGLE_QUOTE = "test'1"
USERNAME_WITH_SPACE = "test 1"


# TODO: enable unittests to work outside of PyCharm
class Test_codelandUsernameValidation(unittest.TestCase):
    def test_check_valid_username_length(self):
        """Test if a valid username length will yield True"""
        result = cuv.check_username_length(USERNAME_VALID)
        self.assertTrue(result)

    def test_check_short_username_length(self):
        """Test if a short username will yield False"""
        result = cuv.check_username_length(USERNAME_SHORT)
        self.assertFalse(result)

    def test_check_long_username_length(self):
        """Test if a long username will yield False"""
        result = cuv.check_username_length(USERNAME_LONG)
        self.assertFalse(result)

    def test_check_empty_username(self):
        """Test if no username is entered will yield False"""
        result = cuv.check_username_length(USERNAME_EMPTY)
        self.assertFalse(result)

    # def test_check_username_is_none(self):
    #     TODO: uncomment out when None username is properly handled
    #     """Test error handling when the username is None"""
    #     result = cuv.check_username_length(USERNAME_NONE)
    #     self.assertFalse(result)

    def test_check_valid_starts_with_letter(self):
        """Test if a username starting with a letter will yield True"""
        result = cuv.check_starts_with_letter(USERNAME_VALID)
        self.assertTrue(result)

    def test_check_starts_with_number(self):
        """Test if a username starting with a number will yield False"""
        result = cuv.check_starts_with_letter(USERNAME_START_NUMBER)
        self.assertFalse(result)

    def test_check_starts_with_special_character(self):
        """Test if a username starting with a special character will yield False"""
        result = cuv.check_starts_with_letter(USERNAME_START_SPECIAL_CHARACTER)
        self.assertFalse(result)

    def test_check_special_character_is_underscore(self):
        """Test if a username containing an underscore will yield True"""
        result = cuv.check_special_characters(USERNAME_VALID)
        self.assertTrue(result)

    def test_check_special_character_is_not_valid(self):
        """Test if a username containing a non-underscore special character will yield False"""
        result = cuv.check_special_characters(USERNAME_WITH_SPECIAL_CHARACTER)
        self.assertFalse(result)

    def test_check_special_character_is_backslash(self):
        """Test if a username containing a backslash will yield False"""
        result = cuv.check_special_characters(USERNAME_WITH_BACKSLASH)
        self.assertFalse(result)

    def test_check_special_character_is_double_quote(self):
        """Test if a username containing a double quote will yield False"""
        result = cuv.check_special_characters(USERNAME_WITH_DOUBLE_QUOTE)
        self.assertFalse(result)

    def test_check_special_character_is_single_quote(self):
        """Test if a username containing a single quote will yield False"""
        result = cuv.check_special_characters(USERNAME_WITH_SINGLE_QUOTE)
        self.assertFalse(result)

    def test_check_special_character_is_space(self):
        """Test if a username containing a space will yield False"""
        result = cuv.check_special_characters(USERNAME_WITH_SPACE)
        self.assertFalse(result)

    def test_check_does_not_end_with_underscore(self):
        """Test if a username not ending with an underscore will yield True"""
        result = cuv.check_ends_with_underscore(USERNAME_VALID)
        self.assertTrue(result)

    def test_check_ends_with_underscore(self):
        """Test if a username ending with an underscore will yield False"""
        result = cuv.check_ends_with_underscore(USERNAME_ENDS_WITH_UNDERSCORE)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
