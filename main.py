# Daniel Spilchuk
# Simple String Calculator


def old_add(numbers):
    """
    This function only adds single digit numbers and is not as effective as the refined Add.
    :param numbers: string of numbers to add
    :return: Resulting addition.
    """
    result = 0

    # if the string is empty, return 0
    if len(numbers) == 0:
        return 0

    # for each character in the numbers
    for index in range(len(numbers)):
        cur_char = numbers[index]
        if index > 0:

            if numbers[index - 1] == "-":
                return Exception("Negatives not allowed, " + numbers[index - 1] + cur_char)
            else:
                if cur_char.isdigit():
                    result += int(cur_char)
        else:
            if cur_char.isdigit():
                result += int(cur_char)

    return result


def new_add(numbers):
    """

    :param numbers:
    :return:
    """
    result = 0

    # if the string is empty, return 0
    if len(numbers) == 0:
        return 0

    # if the size of the problem is larger than 3, then check for special delimiters
    # replace these with commas for ease
    if len(numbers) > 3:
        if (numbers[0] == "/") and (numbers[1] == "/"):
            numbers = numbers.replace(numbers[2], ",")

    split_nums = numbers.split(",")

    # for each list element get rid of newlines
    for num in split_nums:
        num = num.replace("\n", "")

        # if number larger than 3 digits, disregard
        if len(num) > 3:
            continue

        # safety check for digits, then add onto result if positive
        if num.isdigit():
            if int(num) < 0:
                continue
            else:
                result += int(num)

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # base tests
    add_test_one = ""
    add_test_two = "1,2"
    add_test_three = "1,2,5"
    add_test_11 = "578,5"
    add_test_12 = "2,1001"

    # negative tests
    add_test_four = "-1,2,5"
    add_test_ten = "0,-45, 10"

    # newline tests
    add_test_five = "1\n,2,3"
    add_test_six = "1,\n2,4"

    # new delimiter tests
    add_test_seven = "//;\n1;3;4"
    add_test_eight = "//$\n1$2$3"
    add_test_nine = "//@\n2@3@8"

    print("---BEGIN TESTING---")

    ##########################################################
    # tests for Add function
    ##########################################################
    if new_add(add_test_one) != 0:
        print("Failure in Add, empty string")

    if new_add(add_test_two) != 3:
        print("Failure in Add, simple addition")

    if new_add(add_test_three) != 8:
        print("Failure in Add, three number addition")

    try:
        new_add(add_test_four)
    except Exception:
        pass

    try:
        new_add(add_test_ten)
    except Exception:
        pass

    if new_add(add_test_five) != 6:
        print("Failure in z, issue with newline")

    if new_add(add_test_six) != 7:
        print("Failure in z, issue with newline")

    if new_add(add_test_seven) != 8:
        print("Failure in z, issue with delimiter")

    if new_add(add_test_eight) != 6:
        print("Failure in z, issue with delimiter")

    if new_add(add_test_nine) != 13:
        print("Failure in z, issue with delimiter")

    if new_add(add_test_11) != 583:
        print("Failure in z, issue with 3 digit addition")

    if new_add(add_test_12) != 2:
        print(new_add(add_test_12))
        print("Failure in z, issue with 4 digit addition")

    ##########################################################
    # tests for old old_add function
    ##########################################################
    if old_add(add_test_one) != 0:
        print("Failure in old_add, empty string")

    if old_add(add_test_two) != 3:
        print("Failure in old_add, simple addition")

    if old_add(add_test_three) != 8:
        print("Failure in old_add, three number addition")

    try:
        old_add(add_test_four)
    except Exception:
        pass

    try:
        old_add(add_test_ten)
    except Exception:
        pass

    if old_add(add_test_five) != 6:
        print("Failure in old_add, issue with newline")

    if old_add(add_test_six) != 7:
        print("Failure in old_add, issue with newline")

    if old_add(add_test_seven) != 8:
        print("Failure in old_add, issue with delimiter")

    if old_add(add_test_eight) != 6:
        print("Failure in old_add, issue with delimiter")

    if old_add(add_test_nine) != 13:
        print("Failure in old_add, issue with delimiter")

    print("---END OF TESTING---")
