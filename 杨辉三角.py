n=[1]
for i in range(10):
    print(n)
    n.append(0)
    n=[n[k]+n[k-1] for k in range(i+2)]
