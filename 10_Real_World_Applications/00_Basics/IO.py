myfile = open("fruits.txt")
content = myfile.read()
print(content)
myfile.close()
print(content)

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)

def occurences(character,filepath):
    with open(filepath,"r") as myfile:
        content = myfile.read()
        myfile.close()
    return content.count(character)

print(occurences("a", "fruits.txt"))
