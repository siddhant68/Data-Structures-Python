# Selection Sort

l = [10, 7, 8, 9, 1, 5]

for i in range(len(l)):
    ind = i
    for j in range(i+1, len(l)):
        if l[ind] > l[j]:
            ind = j
    
    if i != ind:
        l[i], l[ind] = l[ind], l[i]

print(l)

# Bubble Sort

l = [10, 7, 8, 9, 1, 5]

for i in range(len(l)):
    flag = 0
    
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            flag = 1
            l[j], l[j+1] = l[j+1], l[j]
    
    if flag == 0:
        print(i)
        break

print(l)

# Insertion Sort

l = [10, 7, 8, 9, 1, 5]

for i in range(1, len(l)):
    ele = l[i]
    index = i-1
    while l[index] > ele and index >= 0:
        l[index+1] = l[index]
        index -= 1
    
    l[index+1] = ele

print(l)

# Merge Sort

l = [10, 7, 8, 9, 1, 5]

def merge(l, p, q, r):
    l1 = l[p:q]
    l2 = l[q:r+1]
    
    i = 0
    j = 0
    k = p
    
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            l[k] = l2[j]
            j += 1
            k += 1
        else:
            l[k] = l1[i]
            i += 1
            k += 1
            
    while i < len(l1):
        l[k] = l1[i]
        i += 1
        k += 1
    
        
    while j < len(l2):
        l[k] = l2[j]
        j += 1
        k += 1

def mergeSort(l, p, r):
    if p < r:
        q = (p+r) // 2
    
        mergeSort(l, p, q)
        mergeSort(l, q+1, r)
         
        merge(l, p, q, r)

mergeSort(l, 0, len(l)-1)
print(l)

# Quick Sort

l = [10, 7, 8, 9, 1, 5] 

def partition(l, p, r):
    pivot = l[r]
    pos = p-1
    
    for i in range(p, r):
        if l[i] < pivot:
            pos += 1
            l[pos], l[i] = l[i], l[pos]
    
    pos += 1
    l[pos], l[r] = l[r], l[pos]
    return pos
    

def quickSort(l, p, r):
    if p < r:
        q = partition(l, p, r)
        quickSort(l, p, q-1)
        quickSort(l, q+1, r)

quickSort(l, 0, len(l)-1)
print(l)
