import random

def randomize_string(string):
    chars = list(string)
    random.shuffle(chars)
    return "".join(chars)

def calculate_luhna_sum(digits):
    total = 0
    nine = 9
    for i, char in enumerate(digits):
        num = int(char)
        if i % 2 == 0:
            num *= 2
            if num > nine:
                num = num // 10 + num % 10
        total += num
    return total

def create_ssn(birth_ssn):
    six = 6
    if not isinstance(birth_ssn, str):
        return "Is not a string"
    digits = ""
    for i in birth_ssn:
        if i.isdigit():
            digits += i
        else:
            return "Not valid"
    if len(digits) != six:
        return "Not valid"
    last_three = ""
    three = 3
    i = 0
    while i < three:
        last_three += str(random.randint(0,9))
        i += 1
    first_nine = digits + last_three

    lsum = calculate_luhna_sum(first_nine)
    remainder = lsum % 10
    check = (10 - remainder) % 10

    full_ssn = f"{digits}-{last_three}{check}"
    return full_ssn
