import dotComShip




class gameBoard(object):
    shipcount = 0
    trycount = 0

    def __init__(self):
        self.shipcount = 0
        self.trycout = 0
        self.occupied = set()

    def gameon(self):
        # print self.shipcount
        return self.shipcount

    def check(self, posinput):
        self.trycount += 1
        abool = appleship.checkposition(posinput)
        mbool = msship.checkposition(posinput)
        bbool = baiduship.checkposition(posinput)
        if abool == 1 or mbool == 1 or bbool == 1:
            print "Hit"
            return True
        elif abool == 2 or mbool == 2 or bbool == 2:
            self.shipcount -= 1
            print "You sank a boat"
            return True
        else:
            print "Miss"
            return False

    def checkoccupied(self, ship):
        if not set(ship.poslist).intersection(self.occupied):
                    self.occupied = set(ship.poslist).union(self.occupied)
                    return False
        return True

board = gameBoard()
appleship = dotComShip.dotComShip("Apple")
board.checkoccupied(appleship)
while True:
    msship = dotComShip.dotComShip("MS")
    if not board.checkoccupied(msship):
        break
while True:
    baiduship = dotComShip.dotComShip("Baidu")
    if not board.checkoccupied(baiduship):
        break
board.shipcount = 3
print "The ships are ready."

while board.gameon():
    posinput = raw_input("Please input a position from A1 to G7:")
    board.check(posinput)

print "You finished the game in ", board.trycount