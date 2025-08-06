import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

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

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print("Response from Gemini API:")
    print(response.text)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
