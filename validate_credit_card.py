"""

to write a simple credit card validator using Python.
The algorithm that will be used to verify card numbers is called the Luhn algorithm.
also known as the "modulus 10 algorithm,"

"""


def validate_credit_card(card_number: str) -> bool:
    """This function validates a credit card number."""
    # 1. Change datatype to list[int]
    card_number = [int(num) for num in card_number]

    # 2. Remove the last digit:
    checkDigit = card_number.pop(-1)

    # 3. Reverse the remaining digits:
    card_number.reverse()

    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    # 6. Add the checkDigit back to the list:
    card_number.append(checkDigit)

    # 7. Sum all digits:
    checkSum = sum(card_number)

    # 8. If checkSum is divisible by 10, it is valid.
    return checkSum % 10 == 0


if __name__ == '__main__':
    # American Express
    print(validate_credit_card('245'))  # True
    # print(validate_credit_card('371449635398431'))  # True
    # # American Express Corporate
    # print(validate_credit_card('378734493671000'))  # True