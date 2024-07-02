import glob
import os
import numpy as np
from copy import copy, deepcopy
import sys

#open segmented words file done by Morfessor
file_list = glob.glob(os.path.join(os.getcwd(), "t1.txt"))
#file_list = open("t1.txt", "r",'utf8')

corpus = []

for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.read())
        
        for line in corpus:
            corpus=line.split(",")


corpus=np.matrix(corpus)
print(corpus.shape)

#print(corpus)

corpus=corpus.reshape(400,5,)

#print(corpus)
#print(corpus.shape)
#print(corpus[1,2])
matrix2 = corpus.tolist()

#print(matrix2)

#open the illegal morphemes list file
list2=[]
with open('l1.txt','r','utf8') as f:
    for line in f:
        for word in line.split():
            list2.append(word)
    #print(w)
        
output = []
for row in matrix2:
    new_row = [any(value in list2 and ' ' in element for value in element.split()) for element in row]
    output.append(new_row)
#print(output)
output = np.array(output,dtype=np.int)

#print(output)
a=[]
a=output
a = np.array(a,dtype=np.int)
matrix2=np.array(matrix2,dtype=np.str)
#print("a=",a)
#print("matrix=",matrix2)

b = deepcopy(a)
#print(b)

ia=[]
ja=[]
for count_i, value in enumerate(b):
    for count_j, value in enumerate(value):
        
        #print(count_i,count_j, value)
        if b[count_i][0] == 0:
                x=matrix2[count_i][0]
                #ia.append(x)
                
        elif b[count_i][0]== 1 and b[count_i][1]==0:
                x=matrix2[count_i][1]
                #ia.append(x)
            
        elif b[count_i][0]==1 and b[count_i][1]==1 and b[count_i][2]==0:
                x=matrix2[count_i][2]
        
        elif b[count_i][0:2]==1 and b[count_i][3]==0:
                x=matrix2[count_i][3]
                
        elif b[count_i][0:3]==1 and b[count_i][4]==0:
                x=matrix2[count_i][4]
        
        elif b[count_i][0:4]==1:
             x=matrix2[count_i][0]
    
    ia.append(x)
                     
#print(ia)

sys.stdout = open('output.txt','wt','utf8')
print(ia)