from collections import Counter, defaultdict

#return the duplicate items
def getting_duplicates(data):
    count= Counter(data)
    return [key for key in count.keys() if count[key]> 1]

#return the list of duplcate index idems

def duplicates_index(data):
    duplicate, index= getting_duplicates(data), defaultdict(list)
    for i, d in enumerate(data):
        if d in duplicate: index[d].append(i)
    return index

#check whether list is present in a another list in same order

def contains(listA, listB):
  for i in range(len(listB) - len(listA) + 1):
    if listA == listB[i:i+len(listA)]: return True
  return False



#calculate orbit and basin coverage
def orbit(finalStates):
    orbits=[]
    print('\nORBIT DATA answer for 1.(c)\n')

    for states in finalStates.values():
        duplicate=duplicates_index(states)
        for value in duplicate.values():
            s=states[value[0]:value[1]+1]
            if s not in orbits:
                orbits.append(s)

    #find the basins
    for s in orbits:
        basin=[]
        i=0
        for keys in finalStates.keys():
            if contains(s,finalStates[keys])==True:
                basin.append(keys)


        print('Orbit=',s[0:-1])
        print('len of orbit=',len(s)-1)
        print('Basin=',basin)
        print('relative coverage=',(len(basin)/32*100),'%\n')