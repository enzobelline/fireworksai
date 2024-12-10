import os
api_key = os.getenv("FIREWORKS_API_KEY")
if api_key:
    print(f"API Key Found: {api_key}")
else:
    print("API Key not found. Check your environment setup.")