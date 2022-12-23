# python 3.x

#Take input x, y, z, and n.
x, y, z, n = int(input()), int(input()), int(input()), int(input())

#Create 2d list [[a1,b1,c1],[a2,b2,c2],...] where a, b, and c count 0=> x, y, and z respectively.
#if  a + b + c = n don't add this list to the big one 
print([ [a, b, c] for a in range(0, x+1) for b in range(0, y+1)
    for c in range(0, z+1) if a + b + c != n ]) 
