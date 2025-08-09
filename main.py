import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info

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
    ]
)


    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=SYSTEM_PROMPT,
        )
    )
    print("Response from Gemini API:")
    if response.function_calls:
        for function_call in response.function_calls:
            args = function_call.args
            if verbose:
                print(f"Function call: {function_call.name} with args: {args}")
            if 'directory' not in args:
                args['directory'] = '.'
            print(f"Calling function: {function_call.name}({args})")
           
    else:
        print(response.text)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
