import os


def delete_file(file_name):
    path_temp_file = os.path.join(os.path.abspath(file_name))
    os.remove(path_temp_file)


def is_file(file_name):
    if os.path.exists(file_name):
        return True
    else:
        raise Exception('File not found')
