import re 
import csv
class myStack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def size(self):
        return len(self.stack)
    def empty(self):
        return self.size() == 0
    def top(self):
        return self.stack[-1]
    def pop(self):
        res = self.top()
        self.stack.pop()
        return res

def Priority(c : str): 
    """return priority order of operator"""
    if (c == '('):
        return 0
    elif (c == '>' or c == '~'):
        return 1
    elif (c == 'v' or c == '^'):
        return 2
    else:
        assert(c == '!')
        return 3
def Oper(x : int, y : int , oper : str): 
    """Calculate expression (x oper y), which 'oper' is in [v,^,<->, ->]"""
    if (oper == 'v'):
        return (x | y) #x v y
    elif (oper == '^'):
        return (x & y) #x ^ y
    elif (oper == '>'):
        return ((1 ^ y) | x) #x -> y
    else:
        assert(oper == '~')
        return (1 if (x == y) else 0) #x <-> y

def preprocess(expression : str):  
    expression = re.sub(' ','', expression) #delete all the space
    #for easier programming, I convered all multi-char operators to one-char
    expression = re.sub('<->', '~', expression) 
    expression = re.sub('->', '>', expression)
    #- and ! both are represent for NOT operator
    expression = re.sub('-', '!', expression)  
    #+ and v both are represent for OR operator
    expression = re.sub('\+', 'v', expression)
    #. and ^ both are represent for AND operator
    expression = re.sub('\.', '^', expression)  
    #delete all !! operator
    while (re.search('!!',expression) != None):
        expression = re.sub('!!', '', expression)
    return expression

def GetVariable(expression : str): 
    """Get all variables appeared in 'expression'"""
    SetVar = set()
    ListVar = []
    for c in expression:
        if ('a' <= c) and (c <= 'z') and (c != 'v'): #v is an operator
            if (c in SetVar):
                continue
            SetVar.add(c)
            ListVar.append(c)
    return ListVar

def GetRPN(expression : str): 
    """Use shunting-yard algorithm to get Reverse Polish notation of 'expression' from Infix notation"""
    stack = myStack()
    RPN = myStack()
    for c in expression:
        if c == '(':
            stack.push(c)
        elif c == ')':
            while True:
                x = stack.pop()
                if (x != '('):
                    RPN.push(x)
                else:
                    break
        elif c in ['v','^','>','~','!']:
            while (not stack.empty()) and Priority(c) <= Priority(stack.top()):
                RPN.push(stack.pop())
            stack.push(c)
        elif (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))):
            RPN.push(c)
    while (not stack.empty()): 
        RPN.push(stack.pop())
    return RPN

def Calculate(RPN : myStack, VariableValue: dict):  
    """Calculate value of expression from RPN, with value of variable is stored in 'VariableValue'"""
    res = myStack()
    for c in RPN.stack:
        if (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))): #'v' is an operator
            res.push(VariableValue[c])
        elif (c == '!'):
            res.push(1 ^ res.pop()) # not X, !X, -X
        else:
            assert(c == '^' or c == 'v' or c == '>' or c == '~')
            x = res.pop()
            y = res.pop()
            res.push(Oper(x, y, c))
    assert(res.size() == 1)
    return res.pop()

def WriteToConsole(result : list):
    for row in result:
        tmp = row.pop()
        for x in row:
            print("  ", x, end = "  |", sep = '') 
        print("  ", tmp, sep = '')
        row.append(tmp)

def WriteToFile(result : list):
    csvFile = open('res.csv','w')
    writer = csv.writer(csvFile)
    writer.writerows(result)
    csvFile.close()

def Solve(expression : str):
    result = []

    ListVariable = GetVariable(expression)
    ListVariable.append(expression)
    result.append(ListVariable.copy())
    ListVariable.pop()

    expression = preprocess(expression)
    RPN = GetRPN(expression)
    n = len(ListVariable)

    #brute force all value of all variables
    for mask in range(2 ** n):
        VariableValue = {'0' : 0, '1' : 1}
        cur = []
        for i in range(n):
            VariableValue[ListVariable[i]] = (mask >> (n - i - 1) & 1)
            cur.append(mask >> (n - i - 1) & 1)
        cur.append(Calculate(RPN, VariableValue))
        result.append(cur)
    WriteToConsole(result)
    # WriteToFile(result)

def main():
    expression = input("Enter Logical expression, please note that " + 
                     "your expression should use lower letter to represent variables, " + 
                     "but don't use 'v' as variable, because it is an operator in my code:\n")
    Solve(expression)

if __name__ == '__main__':
    main()
