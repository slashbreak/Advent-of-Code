#! /usr/bin/env python3

from datetime import datetime

# 1518-06-23 00:33 wakes
# [1518-11-01 00:00] Guard #10 begins shift
lines = []
with open('input4') as f:
    for l in f.readlines():
        data = l.strip().split(' ')
        date = data[0][1:] + ' ' + data[1][:-1]
        if data[2] == 'Guard':
            action = data[3][1:]
        else:
            action = data[2]
        a = []
        a.append(date)
        a.append(action)
        lines.append(a)
print(lines[0])
sorted_dates = sorted(lines,key=lambda x:datetime.strptime(x[0],"%Y-%m-%d %H:%M"))

guards = {}
current_guard = sorted_dates[0][1]
prev_minute = 0
prev_status = ""

# generate schedule
# an status is either 'wakes', 'falls', or a Guard_ID
for time,status in sorted_dates:
    hour,minute = map(int,time.split(' ')[1].split(':'))
    
    if status == "wakes" and prev_status == "falls":
        for i in range(prev_minute,minute):
            guards[current_guard][i] += 1
        
    elif status != "falls": # status is a Guard_ID
        current_guard = status
        # if needed, initialise guard schedule
        if current_guard not in guards:
            guards[current_guard] = [0 for x in range(60)]
        # if guard starts work before 00:00, ignore any time before then
        if hour != 0: 
            minute = 0
        # we've started a new guard's schedule, but this will ensure we 
        # count any previous guard's sleepy time
        if prev_status == "falls":
            for i in range(prev_minute,60):
                guards[current_guard][i] += 1
    prev_status = status
    prev_minute = minute

curr_value = 0
curr_max = 0

for key,value in guards.items():
    if sum(value) > curr_value:
        curr_value = sum(value)
        p1_guard = int(key)
        p1_minute = value.index(max(value))
    
    if max(value) > curr_max:
        curr_max = max(value)
        p2_guard = int(key)
        p2_minute = value.index(max(value))
        
print('Part 1:\n\tSleepiest Guard: #{}\n\tMinutes Spent Dozing: {}\n\tMost Snoozed Time: 00:{}\n\tResult: {}'.format(p1_guard, curr_value, p1_minute, p1_guard*p1_minute))
print('Part 2:\n\tGuard with Most Visits From Sandman: #{}\n\tNumber of Black-outs: {}\n\tOptimum Rest Time: 00:{}\n\tResult: {}'.format(p2_guard, curr_max, p2_minute, p2_guard*p2_minute))

    
    