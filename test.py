import string
import random
from readwrite import write_csv
import time

def randstr(l):
    letters = string.ascii_lowercase
    out = ''.join(random.choice(letters) for i in range(l))
    return out


n = 10**5
l = 5


t1 = time.time()

names = []
for i in range(n):
    names.append((randstr(l), randstr(l)))

t2 = time.time()

write_csv("in.csv", names)

t3 = time.time()

print("Generiranje...", t2 - t1)
print("Zapisovanje...", t3 - t2)