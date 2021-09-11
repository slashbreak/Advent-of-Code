# pvo inc -524  if f  >  -1
#  0   1    2   3  4  5   6
commands = {}
globalmax = 0
with open('input8.txt') as f:
    for a in f.readlines():
        command = a.strip().split(' ')
        reg1 = command[0]
        reg2 = command[4]
        if reg1 not in commands:
            commands[reg1] = 0
        if reg2 not in commands:
            commands[reg2] = 0
        if command[1] == 'inc':
            if command[5] == '<':
                if commands[reg2] < int(command[6]):
                    commands[reg1] += int(command[2])
            elif command[5] == '>':
                if commands[reg2] > int(command[6]):
                    commands[reg1] += int(command[2])
            elif command[5] == '>=':
                if commands[reg2] >= int(command[6]):
                    commands[reg1] += int(command[2])
            elif command[5] == '<=':
                if commands[reg2] <= int(command[6]):
                    commands[reg1] += int(command[2])
            elif command[5] == '==':
                if commands[reg2] == int(command[6]):
                    commands[reg1] += int(command[2])
            elif command[5] == '!=':
                if commands[reg2] != int(command[6]):
                    commands[reg1] += int(command[2])            
        elif command[1] == 'dec':
            if command[5] == '<':
                if commands[reg2] < int(command[6]):
                    commands[reg1] -= int(command[2])
            elif command[5] == '>':
                if commands[reg2] > int(command[6]):
                    commands[reg1] -= int(command[2])
            elif command[5] == '>=':
                if commands[reg2] >= int(command[6]):
                    commands[reg1] -= int(command[2])
            elif command[5] == '<=':
                if commands[reg2] <= int(command[6]):
                    commands[reg1] -= int(command[2])
            elif command[5] == '==':
                if commands[reg2] == int(command[6]):
                    commands[reg1] -= int(command[2])
            elif command[5] == '!=':
                if commands[reg2] != int(command[6]):
                    commands[reg1] -= int(command[2])
        if commands[reg1] > globalmax:
            globalmax = commands[reg1]
print(commands)
print(max([i for i in commands.values()] ))
print('max', globalmax)

