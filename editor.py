from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client with the Llama API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Create a prompt template
editor_prompt = "Edit and improve the following report for clarity, grammar, and structure:\n{report}"

# Function to edit the report
def editor_agent_function(report):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a professional editor."},
            {"role": "user", "content": editor_prompt.format(report=report)},
        ],
        model="llama-3.3-70b-versatile",  # Replace with the correct model
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    
    # Extract and return the completion response
    return chat_completion.choices[0].message.content

# Example usage
if __name__ == "__main__":
    report = "Artificial Intelligence (AI) refers to machines simulating human intelligence. It includes..."
    print("Editing report...")
    edited_report = editor_agent_function(report)
    print("Edited report:", edited_report)