

import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    """
    Run a Python file with the specified arguments.

    Args:
        working_directory (str): The base directory to start from.
        file_path (str): The path to the Python file, relative within the working_directory.
        args (list): A list of arguments to pass to the Python script.

    Returns:
        str: The output of the script or an error message if the file cannot be executed.
    """
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ['python', abs_path] + args,
            capture_output=True,
            timeout=30,
            text=True,
            cwd=abs_working_directory

        )
        stdout = result.stdout
        stderr = result.stderr
        exit_code = result.returncode
        
        if not (stdout or stderr):
            return f"No output produced"
        else:
            if exit_code != 0:
                return f"Process exited with code {exit_code}" + f"\nSTDOUT: {stdout}" + "\n" + f"STDERR: {stderr}"
            return f"STDOUT: {stdout}" + "\n" + f"STDERR: {stderr}"
            

    except Exception as e:
        return f"Error: executing python file: {e}"