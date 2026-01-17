import os
from google import genai

# Get API key from environment variable
api_key = os.getenv("AIzaSyDmfzDqsMGkYlw9tOgXnWEFfQMCg6uGyA8")
if not api_key:
    raise ValueError("API key not found. Did you run 'export GOOGLE_API_KEY=AIzaSyDmfzDqsMGkYlw9tOgXnWEFfQMCg6uGyA8' ?")

# Initialize client
client = genai.Client(api_key=api_key)

# Send a test request
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Hello Gemini, say hi in one sentence."
)

print("Response from Gemini:")
print(response.text)