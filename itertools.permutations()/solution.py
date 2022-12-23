#python 3.x

from itertools import permutations
myList=[]

# split the input into string and number ex: HACKER 2 => string=HACKER , number=2
string, number = input().split()

#the string and number variables entered to permutations func
#the output of this function is an permutations opject
#list func will convert it to list and after that it will extended to myList
myList.extend(list(permutations(string, int(number))))

#sort the list alphbeticly
myList.sort()

#apply the join method of all list elements
#and print it line by line
print(*map(lambda x:"".join(x),myList),sep='\n')




