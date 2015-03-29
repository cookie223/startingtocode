class Interval:
    def __init__(self,s=0, e=0):
        self.start=s
        self.end=e

a=Interval(1,5)
b=Interval(

intervals=[a]
newInterval=Interval(6,8)

def Intervalinsert(intervals,newInterval):

    news=newInterval.start
    newe=newInterval.end
    gets=0
    new_intervals=[]
    for i in intervals:
        if i.start<= newInterval.start and i.end < newInterval.start:
            new_intervals.append(i)
            gets=intervals.index(i)+1
            continue
        if i.start<= newInterval.start and i.end >= newInterval.start:
            news=i.start
            gets=intervals.index(i)+1
        if i.start <= newInterval.end and i.end >= newInterval.end:
            newe=i.end
            continue
        if i.start <= newInterval.end and i.end < newInterval.end:
            continue
        if i.start > newInterval.end and i.end > newInterval.end:
            new_intervals.append(i)
            continue
        
            
    #Form the new list
    #print news, newe,gets,gete
    new_intervals.insert(gets,Interval(news,newe))

    return new_intervals

new_intervals = Intervalinsert(intervals,newInterval)
for interval in new_intervals:
    print interval.start,interval.end
        
        