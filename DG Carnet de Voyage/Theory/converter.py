
def print_hex_from_int(decimal_number):
    hexadecimal_number = hex(decimal_number)

    print("Hexadecimal representation:", hexadecimal_number)

def print_int_from_hex(hexadecimal_number):
    decimal_number = int(hexadecimal_number, 16)

    print("Decimal representation:", decimal_number)