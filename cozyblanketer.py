from wordhoard import Hypernyms
import random as r

print("What string do you want to pull through the Blanket Fort?")
my_string = str(input())
new_string = ""
print("\n\n\nPushing \'" + my_string + "\' through the blankets and pillows...\n\n\n")

for word in my_string.split():
    print("Wrapping " + word + "...")
    results = Hypernyms(search_string=word, output_format='list').find_hypernyms()
    print(results)
    if results != None:
        if len(results) > 0:
            target = r.randint(0, len(results) - 1)
            word = results[target]
    
    new_string += word + " "

print("\n\n\nIt made it out!")
print("-----------------------------------")
print(my_string)
print("V")
print(new_string)
print("-----------------------------------")
print("\n... And it's very warm and soft!\n")