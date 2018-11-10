# GET TWO NUMBERS FROM THE USER.
number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter another number: '))

# CHECK IF NUMBERS ARE EQUAL.
if number_1 == number_2:
    print('Numbers are equal')

# CHECK IF NUMBERS AREN'T EQUAL.
numbers_not_equal = (number_1 != number_2)
if numbers_not_equal:
    print('Numbers are not equal')

# CHECK IF ONE NUMBER IS LESS THEN ANOTHER.
number_1_less_than_number_2 = (number_1 < number_2)
if number_1_less_than_number_2:
    print('Number 1 less then number 2')

# CHECK IF ONE NUMBER IS GREATER THAN ANOTHER
number_1_greater_than_number_2 = (number_1 > number_2)
if number_1_greater_than_number_2:
    print('Number 1 greater than number 2')
