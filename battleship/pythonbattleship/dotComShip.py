
import random

class dotComShip(object):
    poscount = 0
    name = ""
    rletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    def __init__(self, nm):
        self.name = nm
        self.poscout = 0
        self.poslist = []
        direction = random.randint(0, 1)
        # 0 stands for down and 1 stands for right
        firstrow = random.randint(0, 4)
        firstcol = random.randint(0, 4)
        if direction:
            for i in range(3):
                self.poslist.append(self.rletters[firstrow] + str(firstcol + 1 + i))
        else:
            for i in range(3):
                self.poslist.append(self.rletters[firstrow + i] + str(firstcol + 1))
        # print self.poslist
        

    def checkposition(self, posinput):
        # @param string is the position
        # return False if not hit else True
        if posinput in self.poslist:
            print "You hit", self.name
            self.poslist.remove(posinput)
        # remember to sink after 3
            if len(self.poslist) == 0:
                print self.name, "has sunk!"
                return 2
            return 1
        else:
            return 0



