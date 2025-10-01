from wordhoard import Homophones
import random as r

print("What string do you want Old Man Joe to recite?")
my_string = str(input())
new_string = ""
print("\n\n\nYou say \'" + my_string + "\' to Old Man Joe...\n\n\n")

for word in my_string.split():
    print("He thinks about " + word + "...")
    result = Homophones(search_string=word).find_homophones()
    if result != None:
        splitRes = result[0].split()
        word = splitRes[-1]
    
    new_string += word + " "

print("\n\n\n\"WHAT? YOU SAID...\"\n")
print("-----------------------------------")
print(new_string + "???")
print("-----------------------------------")
print("\n\"WHAT THE HELL DOES THAT EVEN MEAN?\"\n")