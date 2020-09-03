# Calculating max profit path

grid = [[0, 8, 4, 0, 5],
        [0, 4, 5, 0, 0],
        [1, 0, 0, 0, 20]]

def mpp_rec(grid, x, y, c, profit):
    if x == 0 and y == c:
        return profit + grid[x][y]
    
    if x-1 < 0:
        return mpp_rec(grid, x, y+1, c, profit+grid[x][y])
    
    if y+1 > c:
        return mpp_rec(grid, x-1, y, c, profit+grid[x][y]) 
    
    return max(mpp_rec(grid, x-1, y, c, profit+grid[x][y]),
               mpp_rec(grid, x, y+1, c, profit+grid[x][y]))

def mpp(grid):
    return mpp_rec(grid, len(grid)-1, 0, len(grid[0])-1, 0)

print(mpp(grid))
        
###############################################################################

# Longest Increasing Susbsequence

l = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 6]

def lis(l):
    lis_n = [1] * len(l)
    
    for i in range(1, len(l)):
        for j in range(0, i):
            if l[i] > l[j] and lis_n[i] < lis_n[j] + 1:
                lis_n[i] = lis_n[j] + 1
    
    return max(lis_n)
                    
print(lis(l))

###############################################################################

# Minimum Sum Partition

def msp(l, n, summ):
    if n < 0:
        return summ
    
    return min(msp(l, n-1, abs(summ-(2*l[n]))),
               msp(l, n-1, summ))
    
for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    d = msp(l, n-1, sum(l))
    print(d)
    
###############################################################################

# Treasure and Cities

a = -5 
b = 7
treasure = [4, 8, 2, 9]
color = [2, 2, 3, 2]

def tac(treasure, color, a, b, profit, n, prevC):    
    if n == len(treasure):
        return profit
    
    if prevC != color[n]:
        return max(tac(treasure, color, a, b, profit+(b*treasure[n]), n+1, color[n]),
                   tac(treasure, color, a, b, profit, n+1, prevC))
    else:
        return max(tac(treasure, color, a, b, profit+(a*treasure[n]), n+1, color[n]),
                   tac(treasure, color, a, b, profit, n+1, prevC))
        
print(tac(treasure, color, a, b, 0, 0, 0))
        
###############################################################################

# Number of Subset Sum Problem

l = [5, 10, 12, 13, 15, 18]
s = 30

def nssp(l, s, n):
    if s == 0:
        return 1
    
    if n < 0:
        return 0
    
    if l[n] > s:
        return nssp(l, s, n-1)

    return nssp(l, s-l[n], n-1) + nssp(l, s, n-1)

print(nssp(l, 30, len(l)-1))

###############################################################################

# Subset Sum Problem

l = [3, 34, 4, 12, 5, 2]

s = 9

# DP
mat = [[False] * (s+1) for i in range(len(l))]

def ssp(l, mat):
    for i in range(len(mat)):
        mat[i][0] = True
        
    for i in range(1, len(mat[0])):
        mat[0][i] = False
        
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if l[i] > j:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j] or mat[i-1][j-l[i]]
    return mat[len(l)-1][s]

print(ssp(l, mat))

# Recursion

def ssp(l, s, n):
    if s == 0:
        return True
    
    if n < 0:
        return False
    
    if l[n] > s:
        return ssp(l, s, n-1)
    
    return ssp(l, s-l[n], n-1) or ssp(l, s, n-1)

print(ssp(l, s, len(l)-1))
    
###############################################################################

# Form Biggest number

l = [1, 34, 3, 98, 9, 76, 45, 4]

for i in range(len(l)):
    l[i] = str(l[i])

print(l)

l = ''.join(l)
''.join(sorted(l, reverse=True))

###############################################################################

# First non-repeating character

s = "geeksforgeeks"

d = {}

for i in s:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

for i in s:
    if d[i] == 1:
        print(i)
        break

###############################################################################

# 0-1 Knapsack

# Bottom-Up Dp



# Recursion

wt = [2, 7, 3, 4]
value = [5, 20 , 20, 10]
capacity = 11

def ks(wt, value, profit, capacity, n):
    if n < 0 or capacity == 0:
        return profit
    
    if wt[n] > capacity:
        return ks(wt, value, profit, capacity, n-1)
    
    return max(ks(wt, value, profit+value[n], capacity-wt[n], n-1),
               ks(wt, value, profit, capacity, n-1))
    
print(ks(wt, value, 0, 11, len(wt)-1))

###############################################################################

# Stairs

# Recursion O(k^n)

def nos(n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    return nos(n-1) + nos(n-2) + nos(n-3)

print(nos(4))

# Bottom Up DP O(k*n)

def nos(n, k):
    l = [0] * (n+1)
    
    l[0] = 1
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i-j >= 0:
                l[i] += l[i-j]
    
    return l[n]

print(nos(4, 3))

###############################################################################

# Number of Coins

l = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
v = 93

def noc(l, v, count, n, sol):
    if v == 0:
        return count, sol
    
    if v < l[n]:
        return noc(l, v, count, n-1, sol)
    
    count += 1
    sol.append(l[n])
    return noc(l, v-l[n], count, n, sol) 

print(noc(l, v, 0, len(l)-1, []))

###############################################################################

# Union Find
l = [0, 1, 2, 3, 3, 4, 4, 2]

parent = [-1] * (max(l)+1)

def findRec(v, source, parent, count):
    if parent[v] > 0:
        count += 1
        return findRec(parent[v], source, parent, count+1)
    else:
        if count > 1:
            parent[source] = v
        return v

def find(v):
    return findRec(v, v, parent, 0)

def union(p1, p2):
        if parent[p1] <= parent[p2]:
            parent[p1] += parent[p2]
            parent[p2] = p1
        else:
            parent[p2] += parent[p1]
            parent[p1] = p2

flag = 0
for i in range(0, len(l)-1, 2):
    if find(l[i]) == find(l[i+1]):
        print(find(l[i]), find(l[i+1]))
        print('Detected')
        flag = 1
        break
    else:
        union(find(l[i]), find(l[i+1]))
    
if flag == 0:
    print('Not Detected')
###############################################################################

# Rat Maze Problem Backtracking

mat = [[1, 0, 0, 0]
       [1, 1, 0, 1]
       [0, 1, 0, 0]
       [1, 1, 1, 1]]

n = len(mat)

def pathPossible(mat, x, y):
    if mat[x][y] == 1 and x<n and y<n:
        return True
    
    return False

def rm(mat, x, y):
    if x == n and y == n:
        return True
    
    if pathPossible(mat, x, y+1):
        rm(mat, x, y)
        
    if pathPossible(mat, x+1, y):
        rm(mat, x, y)
        

###############################################################################

# N-Queens Backtracking

n = 6
mat = [['_'] * n for i in range(n)]
ctr = 0

def isSafe(mat, row, column):
    i = row-1
    while i >= 0:
        if mat[i][column] == 'Q':
            return False
        i -= 1
    
    i = row-1
    j = column-1
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i -= 1 
        j -= 1
    
    i = row-1 
    j = column+1
    while i >= 0 and j < n:
        if mat[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True
    
def nq(mat, row):
    global ctr
    
    if row == n:
        for i in mat:
            for j in i:
                print(j, sep=' ', end=' ')
            print()
        print('\n----------------------\n')
        
        ctr += 1
        return 
    
    for i in range(n):
        if isSafe(mat, row, i):
            mat[row][i] = 'Q'
            nq(mat, row+1)
            mat[row][i] = '_'

nq(mat, 0)
print(ctr)
            
###############################################################################

# Subset Sum Problem Backtracking

l = [3, 34, 4, 12, 5, 2]
s = 30

def ssp(l, n, s):
    if s == 0:
        return True
    
    if n < 0 and s != 0:
        return False
    
    if l[n] > s:
        return ssp(l, n-1, s)
    
    return ssp(l, n-1, s-l[n]) or ssp(l, n-1, s)

print(ssp(l, len(l)-1, s))
