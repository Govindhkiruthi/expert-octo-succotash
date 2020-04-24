import array as arr
from numpy import *

def main():
    #Created Dictionary for taking column from given input.
    thisdict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6
    }
    #open text file which has paragraph
    myfile = open("Cut_up.txt", 'rt')
    #Getting input
    Exp = str(input('Enter the input'))
    Exp=Exp.upper()
    noofcol = 0
    #Find Number of columns to split
    for i in Exp:
        if i != '+':
            noofcol += 1
    noi = []
    col1 = []
    col2 = []
    lines = myfile.readlines()
    l = 0
    counter = 1
    #iterate lines in paragraph and split the paragraph
    for line in lines:
        # noi = []
        if counter == 1:
            l = len(line)
            strpos = int(l / noofcol)
            val = 0
            for i in range(0, noofcol - 1):
                val += strpos
                noi.append(val)
            noi.append(l)
        counter += 1
        start = 0
        itr=1
        for i in noi:
            temp=line[start:i]
            if temp[0]==' ':
                temp=temp[1:i-1]

            col1.append(temp)
            #col1.append(line[start:i])
            start = i
            itr+=1
        totrec=counter*noofcol
        diff=totrec-len(col1)
        for i in range(0,diff):
            col1.append('')
    myfile.close()
    #Store the values in array
    arr1=array(col1)
    arr2=arr1.reshape(counter,noofcol)
    #print(arr2)
    vol = 0
    nos = []
    nos = Exp.split('+')
    # permutate the column as per input and write it in output  text file
    f = open("Output.txt", 'w+')
    inc=1
    for a in nos:
        col2=[]
        noofcol=0
        for k in a:
            col2.append(thisdict[k])
            noofcol += 1
        vol = 0
        for i in range(0, counter):
            op = ''
            b=0
            for j in col2:
                b+=1
                j= j - 1
                op = " ".join([op, arr2[i][j]])
                if b == noofcol and op !='':
                    f.write(op)
                    if inc<len(nos):
                        f.write('\n')
        inc+=1
    f.close()
main()