from my_functions.file_utils import get_files

file_list = []
get_files(r"C:\Work\PythonSuli", file_list)

print(f"Files found: {len(file_list)}")