from functions.get_files_info import get_files_info


if __name__ == "__main__":
    print("Test case 1")
    print(get_files_info("calculator", "."))
    print("Test case 2")
    print(get_files_info("calculator", "pkg"))
    print("Test case 3")
    print(get_files_info("calculator", "/bin"))
    print("Test case 4")
    print(get_files_info("calculator", "../"))
