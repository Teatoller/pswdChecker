# password_checker.py
import re  # regular expression matching operation module
while True:
    """ Infinite loop that holds true as long as password is invalid """
    password_checker = input("Input a password: ")
    valid = False
    if not re.search('[a-z]', password_checker):
        continue
    elif not re.search('[1-9]', password_checker):
        continue
    elif not re.search('[A-Z]', password_checker):
        continue
    elif not re.search('[$#@]', password_checker):
        continue
    elif (len(password_checker) < 6 or len(password_checker) > 12):
        continue
    elif re.search('[\s]', password_checker):
        continue
    else:
        valid = True
        break
    if (valid):
        print('Input Password is valid')
