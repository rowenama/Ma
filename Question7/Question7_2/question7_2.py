def coortoindex_dD(inputdata, *L):
    s = [1]
    outputindex = 0
    for i, data in enumerate(L):
        s.append(s[i] * data) 
    for i in range(len(L)):
        outputindex = outputindex + (inputdata[i]*s[i])
    return outputindex

def indextocoor_2d(inputdata, *L):
    s = [1]
    outputcoor = [0 for x in range(len(L))]
    for i, data in enumerate(L):
        s.append(s[i] * data)
    for i in reversed(range(len(L))):
        outputcoor[i] = inputdata // s[i]
        inputdata = inputdata - outputcoor[i]*s[i]
    return outputcoor

file1 = open("input_index_7_2.txt", 'r')
file2 = open("input_coordinates_7_2.txt", 'r')
fileout1 = open("output_index_7_2.txt", 'w')
fileout1 = open("output_index_7_2.txt", 'a')
fileout2 = open("output_coordinates_7_2.txt", 'w')
fileout2 = open("output_coordinates_7_2.txt", 'a')

L = [4,8,5,9,6,7]

# index to coordinates
inputindex = []
outputcoor = []
## file input
for i, line in enumerate(file1):
    if i > 0:
        inputindex.append(int(line.strip()))

# Compute the corresponding coordinates
for data in inputindex:
    outputcoor.append(indextocoor_2d(data, L[0],L[1],L[2],L[3],L[4],L[5]))

fileout2.write("x1\tx2\tx3\tx4\tx5\tx6\n")
for data in outputcoor:
    current_data = ""
    for i in range(len(L)):
        current_data = current_data + str(data[i]) + "\t" 
    current_data = current_data + "\n"
    fileout2.write(current_data)

# coordinates to index
inputcoor = []
outputindex = []
## file input
for i, line in enumerate(file2):
    if i > 0:
        inputcoor.append([int(elt.strip()) for elt in line.split('\t')])

## Compute the corresponding index
for data in inputcoor:
    outputindex.append(coortoindex_dD(data, L[0],L[1],L[2],L[3],L[4],L[5]))

fileout1.write("index\n")
for data in outputindex:
    current_data = str(data) + "\n"
    fileout1.write(current_data)

file1.close()
file2.close()
fileout1.close()
fileout2.close()
