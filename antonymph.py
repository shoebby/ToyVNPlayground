from wordhoard import Antonyms
import random as r

print("What string do you want to give to the Antonymph")
my_string = str(input())
new_string = ""
print("\n\n\nShe's doing... Something to \'" + my_string + "\'...\n\n\n")

for word in my_string.split():
    print("Bewitching " + word + "...")
    results = Antonyms(search_string=word, output_format='list').find_antonyms()

    if results != None:
        target = r.randint(0, len(results) - 1)
        word = results[target]
    
    new_string += word + " "

print("\n\n\nThe Antonymph has finished!")
print("-----------------------------------")
print(my_string)
print("V")
print(new_string)
print("-----------------------------------")
print("\nYou should probably say thanks...\n")