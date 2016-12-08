#!/usr/bin/python
f=open('./BN/bng-noun.dix')
inp = raw_input('Enter Word:')
p=len(inp)
partbl = f.readlines()
f.close()

for i in range(len(partbl)):
    partbl[i]= partbl[i].split()

i=0
j=0
result =[]
for i in range(len(partbl)):
    if len(partbl[i])>1:
        if partbl[i][1].startswith('lm='):
            if inp==partbl[i][1].split('\"')[1]:
                print partbl[i]
                result+=[partbl[i]]
add1=""
add2=""
found=[]

for i in range(len(partbl)):
    if (len(partbl[i])>0):
            if (partbl[i][0]=="<pardef"):
                if "/" in partbl[i][1]:
                    add1 = partbl[i][1].split('\"')[1].split('/')[0]
                    add2 = partbl[i][1].split('/')[1].split('_')[0]
                else:
                    add1 = partbl[i][1].split('\"')[1].split('_')[0]
                    add2=""
                word=add1+add2
                #print word
                if(word==inp):
                    j=i
                    for j in range(i+1, len(partbl)):
                        if (partbl[j][0] == '</pardef>'):
                            break
                        add = partbl[j][0].split('>')[3].split('<')[0]
                        rem = partbl[j][0].split('>')[-1].split('<')[0]
                        #print rem
                        if(len(rem)>0):
                            form = inp[:-len(rem)]+add
                        else:
                            form = inp+add
                        if (partbl[j][0] != '</pardef>') :
                            print form


if len(result)>0:
    print 1

# To create paradigm tables for words which are not found in our dictionary.
else:
    lchar = inp[-1]
    print lchar
    nfpt = []   #not found 'in' paradigm table
    for i in range(len(partbl)):
        if (len(partbl[i])>0):
            if (partbl[i][0] == '<pardef') :
                j=i
                #root = partbl[i][1].split("\"")[1].split('/')[0].split('_')[0]
                root = partbl[i][1].split("\"")[1]
                print root
                search = partbl[i][1].split("\"")[1]
                if lchar==search.split('_')[0][-1]:
                    nfpt+=[[root]]
                    for j in range(i+1,(len(partbl))):
                        if (len(partbl[j])>0):
                            if (partbl[j][0] == '</pardef>') :
                                break
                            add = partbl[j][0].split('>')[3].split('<')[0]
                            rem = partbl[j][0].split('>')[-1].split('<')[0]
                            if(len(rem)>0):
                                form = inp[:-len(rem)]+add
                            else:
                                form = inp + add
                            nfpt[-1]+=[form]
                            #print root+partbl[j][0].split('>')[3].split('<')[0]

#    print nfpt
    print
    for par in nfpt:
        par.append(0)
        for wform in par[1:-1]:
            g=open('../dataset.txt')
            lines=g.readlines()
            g.close()
            for line in lines:
                if wform==line.strip('\n'):
                    par[-1]+=1
    max=0
    pmax=[]
    for par in nfpt:
        if(par[-1]>max):
            max=par[-1]
            pmax=par
        elif(par[-1]==max):
            pmax.append(par)
    print 
    print pmax  
    print pmax[0][0]        
    X=inp
    x=open('./BN/bng-noun.dix','r')
    mines=x.readlines()
    x.close()
    for m in range(len(mines)):
        if "</section>" in mines[m]:
            r=mines[m]
            ll=m
            for i in range(len(pmax)):
                Y=pmax[i][0]
                Z=pmax[i][0]
                S="<e lm=\""+X+"\"><i>\""+Y+"\"</i><par n=\""+Z+"\"/></e>"
                mines.insert(ll,S)
                ll=ll+1   
            line=ll     
            
    #mines.insert(line,r)
    #mines.insert(line+1,"</dictionary>")        
    x1=open('./bng.dix','w')
    x1.writelines(mines)
    x1.close()      
