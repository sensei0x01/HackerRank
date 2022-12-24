arr=list()

def insert(line):
    arr.insert(int(line[0]),int(line[1]))

def print_arr(line):
    print(arr)

def remove(line):
    arr.remove(int(line[0]))

def append(line):
    arr.append(int(line[0]))

def sort(line):
    arr.sort()

def pop(line):
    arr.pop()

def reverse(line):
    arr.reverse()

dispatcher={
    "insert":insert,
    "print": print_arr,
    "remove": remove,
    "append": append,
    "sort": sort,
    "pop": pop,
    "reverse": reverse
}

def call_func(func,line):
    try:
        return dispatcher[func](line)
    except:
        return "Invalid function"


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        func,*line=input().split()
        call_func(func,line)