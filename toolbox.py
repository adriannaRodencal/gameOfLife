#
# Do as many 'lists' and functions you can and check grade.
#
def get_largest(listOfNumbers):
    """Return largest number from an array of numbers."""
    #
    # Check to see if list is empty
    #
    if listOfNumbers == []:
        largest = None
    else:
        #
        # Assume the first number is the largest
        #
        largest = listOfNumbers[0]
    #
    # Loop through the list looking for a larger number
    #
    for number in listOfNumbers:
        if number > largest:
            largest = number
    return largest


def get_smallest(listOfNumbers):
    """Return smallest number from an array of numbers."""
    if listOfNumbers == []:
        smallest = None
    else:
        smallest = listOfNumbers[0]
    for number in listOfNumbers:
        if number < smallest:
            smallest = number
    return smallest


def is_smallest(listOfNumbers, isSmallest):
    """Return smallest number and whether it is True or False."""
    smallest = get_smallest(listOfNumbers)
    if isSmallest == smallest:
        isSmallest = True
    else:
        isSmallest = False
    return isSmallest


def get_total(listOfNumbers):
    """Return sum of all the numbers."""
    if listOfNumbers == []:
        total = None
    else:
        total = 0
    for number in listOfNumbers:
        total = total + number
    return total


def get_average(listOfNumbers):
    """Return average of all numbers."""
    total = 0
    count = 0
    average = 0
    if listOfNumbers == []:
        average = None
    for number in listOfNumbers:
        count = count + 1
        total = total + number
        average = total / count
    return average


def is_in_list(listOfNumbers, listNumber):
    length = len(listOfNumbers)
    count = 0
    while count < length:
        if listOfNumbers[count] == listNumber:
            return True
        count = count + 1
    else:
        return False


def get_largest_position(listOfNumbers):
    """Return first index of the largest number."""
    if listOfNumbers == []:
        position = None
    count = 0
    largest = get_largest(listOfNumbers)
    for number in listOfNumbers:
        count = count + 1
        if number == largest:
            position = count - 1
            if position < 0:
                position = 0
            return position


def make_list(amountOfTimes, number):
    """Given an integer and number return integer elements that have the value of Y."""
    count = 0
    returnList = []
    if amountOfTimes != int(amountOfTimes):
        return None
    for count in range(int(amountOfTimes)):
        returnList.append(number)
        count = count + 1
    return returnList


def get_range(listOfNumbers):
    """Return range of array of numbers."""
    if listOfNumbers == []:
        return None
    largest = get_largest(listOfNumbers)
    smallest = get_smallest(listOfNumbers)
    listRange = (smallest, largest)
    listRange = list(listRange)
    return listRange


def purge1(listOfNumbers, numberRemove):
    """Return a list with all occurrences of the value removed."""
    count = 0
    newList = 0
    length = len(listOfNumbers)
    if count < length:
        if listOfNumbers[count] == numberRemove:
            remove = True
        else:
            remove = False
        if remove == True:
            newList.append(listOfNumbers)
        count = count + 1
    return newList


def purge(listOfNumbers, numberRemove):
    count = 0
    for number in listOfNumbers:
        if number == numberRemove:
            position = None
        if number != numberRemove:
            listOfNumbers[count]
        count = count + 1
    return listOfNumbers


def index_is(listOfNumbers):
    """Returns position of the value within the array."""
    listOfNumbers.values(listOfNumbers)


def get_median(listOfNumbers):
    """Return median of array of numbers."""
    length = len(listOfNumbers)
    position = round(length / 2)
    print(length)
    print(listOfNumbers)
    print(position)
    if length % 2 == 0:
        median = get_average([position - 1, position])

    else:
        median = listOfNumbers[position - 1]
    print(median)
    return median


def combine_sorted():
    """Sorta and return numbers in array IN ORDER."""


def get_mode():
    """Return the mode of the array of numbers."""


def is_number(testValue):
    """Returns True if testValue is an integer and False otherwise."""
    isNumber = True
    testValue = str(testValue).strip()
    length = len(testValue)
    count = 0
    decimalCount = 0
    if length == 0:
        isNumber = False
    while count < length:
        if testValue[count] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            count = count + 1
        elif testValue[count] in ['+', ',', '-'] and count == 0 and length != 1:
            count = count + 1
        elif testValue[count] == '.' and length != 1 and decimalCount == 0:
            count = count + 1
            decimalCount = decimalCount + 1
        else:
            isNumber = False
            break

    return isNumber


def get_integer(prompt):
    """Asks the user the prompt and verifies they enter an integer"""
    #
    # If there's no space at the end of prompt, add one.
    #
    if prompt[-1] != " ":
        prompt = prompt + " "
    number = input(prompt)
    #
    # We're only going to use prompt again if they entered something that
    # is not an integer, so it's simpler just to change the prompt once
    # outside the loop.
    #
    prompt = prompt + "(integers only) "
    #
    # If they didn't enter an integer, ask them to enter one.
    #
    while not is_integer(number):
        number = input(prompt)
    number = int(number)
    return number


def is_integer(number):
    """Returns True is number is an interger else it returns False."""
    isInteger = True
    #
    # Remove leading and trailing whites space and
    # check for 4 special cases of non-integers. Then
    # remove any leading positive or negative signs.
    #
    number = str(number).strip()
    if number in ['', '.', '+', '-']:
        isInteger = False
    if isInteger and number[0] in '+-':
        number = number[1:]
        #
    # Loop through the string checking to make sure
    # the characters are all legal integer characters.
    #
    position = 0
    legalValues = '0123456789.'
    while isInteger and position <= len(number) - 1:
        if number[position] not in legalValues:
            isInteger = False
        if number[position] == '.':
            legalValues = '0'
        position += 1

    return isInteger


def get_number(prompt):
    """Asks the user the prompt and verifies they enter a float"""
    if prompt[-1] != " ":
        prompt += " "
    number = input(prompt)
    while not is_number(number):
        if prompt[-16:] != " (numbers only) ":
            prompt = prompt + "(numbers only) "
        number = input(prompt)
    number = float(number)
    return number


def is_number(number):
    '''Returns True is testValue is a number, otherwise returns False.'''
    isNumber = True
    testValue = str(number)
    isNumber = True
    #
    # Remove leading and trailing whites space and
    # check for 4 special cases of non-numbers. Then
    # remove any leading positive or negative signs.
    #
    number = str(number).strip()
    if number in ['', '.', '+', '-']:
        isNumber = False
    if isNumber and number[0] in '+-':
        number = number[1:]
        #
    # Loop through the string checking to make sure
    # the characters are all legal integer characters.
    #
    legalValues = '.0123456789'
    for character in number:
        if character not in legalValues:
            isNumber = False
        if character == '.':
            legalValues = '0123456789'

    return isNumber


def get_positive_number(prompt):
    """returns a positive number."""
    number = get_number(prompt)
    while number < 0:
        print("You have to enter a positive value.")
        number = get_number(prompt)
    return number


def get_integer_between(low, high, prompt="Enter an integer:"):
    prompt += " (" + str(low) + "-" + str(high) + ")"
    number = get_integer(prompt)
    while (number < low) or (number > high):
        number = get_integer(prompt)
    return number


def get_boolean(prompt):
    """Ask the user a yes or no question"""
    prompt = prompt + " (y/n) "
    answer = input(prompt)
    answer = answer.lower()
    if answer in ['yes', 'sure', 'yeah', 'true', 'absolutely', 'y', 'da', 'si']:
        answer = True
    elif answer in ['n', 'no', 'nope', 'nah']:
        answer = False
    else:
        prompt = "Does " + answer + " mean yes or no?"
        answer = get_boolean(prompt)
    return answer


def get_string(prompt):
    """Get and return a non-empty string"""
    if prompt[-1] != " ":
        prompt = prompt + " "
    string = input(prompt)
    while not string:
        if prompt[-31:] != " (you have to enter something) ":
            prompt = prompt + "(you have to enter something) "
        string = input(prompt)
    return string


def money(number):
    """Convert any number into a reasonable dollar amount string."""
    number = round(number, 2)
    #
    # We're saving whether it's negative so that we can
    # add praentheses at the end.
    #
    if number < 0:
        isNegative = True
    else:
        isNegative = False
    #
    # No negatives when we convert to string.
    #
    number = abs(number)
    string = str(number)
    #
    # Just makeing sure that the index is in range.
    #
    if len(string) > 1:
        if string[-2] == ".":
            string = string + "0"
        elif string[-3] == ".":
            string = string
        else:
            string = string + ".00"
    else:
        string = string + ".00"
    string = "$" + string
    if isNegative:
        string = "(" + string + ")"

    return string


def print_separator(character, length=60):
    """Prints length number of characters."""
    string = (character[0] * int(length))
    print(string)


def print_centered(string, length=60, character=" "):
    """Prints a string centered on a line of length length."""
    stringLength = len(string)
    padding = int((length - stringLength) / 2)
    if padding > 0:
        centeredString = character[0] * padding + string + character[0] * padding
    else:
        centeredString = string[:length]
    print(centeredString)


def yes_or_no(prompt):
    """This allows my older code to work."""
    return get_boolean(prompt)


def make_percent(percent):
    """Return decimal as percent value"""
    newPercent = percent * 100
    string = f'{newPercent:0.05}%'
    return (string)
