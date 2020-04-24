
import textwrap
#from numpy import *
def main():
    switcher = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6
    }
    #Reading the input values
    inputdoc = open("Cut_up.txt", 'rt')
    splitexp = input('Enter the input')
    n=len(splitexp)
    splitexpchararr=list(splitexp)

    splittedstrings=[]
    #Reading lines from file
    doclines = inputdoc.readlines()

    #Split the lines in the document into n columns
    consol=[]
    Nol=1
    for line in doclines:
        noofchars = int(len(line)/len(splitexp))
        splittedstrings = textwrap.wrap(line, noofchars)
        if(len(splittedstrings) > len(splitexp)):
            splittedstrings[n-1:n+1] = [' '.join(splittedstrings[n-1:n+1])]
        while len(splittedstrings) < n:
            splittedstrings.append(' ')
         #======================================================================================
        consol.append(splittedstrings)
        Nol+=1
    splitedexpression = splitexp.split('+')
    oFile = open('Output-2.txt','w+')
    output = ''
    # Combine the splited column as per input and write it in output text file
    for i in splitedexpression:
        for row in range(0,Nol-1):
            for col in i:
                #print(col)
                #print(consol[row][switcher[col]-1])
                temp1=switcher[col]-1
                temp=consol[row][temp1]
                #print(temp)
                output=' '.join([output,temp])
            oFile.write(output+'\n')
            output = ' '
    oFile.close()
            #========================================================================================
            #Merge the columns into given forms to make a new paragraph
            #print([' '.join(x) for x in zip(splittedstrings[splitexparrindex[0]], splittedstrings[1])])
main()





