class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dictbychars = {} # sorted chars as key
        for str in strs:
            if len(str) == 0: # leetcode judgement counts ["", ""]
                break         # delete this two lines
            charlist = list(str)
            charlist.sort()
            chars = "".join(charlist)
            dictbychars[chars] = dictbychars.get(chars, []) + [str]
        result  = [] # get list of more than 1 string
        for anagramlist in dictbychars.values():
            if len(anagramlist) > 1:
                result.append(anagramlist) # for leetcode judgement use result += anagramlist
        return result

strs = ['xyz', 'xzy', 'abc', 'ab', 'ba']
empty = []

s = Solution()
if __name__ == '__main__':
    print s.anagrams(strs)
    print s.anagrams(empty)