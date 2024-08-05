password = input("Enter a new password: ")

#dictionary instead of a list
result = {}

if len(password) >= 8:
    result["lenght"] =True
else:
    result["lenght"] = False

result["digit"] = False
for char in password:
    if char.isdigit():
        result["digit"] = True


result["upper"] = False
for char in password:
    if char.isupper():
        result["upper"] = True

#by default is True, so you don't need all(result) == True
if all(result):
    print("Strong Password")
    print(result)
else:
    print("Weak Password")
    print(result)