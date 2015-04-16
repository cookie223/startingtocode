import re
import sys

def simplifyPath(Path):
    Pathstore = re.split('/',Path)
    Pathoutput = []
    for item in Pathstore:
        if item == '':
            pass
        elif item == '..':
            try:
                Pathoutput.pop()
            except:
                pass
        elif item == '.':
            pass
        else:
            Pathoutput.append(item)
    Pathoutput.insert(0,'')
    res = '/'.join(Pathoutput)
    if len(res)== 0:
        res = '/'
    return res
if __name__ =='__main__':
    print simplifyPath(sys.argv[1])
