s=input(("enter a string"))

vowels=0
digits=0

for ch in a s:
    if ch.lower() in "AEIOU":
        vowel +=1
    elif ch.isdigit():
        digits +=1

print("vowels:",vowels)
print("digits:",digits)         
