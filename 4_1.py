# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:54:58 2017
第四次 非循环子图法（邻接矩阵） 和  贪婪算法（字典）
@author: tideking  
"""
"""
import numpy as np
w='AGTATTGGCAATC'
z='AATCGATG'
u='ATGCAAACCT'
x='CCTTTTGG'
y='TTGGCAATCACT'
seq1=[w,z,u,x,y]
seq2=[w,z,u,x,y]
def get_link(s1,s2):
    l = min(len(s1),len(s2))
    while l>0:
        if s2[:l] == s1[-l:]:
            return l
        else:
            l-=1
    return 0
def overlap(s1,s2):           #将两条序列去除首尾overlap后合并
    weit = get_link(s1,s2)
    s = s1 + s2[weit:]
    #print(s)
    return s
matrix=np.empty(shape=(len(seq1),len(seq2)),dtype=int)
for i in range(len(seq1)):
    for j in range(len(seq2)):
        if i==j:
            matrix[i][j]=0
        else:
            matrix[i][j]=get_link(seq1[i],seq2[j])
print matrix
s=[]
for i in range(len(seq1)):
    if matrix[:,i].tolist()==[0,0,0,0,0]:
        s.append(seq1[i])
        matrix[i,:]=0
#print s
for j in range(len(s)-1):
    s[j+1]=overlap(s[j],s[j+1])
    
print s[4]
"""
w='AGTATTGGCAATC'
z='AATCGATG'
u='ATGCAAACCT'
x='CCTTTTGG'
y='TTGGCAATCACT'
seq1=[w,z,u,x,y]
seq2=[w,z,u,x,y]
def get_link(s1,s2):    #给任意两点赋权值的函数
    l = min(len(s1),len(s2))
    while l>0:
        if s2[:l] == s1[-l:]:
            return l
        else:
            l-=1
    return 0
def overlap(s1,s2):           #将两条序列去除首尾overlap后合并函数
    weit = get_link(s1,s2)
    s = s1 + s2[weit:]
    #print(s)
    return s
def assemble(a):
    if len(a)>1:
        for j in range(len(a)-1):
            a[j+1]=overlap(a[j],a[j+1])
    else:
        a=a
    return a[len(a)-1]    
weight={}
pointst={w:[],z:[],u:[],x:[],y:[]}
maxlist={w:[],z:[],u:[],x:[],y:[]}
for i in range(len(seq1)):           #寻找每个点的最大权值出度
    for j in range(i+1,len(seq2)):
        weight[seq1[i],seq2[j]]=get_link(seq1[i],seq2[j])
        pointst[seq1[i]].append(weight[seq1[i],seq2[j]])
        maxlist[seq1[i]]=max(pointst[seq1[i]])   
#print weight
#print pointst
#print maxlist
keyst=[]        
for i in range(len(seq1)):              #寻找每个点最大权值出度所在的边
    for j in range(i+1,len(seq2)):
        if maxlist[seq1[i]]==weight[seq1[i],seq2[j]]:
            keyst.append([seq1[i],seq2[j],maxlist[seq1[i]]])
#print keyst
for i in range(len(keyst)):       #留每个点最大权值入度所在的边
    for j in range(i+1,len(keyst)):
        if keyst[i][1]==keyst[j][1]:
            if keyst[i][2]>=keyst[j][2]:
                 keyst.pop(j)
            else:
                 keyst.pop(i) 
#print keyst
zero_du=[]                      #将有向图转化为几条通路           
s=[]
for i in range(len(keyst)):
    for j in range(i+1,len(keyst)):
        if keyst[i][0]!=keyst[j][1] and keyst[i][1]!=keyst[j][0] :
            zero_du.append(keyst[i])
        else:
            s1=overlap(keyst[i][0],keyst[i][1])
            s2=overlap(keyst[j][0],keyst[j][1])
            s.append(overlap(s1,s2))
#print zero_du
sq=[]
for i in range(len(zero_du)):
    sq.append(overlap(zero_du[i][0],zero_du[i][1]))
#print sq   
m=assemble(sq) 
n=assemble(s)   
print  '结果：'  ,m+n
        
    

          
            
          
        
        
    
        

          