x,y=input().split()
a=int(x)
b=float(y)
c=b-a-0.50
if (a%5!=0 or b-(a+0.50)<0):
    print("{0:.2f}".format(b))
else:
    print("{0:.2f}".format(c))
