
# Given a string of digits, keep summing the digits and convert them to Hexadecimal. Repeat the same process till minimal hexadecimal Value is attained. (Validation of strings had to be done as well). Input 8981 Output B. Eg. 8981 -> Sum=26 ->Hexa Value 1A->Sum=1+10=11->Hexa Value B (Answer)
def sum_digits_to_hex(s):
    def sum_digits(s):
        # Sum the digits of the string and then change it to hex
        return hex(sum([int(digit, 16) for digit in s]))[2:].upper()
    
    while(len(s) > 1):
        s = sum_digits(s)
        print(s)
    return s

print(sum_digits_to_hex('8981'))
    