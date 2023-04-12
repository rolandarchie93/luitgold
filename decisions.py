import random

number = random.randint(0,10)

print(number)

thresh = 5

if(number > thresh):
    print("Big number")
elif(number < 5): # else if
    print("Small number")
else: # elif(number == 6):
    print("Number is", str(thresh))