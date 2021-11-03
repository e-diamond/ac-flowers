
def decimal(value, base):
    result = 0
    for i, digit in enumerate(reversed(value)):
        result = result + int(digit)*(base**i)
    return result 
