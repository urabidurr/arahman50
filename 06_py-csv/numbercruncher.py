#Abidur Rahman
#AMA
#SoftDev
#K06 -- Read from file, return job class based on specified percentage in data set
#Time spent: 0.2


fCVS = open("occupations.csv")

stf = fCVS.read().strip()


def createDict(text):
    #print(text)
    l = text.split("\n")
    #print(l)
    
    dicts = {}
    pair = []
    
    for i in l:
        if i[0] == '"':
            pair = i.split('",')
            pair[0] = pair[0][1:]
            print(pair)
            dicts[pair[0]] = pair[1]
    
    print(dicts)
            
        
        
    #print(dicts)
    
createDict(stf)