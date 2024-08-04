while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            #Alternatively use with instead, so you don't need close() this is recommended method.
            #with open('files/todos.txt', 'r') as file:
            #    todos = file.readlines()
            
            todos.append(todo)
            
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            
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
            
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'complete':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            
            number = int(input("Number of the todo to complete: "))
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
print("Bye")
