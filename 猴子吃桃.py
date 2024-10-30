'''a=1434
b=int(input())
if(a>=10 and a<50 or b>a and b>=30 and "3" in str(a)):
    print(a)'''
a=1

for i in range(9):
    a=(a+1)*2
    print(a)
print("小猴子第一天一共摘了{}个桃子".format(a))
