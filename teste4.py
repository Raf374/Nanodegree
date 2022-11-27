h=0;
j=0;
k=0;
l=0;
m=0;

h=3;
j=10//h;

if(j<5):
    k=3**h
    l=5-h
else:
    if(j<=10):
        k=4*h
        l=8/h
        h=8

m=k%l+h+j

print(h, j, k, l, m) 
