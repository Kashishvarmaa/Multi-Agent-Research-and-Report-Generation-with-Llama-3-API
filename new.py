# Import required libraries
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Check if the key is loaded correctly
if api_key:
    print("API key loaded successfully!")
else:
    print("API key not found. Check your .env file.")



# Load environment variables
load_dotenv()

# Print all environment variables to check if it’s loaded
print(os.environ)