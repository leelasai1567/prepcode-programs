string=input("enter a string")
vowels=0
characters=0
special=0
for ch in string:
    if ch in "aeiouAEIOU":
        vowels+=1
    elif ch.isalpha():
        characters+=1
    elif not ch.isdigit()and ch!=" ":
        special+=1


print("vowels:",vowels)
print("charactres:",characters)
print("special characters:",special)      


