from orbits import orbit


class B_Network:

    def __init__(self):
        self.B_Network={}


        #read the data and create a object of class gene for each gene
        data =["A a B",
               "B i A",
               "B i D",
               "C a A",
               "C a D",
               "D a C",
               "E a D",
               "E a E",]
        for line in data:
            line=line.split()

            #check whether the gene is already in the list or not
            if line[0] not in self.B_Network.keys():
                self.B_Network[line[0]]=gene(line[0])
            if line[2] not in self.B_Network.keys():
                self.B_Network[line[2]] = gene(line[2])

            #check and save the effect of partner protein
            if line[1]=='a':
                self.B_Network[line[2]].List_a.append(self.B_Network[line[0]])
            else:
                self.B_Network[line[2]].List_i.append(self.B_Network[line[0]])



    def simulate(self):

        for gene in self.B_Network.values():
            activate=0
            for g in gene.List_a:
                if g.current=='1':
                    activate+=1
# check the current status of genes which inhibit this particular gene
            inhibit=0
            for g in gene.List_i:
                if g.current=='1':
                    inhibit+=1

#check whether this gene going to be activate or inhibit in the next iteration
            if activate>3*inhibit:
                gene.next='1'
            else:
                gene.next='0'
            #print(inhibit)
#change the current status of genes based on above results
        for gene in self.B_Network.values():
            gene.current=gene.next
            gene.next='0'

    #return the current status of the gene in interger form
    def currentStatus(self):
        i_value=[]

        sortedKeys = sorted(b.B_Network.keys())
        #Get the current state of each gene
        for key in sortedKeys:
            i_value.append(self.B_Network[key].current)
        #convert the list of binary into string and reversed it
        i_value=''.join(str(e) for e in i_value)[::-1]
        i_value=int(i_value,2)
        return i_value
       # print(i)

#store the gene data
class gene:

    def __init__(self,id):
        self.id=id
        self.List_a=[]   #list of genes which activate this gene
        self.List_i=[]   #list of genes which inhibit this gene
        self.current=0  #current state of gene
        self.next=0     #next state of gene

#to get initial state and the sequence
def iterator(initialStates):
    final_states = {}
    for i in initialStates:
        final_states[i] = []
        # convert integer into binary and reverse it.
        initial = list('{0:06b}'.format(i)[::-1])

        # sort the keys
        sortedKeys = sorted(b.B_Network.keys())

        # Assign the initial state
        i_value = 0
        for key in sortedKeys:
            b.B_Network[key].current = initial[i_value]
            i_value += 1

        final_states[i].append(b.currentStatus())
        c = True
        # simulate the network
        while (c == True):
            b.simulate()
            if b.currentStatus() in final_states[i]:
                final_states[i].append(b.currentStatus())
                break
            else:
                final_states[i].append(b.currentStatus())
    return final_states


b=B_Network()
initialStates=[7,13,17,23]
finalStates=iterator(initialStates)
print('Answer for 1.(b)\n')
for key in finalStates.keys():
    print('\nSequence for initial state=',finalStates[key])
initialStates=range(0,32)
finalStates=iterator(initialStates)
orbit(finalStates)



