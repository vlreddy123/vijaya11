#sum of digits
n=int(input('enter the number:'))
i=0
while n!=0:
    i=i+n%10
    n=n//10
    print('sum of digits are',i)
    
    
output:
enter the number:963
sum of digits are 3
sum of digits are 9
sum of digits are 18
