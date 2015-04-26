class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if s is None or len(s) == 1:
            return False
        else:
            stack = []
            for c in s:
                if c == '(' or c == '[' or c == '{':
                    stack.append(c)
                elif c == ')':
                    try:
                        last = stack.pop()
                    except:
                        last = None
                    if not last == '(':
                        return False
                elif c == ']':
                    try:
                        last = stack.pop()
                    except:
                        last = None
                    if not last == '[':
                        return False
                elif c == '}':
                    try:
                        last = stack.pop()
                    except:
                        last = None
                    if not last == '{':
                        return False
                else:
                    pass
        if len(stack) == 0:
            return True
        else:
            return False