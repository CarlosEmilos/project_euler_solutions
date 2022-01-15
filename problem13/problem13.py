with open("problem13/input.txt", "r") as f:
    x = f.read().splitlines()

def parse(x):
    #returns a list of lists
    newlist = []
    for i, strings in enumerate(x):
        #strings = strings.split()
        #create a new list in our list
        newlist.append(int(strings))
        #for j in strings:
        #    newlist[i].append(int(j))
    return newlist

#print(parse(x))

print(sum(parse(x)))
