
def cir(i,l):
        'For simplify the number'
        if i < l:
            return i
        else:
            return i-l

def canCompleteCircuit(gas, cost):
    start = 0
    gasleft = 0
    position = start
    count =0
    while start < len(gas):
        gasleft += gas[cir(position,len(gas))]
        gasleft -= cost[cir(position,len(gas))]
        if gasleft >=0 and count <len(gas):
            position +=1
            count +=1
        elif count == len(gas):
            break
        elif gasleft <0:
            start = position+1
            position = start
            gasleft=0
            count =0
            continue
    if count == len(gas):
        return start
    else:
        return -1

print canCompleteCircuit(1, 2)