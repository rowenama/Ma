# define operation
operation = ['R', 'D']

# find the sum of the path
def findsum (InputData, path):
    current = InputMatrix[0][0]
    i = 0
    j = 0
    for data in path:
        if data:
            i = i+1
        else:
            j = j+1            
        current = current + InputMatrix[i][j]
    return current

#find the path of the right sum
def createpath(InputData, M, N):
    Rem = 0
    for i in range(M+1):
        Rem = Rem + i 
    InputData = InputData - Rem
    Div_x = InputData // (N-1)
    Mod_x = InputData % (N-1)
    Path = []
    for i in range(1,M+1):
        if i == Div_x:
            for j in range(N-1-Mod_x):
                Path.append(0)
        elif i == Div_x+1:
            for j in range(Mod_x):
                Path.append(0)
        Path.append(1)
    Path.pop()

    return Path

# main function
if __name__ == '__main__':
    
    DesireSum = [65,72,90,110]
    M = 9
    N = 9
    #InputMatrix = [[y+1 for x in range(N)] for y in range(M)]

    for data in DesireSum:
        pathforsum = createpath(data, M, N)
        print(data, end =" ")
        for data in pathforsum:
            print(operation[data], end ="")
        print()

    print()

    DesireSum = [87127231192,5994891682]
    M = 90000
    N = 100000
    #InputMatrix = [[y+1 for x in range(N)] for y in range(M)]

    for data in DesireSum:
        pathforsum = createpath(data, M, N)
        print(data, end =" ")
        for data in pathforsum:
            print(operation[data], end ="")
        print()

