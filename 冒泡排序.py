def iny(ss):
    for j in range(len(ss)):
        for i in range(len(ss)-1):
            if ss[i]<ss[i+1]:
                ss[i],ss[i+1]=ss[i+1],ss[i]
    print(ss)   
lin1=[12,0,10,9,8,-1,21,-6]
iny(lin1)
