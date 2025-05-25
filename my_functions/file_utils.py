import os
def get_files(root_folder: str, file_list: list, filter: str=None):
    """
    This function finds files in a given folder and its subfolders. 
    You can use and optional filter.\n
    params:
        root_folder (str): The folder where the function starts.
        file_list (list): You have to provide an empty list where files will be collected.
        filter (str) (optional): Filter out files with a string. 
    """

    # error checks
    assert os.path.isdir(root_folder), f"{root_folder} must be a folder."
    assert isinstance(file_list, list), "file_list must be a type of list."

    if filter:
        assert isinstance(filter, str), "filter must be a type of string."

    print(f"Searching in {root_folder}...")

    # collect files and folders in root_folder
    folder_content = os.listdir(root_folder)

    # separate folders and files
    folders = []
    for i in folder_content:
        abs_path = os.path.join(root_folder, i)
        if os.path.isfile(abs_path):
            # add files to file_list
            # if we have filter check file
            if filter:
                if filter in abs_path:
                    file_list.append(abs_path)
            else:
                file_list.append(abs_path)
        else:
            # collect folders
            folders.append(abs_path)

    # Recursion: if we found folder call get_files() again with the first folder
    for folder in folders:
        get_files(folder, file_list, filter)

if __name__ == "__main__":
    my_photos = []
    # r = raw string
    get_files(r"C:\Work\PythonSuli", my_photos, filter=".txt")

    print(f"Found files: {len(my_photos)}")