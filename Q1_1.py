name= input ('enter your name ')
l=['ali','ahmad','hasan','sam','sally','deemah','john','karam']
if name in l:
    num = int(input ( 'enter the number of courses '))
    if num > 64:
        print('wrong value')
    elif num==64:
        print ('congratulation '+name+' you are a graduate')
    else:
        print ('good luck '+name+' you are not a graduate')

else:
    print ('sorry '+name+' you are not in list')
