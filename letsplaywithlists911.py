L = [4,5,1,2,9,7,10,0]
print("Original list :,", L)


count = 0

for i in L:
    count = count + i


print("\nsum =", count)

avg = count/len(L)
print("average =",avg)

L.sort()

print("\nSorted list: ",L)

print("\nSmallest element is: ",L[0])
print("\nSmallest element is: ",L[-1])
