import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys



def main():    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("prompt needed")
        sys.exit(1)
    
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose = True
    prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model = "gemini-2.0-flash-001", contents = messages
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print(response.text)

main()