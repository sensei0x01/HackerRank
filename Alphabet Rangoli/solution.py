# number of rows = (n*2)-1
# number of columns = (n*4)-3

import string
def print_rangoli(size):
    # your code goes here
    
    alpha=string.ascii_lowercase #string contains all the alphapet

    line=[]
    for i in range(size): #assume size=5

        #Create the row's string from the max alpha line to the lowwest one
        s="-".join(alpha[i:size]) # for first iteration  s = a-b-c-d-e
        
        # add the left half of the line
        s=(s[::-1]+s[1:]).center(size*4-3,"-") # for first e-d-c-b-a-b-c-d-e
        
        #list contains the lines string
        line.append(s)

    # after this loop line content is 
    # ['e-d-c-b-a-b-c-d-e', '--e-d-c-b-c-d-e--', '----e-d-c-d-e----', '------e-d-e------', '--------e--------']
    
    #we have all lines pattern in this list 
    print("\n".join(line[::-1]+line[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)