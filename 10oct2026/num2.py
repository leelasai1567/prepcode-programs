num=12345
reversed=0

while(num>0):
    last_value=num%10
    num=num//10


reverse=(reversed+num)*10


print(reverse/10)   