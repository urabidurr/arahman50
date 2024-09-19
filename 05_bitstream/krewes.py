f = open("krewes.txt", "r")
j = f.read()

t = 0
g = j.split("@@@")[:-1]

print(g)

h = []
for hx in g:
    gx = hx.split("$$$")
    print(hx.split("$$$"))
    h.append(gx)

print(h)

dictP = {4: [], 5: []}

for gx in h:
    print(gx[0])
    print(gx)
    if gx[0] == "4":
        dictP[4].append({gx[1]: gx[2]})
    elif gx[0] == "5":
        dictP[5].append({gx[1], gx[2]})
    else:
        print("h")
    
print(dictP)
