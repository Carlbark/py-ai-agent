
from re import match
from unittest import case
from google.genai import types 
from functions.get_files_info import get_files_info
from functions.get_files_info import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def call_function(function_call_part, verbose=False):
    """
    function_call_part is a types.FunctionCall that most importantly has:

    - .name property (the name of the function, a string)
    -  .args property (a dictionary of named arguments to the function)
    If verbose is specified, print the function name and args:

    print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    Otherwise, just print the name:

    print(f" - Calling function: {function_call_part.name}")
    """
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    # Here you would typically call the actual function with the provided args
    # For example:
    # result = some_function(**function_call_part.args)
    # return result
    function_name = function_call_part.name
    working_directory = "./calculator"  # Assuming a fixed working directory for this example
    match function_name:
        case "get_files_info":
            result = get_files_info(working_directory=working_directory, **function_call_part.args)
        case "get_file_content":
            result = get_file_content(working_directory=working_directory, **function_call_part.args)
        case "write_file":
            result = write_file(working_directory=working_directory, **function_call_part.args)
        case "run_python_file":
            result = run_python_file(working_directory=working_directory, **function_call_part.args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"}
                    )
                ]
            )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result}
            )
        ]
    )
    
    