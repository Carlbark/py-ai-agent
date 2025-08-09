import os
from google import genai
from google.genai import types
from config import *

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

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

def get_file_content(working_directory, file_path):
    """
    Get the content of a file.

    Args:
        working_directory (str): The base directory to start from.
        file_path (str): The path to the file, relative within the working_directory.

    Returns:
        str: The content of the file or an error message if the file does not exist.
    """
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(abs_working_directory):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.isfile(full_path):
        return f"Error: File not found or is not a regular file: \"{file_path}\""
    
    with open(full_path, 'r') as file:
        if os.path.getsize(full_path) > MAX_CHARS:
            file_content_string = file.read(MAX_CHARS)
            return file_content_string + f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters.]"
        else:
            return file.read()
