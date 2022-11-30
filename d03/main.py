# input user action

todos = []

while True:
    user_action = input('enter add, show, edit, or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo: ')
            todos.append(todo) # add todo to list
        case 'show':
            for i, item in enumerate(todos):
                print(i+1,item.capitalize())

        case 'edit':
            item = input('enter item number: ')
            print(item, todos[int(item)-1])
            new_item = input('enter new item todo: ')
            todos[int(item)-1] = new_item

        case 'exit':
            break
        case _:
            print('unknown action')

print('bye')
