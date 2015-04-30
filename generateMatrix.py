import sys
import operator


class Solution:
    def layerbylayer(self, nlayer):
        layerlength = self.n - nlayer * 2  # layer starts from 0
        if not layerlength:
            return None
        if layerlength == 1:
            self.ans[nlayer][nlayer] = self.nownum
        else:
            nowx, nowy = nlayer, nlayer
            for dire in self.directions:
                for i in range(layerlength - 1):
                    self.ans[nowx][nowy] = self.nownum
                    nowx, nowy = tuple(map(operator.add, (nowx, nowy), dire))
                    self.nownum += 1
            self.layerbylayer(nlayer + 1)

    def generateMatrix(self, n):
        self.n = n
        self.nownum = 1
        self.ans = [[0] * n for i in range(n)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.layerbylayer(0)
        return self.ans


s = Solution()
if __name__ == '__main__':
    print s.generateMatrix(int(sys.argv[1]))
