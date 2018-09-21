# password_checker.py
import re  # regular expression matching operation module


class Password_checker:
    while True:
        """ Infinite loop that holds true as long as password is invalid """
        password_input = input("Input a password: ")
        valid = False
        """ checks if password has a lower case alpha or not """
        if not re.search('[a-z]', password_input):
            print(
                'Password Failed: Must have a lowercase alpha between [a-z]')
            continue
        elif not re.search('[1-9]', password_input):
            """ checks if password has a number or not """
            print('Password Failed: Should contain a number between [0-9]')
            continue
        elif not re.search('[A-Z]', password_input):
            """ checks if password has an uppercase alpha or not """
            print(
                'Password Failed: Must have any uppercase alpha between [A-Z]')
            continue
        elif not re.search('[$#@]', password_input):
            """ checks if password contains a special character or not """
            print(
                'Password Failed: Must have one of the following character [$#@]')
            continue
        elif (len(password_input) < 6 or len(password_input) > 12):
            """ checks if password length is atleast 6 or 12 long or not """
            print('Password Failed: Should between 6 and 12 characters')
            continue
        elif re.search('[\s]', password_input):
            """ checks if the password contain space(s) or not """
            print('Password Failed: Should not contain any space')
            continue
        else:
            """ If Password passes all checks print valid and
             exit from loop """
            valid = True
            break

    if (valid):
        print('Password is valid, passed!')
