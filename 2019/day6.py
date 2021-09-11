#!/usr/bin/env python3

#AOC 2019 day 6
orbits = []
with open('input6','r') as f:
    for l in f.readlines():
        orbits.append([x for x in l.strip().split(')')])
        
print(orbits)
        
planets = {}
for point, satellite in orbits:
    planets[satellite] = point

print(len(orbits))
#print(planets, len(planets))

def plot_route(planets, src, dest, route, count=1):
    route.append(src)
    if src == dest:
        #route.append(src)
        return 0
    if planets[src] == dest:
        #route.append(src)
        return count
    else:
        #route.append(src)
        return plot_route(planets, planets[src], dest, route, count+1)

total = 0
routes = {}
for plan in planets.keys():
    a = []
    orbit_count = plot_route(planets, plan, 'COM', a)
    print('Planet {0}, count {1}'.format(plan, orbit_count))
    #print(a)
    total += orbit_count
    a.append('COM')
    routes[plan] = a

print('total {}'.format(total))

count = 0
last = 'COM'
for i in routes['YOU']:
    if not i in routes['SAN']:
        count += 1
        
    else:
        last = i
        break
print(last)
count += routes['SAN'].index(last) -2
print('Part 2: {}'.format(count))