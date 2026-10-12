num=12345
reversed=0

while(num>0):
    last_value=num%10
    num=num//10
    reversed=(reversed*10)+last_value
    print(reversed)

 