import random as r
special_characters=["!","@","#","$","&","_"]
password=""
n=int(input("Enter the length of the password"))
for i in range(n):
    choice=r.randint(1,4)
    if choice==1:
        password+=chr(r.randint(65,90))
    elif choice==2:
        password+=special_characters[r.randint(0,len(special_characters)-1)]
    elif choice==3:
        password+=chr(r.randint(97,122))
    else:
        password+=str(r.randint(0,9))
print("Generated password is:",password)
