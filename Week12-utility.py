# 
#Walter Rodenberger
#CSCI 102 - Section A
#Week 12 - Part B

def PrintOutput(str):
    print('OUTPUT ' + str)

def LoadFile(F):
    f = open(F, 'r')
    return f.read().splitlines()

def UpdateString(str1,  str2, n):
    edit = list(str1)
    edit[n] = str2
    PrintOutput(''.join(edit))

def FindWordCount(lis, str1):
    for line in lis:
        liss.append(list(line))
    return liss.count(str1)

def ScoreFinder(lis1, lis2, str1):
    x = 0
    ret = 'player not found'
    while x < len(lis1):
        if(lis1[x].lower() == str1.lower()):
            ret = lis1[x] + ' got a score of ' + str(lis2[x])
        x += 1
    PrintOutput(ret)

def Union(lis1, lis2):
    return lis1 + lis2

def Intersection(lis1, lis2):
    both = []
    for name in lis1:
        for name1 in lis2:
            if(name == name1):
                both.append(name)
    return both

def NotIn(lis1, lis2):
    no = []
    for name in lis1:
        if(not(name in lis2)):
            no.append(name)
    return no
