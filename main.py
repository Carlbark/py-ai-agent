import os
from pyexpat.errors import messages
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info
from functions.get_files_info import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function

# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    print("Hello from py-ai-agent!")

    contents = sys.argv[1] if len(sys.argv) > 1 else None
    if contents is None:
        raise Exception("No contents provided. Please provide a string as an argument.")
    verbose = sys.argv[2] == "--verbose" if len(sys.argv) > 2 else False
    if verbose:
        print(f"User prompt: {contents}")

    messages = [types.Content(role="user", parts=[types.Part(text=contents)]),]

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

    count = 0
    print("AI loop started")
    # Limit the number of iterations to avoid infinite loops
    while count <= 20:
        count += 1
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=SYSTEM_PROMPT,
            )
        )
        
        # if verbose:
        # print(response)
    
        for candidate in response.candidates:
            for part in candidate.content.parts:
                if getattr(part, "text", None):
                    messages.append(types.Content(role="assistant", parts=[types.Part(text=part.text)]))
                elif getattr(part, "function_call", None):
                    messages.append(types.Content(role="assistant", parts=[types.Part(function_call=part.function_call)]))

        if response.function_calls:
            for function_call in response.function_calls:
                args = function_call.args

                if function_call.name == "get_files_info" and 'directory' not in args:
                    args['directory'] = '.'
                
                result = call_function(function_call, verbose=verbose)
                function_response = result.parts[0].function_response.response
                messages.append(
                    types.Content(
                        role="tool",
                        parts=[types.Part.from_function_response(
                            name=function_call.name,
                            response=function_response
                        )]
                    )
                )

                if not function_response:
                    raise Exception(f"Fatal error: Function {function_call.name} returned no response.")
                elif verbose:
                    print(f"-> {function_response}")
            

        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        assistant_text = None
        for candidate in response.candidates:
            for part in candidate.content.parts:
                if getattr(part, "text", None):
                    assistant_text = part.text
                    break
            if assistant_text:
                break

        if assistant_text and not response.function_calls:
            print(f"Assistant: {assistant_text}")
            break
   

if __name__ == "__main__":
    main()
