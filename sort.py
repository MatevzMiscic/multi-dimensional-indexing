
def sort(A, B, orient, direc):
    n = len(A)
    m = n // 2
    if n == 1:
        return [0]
    if n == 0:
        return []
    #print("A =", A)
    #print("B =", B)
    C = []
    d = [-1, 1, 1, -1]
    o = [0, 0, 0, 2]
    flagA = [1 for _ in range(n)]
    flagB = [1 for _ in range(n)]
    for i in range(m):
        flagA[A[i]] = 0
        flagB[B[i]] = 0
    Asub = [[], [], [], []]
    Bsub = [[], [], [], []]
    for i in range(n):
        a = A[i]
        j = 2 * flagA[a] + (flagA[a] + flagB[a]) % 2
        Asub[j].append(a)
        b = B[i]
        j = 2 * flagA[b] + (flagA[b] + flagB[b]) % 2
        Bsub[j].append(b)
    for i in range(4):
        idx = (orient + direc*i) % 4
        mapToDense = [-1 for _ in range(n)]
        mapToSparse = [0 for _ in range(len(Asub[idx]))]
        for u in Asub[idx]:
            mapToDense[u] = 1
        count = 0
        for j in range(n):
            if mapToDense[j] == 1:
                mapToDense[j] = count
                mapToSparse[count] = j
                count += 1
        A2 = [mapToDense[a] for a in Asub[idx]]
        B2 = [mapToDense[b] for b in Bsub[idx]]
        C2 = sort(A2, B2, orient + o[i], direc * d[i])
        for c in C2:
            C.append(mapToSparse[c])
    #print("C =", C)
    return C




def sort2(names):
    n = len(names)
    list1 = [(a, i) for i, (a, _) in enumerate(names)]
    list2 = [(b, i) for i, (_, b) in enumerate(names)]
    A = [i for _, i in sorted(list1)]
    B = [i for _, i in sorted(list2)]
    C = sort(A, B, 0, 1)
    order = [names[i] for i in C]
    out = [(a, b, i) for i, (a, b) in enumerate(order)]
    return out
    




"""
A = [3, 1, 6, 0, 2, 4, 5]
B = [3, 0, 4, 6, 2, 1, 5]
AB = zip(A, B)
print(sort(A, B, 0, 1))
"""


n = 4
names = []
for i in range(n):
    for j in range(n):
        names.append((i, j))
#print(names)
#print(sort2(names))