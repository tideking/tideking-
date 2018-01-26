#This is a demo for reading sequence files in fasta format. 
#Author: Bin-Guang Ma; Date: 2015-12-12

def readIntoList(filename):
    ifl=file(filename,'rt')
    iflst=ifl.readlines()
    ifl.close()         
    iflstlen=len(iflst)
    seqlist=[]
    aseq = []
    titstr = ''
    seqstr=''
    for i in iflst:
        i = i.strip()
        if i[0]=='>':
            titstr = i
            if seqstr!='':
                aseq.append(pretitstr)
                aseq.append(seqstr)
                seqlist.append(aseq)                
                seqstr = ''
                aseq = []
        else:
            seqstr += i
            pretitstr = titstr
    aseq = [titstr, seqstr] 
    seqlist.append(aseq)
    return seqlist            
   
faflname = 'C:/GCA_001815865.1_ASM181586v1_genomic.fna'

seqlst = readIntoList(faflname)
for s in seqlst:
    print s[0][:15], s[1][:15]

print 'done!(^_^)'
