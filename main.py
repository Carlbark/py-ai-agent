import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from py-ai-agent!")

    contents = sys.argv[1] if len(sys.argv) > 1 else None
    if contents is None:
        raise Exception("No contents provided. Please provide a string as an argument.")
    else:
        print(f"Contents: {contents}")

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=contents
    )
    print("Response from Gemini API:")
    print(response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
