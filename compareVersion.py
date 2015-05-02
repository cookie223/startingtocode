import sys


class Solution:
    def compareVersion(self, version1, version2):
        if not version1 or not version2:
            return None
        ver1list = version1.split(".")
        ver2list = version2.split(".")
        for i in range(max(len(ver1list), len(ver2list))):
            try:
                ver1current = int(ver1list[i])
            except:
                ver1current = 0
            try:
                ver2current = int(ver2list[i])
            except:
                ver2current = 0
            if ver1current > ver2current:
                return 1
            elif ver1current < ver2current:
                return -1
            else:
                pass
        return 0


if __name__ == '__main__':
    s = Solution()
    print s.compareVersion(sys.argv[1], sys.argv[2])
