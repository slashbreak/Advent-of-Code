root = "vgzejbd"

d = {}

class Node:

    def __init__(self, name, weight, *childdata):
        self.children = []
        self.name = name
        self.weight = int(weight)
        self.total = self.weight
        self.childWeights = []
        self.childdata = childdata
        for i in self.childdata:
            #print(d[i])
            
            t = Node(*d[i])
            self.children.append(t)
    def addChildWeight(self):
        if len(self.children) < 1 :
            self.total = int(self.weight)
        else:
            print(self.name,self.total)
            for i in self.children:
                
                self.total += i.addChildWeight()
                print(i.name, i.total)
            
        return self.total
            #self.childWeights.append(self.addChildWeight(i))
        #print("ok")


with open('input7.txt') as f:
    for n in f.readlines():
        a = n.strip().split()
        d[a[0]] = a
        
        #nodes.append(a)
print(d[root])
t = Node(*d[root])    
nodes = []
print(len(t.children[0].children[0].children[0].children[0].children), "here")
print(t.children)
a = t.addChildWeight()
#print(a)
#t = 0
''' def weights(node, nChild):
    global t
    w = []

    if nChild < 1:
        return t
    else:
        for i in node.children:
            print(i.weight)
            t += weights(i, len(i.children))
            w.append( weights(i, len(i.children)))
        print('done', t)    
print(weights(t, len(t.children)))
'''
print(t.total, t.weight, t.name)
for i in t.children:
    print(i.total, i.weight, i.name)
print('  ssssss   ')
for i in t.children[1].children:
    print(i.total, i.weight, i.name)
print('  ssssss   ')
for i in t.children[1].children[4].children:
    print(i.total, i.weight, i.name)
