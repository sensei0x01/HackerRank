myDict = dict()
LengthOfMarks=3
for _ in range(int(input())):# take the total number of students
    #for each line it will take the name ==> studentName and 
    #the marks ==> marks 
    studentName, *marks = input().split()
    # map function will apply the float func on all
    # elements in marks list.
    # studentName is the key of myDict and marks is the value
    myDict[studentName] = list(map(float,marks))

queryName = input()
#
avr = (sum(myDict[queryName])/LengthOfMarks)
avr = "{:.2f}".format(avr)
print(avr)
