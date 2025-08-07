import os


def get_files_info(working_directory, directory="."):
    """
    Get information about files in the specified directory.

    Args:
        working_directory (str): The base directory to start from.
        directory (str): The subdirectory to inspect, relative within the working_directory. Defaults to the current directory.

    Returns:
        list: A list of dictionaries containing file information.
    """
   # print(f"Working directory: {working_directory}")
   # print(f"Directory to inspect: {directory}")
    full_path = os.path.join(working_directory, directory)
   # print(f"Full path to inspect: {full_path}")
    abs_working_directory = os.path.abspath(working_directory)
   # print(f"Absolute working directory: {abs_working_directory}")
    abs_path = os.path.abspath(full_path)
   # print(f"Absolute path: {abs_path}")
    # Check if directory exists within the working directory
    if not abs_path.startswith(abs_working_directory):
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    if not os.path.isdir(full_path):
        return f"Error: \"{directory}\" is not a directory"
    files_info = []
    dir_contents = os.listdir(full_path)
    
    # print(f"Dir_contents: {dir_contents}:")
    for item in dir_contents:
        item_path = os.path.join(full_path, item)
      #  print(f"Item path: {item_path}")
        is_dir = os.path.isdir(item_path)
      #  print(f"Item: {item}, Is directory: {is_dir}")
        files_info.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}")
    
    return "\n".join(files_info)
