# class Todo:
#     def __init__(self):
#         self.items = []

#     def add_todos(self, item):
#         self.items.append(item)
#         print('Item added successfully')

#     def view_todos(self):
#         print('Todo List:')
#         for index, item in enumerate(self.items, start=1):
#             print(f'{index}. {item}')

#     def remove_items(self, index):
#         index = int(index) 
#         if 1 <= index <= len(self.items):
#             del self.items[index - 1]
#             print('Item removed successfully')
#         else:
#             print('Invalid Index')

# todo_list = Todo()

# while True:
#     print('''Which operation do you want to perform? 
#     1. Add Todos
#     2. View Todos
#     3. Delete Todos Items
#     4. Exit
#     ''')
    
#     choice = input('Enter your Choice: ')

#     if choice == '1':
#         item = input('Add Items: ')
#         todo_list.add_todos(item)

#     elif choice == '2':
#         todo_list.view_todos()

#     elif choice == '3':
#         index = input('Enter the index you want to delete: ')
#         todo_list.remove_items(index)

#     elif choice == '4':
#         break

#     else:
#         print('Invalid Choice!!')


items = []

def add_items(item):
    items.append(item)
    print("Item added successfully")

def view_items():
    print(items)

def remove_items(index):
    del items[index]
    print("Item removed successfully")

while True:
    print('''Which operation do you want to perform??
    1. Add Todos
    2. View Todos
    3. Delete Todos Items
    4. Exit
    ''')
    operation = input("Enter the operation you want to perform: ")
    
    if operation.isdigit():
        operation = int(operation)
        if operation == 1:
            a = input('Add Todos: ')
            add_items(a)
        elif operation == 2:
            view_items()
        elif operation == 3:
            b = int(input("Enter the index of todos items you want to delete: "))
            remove_items(b)
        elif operation == 4:
            break
        else:
            print('Invalid Operation')
    else:
        print("Please enter a valid operation number.")
