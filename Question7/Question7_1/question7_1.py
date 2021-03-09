def coortoindex_2d(inputdata,L1,L2):
    outputindex = inputdata[0] + inputdata[1]*L1
    return outputindex

def indextocoor_2d(inputdata,L1,L2):
    outputcoor = [-1,-1]
    outputcoor[1] = inputdata // L1
    outputcoor[0] = inputdata % L1
    return outputcoor

file1 = open("input_index_7_1.txt", 'r')
file2 = open("input_coordinates_7_1.txt", 'r')
fileout1 = open("output_index_7_1.txt", 'w')
fileout1 = open("output_index_7_1.txt", 'a')
fileout2 = open("output_coordinates_7_1.txt", 'w')
fileout2 = open("output_coordinates_7_1.txt", 'a')

L1 = 50
L2 = 57
 
# index to coordinates
inputindex = []
outputcoor = []
for i, line in enumerate(file1):
    if i > 0:
        inputindex.append(int(line.strip()))

for data in inputindex:
    current_data = indextocoor_2d(data, L1, L2)
    outputcoor.append(current_data)

#append on the file
fileout2.write("x1\tx2\n")
for data in outputcoor:
    current_data = str(data[0]) + "\t" + str(data[1]) + "\n"
    fileout2.write(current_data)

# coordinates to index
inputcoor = []
outputindex = []
for i, line in enumerate(file2):
    if i > 0:
        inner_list = [int(elt.strip()) for elt in line.split('\t')]
        inputcoor.append(inner_list)

for data in inputcoor:
    current_data = coortoindex_2d(data, L1, L2)
    outputindex.append(current_data)

#append on the file
fileout1.write("index\n")
for data in outputindex:
    current_data = str(data) + "\n"
    fileout1.write(current_data)

file1.close()
file2.close()
fileout1.close()
fileout2.close()
