
# change a given number to base 10 (returns int)
def decimal(value, base):
    result = 0
    for i, digit in enumerate(reversed(value)):
        result = result + int(digit)*(base**i)
    return result

# change a given number to base 3 (returns str)
def ternary(value, base):
    if base != 10:
        value = decimal(str(value), base)

    result = ""
    while value:
        result = str(value % 3) + result
        value = value // 3

    return result

# pads a gene string with leading zeros 
def pad(value, length):
    while len(value) < length:
        value = "0" + value
    return value
