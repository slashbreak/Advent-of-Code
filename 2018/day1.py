#aoc2018 day 1
import itertools

frequencies = set()
frequencies.add(0)
current_frequency = 0
data = map(int, open('input1').read().split('\n'))

print('Part 1: %i' % sum(data))

for f in itertools.cycle(data):
    current_frequency += f
    if current_frequency in frequencies:
        print('Part 2: %i' % current_frequency)
        break
    frequencies.add(current_frequency)
