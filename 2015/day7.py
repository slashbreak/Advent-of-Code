override = "16076" # for part 2

registers = {}
operations = ['NOT','OR','AND','RSHIFT','LSHIFT']
commands = []
with open('input7.txt') as f:
    for l in f.readlines():
        p = l.strip().split(' ')
        length = len(p)
        for i,c in enumerate(p):
            if c not in operations:
                if not c.isdigit():
                    if c not in registers:
                        registers[c] = None
                else:
                    p[i] = int(c)
        commands.append(p)

while len(commands) != 0:
    commands_copy = commands[:]
    for c in commands_copy:
        l = len(c)
        if l == 2:
            if type(c[0]) == int:
                registers[c[1]] = c[0]
                commands.remove(c)
            elif registers[c[0]] != None:
                registers[c[1]] = registers[c[0]]
                commands.remove(c)
        if l == 3:
            if registers[c[1]] != None:
                registers[c[2]] = 65535 - registers[c[1]]
                commands.remove(c)
        if l == 4:
            if c[1] == 'OR':
                if type(c[0]) == int:
                    if registers[c[2]] != None:
                        registers[c[3]] = (c[0] | registers[c[2]])
                        commands.remove(c)
                elif type(c[2]) == int:
                    if registers[c[2]] != None:
                        registers[c[3]] = (c[2] | registers[c[0]])
                        commands.remove(c)
                elif registers[c[0]] != None and registers[c[2]] != None:
                    registers[c[3]] = (registers[c[0]] | registers[c[2]])
                    commands.remove(c)
            elif c[1] == 'AND':
                if type(c[0]) == int:
                    if registers[c[2]] != None:
                        registers[c[3]] = (c[0] & registers[c[2]])
                        commands.remove(c)
                elif type(c[2]) == int:
                    if registers[c[2]] != None:
                        registers[c[3]] = (c[2] & registers[c[0]])
                        commands.remove(c)
                elif registers[c[0]] != None and registers[c[2]] != None:
                    registers[c[3]] = (registers[c[0]] & registers[c[2]])
                    commands.remove(c)
            elif c[1] == 'RSHIFT':
                if registers[c[0]] != None:
                    registers[c[3]] = (registers[c[0]] // (2**c[2]))
                    commands.remove(c)
            elif c[1] == 'LSHIFT':
                if registers[c[0]] != None:
                    registers[c[3]] = (registers[c[0]] * (2**c[2]) & 65535)
                    commands.remove(c)

print(registers['a'])
