with open("fruits.txt", "a+") as myfile:
    myfile.write("\nokra")
    myfile.seek(0)
    content = myfile.read()
print(content)