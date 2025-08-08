from functions.get_files_info import *
from functions.write_file import write_file
from functions.run_python import run_python_file


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
    
    print("Test case 1")
    #print(get_file_content("calculator", "lorem.txt"))
    print(get_file_content("calculator", "main.py"))
    print("Test case 2")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Test case 3")
    print(get_file_content("calculator", "/bin/cat"))
    print("Test case 4")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))



    print("Test case 1")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("Test case 2")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("Test case 3")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    """

    print("Test case 1")
    print(run_python_file("calculator", "main.py"))
    print("Test case 2")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("Test case 3")
    print(run_python_file("calculator", "tests.py"))
    print("Test case 4")
    print(run_python_file("calculator", "../main.py"))
    print("Test case 5")
    print(run_python_file("calculator", "nonexistent.py"))
    
