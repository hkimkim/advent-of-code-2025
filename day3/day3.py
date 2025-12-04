"""
Day 3 🎄

Part One

Goal: find the largest two digit number

Conditions:
1. two digits
2. tens digit should be the big as possible 

1. Define sum = 0
2. Define largest_joltage = 0 
3. Itreate over the banks
4. Define two pointers p1, p2 where p1 is first index and p2 is second index
5. if banks[p1] > banks[p2]:
6. if banks[p1] + banks[p2] > largest_joltage, update largest_joltage 
7. increment p2
8. if bank[p1] == banks[p2]: p1 should jump to p2 and p2 should be p2 + 1
9. if bank[p1] < banks[p2]:
10. increment both p1, p2 


Part Two

Conditions:
1. must be 12 digits -> number of digits left  == current found digits -> take the whole ending digits
2. find the largest digit for higher decimal places 

Logic:
1. Define two pointers: p1, p2 (Same logic as )
2. Define count of decimal place (this is the key differene with part one)
3. if bank[p1] > bank[p2] -> increment p2
4. if bank[p1] <= bank[p2] -> p1 = p2, increment p2

"""
from input import INPUT, EXAMPLE_INPUT

def readInput(input : str):
    return input.split("\n")

def partOne():
    banks = readInput(INPUT)

    sum = 0
    for bank in banks:
        p1 = 0
        p2 = p1 + 1
        largest_joltage =int(bank[p1] + bank[p2])

        while (p2 < len(bank) - 1):
            current_joltage = int(bank[p1] + bank[p2])
            if (current_joltage > largest_joltage):
                largest_joltage = current_joltage
            
            if (bank[p1] <= bank[p2]):
                p1 = p2

            p2 += 1
        
        current_joltage = int(bank[p1] + bank[p2])
        if (current_joltage > largest_joltage):
            largest_joltage = current_joltage    
        
        sum += largest_joltage

    return sum

def partTwo():
    banks = readInput(EXAMPLE_INPUT)
    sum = 0
    for bank in banks:
        p1 = 0
        p2 = p1
        num = ""
        count = 0 
        remaining = len(bank) - count
        # largest_joltage =int(bank[p1] + bank[p2])

        while (p2 < remaining):
            # current_joltage = int(bank[p1] + bank[p2])
            # if (current_joltage > largest_joltage):
            #     largest_joltage = current_joltage
            
            if (bank[p1] < bank[p2]):
                p1 = p2
            else:
                num += bank[p2]
                count += 1

            p2 += 1
            remaining = len(bank) - count

        print(num)
        print(len(num))

        
        
        # current_joltage = int(bank[p1] + bank[p2])
        # if (current_joltage > largest_joltage):
        #     largest_joltage = current_joltage    
        
        # sum += largest_joltage

    return sum


if __name__ == "__main__":
    # result = partOne()
    result = partTwo()
    print(result)