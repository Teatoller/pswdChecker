# password_checker.py

"""
Question:
A website requires the users to input username and password to register.
 Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated
passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
>>>ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
>>>ABd1234@1

"""
import re  # regular expression matching operation module
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
        print('Password Failed: Should contain a number between [1-9]')
        continue
    elif not re.search('[A-Z]', password_input):
        """ checks if password has an uppercase alpha or not """
        print(
            'Password Failed: Must have any uppercase alpha between [A-Z]')
        continue
    elif not re.search('[$#@]', password_input):
        """ checks if password contains a special character or not """
        print(
            'Password Failed: Must have at least a special character [$#@]')
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
        """ If Password passes all checks print valid and exit from loop """
        valid = True
        break
if (valid):
    print('Password is valid, passed!')
