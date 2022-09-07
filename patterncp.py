r = int(input("enter row no "))
x= r
y= r
for out in range(1,r+1):
    for inn in range(1,r*2):
        if(inn>x and inn<y):
            print(" ", end=" ")
        else:
            print("*",end=" ")
    x-=1
    y+=1
    print("\r")

for out in range(1,r+1):
    for inn in range(1,r*2):
            if (inn<=out or inn>=r*2-out):
                print("*",end=" ")
            else:
                print(" ", end=" ")
    print("\r")

k=0
for i in range(1,r+1):
    for space in range(1,(r-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("*",end=" ")
        k+=1
    k=0
    print()