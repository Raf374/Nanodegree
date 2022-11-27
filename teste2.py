h=0;
j=0;
k=0;
l=0;
m=0;

h=3;

j=9%2+h;

if(j<5):
    k=3
    l=4
else:
    if(j<10):
        k=6
        l=7
        h=8
    else:
        k=9
        l=10

m=h+k+l*(j-3)

print('h=',h,'j=',j,'k=',k,'l=',l,'m=',m)
