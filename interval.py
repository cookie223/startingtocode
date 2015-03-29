class Interval:
    def __init__(self,s=0, e=0):
        self.start=s
        self.end=e

a=Interval(3,4)
b=Interval(6,9)
intervals=[a,b]
newInterval=Interval(1,2)

def Intervalinsert(intervals,newInterval):
    #Get the new start and end; Get the first and last index to delete
    news=newInterval.start
    newe=newInterval.end
    gets = -1
    gete = -2
    for i in intervals:
        if i.start<= newInterval.start and i.end < newInterval.start:
            continue
        if i.start<= newInterval.start and i.end >= newInterval.start:
            news=i.start
            gets=intervals.index(i)
        if i.start> newInterval.start and i.end >= newInterval.start and gets==-1:
            gets=intervals.index(i)
        if i.start <= newInterval.end and i.end >= newInterval.end:
            newe=i.end
            gete=intervals.index(i)
            continue
        if i.start <= newInterval.end and i.end < newInterval.end:
            gete=intervals.index(i)
            continue
        if i.start > newInterval.end and i.end > newInterval.end and gete == -2 :
            gete=intervals.index(i)-1
            continue
            
    #Form the new list
    print news, newe,gets,gete
    new_intervals=[]
    i=0
    while i <gets:
        new_intervals.append(intervals[i])
        i+=1
        
    new_intervals.append(Interval(news,newe))
    i=gete
    while i < len(intervals):
        i+=1
        try:
            new_intervals.append(intervals[i])
            continue
        except:
            continue

    return new_intervals

new_intervals = Intervalinsert(intervals,newInterval)
for interval in new_intervals:
    print interval.start,interval.end
        
        