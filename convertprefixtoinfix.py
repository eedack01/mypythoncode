prefix = '7 * 8 + 9 9'
oldlist= list(prefix.replace(' ',''))
newlist = []
i = 0

while i < len(oldlist):
    i+=1
    if i == len(oldlist):
        i=0
    if oldlist[i].isdigit() or oldlist[i].isalpha():
        newlist.append(oldlist[i])
        oldlist.pop(i)
        if len(oldlist)==0:
            break
        if not oldlist[i-1].isdigit() and not oldlist[i-1].isalpha():
            newlist.append(oldlist[i-1])
            oldlist.pop(i-1)
            i=0
