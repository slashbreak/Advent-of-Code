#! /usr/bin/env python3
plant = []
edge_buffer = '......................................................................................................................'
edge_len = len(edge_buffer)
with open('input12') as f:
    initial_state = '...'+f.readline().strip().split(' ')[2] + edge_buffer
    f.readline()
    for l in f.readlines():
        a = l.strip().split(' ')
        #print(a)
        if a[2] == '#':
            plant.append(a[0])
        
print(initial_state)
#print(plant)

temp_plant = initial_state
plant_sum = temp_plant.count('#')
prev = 0
for i in range(120):
    next_state = ''
    for j in range(len(initial_state)):
        to_check = temp_plant[j-2:j+3]
        if to_check in plant:
            next_state += '#'
        else:
            next_state += '.'
    temp_plant = next_state
    plant_sum = 0
    for a in range(len(temp_plant)):
        if temp_plant[a] == '#':
            plant_sum += a - 3
    #plant_sum = temp_plant.count('#')
    #print(i+1, plant_sum, plant_sum - prev)
    print(temp_plant, i+1, plant_sum)
    prev = plant_sum
n = 50000000000
a = (n)*80
print(n,a)