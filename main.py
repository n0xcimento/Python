alph = 'abcdef'
tl = []

def indexFrom(tuplel, key):
    for indx in range(len(tuplel)):
        if tuplel[indx][1] == key:
            return indx

for (a,b) in enumerate(alph):
    tl.append((a,b))

print(tl)

tl[4][0] = 2

if indexFrom(tl, 'e'):
    print(tl[indexFrom(tl, 'e')])
    tl[indexFrom(tl, 'e')][0] -= 2

print(tl)