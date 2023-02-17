FILEPATH = "text.txt"
# by this way, if you want to change your file name,
# you can change directly by using FILEPATH variable
def get_todos(filepath=FILEPATH):
    """Read the text file and return
    the list of the to-do items"""
    with open(filepath, "r") as file_local:
        content_local = file_local.readlines()
    return content_local


def add_todos(todo_arg, file_path=FILEPATH):
    """Write to-do items list in the text file"""
    with open(file_path, "a") as file_local:
        file_local.write(todo_arg+"\n")


def write_todos(Todoss, file_path=FILEPATH):
    with open(file_path, "w") as file_local:
        file_local.writelines(Todoss)

if __name__ == "__main__":
    print("hello")