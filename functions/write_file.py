import os
from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    """
    Write content to a file.

    Args:
        working_directory (str): The base directory to start from.
        file_path (str): The path to the file, relative within the working_directory.
        content (str): The content to write to the file.

    Returns:
        str: A success message or an error message if the file cannot be written.
    """
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, 'w') as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: Could not write to \"{file_path}\": {e}"