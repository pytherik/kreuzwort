from pathlib import Path
from random import randint
# choice, random, shuffle?

path = Path.home()/"words.txt"
sol = []
max_len = 15
with path.open("r") as words:
    for el in words:
        word = el.strip()
        if len(word) > max_len:
            continue
        sol.append(word)
coords = []
for i in range(20):
    row = []
    for j in range(20):
        row.append(".")
    coords.append(row)

##senkwort = []
##senkpos = []
waagwort = []      # liste der Zufallswörter
waagpos = []       # und die Koordinaten dazu

def check_coords(word):
    i = 0
    global posx
    global posy
    while posx + len(word)-1 >= 20:
        posx = randint(0, 17)
        i += 1
        if i > 6:
            return False
    i = 0
    j = 0    
    for letter in range(len(word)):
        if coords[posy][posx + letter] != "." or posx + letter > 19:
            return False
        if (posy +1 <= 19 and coords[posy + 1][posx + letter] != "."):
            i += 1
        if (posy -1 >=  0 and coords[posy - 1][posx + letter] != "."):
            j += 1
        if j == 3 or i == 3:
            return False
    return True
wörter = 0
while wörter < 30:
    posx = randint(0, 17)
    posy = randint(0, 19)
    word = sol[randint(0, len(sol)-1)]
    if check_coords(word):
        i = 0
        posyx = []
        waagwort.append(word)
        for letter in word:
            coords[posy][posx + i] = letter
            posyx.append([posy, posx +i])
            i += 1
        if posx +i <= 19:
            coords[posy][posx + i] = " "
        waagpos.append(posyx)
        wörter += 1

for i in range(20):
    for j in range(20):
        print(coords[i][j],end ="  ")
    print()
    
    
    
    

    
    




    
        
