n= int(input('enter your number - '));
x=0;y=0;
import pascal as ps
arr=ps.arr;
while x<n:
    while y<2*n:
        if arr[x][y]==0:
            print('   ');
        else:
            print(arr[x][y]);
        y=y+1;
    x=x+1;