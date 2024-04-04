import math


def add(num1, num2):
    """
    Addition of two numbers
    :param num1: number 1 for calculation
    :param num2: number 2 for calculation
    :return: result of calculation
    """
    return num1 + num2


def sub(num1, num2):
    """
    Substracts two numbers
    :param num1: number 1 for calculation
    :param num2: number 2 for calculation
    :return: result of calculation
    """
    return num1 - num2


def mul(num1, num2):
    """
    multiply of two numbers
    :param num1: number 1 for calculation
    :param num2: number 2 for calculation
    :return: result of calculation
    """
    return num1 * num2


def div(num1, num2):
    """
    division of two numbers
    :param num1: number 1 for calculation
    :param num2: number 2 for calculation
    :return: result of calculation
    """
    return num1 / num2


def pow(num1):
    """
    Squares two numbers
    :param num1: number to square
    :return: result of calculation
    """
    return num1 * num1


def sqrt(num1):
    """
    return the root of a number
    :param num1: number to get the root of
    :return: result of calculation
    """
    return math.sqrt(num1)


def main():
    result_add = add(5, 5.5)
    result_div = div(10, 3)
    result_mul = mul(3, 3)
    result_sub = sub(10, 4.4)
    result_pow = pow(23)
    result_sqrt = sqrt(81)

    print(result_add)
    print(result_div)
    print(result_mul)
    print(result_sub)
    print(result_pow)
    print(result_sqrt)


if __name__ == '__main__':
    main()