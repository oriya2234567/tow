def decimaltobinary(decimalnum,sibnum):# get to parmters
    ########################################################## this is without func bin
    # binarynum = ""
    # while decimalnum > 0:
    #     if decimalnum % 2 ==0:
    #         binarynum = "0"+ binarynum
    #         decimalnum = decimalnum /2
    #     else:
    #         decimalnum = decimalnum //2
    #         binarynum =  "1" +binarynum

    #with bin func
    binarynum =  bin(decimalnum)# convert decimal num to binari
    binarynum = binarynum[2:]#remov (0b) form the binari num
    print(sibnum-len(binarynum))# chak if we neef to fill zero in the number
    for i in range(sibnum-len(binarynum)):#loof for fןll zero in the binari number
        binarynum ="0"+ binarynum
    return binarynum
                
        
def twocomplemnt(binarynum,sibnum):
    binarynum = str(binarynum)
    twocomplemntbin = ""
    index =0
    for item in binarynum:
        if item == "0":
            twocomplemntbin += "1"
            index = index +1
        else:
            twocomplemntbin += "0"
            index = index + 1
    twocomplemntbin = int(twocomplemntbin,2)
    twocomplemntbin = twocomplemntbin + 1
    z = decimaltobinary(twocomplemntbin,sibnum)
    return z



decimalnum = int(input("enter number you want  convert to binary " ))
sibnum = int(input("enter to representation of the num "))
x = decimaltobinary(decimalnum,sibnum)
print(x)#print the binary num before twocomplemnt
z = twocomplemnt(x,sibnum)
print(z)



