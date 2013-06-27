import numpy

def Floida(M):
    l = len(M)
    R =M
    P = numpy.zeros((l,l),'int')
    for i in range(l):
        for j in range(l):
            if M[i][j] != 0:
                P[i][j] = j
    for k in range(l):
        for i in range(l):
            for j in range(l):
                empty = R[i][j] == 0
                be_min = R[i][j] > R[i][k] + R[k][j]
                not_empty1 = R[i][k] != 0
                not_empty2 = R[k][j] !=0
                inequality = i != j
                if (empty or (be_min and not_empty1 and not_empty2)) and inequality: 
                    P[i][j] = k
                if be_min:
                    R[i][j] = R[i][k] + R[k][j]         
        return(R,P)

def longpath(lon, p):
    l=len(lon)
    w = 0
    for i in range(l):
        for j in range(l):
            if lon[i][j] > w:
                w = lon[i][j]
                v = i
                u = j
    short_path(p, v, u)
    print v,u

def short_path(P, v,u):
        if P[v][u] <> -1:   
            t = v
            path = str(t+1)
            while t != u:
                t = P[t][u]
                path = path + '->' +str(t+1)
            print path
        else:
            return 'error'
    
def fileimport(name):
    s=open(name, 'r').read()
    l=len((open(name).readline()).split(" "))
    les=len(s)
    M=numpy.zeros((l,l),"int")
    S=''
    n=0
    i=0
    j=0
    while n< len(s):
        if not(s[n]==' ') and not (s[n]=="\n"):
            S+=str(s[n])
        elif (s[n]==' ') and not(s[n+1]=="\n"):
            M[j][i]=(int(S))
            i+=1
            S=''
        elif (s[n]=="\n"):
            M[j][i]=(int(S))
            i=0
            j+=1               
            S=''
        n+=1
    print "Complete"
    return(M)

def print_for_graphviz(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i][j] != 0:
                print i+1,'->',j+1 ,'[label=',n[i][j],']'   

def write(N,filename):
    f=open(filename,'w')
    for i in range(len(N)):
        f.write('\n')
        for j in range(len(N)):
            f.write(str(N[i][j]))
            f.write(' ')
