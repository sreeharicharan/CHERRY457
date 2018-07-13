
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for r in range(lower,upper + 1):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = r
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if r == sum:
       print(r)
