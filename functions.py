TODOS_FILE_PATH = 'todos.txt'


def get_todos(filepath=TODOS_FILE_PATH):
    '''
        Read a text file and return the list of to-do items.
    '''
    with open(filepath, 'r') as file:
        result = file.readlines()
    return result


def write_todos(todos_arg, filepath=TODOS_FILE_PATH):
    """
        Writes given list of todos to a text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# code inside modules is executed when imported
# only execute this code when this file is executed directly

# __name__ is the name of the file
# files have the name __main__ when executed directly


if __name__ == '__main__':
    print(get_todos())
