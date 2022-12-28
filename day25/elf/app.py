from queue import LifoQueue
from typing import Type, List

def run():
    """main entry point
    """
    # Load the file 
    with open('input.txt') as f:
        lines = f.readlines()

    # do something to each line and create a list with the resulting items
    all_balloon_sums = [process_line(x.strip()) for x in lines]
    total_fuel_tens = sum(all_balloon_sums)
    print(f'Total Fuel 10s: {total_fuel_tens}')
    # sums is in decimal format, convert back to elf format
    print(f'Total Fuel Elf: {convert_to_snafu(total_fuel_tens)}')

    
def convert_to_snafu(num: int):
    if num:               # if d is not zero
        a, b = divmod(num+2, 5)
        return convert_to_snafu(a) + '=-012'[b]
    else: return ''     # base case
    
def process_line(line: str) -> int:
    # count # of chars in that line. num - 1 is highest power of leftmost char
    current_power = len(line) - 1
    total_value = 0
    
    # process each character and map it to it's value
    for char in line:
        char_as_num = convert_to_num(char)
        value = char_as_num * (5 ** current_power)
        current_power -= 1
        total_value += value
    return total_value    
    
def convert_to_base_five(total: int) -> str:
    s = ""
    while total:
        s = str(n % 5) + s
        n //= 5
    return s
    
def convert_to_num(char: str) -> int:
    match char:
        case '2':
            return int(char)
        case '1':
            return int(char)
        case '0':
            return int(char)
        case '-':
            return -1
        case '=':
            return -2
        case default:
            print(f'unmatched case: {char}')
            return None  
