from functions.get_files_info import *


if __name__ == "__main__":
    
    """
    print("Test case 1")
    print(get_files_info("calculator", "."))
    print("Test case 2")
    print(get_files_info("calculator", "pkg"))
    print("Test case 3")
    print(get_files_info("calculator", "/bin"))
    print("Test case 4")
    print(get_files_info("calculator", "../"))
    """
    print("Test case 1")
    #print(get_file_content("calculator", "lorem.txt"))
    print(get_file_content("calculator", "main.py"))
    print("Test case 2")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Test case 3")
    print(get_file_content("calculator", "/bin/cat"))
    print("Test case 4")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))



