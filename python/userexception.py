class InvalidAge(Exception):
    print('Custom error')
    pass

age = 18

try:
    ag =int(input("Enter age : "))
    if ag<age:
        raise InvalidAge('less than 18')
except InvalidAge as ce:
    print(ce)