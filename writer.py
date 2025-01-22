from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client with the Llama API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Create a prompt template
writer_prompt = "Write a detailed report based on the following research data:\n{content}"

# Function to generate the report
def writer_agent_function(research_data):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a professional writer."},
            {"role": "user", "content": writer_prompt.format(content=research_data)},
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
    research_data = "Artificial Intelligence is a field that enables machines to mimic human intelligence..."
    print("Writing report...")
    report = writer_agent_function(research_data)
    print("Generated report:", report)