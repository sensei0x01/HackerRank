#python 3.x

#print_formatted func
def print_formatted(number):
    #Each value should be space-padded to match the width of the binary value
    maxLength=len(f"{number:b}") 
    #loop from 1 to number 
    for i in range(1,number+1):# +1 to include number 
        #:d=>decimal
        #:o=>octal
        #:X=>hex upper-case
        #:b=>binary
        #right justify
        print(f"{i:d}".rjust(maxLength),f"{i:o}".rjust(maxLength),f"{i:X}".rjust(maxLength),f"{i:b}".rjust(maxLength))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)