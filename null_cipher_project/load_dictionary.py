def load(file_name):
    with open(file_name) as file:
        return file.read().lower().split()
