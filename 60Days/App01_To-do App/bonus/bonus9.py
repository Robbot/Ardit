password = input("Enter a new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for char in password:
    if char.isdigit():
        digit = True
result.append(digit)

upper = False
for char in password:
    if char.isupper():
        upper = True
result.append(upper)

# print(result)
#print(all(result))
if all(result) == True:
    print("Strong Password")
else:
    print("Weak Password")