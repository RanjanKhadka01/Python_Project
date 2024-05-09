items = []

def add_items(item):
  items.append(item)
  print("Items added Successfully")

def view_items():
  print(items)

def remove_items(index):
  del items[index]



while True:
  print('''Which operation do you want to perform ??
        1. Add Todos
        2. View Todos
        3. Delete Todos Items
        4. Exit
        ''')
  operation = int(input("Enter the operation you want to perform? "))
  if operation == 1:
    a = input('Add Todos: ')
    add_items(a)

  elif operation == 2:
    view_items()

  elif operation == 3:
    b = int(input("Enter the index of todos items you want to delete.."))
    remove_items(b)

  elif operation == 4:
    break

  else:
    print('Invalid Operation')
