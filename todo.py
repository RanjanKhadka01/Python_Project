class Todo:
    def __init__(self):
        self.items = []

    def add_todos(self, item):
        self.items.append(item)
        print('Item added successfully')

    def view_todos(self):
        print('Todo List:')
        for index, item in enumerate(self.items, start=1):
            print(f'{index}. {item}')

    def remove_items(self, index):
        index = int(index)  # Convert index to integer
        if 1 <= index <= len(self.items):
            del self.items[index - 1]
            print('Item removed successfully')
        else:
            print('Invalid Index')

todo_list = Todo()

while True:
    print('''Which operation do you want to perform? 
    1. Add Todos
    2. View Todos
    3. Delete Todos Items
    4. Exit
    ''')
    
    choice = input('Enter your Choice: ')

    if choice == '1':
        item = input('Add Items: ')
        todo_list.add_todos(item)

    elif choice == '2':
        todo_list.view_todos()

    elif choice == '3':
        index = input('Enter the index you want to delete: ')
        todo_list.remove_items(index)

    elif choice == '4':
        break

    else:
        print('Invalid Choice!!')
