x=int(input("Enter any number: "))
r=list(map(int,str(x)))
s=list(map(lambda x:x**3,r))
if(sum(s)==x):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
