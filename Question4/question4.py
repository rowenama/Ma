# Given Inputs
L1 = 20
L2 = 10
InputImage= [
[0,	0,	0,	0,	1,	1,	0,	0,	0,	1,	0,	1,	0,	1,	1,	1,	0,	0,	1,	1],
[1,	0,	1,	0,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	0,	1,	0,	1,	0,	1,	0,	0,	0,	0,	0,	1,	0],
[0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	1,	0,	0,	0,	1,	1,	1,	0,	1,	1],
[1,	0,	0,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	0,	1,	1,	1,	0,	1,	1],
[1,	1,	1,	1,	0,	1,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	1,	0,	1],
[1,	1,	0,	0,	0,	0,	1,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	1,	0,	1],
[0,	1,	0,	0,	0,	1,	1,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	1,	1,	1],
[0,	0,	1,	1,	1,	0,	0,	1,	0,	1,	0,	0,	1,	0,	0,	0,	1,	1,	1,	0],
[1,	0,	1,	0,	1,	0,	1,	1,	1,	1,	0,	0,	1,	0,	1,	0,	0,	0,	0,	1]
]

OutputMatrix = [[0 for x in range(L1)] for y in range(L2)]

# 4-connectivity
CountNum = 1

# frist determine the connection of each pixel with its upper and left neighour
for i, data_i in enumerate(InputImage):
    for j, data_j in enumerate(data_i):
        if data_j>0:
            Con = [CountNum]
            if j!=0:
                Con.append(OutputMatrix[i][j-1])
            if j<L1-1:
                Con.append(OutputMatrix[i][j+1])
                if data_i[j+1] >= 1 and i!=0:
                    Con.append(OutputMatrix[i-1][j+1])
            if i!=0:
                Con.append(OutputMatrix[i-1][j])
            if i<L2-1:
                Con.append(OutputMatrix[i+1][j])
            flag = min(list(filter(lambda a: a != 0, Con)))
            if len(list(filter(lambda a: a != 0, Con)))==1:
                CountNum = CountNum + 1
            OutputMatrix[i][j] = flag

Seq=[0]
# then determine the connection of each pixel with its lower and right neighour
for i, data_i in reversed(list(enumerate(InputImage))):
    for j, data_j in reversed(list(enumerate(data_i))):
        if data_j>0:
            Con = [OutputMatrix[i][j]]
            if j!=0:
                Con.append(OutputMatrix[i][j-1])
            if j<L1-1:
                Con.append(OutputMatrix[i][j+1])
            if i!=0:
                Con.append(OutputMatrix[i-1][j])
            if i<L2-1:
                Con.append(OutputMatrix[i+1][j])
            Con = list(filter(lambda a: a != 0, Con))
            if len(Con)>=1:
                flag = min(Con)
                OutputMatrix[i][j] = flag
                Seq.append(flag)

#sort all the existing connection and order them
Seq = list(set(Seq))

#Output the result
for i, data in enumerate(OutputMatrix):
    for j, data_j in enumerate(data):
        print(Seq.index(data_j), end =" ")
    print()
