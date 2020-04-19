def main():

    myfile=open("Cut_up.txt" ,'rt')
    noi = []
    col1 = []
    noofcol = 4
    col2 = [2,1,4,3]
    lines=myfile.readlines()
    l=0
    counter=1
    for line in lines:
        #noi = []
        if counter==1:
            l = len(line)
            #print(line)
            #print(l)
            strpos =int(l/noofcol)
            #print(strpos)
            #print(nos)
            val=0
            for i in range(0,noofcol-1):
                val+=strpos
                noi.append(val)
            noi.append(l)
        counter+= 1
        #print(noi)
        start=0
        counter1=1
        for i in noi:
            col1.append(line[start:i])
            start = i
            '''if counter1==1:
                col1.append(line[start:i])
                start=i
                counter1 += 1
            elif counter1==2:
                col2.append(line[start: i])
                start = i
                counter1 += 1
            else:
                col3.append(line[start: i])
                start = i
                counter1 += 1'''
        #print(col1,end=' ')
        #print(col2,end=' ')
        #print(col3,end=' ')
        #print()
        #break
    print(col1)
    myfile.close()
    print(counter)
    vol=0
    f=open("Output.txt",'w+')
    for i in range(1,counter):
        op=''
        for j in col2:
            ind = vol+j-1
            op = "".join([op, col1[ind]])
        vol = vol+noofcol
        f.writelines(op)
        print(op)
    f.close()
        #break


main()