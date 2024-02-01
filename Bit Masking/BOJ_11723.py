import sys

def solution():
    M = int(sys.stdin.readline().rstrip())
    set_value = 0

    for _ in range(M):
        input_command = sys.stdin.readline().split()
        command = ""
        bit_value = 0
        
        if len(input_command) == 2:
            command = input_command[0]
            value = int(input_command[1])
            bit_value = 1 << value
        else:
            command = input_command[0]

        if command == "add":
            set_value = set_value | bit_value
        elif command == "remove":
            set_value = set_value & (~bit_value)
        elif command == "check":
            print(1 if set_value & bit_value == bit_value else 0)
        elif command == "toggle":
            set_value = set_value ^ bit_value
        elif command == "all":
            set_value = 0b111111111111111111111
        elif command == "empty":
            set_value = 0


solution()