l=[]
d=int(input('enter a decimal number:'))
while d>=1:
    b_num=d%2
    d=d//2
    l.append(b_num)
l.reverse()
print(l)
