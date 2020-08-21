# Stack or Queue in list

l = [1, 2, 3]

l.append(4)
l.pop()
print(l)

l.append(4)
l.pop(0)
print(l)
###################################################################

# Sorting objects

l = [['s', 1 , 2, 3], ['o', 4, 5, 6], ['r', 4, 5, 7]]

l.sort(key=lambda x: sum(x[1:])/(len(x)-1), reverse=True)

print(l[0][0])

###################################################################

# arranging zeros and ones

l = [0, 0, 0, 0, 1, 1, 0, 1, 0]

prev = -1
ptr = -1
for i in range(len(l)):
    if l[i] < 1:
        ptr += 1
        l[ptr], l[i] = l[i], l[ptr]

print(l)

##################################################################

# particular sum out of two arrays

l1 = [0, 3, 4, 6, 11, 17, 19]
l2 = [1, 5, 7, 8, 13]

ctr = 0

s = 18

i = 0
j = len(l2)-1

while i < len(l1) and j >= 0:
    if l1[i] + l2[j] > s:
        j -= 1
    elif l1[i] + l2[j] < s:
        i += 1
    else:
        print(l1[i], l2[j])
        ctr += 1
        i += 1
        j -= 1

print(ctr)
    









        