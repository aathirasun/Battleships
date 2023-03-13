list=((1," ",3),(1," ",3))
x=''
for i in list:
    print(i)
    for j in i:
     x+=str(j)
    x+='\n'
print(x)

l=[]
j=0
l=x.split('\n')
print(l)