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

    assert os.path.isdir(root_folder), f"{root_folder} must be a folder."
    assert isinstance(file_list, list), "file_list must be a type of list."

    if filter:
        assert isinstance(filter, str), "filter must be a type of string."

    

if __name__ == "__main__":
    my_photos = "Robert"
    get_files("fefwfewfw", my_photos, filter=".jpg")