from wordhoard import Synonyms
import random as r

print("What string do you want to thesaurize")
my_string = str(input())
new_string = ""
print("Thesaurizing \'" + my_string + "\'!\n\n\n")

for word in my_string.split():
    print("Digesting " + word + "...")
    results = Synonyms(search_string=word, output_format='list').find_synonyms()
    print("Found " + str(results))

    if results != None:
        target = r.randint(0, len(results) - 1)
        word = results[target]
    
    new_string += word + " "
    print("Progress: " + new_string + "\n")

print("Fully thesaurized!\n" + "-----------------------------------\n" + my_string + "\nV\n" + new_string + "-----------------------------------\n")