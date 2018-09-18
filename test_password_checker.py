# test_password_checker.py
import re
import unittest
from password_checker import Password_checker


class TddInPassword_checker(unittest.TestCase):

    def test__method_returns_lower_alpha_in_result(self):
        p = re.compile('[a-z]+')
        p.match('[a-z]')

    def test__method_contains__number_in_result(self):
        p = re.compile('[1-9]+')
        p.match('[1-9]')

    def test__method_returns_upper_alpha_in_result(self):
        p = re.compile('[A-Z]+')
        p.match('[A-Z]')

    def test__method_contains_special_character_in_result(self):
        p = re.compile('[$#@]+')
        p.match('[$#@]')

    def test__method_contains_accepatable_length_in_result(self):
        p = re.compile(
            '[len(password_input) < 6 or len(password_input) > 12]+')
        p.match('len(password_input) < 6 or len(password_input) > 12')

    def test__method_contains_no_space_in_result(self):
        p = re.compile('[\s]+')
        p.match('[\s]')


if __name__ == '__main__':
    unittest.main()
