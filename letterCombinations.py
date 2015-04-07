import sys

def convert(i):
    if i == '1':
        return None
    elif i == '2':
        return ['a','b','c']
    elif i == '3':
        return ['d','e','f']
    elif i == '4':
        return ['g','h','i']
    elif i == '5':
        return ['j','k','l']
    elif i == '6':
        return ['m','n','o']
    elif i == '7':
        return ['p','q','r','s']
    elif i == '8':
        return ['t','u','v']
    elif i == '9':
        return ['w','x','y','z']
        
def letterCombinations(digits):
    digits_list=[i for i in str(digits)]
    output_list=[]
    if len(digits_list) == 1 :
        return convert(digits_list[0])
    elif len(digits_list) ==0:
        return []
    else:
        i=digits_list.pop() #pop the right most
        if i == '1':
            result = letterCombinations("".join(digits_list))
        else:
            factor1=convert(i)
            factor2=letterCombinations("".join(digits_list))
            result=[]
            for a in factor1:
                for b in factor2:
                    result.append(b+a)#b first
        return result
        
if __name__ =='__main__':
    print letterCombinations(int(sys.argv[1]))
        
        