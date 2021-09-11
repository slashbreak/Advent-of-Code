#!/usr/bin/env python3

#AOC 2019 day 1
numbers = []    
with open('input1','r') as f:
    for l in f.readlines():
        numbers.append(int(l.strip()))

def calculate_fuel(num):
    return num // 3 - 2


def part_1(nums):
    total_fuel = 0
    for x in nums:
        total_fuel += calculate_fuel(x)
    return total_fuel
part_1_total = part_1(numbers)
#part_1_total = 100756
print(part_1_total)


#numbers = [100756]

def part_2(nums):
    
    total = 0
    for x in nums:
        sub_total = 0
        
        to_check = calculate_fuel(x)
        while to_check > 0:
            sub_total += to_check
            to_check = calculate_fuel(to_check)
        total += sub_total
    return total
print(part_2(numbers))
        
