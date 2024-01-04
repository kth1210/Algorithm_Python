import sys

def solution():
    input_formula = sys.stdin.readline().rstrip()
    minus_splitted_formula = input_formula.split('-')

    numbers = []
    for formula in minus_splitted_formula:
        plus_splitted_formula = map(int, formula.split('+'))
        numbers.append(sum(plus_splitted_formula))
    
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
        
    print(result)

solution()