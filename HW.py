'''
1) 1 3 5 7 9
2) 2 4 6 8 10
3) 1 3 6 8 10
4) 1 4 9 16 25
5) 1 * 3 * 5
6) 1*
   2**
   3*
   4**
   5*
7)12345
  12345
  12345
  12345
  12345

8)54321
  54321
  54321
  54321
  54321

9)11111
  22222
  33333
  44444
  55555

10) 1*3*5
    1*3*5
    1*3*5
    1*3*5
    1*3*5

11)1
   12
   123
   1234
   12345
'''


#1
print('Excercise 1\n')
x=1
while x<10:
    print(x)
    x+=2

print(" ")
print('Excercise 2\n')
#2
x=2
while x<10:
    print(x)
    x+=2
    
print(" ")
print('Excercise 3')
#3
x=1
y=1
while x<16:
    print(x)
    y+=1
    x+=y
    

print(" ")
print('Excercise 4\n')

#4   
x=1
while x<=5:
    print(x**2, end=" ")
    x+=1
    

#2nd method
x=0
y=1
while  x<25:
    x=x+y
    print(x, end=" ")
    y+=2

print(" ")
print('Excercise 5\n')
#5

x=1
while x<=5:
    if x<5:
        print(x,end=" * ")
    else:
        print(x)
    print()
    x+=2

print(" ")
print('Excercise 6\n')
#6

x=1
while x<= 5:
    if x%2==0:
        print(f"{x}**")
    else:
        print(f"{x}*")
    x+=1

print(" ")
print('Excercise 7\n')
#7

x=1
while x<=5:
    y=1
    while y <=5:
        print(y,end="")
        y+=1
    print()
    x+=1

print(" ")
print('Exercise 8\n')
#8

x=1
while x<=5:
    y=5
    while y >=1:
        print(y,end="")
        y-=1
    print()
    x+=1

print(" ")
print("Excercise 9 \n")
#9

x=1
while x<=5:
    y=1
    while y <=5:
        print(x , end=" ")
        y+=1
    print()
    x+=1

print(" ")
print("Excercise 10 \n")
#10

x=1
while x <=5:
    y =1
    while y <=5:
        if y <5:
            print(y,end="*")
        else:
            print(y,end="")
        y+=2
    print()
    x+=1


print(" ")
print("Excercise 11 \n")
#11

x=1
while x <=5:
    y=1
    while y<=x:
        print(y,end="")
        y+=1
    print()
    x+=1

print(" ")
