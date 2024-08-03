while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            new_todos = []
            
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            # Alternatively instead you can use list comprehension
            # new_todos = [item.strip('\n') for item in todos]
            # so one line instead instead 5 lines
            
            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
print("Bye")
