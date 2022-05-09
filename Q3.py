import json
q = {}   #Questions
s = 0   #score
num =1   #number of questions
a= open("q.json",'r')
q = json.load(a)
a.close()
name= input("please enter your full name:")
print("welcome" , name , "to your Quiz")
print("writ t or f")
for qu in q.keys():
    print("Q",num,qu)
    res= input("the answer is")
    if res.upper()==q[qu].upper():
        s=s+1
        print("very good")
        num=num+1
    else:
        print("wrong answer")
        num=num+1

    result={name:s}
    f= open("score.txt",'w')
    result=json.dump(result,f)
    f.close()
