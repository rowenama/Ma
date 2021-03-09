#Given the inputs
#ColorBeads = [12, 13] # 12 Red and 13 Blue
#ColorName = ["R","B","N"]
#L = 5

ColorBeads = [139,1451,977,1072,457] 
ColorName = ["R","B","G", "W", "Y", "N"]
L = 64

# create a zero matrix for output
ColorMatrix = [[-1 for x in range(L)] for y in range(L)]

# forming the the color
for i, data_i in enumerate(ColorMatrix):
    for j, data_j in enumerate(data_i):
        Tmp_ColorBeads = ColorBeads[:]
        if j!=0 and i!=0:
            TCol = ColorMatrix[j][i-1]
            RCol = ColorMatrix[j-1][i]
            Tmp_ColorBeads[TCol]=0
            Tmp_ColorBeads[RCol]=0
        elif i==0 and j!=0:
            LCol = ColorMatrix[j-1][i]
            Tmp_ColorBeads[ColorMatrix[j-1][i]] = 0
        elif j==0 and i!=0:
            TCol = ColorMatrix[j][i-1]
            Tmp_ColorBeads[TCol]=0
        
        # finding the next higest number of color
        ColorMatrix[j][i] = Tmp_ColorBeads.index(max(Tmp_ColorBeads))
        ColorBeads[ColorMatrix[j][i]] = ColorBeads[ColorMatrix[j][i]]-1


#output the result
for i, data in enumerate(ColorMatrix):
    for j, data_j in enumerate(data):
        print(ColorName[data_j], end =" ")
    print()
